---
icon: lucide/book-open-text
---

# Technical Information

This tool is built primarily in Python.

The codebase is modular and is split into code to group the incoming activity
data into functional areas, an 'engine' that performs the conversion to
capacity estimates using agreed logic, and the public facing interface for 
submitting a conversion run.

Reusable data elements (like lookups) are held in separate files that are
audited and version controlled independently.
These include:


- [Assumptions register](assumptions-register)
- [Classification register](classification-register)
- [Functional area catalogue](functional-area-catalogue)
- [Conversion archetypes catalogue](conversion-archetypes-catalogue)

These elements are combined as shown in the [calculation traceability matrix](calculation-traceability-matrix).

For a descriptive overview of how the model works, see the [model architecture](technicalmodel-architecture).
