"""Validate reference relationships and generate documentation; no model calculations."""

import argparse
import csv
import math
import sys
from pathlib import Path
from string import Template

import yaml

ROOT = Path(__file__).resolve().parent
DEPENDENCIES = ("exclude_functional_areas", "deduct_workload_from")


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)


def read_yaml(path):
    return yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueLoader)


def index(rows, key, label):
    result = {}
    for row in rows:
        identifier = row.get(key)
        if not isinstance(identifier, str) or not identifier.strip():
            raise ValueError(f"{label}: missing {key}")
        if identifier in result:
            raise ValueError(f"{label}: duplicate ID {identifier}")
        result[identifier] = row
    return result


def class_refs(expression, classes):
    if isinstance(expression, str):
        if expression not in classes:
            raise ValueError(f"Unknown classification ID: {expression}")
        return [expression]
    if not isinstance(expression, dict) or len(expression) != 1:
        raise ValueError(
            f"Classification must be one all_of/any_of expression: {expression}"
        )
    operator, children = next(iter(expression.items()))
    if (
        operator not in ("all_of", "any_of")
        or not isinstance(children, list)
        or not children
    ):
        raise ValueError(f"Invalid classification expression: {expression}")
    return [
        identifier for child in children for identifier in class_refs(child, classes)
    ]


def check_cycles(edges, label):
    done = set()

    def visit(node, stack):
        if node in stack:
            raise ValueError(f"{label} cycle: " + " -> ".join(stack + [node]))
        if node in done:
            return
        for target in edges.get(node, []):
            visit(target, stack + [node])
        done.add(node)

    for node in edges:
        visit(node, [])


def load_references(root=ROOT):
    ref = root / "references"
    classes = index(
        read_yaml(ref / "classification_register.yaml")["classifications"],
        "id",
        "Classifications",
    )
    archetypes = index(
        read_yaml(ref / "conversion_archetypes_catalog.yaml")["conversion_archetypes"],
        "id",
        "Archetypes",
    )
    areas = index(
        read_yaml(ref / "functional_area_specifications.yaml")["functional_areas"],
        "id",
        "Functional areas",
    )
    with (ref / "assumptions_register.csv").open(
        encoding="utf-8-sig", newline=""
    ) as file:
        assumptions = index(list(csv.DictReader(file)), "Assumption ID", "Assumptions")
    warnings = []
    parent_edges = {}
    for identifier, row in classes.items():
        parent = row.get("parent")
        if parent and parent not in classes:
            raise ValueError(f"{identifier}: unknown parent {parent}")
        parent_edges[identifier] = [parent] if parent else []
        if not row.get("definition") or not row.get("logic"):
            warnings.append(
                f"{identifier}: incomplete description or logic (generation allowed)"
            )
    check_cycles(parent_edges, "Classification parent")
    for identifier, row in assumptions.items():
        value = float(row["Value"])
        if not math.isfinite(value) or value < 0:
            raise ValueError(f"{identifier}: invalid value")
        if row["Type"] == "proportion" and value > 1:
            raise ValueError(f"{identifier}: proportion must be between 0 and 1")
        if row["Assumption Category"] not in ("pathway", "operational"):
            raise ValueError(f"{identifier}: unsupported assumption category")
    edges = {}
    for identifier, area in areas.items():
        if area["archetype_id"] not in archetypes:
            raise ValueError(f"{identifier}: unknown archetype")
        archetype = archetypes[area["archetype_id"]]
        if area["primary_workload_object"] not in archetype["typical_workload_object"]:
            raise ValueError(f"{identifier}: workload incompatible with archetype")
        if not archetype.get("operational_constraint"):
            raise ValueError(f"{identifier}: archetype needs operational_constraint")
        calculations = area["calculations"]
        if not calculations:
            raise ValueError(f"{identifier}: no calculations")
        index(calculations, "subgroup_id", identifier + " subgroups")
        edges[identifier] = []
        for calculation in calculations:
            context = identifier + "/" + calculation["subgroup_id"]
            if not calculation.get("subgroup_label") or not calculation.get(
                "capacity_output"
            ):
                raise ValueError(f"{context}: missing label or output")
            class_refs(calculation["classification"], classes)
            ids = calculation["assumption_ids"]
            if not isinstance(ids, list) or len(set(ids)) != len(ids):
                raise ValueError(f"{context}: invalid or repeated assumption IDs")
            for assumption_id in ids:
                if assumption_id not in assumptions:
                    raise ValueError(f"{context}: unknown assumption {assumption_id}")
                if assumptions[assumption_id]["Functional Area ID"] != identifier:
                    warnings.append(
                        f"{context}: assumption {assumption_id} has a different registered area"
                    )
            for field in DEPENDENCIES:
                targets = calculation.get(field, [])
                if not isinstance(targets, list) or len(set(targets)) != len(targets):
                    raise ValueError(f"{context}: invalid {field}")
                for target in targets:
                    if target not in areas or target == identifier:
                        raise ValueError(f"{context}: invalid dependency {target}")
                    if (
                        field == "deduct_workload_from"
                        and areas[target]["primary_workload_object"]
                        != area["primary_workload_object"]
                    ):
                        raise ValueError(
                            f"{context}: deduction workload units differ from {target}"
                        )
                edges[identifier].extend(targets)
    check_cycles(edges, "Functional-area dependency")
    return classes, assumptions, archetypes, areas, warnings


def cell(value):
    return str(value or "").replace("|", r"\|").replace("\n", "<br>")


def table(headers, rows):
    return "\n".join(
        [
            "| " + " | ".join(headers) + " |",
            "| " + " | ".join("---" for _ in headers) + " |",
        ]
        + ["| " + " | ".join(cell(value) for value in row) + " |" for row in rows]
    )


def expression_text(expression):
    if isinstance(expression, str):
        return f"`{expression}`"
    operator, children = next(iter(expression.items()))
    joiner = " AND " if operator == "all_of" else " OR "
    return "(" + joiner.join(expression_text(child) for child in children) + ")"


def render(content, refs, titles, root=ROOT):
    classes, assumptions, archetypes, areas, _ = refs
    allowed = {
        "functional_area_id",
        "title",
        "definition",
        "activity_classification",
        "workload_derivation",
        "capacity_conversion",
        "notes",
    }
    if set(content) - allowed:
        raise ValueError(f"Unknown page fields: {sorted(set(content) - allowed)}")
    for field in allowed - {"notes"}:
        if not isinstance(content.get(field), str) or not content[field].strip():
            raise ValueError(f"Page requires non-empty {field}")
    area = areas[content["functional_area_id"]]
    archetype = archetypes[area["archetype_id"]]
    calculations = area["calculations"]
    ids = list(dict.fromkeys(i for c in calculations for i in c["assumption_ids"]))
    # The register supplies applicability labels, including narrower/shared subgroups.
    assumption_rows = [
        (
            assumptions[i]["Subgroup"],
            assumptions[i]["Metric"],
            assumptions[i]["Assumption Category"].capitalize(),
        )
        for i in ids
    ]

    def area_name(identifier):
        # Link only pages included in the pilot: no invented routes for other areas.
        if identifier in titles:
            title, slug = titles[identifier]
            return f"[{title}]({slug}.md)"
        return identifier.replace("_", " ").lower()

    def join_names(names):
        if len(names) < 2:
            return "".join(names)
        if len(names) == 2:
            return " and ".join(names)
        return ", ".join(names[:-1]) + " and " + names[-1]

    descriptions = []
    for field, lead in [
        ("exclude_functional_areas", "Exclude activity qualifying for"),
        ("deduct_workload_from", "Deduct allocated workload from"),
    ]:
        groups = {}
        for calculation in calculations:
            targets = tuple(calculation.get(field, []))
            if targets:
                groups.setdefault(targets, []).append(calculation["subgroup_label"])
        for targets, labels in groups.items():
            qualifier = (
                ""
                if len(labels) == len(calculations)
                else "For " + ", ".join(labels) + ": "
            )
            descriptions.append(
                "**"
                + (
                    "Exclusions"
                    if field == "exclude_functional_areas"
                    else "Workload deductions"
                )
                + ":** "
                + qualifier
                + lead
                + " "
                + join_names([area_name(t) for t in targets])
                + "."
            )
    scope = "\n\n" + "\n\n".join(descriptions) if descriptions else ""

    details = [
        "**Capacity outputs**",
        "\n".join(
            "* `" + output + "`"
            for output in dict.fromkeys(c["capacity_output"] for c in calculations)
        ),
        f"**Conversion archetype:** {archetype['conversion_archetype']} · `{archetype['id']}`",
        f"**Operational constraint:** {archetype['operational_constraint']}",
        f"**Workload object:** `{area['primary_workload_object']}`",
        "**Classification expressions**",
        table(
            ["Subgroup", "Expression"],
            [
                (c["subgroup_label"], expression_text(c["classification"]))
                for c in calculations
            ],
        ),
    ]
    used_classes = list(
        dict.fromkeys(
            i for c in calculations for i in class_refs(c["classification"], classes)
        )
    )
    details.extend(
        [
            "**Classification definitions**",
            table(
                ["ID", "Definition", "Rule"],
                [
                    (
                        f"`{i}`",
                        classes[i].get("definition") or "Not documented",
                        classes[i].get("logic") or "Not documented",
                    )
                    for i in used_classes
                ],
            ),
        ]
    )
    class_notes = [
        f"* `{i}`: {classes[i]['notes']}"
        for i in used_classes
        if classes[i].get("notes")
    ]
    if class_notes:
        details.extend(["**Classification notes**", "\n".join(class_notes)])
    details.extend(
        [
            "**Assumption references**",
            table(
                ["Subgroup", "Assumption ID"],
                [(assumptions[i]["Subgroup"], f"`{i}`") for i in ids],
            ),
        ]
    )
    for field in DEPENDENCIES:
        rows = [
            (c["subgroup_label"], ", ".join(f"`{t}`" for t in c[field]))
            for c in calculations
            if c.get(field)
        ]
        if rows:
            details.extend(
                [
                    "**"
                    + (
                        "Activity exclusions"
                        if field == "exclude_functional_areas"
                        else "Workload deductions"
                    )
                    + "**",
                    table(["Subgroup", "Functional-area IDs"], rows),
                ]
            )
    notes = content.get("notes", "")
    if not isinstance(notes, str):
        raise TypeError("notes must be Markdown text")
    context = dict(
        content,
        definition_indented="\n".join(
            "    " + line if line else "" for line in content["definition"].splitlines()
        ),
        scope=scope,
        assumptions=table(["Subgroup", "Assumption", "Type"], assumption_rows),
        notes_section=("## Notes\n\n" + notes.strip()) if notes.strip() else "",
        technical_details="\n".join(
            "    " + line if line else "" for line in "\n\n".join(details).splitlines()
        ),
    )
    return (
        Template((root / "templates/fun_area_page.md").read_text()).substitute(context).rstrip()
        + "\n"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check", action="store_true", help="Validate and render without writing"
    )
    args = parser.parse_args()
    try:
        refs = load_references()
        pages = [
            (p.stem, read_yaml(p)) for p in sorted((ROOT / "content").glob("*.yaml"))
        ]
        if not pages:
            raise ValueError("No content files found")
        index([data for _, data in pages], "functional_area_id", "Page content")
        titles = {
            data["functional_area_id"]: (data["title"], slug) for slug, data in pages
        }
        generated = [(slug, render(data, refs, titles)) for slug, data in pages]
        for warning in refs[-1]:
            print("Warning: " + warning, file=sys.stderr)
        if not args.check:
            output = ROOT.parents[1] / "docs/functional-areas-preview"
            output.mkdir(parents=True, exist_ok=True)
            for slug, page in generated:
                (output / (slug + ".md")).write_text(page, encoding="utf-8")
                print("Generated docs/functional-areas/preview/" + slug + ".md")
        print(f"Validated {len(refs[3])} areas and {len(generated)} pilot pages.")
    except (ValueError, KeyError, TypeError, yaml.YAMLError) as error:
        raise SystemExit("Generation failed: " + str(error))


if __name__ == "__main__":
    main()
