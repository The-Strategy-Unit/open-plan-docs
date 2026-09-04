---
hide:
  - toc
---

# Calculation Traceability Matrix

The glue table that links classifications, assumptions, archetypes and outputs.

A row represents a unique workload-to-capacity calculation pathway requiring distinct classifications, assumptions, workload derivation logic or capacity outputs.

<div class="compact-table" markdown="1">
{{ pd_read_yaml("docs/data/calculation_traceability_matrix.yaml").fillna("") | convert_to_md_table }}
</div>

<div class="compact-table" markdown="1">

 **MOVE TO EXTERNAL YAML FILE AS FUN AREAS ARE COMPLETED**

| Functional area                 | Subgroup                         | Classification IDs                                                                               | Workload Assumptions                                                                                      | Formula ID             | Operational Assumptions                                                      | Capacity Output                                     |
|---------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|------------------------|------------------------------------------------------------------------------|-----------------------------------------------------|
| BEDS_CRITICAL_CARE              | Neonatal                         | CLASS_AGE_NEONATAL, CLASS_WELL_BABIES                                                            | CRITICAL_CARE_NEONATAL_PC_BDS                                                                             | FRM_BED_OCCUPANCY      | CRITICAL_CARE_NEONATAL_OCC, CRITICAL_CARE_ANNUAL_OPER_HOURS                  | NEONATAL_CRITICAL_CARE_BEDS                         |
</div>