---
title: Technical Information
icon: lucide/book-open-text
---

#### ∑ Technical Information

This tool is built primarily in Python.

The codebase is modular and is split into a) code to group the incoming activity
data into functional areas, b) an 'engine' that performs the conversion to
capacity estimates using agreed logic, and c) the public facing interface for submitting a conversion
run.

Reusable data elements (like lookups) are held in separate files that are
audited and version controlled independently.
These include:

- [Assumptions register](/docs/technical-information/assumptions-register.md)
- [Classification register](/docs/technical-information/classification-register.md)
- [Funtional area catalogue](/docs/technical-information/functional-area-catalogue.md)
- [Conversion archetypes catalogue](/docs/technical-information/conversion-archetypes-catalogue.md)
- [Calculation traceability matrix](/docs/technical-information/calculation-traceability-matrix.md)

All the code is publicly available in the following GitHub repositories:

- [Functional area mapping](https://github.com/The-Strategy-Unit/nhp_functional_area_mapping)
- [Conversion logic](https://github.com/The-Strategy-Unit/nhp_capacity_conversion_logic.git)
- [User interface]()

Please see our open-source policy [here](https://connect.strategyunitwm.nhs.uk/open-source-policy/).