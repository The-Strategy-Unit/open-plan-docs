# OpenPlan Docs

Documentation for Open Plan, the Strategy Unit's open source model for converting hospital activity into capacity requirements.
Funded by the New Hospital Programme (NHP) and part of the [NHP model](https://connect.strategyunitwm.nhs.uk/nhp/project_information/).

## How to contribute

### External contributors

Please raise queries by creating [new GitHub issues](https://github.com/The-Strategy-Unit/open-plan-docs/issues/new), or by contacting us at [mlscu.su.datascience@nhs.net](mailto:mlscu.su.datascience@nhs.net)

### Internal contributors

This section is for internal contributors within the Strategy Unit, and assumes that you have `uv` installed in line with internal recommendations.

1. Clone this repository to your local machine
1. Create a new virtual environment with `uv sync --all-extras`
1. Activate the new virtual environment with `.\.venv\scripts\activate.ps1`

Once you have made your changes, view them locally with the command `uv run zensical serve`.

## Publishing

This website is automatically [published to GitHub pages](https://the-strategy-unit.github.io/open-plan-docs/) via a GitHub workflow on merge to the `main` branch.
