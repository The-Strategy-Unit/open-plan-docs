"""Zensical macros for rendering YAML data as Markdown tables."""

from __future__ import annotations

from html import escape
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pandas import DataFrame


def yaml_selection_to_df(path: str, key: str):
    import pandas as pd
    import yaml

    with Path(path).open(encoding="utf-8") as stream:
        return pd.DataFrame(yaml.safe_load(stream)[key])


def _cell_to_chips(value: Any) -> Any:
    """Render list cells as styled chips; leave other cells unchanged."""
    if isinstance(value, list):
        return "".join(
            f'<span class="chip">{escape(str(item))}</span>' for item in value
        )
    return value


def format_list_cells(df: DataFrame) -> DataFrame:
    """Format list-valued DataFrame cells before convert_to_md_table."""
    return df.map(_cell_to_chips)


def _classification_chips(value: Any) -> str:
    """Render nested all_of/any_of rules, preserving Boolean grouping."""
    if isinstance(value, str):
        return f'<span class="chip">{escape(value)}</span>'

    if isinstance(value, list):
        return " ".join(_classification_chips(item) for item in value)

    if isinstance(value, dict):
        groups = []
        for operator, conditions in value.items():
            if operator in ("all_of", "any_of"):
                joiner = " AND " if operator == "all_of" else " OR "
                parts = [_classification_chips(item) for item in conditions]
                groups.append("(" + joiner.join(parts) + ")")
            else:
                groups.append(
                    f'<span class="chip">{escape(str(operator))}</span> '
                    + _classification_chips(conditions)
                )
        return " ".join(groups)

    return f'<span class="chip">{escape(str(value))}</span>'


def functional_area_specifications_table(path: str):
    """Read functional area YAML; return one DataFrame row per calculation."""
    import pandas as pd
    import yaml

    with Path(path).open(encoding="utf-8") as stream:
        areas = yaml.safe_load(stream)["functional_area_specifications"]

    rows = []
    for area in areas:
        for calc in area.get("calculations", []):
            rows.append(
                {
                    "Functional area": area["id"],
                    "Care setting": area.get("care_setting", ""),
                    "Output type": area.get("output_type", ""),
                    "Workload": area.get("primary_workload_object", ""),
                    "Archetype": area.get("archetype_id", ""),
                    "Subgroup": calc.get("subgroup_label", ""),
                    "Classification": _classification_chips(
                        calc.get("classification", {})
                    ),
                    "Assumptions": calc.get("assumption_ids", []),
                    "Exclusions": calc.get("exclude_functional_areas", []),
                    "Deductions": calc.get("deduct_workload_from", []),
                    "Capacity output": calc.get("capacity_output", ""),
                }
            )

    return pd.DataFrame(rows).fillna("")


def define_env(env) -> None:
    """Register Zensical's custom filter and macro."""
    env.macro(yaml_selection_to_df)
    env.filter(format_list_cells)
    env.macro(functional_area_specifications_table)


def main():
    print("Hello from open-plan-docs-test!")


if __name__ == "__main__":
    main()
