"""
Zensical macros module (module_name = "main" by default).
Registers a `format_list_cells` filter you chain BEFORE the built-in
`convert_to_md_table` filter, since zensical's `_convert_to_md_table`
has no special handling for list-typed cells (it just calls
`df.to_markdown(tablefmt="pipe")` via tabulate, which stringifies
lists as their raw Python repr).

Usage in markdown:

    <div class="compact-table" markdown="1">
    {{ pd_read_yaml("docs/data/calculation_traceability_matrix.yaml").fillna("")
       | format_list_cells
       | convert_to_md_table }}
    </div>
"""

from __future__ import annotations

from html import escape
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pandas import DataFrame


def _cell_to_chips(value: Any) -> Any:
    """Render list-typed cells as inline chip spans; leave others untouched."""
    if isinstance(value, list):
        return "".join(
            f'<span class="chip">{escape(str(v))}</span>' for v in value
        )
    return value


def format_list_cells(df: DataFrame) -> DataFrame:
    """Jinja filter: convert list cells to chip HTML before convert_to_md_table."""
    return df.map(_cell_to_chips)


def define_env(env) -> None:
    """Zensical macros entry point — called automatically on build/preview."""
    env.filter(format_list_cells)

def main():
    print("Hello from open-plan-docs-test!")


if __name__ == "__main__":
    main()
