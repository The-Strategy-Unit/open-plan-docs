# Functional area page generation

This generator combines shared reference data with page-specific narrative content to produce functional area documentation.

Generated pages currently appear alongside the existing pages under **Preview**, so they can be reviewed and compared before replacement.

## Folder structure

```text
generate/functional-areas/
├── generate.py
├── test_generate.py
├── content/
│   └── <page-slug>.yaml
├── references/
│   ├── classification_register.yaml
│   ├── assumptions_register.csv
│   ├── conversion_archetypes_catalog.yaml
│   └── functional_area_specifications.yaml
└── templates/
    └── fun_area_page.md
```

Generated Markdown is written to `docs/functional-areas-preview/`.

## Sources of information

| Source | Maintained information |
|---|---|
| Classification register | Reusable activity classification rules |
| Assumptions register | Assumption definitions, values and supporting information |
| Conversion archetype catalogue | Reusable conversion methods and operational constraints |
| Functional area specifications | Relationships between functional areas, subgroups, classifications, assumptions, archetypes and capacity outputs |
| Content YAML files | Page titles, definitions, explanations, formulae and notes |
| Markdown template | Shared page structure and presentation |

The functional area specification references items in the other registers by ID. It also describes exclusions and workload deductions between functional areas.

The generator documents these relationships. It does not execute the capacity model or calculate capacity requirements.

## Setup

The generator requires PyYAML, which should be declared in the repository's `pyproject.toml`.

Run commands from the repository root.

## Generate pages

```bash
uv run python generate/functional-areas/generate.py
```

Review the resulting changes in `docs/functional-areas-preview/`.

Do not edit generated Markdown directly: the next generation run will overwrite those changes. Edit the corresponding content file, reference file or template instead.

## Run checks

After generating the pages, run:

```bash
uv run python -m unittest discover -s generate/functional-areas -p test_generate.py
```

The tests cover selected relationship validation failures, nested classification expressions, dependency cycles and generated page consistency.

They also check that generated pages match their source files and follow the expected page structure. They do not establish that the documented rules match the Python model implementation.

## Update an existing page

1. Edit narrative content in `content/<page-slug>.yaml`.
2. Update reference data if classifications, assumptions or relationships have changed.
3. Regenerate the pages.
4. Run the tests.
5. Review the rendered page and Git diff.
6. Commit the source changes and generated Markdown together.

Changes to shared reference data or the template may affect several pages. Review all affected generated files.

## Add a functional area page

1. Ensure the functional area is defined in the specification.
2. Ensure its referenced classifications, assumptions and archetype exist.
3. Add a content YAML file, using an existing file as the starting point.
4. Set `functional_area_id` to the corresponding specification ID.
5. Use the content filename as the intended page slug.
6. Generate the page and run the tests.
7. Add an explicit navigation entry in `zensical.toml`.
8. Review the rendered page.

When adding related pages, also check that exclusion and workload deduction references link to the intended pages.

## Preview and build the site

Generation is currently a separate step: run the generator before serving or building the site.