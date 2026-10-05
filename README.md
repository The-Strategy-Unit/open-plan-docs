# OpenPlan Docs

Documentation for the Strategy Unit's **OpenPlan Hospital Capacity Model** — a common framework for translating hospital demand into capacity requirements. The Capacity Model takes estimated future activity from the upstream [OpenPlan Hospital Demand Model](https://connect.strategyunitwm.nhs.uk/nhp/project_information/) and translates it into estimates of the physical capacity required. This work is funded by the **New Hospital Programme (NHP)**.

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

This website is automatically [published](https://connect.strategyunitwm.nhs.uk/capacity-model-docs/) via a GitHub release.
