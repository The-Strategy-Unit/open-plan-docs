#### What is a theatre for inpatient procedures

> A theatre for inpatient procedures is a dedicated operating space used to perform surgical interventions requiring admission to hospital and ongoing inpatient care following the procedure.

---
#### Capacity outputs
* ADULT_ELECTIVE_SURGICAL_INPATIENT_PROC_THEATRES  
* ADULT_NON_ELECTIVE_SURGICAL_INPATIENT_PROC_THEATRES  
* PAEDIATRIC_ELECTIVE_INPATIENT_PROC_THEATRES  
* PAEDIATRIC_NON_ELECTIVE_INPATIENT_PROC_THEATRES
#### Conversion archetype
* time utilisation — FRM_TIME_UTIL
#### Operational constraint
* Schedulable procedural operating time

---
#### Activity classification logic

Cardiac catheter and interventional radiology activity must be excluded from inpatient procedures activity used for the calculation of theatres, to avoid double-counting.


| Subgroup                    | Classification IDs                                                       |
| --------------------------- | ------------------------------------------------------------------------ |
| adult elective surgical     | CLASS_HAS_PROCEDURE, CLASS_AGE_ADULT, CLASS_ELECTIVE, CLASS_SURGICAL     |
| adult non-elective surgical | CLASS_HAS_PROCEDURE, CLASS_AGE_ADULT, CLASS_NON_ELECTIVE, CLASS_SURGICAL |
| paediatric elective         | CLASS_HAS_PROCEDURE, CLASS_AGE_CHILD, CLASS_ELECTIVE                     |
| paediatric non-elective     | CLASS_HAS_PROCEDURE, CLASS_AGE_CHILD, CLASS_NON_ELECTIVE                 |

---
#### Workload derivation

Primary workload object: procedure hours

$$\text{procedure hours} = \text{procedures} \times \frac{\text{procedure time minutes}} {60}$$

---
#### Capacity conversion

$$\text{required inpatient theatres} = \frac{\text{procedure hours}} {\text{annual operational hours} \times \text{utilisation}}$$

---
#### Assumptions

| Subgroup                    | Assumption               | Category    | Assumption ID                                                |
| --------------------------- | ------------------------ | ----------- | ------------------------------------------------------------ |
| adult elective surgical     | procedure time           | workload    | INPATIENT_THEATRE_ADULT_ELECTIVE_SURGICAL_PROC_TIME          |
| adult non-elective surgical | procedure time           | workload    | INPATIENT_THEATRE_ADULT_NON_ELECTIVE_SURGICAL_PROC_TIME      |
| paediatric elective         | procedure time           | workload    | INPATIENT_THEATRE_PAEDIATRIC_ELECTIVE_SURGICAL_PROC_TIME     |
| paediatric non-elective     | procedure time           | workload    | INPATIENT_THEATRE_PAEDIATRIC_NON_ELECTIVE_SURGICAL_PROC_TIME |
| all groups                  | utilisation              | operational | INPATIENT_THEATRE_UTIL                                       |
| all groups                  | annual operational hours | operational | INPATIENT_THEATRE_ANNUAL_OPERATIONAL_HOURS                   |

---
#### Known issues / limitations

---
#### Dependencies
* No dependencies.

---
#### Future enhancements

---
