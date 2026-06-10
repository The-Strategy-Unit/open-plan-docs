#### What is a theatre for daycase procedures

> A theatre for daycase procedures is a dedicated procedural operating space used to perform planned same-day surgical interventions that do not require an overnight hospital stay.

---
#### Capacity outputs
* ADULT_SURGICAL_DAYCASE_PROC_THEATRES
* PAEDIATRIC_DAYCASE_PROC_THEATRES
#### Conversion archetype
* time utilisation — FRM_TIME_UTIL
#### Operational constraint
* Schedulable procedural operating time

---
#### Activity classification logic

Excludes renal daycase, endoscopy daycase, and haematology-oncology daycase activity cohorts.

| Subgroup       | Classification IDs                                                  |
| -------------- | ------------------------------------------------------------------- |
| adult surgical | CLASS_DAYCASE, CLASS_HAS_PROCEDURE, CLASS_AGE_ADULT, CLASS_SURGICAL |
| paediatric     | CLASS_DAYCASE, CLASS_HAS_PROCEDURE, CLASS_AGE_CHILD                 |

---
#### Workload derivation

Primary workload object: procedure hours

$$\text{procedure hours} = \text{procedures} \times \frac{\text{procedure time minutes}} {60}$$

---
#### Capacity conversion

$$\text{required daycase theatres} = \frac{\text{procedure hours}} {\text{annual operational hours} \times \text{utilisation}}$$

---
#### Assumptions

| Subgroup       | Assumption               | Category    | Assumption ID                            |
| -------------- | ------------------------ | ----------- | ---------------------------------------- |
| adult surgical | procedure time           | workload    | DAYCASE_THEATRE_ADULT_SURGICAL_PROC_TIME |
| paediatric     | procedure time           | workload    | DAYCASE_THEATRE_PAEDIATRIC_PROC_TIME     |
| all groups     | utilisation              | operational | DAYCASE_THEATRE_UTIL                     |
| all groups     | annual operational hours | operational | DAYCASE_THEATRE_ANNUAL_OPERATIONAL_HOURS |

---
#### Known issues / limitations
* Exclusions must be applied consistently to avoid double-counting with renal, endoscopy and haematology/oncology daycase capacity domains.

---
#### Dependencies
* Requires exclusion of specialist activity in renal, endoscopy, and haematology/oncology daycase capacity domains.

---
#### Future enhancements

---
