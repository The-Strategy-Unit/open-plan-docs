# OpenPlan Docs

Documentation for the Strategy Unit's **OpenPlan Hospital Capacity Model** — a common framework for translating hospital demand into capacity requirements. The Capacity Model takes estimated future activity from the upstream [OpenPlan Hospital Demand Model](https://connect.strategyunitwm.nhs.uk/nhp/project_information/) and translates it into estimates of the physical capacity required. This work is funded by the **New Hospital Programme (NHP)**.

## How to contribute

### External contributors

Please raise queries by creating [new GitHub issues](https://github.com/The-Strategy-Unit/open-plan-docs/issues/new), or by contacting us at [mlscu.su.datascience@nhs.net](mailto:mlscu.su.datascience@nhs.net)

### Internal contributors

These instructions assume that you have `uv` installed in line with internal recommendations. Run all commands from the repository root.

1. Clone the repository and create a branch for your changes
2. Install the project dependencies, including the development tools: `uv sync`

### Preview and build

Review the affected pages in the local preview.

If you have changed functional area source files, regenerate those pages first using the instructions below.

```bash
uv run zensical serve
```

Before submitting a PR, also check that the site builds successfully:

```bash
uv run zensical build --clean
```

## Generating functional area documentation

Functional area pages combine four shared reference files with page-specific narrative content and a common template. Maintain these sources and commit the generated Markdown and catalogue CSV alongside any source changes.

Generation is a separate step: serving or building the site does not itself regenerate these pages.

### Folder structure

```text
generate/functional-areas/
├── generate.py
├── generate_catalog.py
├── test_generate.py
├── content/
│   └── <page-slug>.yaml
├── references/
│   ├── assumptions_register.csv
│   ├── classification_register.yaml
│   ├── conversion_archetypes_catalog.yaml
│   └── functional_area_specifications.yaml
│   └── fun_area_catalog.csv (generated)
│   └── daycase_tretspef_mapping.xlsx
└── templates/
    └── fun_area_page.md
```

Generated Markdown is written to `docs/functional-areas/`. The content filename determines the generated page filename: for example, `critical-care-beds.yaml` produces `critical-care-beds.md`.

### Sources of information

Each page uses the functional area specification to look up its classification rules, assumptions and conversion archetype in the other three reference files. Page-specific YAML supplies the narrative, and the template controls the shared layout.

| Source | Maintained information |
|---|---|
| Classification register | Reusable activity classification rules |
| Assumptions register | Assumption definitions, values and supporting information |
| Conversion archetype catalogue | Reusable conversion methods and operational constraints |
| Functional area specifications | Functional areas, subgroups, capacity outputs and references to classifications, assumptions and archetypes; activity exclusions and workload deductions |
| Content YAML files | Page titles, definitions, readable classification explanations, formulae and optional notes |
| Markdown template | Shared page structure and presentation |

The specifications file links items by ID. Keep `functional_area_id` in each content file aligned with the corresponding specification entry. These identifiers remain unchanged when a page is renamed.

The generator assembles and validates documentation. The calculations are implemented separately in [capacity conversion logic](https://github.com/The-Strategy-Unit/nhp_capacity_conversion_logic).

### Generate pages and catalogue

```bash
uv run python generate/functional-areas/generate.py
uv run python generate/functional-areas/generate_catalog.py
```
The catalogue is written to `generate/functional-areas/references/fun_area_catalog.csv`. It contains one row per functional area and uses the functional area specification and the conversion archetype catalogue. Run both commands routinely; if the catalogue is unchanged, there is no CSV change to commit.

Review the resulting changes in `docs/functional-areas/` and in the catalogue CSV. Make edits in the source files or template, since regeneration overwrites the generated files.

### Run checks

```bash
uv run python -m unittest discover -s generate/functional-areas -p test_generate.py
```

The tests check selected reference-validation rules, nested classification references, dependency cycles and generated page structure. They also verify that each content file has a corresponding Markdown page and that both the Markdown and the catalogue CSV match freshly rendered output.

When editing locally, regenerate the pages and then run the tests. In CI, run the tests without regenerating first so they can detect outdated committed files. The tests compare the files with the expected output without overwriting them.

These checks do not verify clinical logic, formula accuracy, visual layout or agreement with the model implementation. Review the rendered pages and run the site build separately.

### Update an existing page

1. Edit narrative content in `generate/functional-areas/content/<page-slug>.yaml`
2. Update the relevant reference files if rules, assumptions or relationships have changed
3. Regenerate the pages and run the tests
4. Preview the affected pages and build the site
5. Review the Git diff and commit the source changes with any updated Markdown and catalogue CSV

Shared reference or template changes may affect several pages. Review all affected output.

### Add or rename a page

1. Define the functional area in the specification and ensure its referenced classifications, assumptions and archetype exist
2. Add a content YAML file using an existing page as a starting point. Set `functional_area_id` to the specification ID
3. Choose a readable, service-first filename, such as `maternity-assessment-beds.yaml`
4. Regenerate the pages and catalogue and run the tests
5. Add or update the explicit navigation entry in `zensical.toml` and links from the functional area index
6. Preview the page, check related exclusions and deductions, and build the site

When renaming a page, remove the old generated Markdown if it remains after generation, and update manually maintained links and any filename-specific tests. Add redirects for previously published URLs where appropriate. Generated links between functional areas use the current content filenames.

If a page is retired without a replacement, consider retaining a short explanation at its existing URL.

## Publishing

This website is automatically [published](https://connect.strategyunitwm.nhs.uk/capacity-model-docs/) via a GitHub release.
