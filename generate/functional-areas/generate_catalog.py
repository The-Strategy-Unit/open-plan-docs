import csv
import io
from pathlib import Path

import yaml

from generate import read_yaml

ROOT = Path(__file__).resolve().parent
REFERENCES = ROOT / "references"
OUTPUT = REFERENCES / "fun_area_catalog.csv"

COLUMNS = (
    "Functional Area ID",
    "Conversion Archetype",
    "Operational Constraint",
    "Primary Workload Object",
    "Output Type",
    "Care Setting",
)


def render_catalog():
    """Return the generated catalogue as CSV text without writing a file."""
    areas = read_yaml(REFERENCES / "functional_area_specifications.yaml")[
        "functional_area_specifications"
    ]

    archetypes = {
        row["id"]: row
        for row in read_yaml(REFERENCES / "conversion_archetypes_catalog.yaml")[
            "conversion_archetypes"
        ]
    }

    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=COLUMNS, lineterminator="\n")
    writer.writeheader()

    for area in sorted(areas, key=lambda row: row["id"]):
        archetype = archetypes[area["archetype_id"]]
        writer.writerow(
            {
                "Functional Area ID": area["id"],
                "Conversion Archetype": archetype["conversion_archetype"],
                "Operational Constraint": archetype["operational_constraint"],
                "Primary Workload Object": area["primary_workload_object"],
                "Output Type": area["output_type"],
                "Care Setting": area["care_setting"],
            }
        )

    return buffer.getvalue()


def main():
    try:
        OUTPUT.write_text(render_catalog(), encoding="utf-8", newline="")
    except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as error:
        raise SystemExit(f"Catalogue generation failed: {error}") from error

    print(f"Generated {OUTPUT.relative_to(ROOT.parent.parent).as_posix()}")


if __name__ == "__main__":
    main()
