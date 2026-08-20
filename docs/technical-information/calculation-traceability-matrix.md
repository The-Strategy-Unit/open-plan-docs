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
| THEATRES_DAYCASE_PROC           | Adult surgical                   | CLASS_DAYCASE, CLASS_HAS_PROCEDURE. CLASS_AGE_ADULT, MAP_SURGICAL                                | DAYCASE_THEATRE_ADULT_SURGICAL_PROC_TIME                                                                  | FRM_TIME_UTIL          | DAYCASE_THEATRE_UTIL, DAYCASE_THEATRE_ANNUAL_OPERATIONAL_HOURS               | ADULT_SURGICAL_DAYCASE_PROC_THEATRES                |
| THEATRES_DAYCASE_PROC           | Paediatric                       | CLASS_DAYCASE, CLASS_HAS_PROCEDURE, CLASS_AGE_CHILD                                              | DAYCASE_THEATRE_PAED_PROC_TIME                                                                            | FRM_TIME_UTIL          | DAYCASE_THEATRE_UTIL, DAYCASE_THEATRE_ANNUAL_OPERATIONAL_HOURS               | PAEDIATRIC_DAYCASE_PROC_THEATRES                    |
| THEATRES_INPATIENT_PROC         | Adult elective surgical          | CLASS_HAS_PROCEDURE, CLASS_AGE_ADULT, CLASS_ELECTIVE, MAP_SURGICAL                               | INPATIENT_THEATRE_ADULT_ELEC_SURGICAL_PROC_TIME                                                           | FRM_TIME_UTIL          | INPATIENT_THEATRE_UTIL, INPATIENT_THEATRE_ANNUAL_OPERATIONAL_HOURS           | ADULT_ELECTIVE_SURGICAL_INPATIENT_PROC_THEATRES     |
| THEATRES_INPATIENT_PROC         | Adult non-elective surgical      | CLASS_HAS_PROCEDURE, CLASS_AGE_ADULT, CLASS_NON_ELECTIVE, MAP_SURGICAL                           | INPATIENT_THEATRE_ADULT_NON_ELECTIVE_SURGICAL_PROC_TIME                                                   | FRM_TIME_UTIL          | INPATIENT_THEATRE_UTIL, INPATIENT_THEATRE_ANNUAL_OPERATIONAL_HOURS           | ADULT_NON_ELECTIVE_SURGICAL_INPATIENT_PROC_THEATRES |
| THEATRES_INPATIENT_PROC         | Paediatric elective              | CLASS_HAS_PROCEDURE, CLASS_AGE_CHILD, CLASS_ELECTIVE                                             | INPATIENT_THEATRE_CHILD_ELEC_SURGICAL_PROC_TIME                                                           | FRM_TIME_UTIL          | INPATIENT_THEATRE_UTIL, INPATIENT_THEATRE_ANNUAL_OPERATIONAL_HOURS           | PAEDIATRIC_ELECTIVE_INPATIENT_PROC_THEATRES         |
| THEATRES_INPATIENT_PROC         | Paediatric non-elective          | CLASS_HAS_PROCEDURE, CLASS_AGE_CHILD, CLASS_NON_ELECTIVE                                         | INPATIENT_THEATRE_CHILD_NON_ELECTIVE_SURGICAL_PROC_TIME                                                   | FRM_TIME_UTIL          | INPATIENT_THEATRE_UTIL, INPATIENT_THEATRE_ANNUAL_OPERATIONAL_HOURS           | PAEDIATRIC_NON_ELECTIVE_INPATIENT_PROC_THEATRES     |
| LABS_CARDIAC_CATH_PROC          | All groups                       | (CLASS_CARDIOLOGY AND CLASS_HAS_PROCEDURE) OR (CLASS_CARDIAC_CATH)                               | LABS_CARDIAC_CATH_PROC_TIME                                                                               | FRM_TIME_UTIL          | LABS_CARDIAC_CATH_UTIL, LABS_CARDIAC_CATH_ANNUAL_OPERATIONAL_HOURS           | CARDIAC_CATH_PROC_LABS                              |
| ROOMS_INT_RADIOLOGY_PROC        | All groups                       | CLASS_INT_RADIOLOGY, CLASS_HAS_PROCEDURE                                                         | INT_RADIOLOGY_PROC_TIME                                                                                   | FRM_TIME_UTIL          | INT_RADIOLOGY_PROC_UTIL, INT_RADIOLOGY_PROC_ANNUAL_OPERATIONAL_HOURS         | INT_RADIOLOGY_PROC_ROOMS                            |
</div>