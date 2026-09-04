#### What is a theatre for obstetric procedures

> A theatre for obstetric procedures is a dedicated operating space used to perform childbirth-related surgical and procedural interventions, typically within labour ward or maternity services.

---
#### Capacity outputs
* OBSTETRIC_PROC_THEATRES
#### Conversion archetype
* time utilisation — FRM_TIME_UTIL
#### Operational constraint
* Schedulable procedural operating time

---
#### Activity classification logic

Cases requiring an obstetric theatre are defined as: maternity spells with a birth episode and a primary procedure code of:

* R17 elective C-section delivery or
* R18 other C-section delivery

| Branch                 | Classification IDs                                              |
| ---------------------- | --------------------------------------------------------------- |
| elective C-section     | CLASS_MATERNITY, CLASS_BIRTH_EVENT, CLASS_BIRTH_ELECTIVE_CSECTION    |
| non-elective C-section | CLASS_MATERNITY, CLASS_BIRTH_EVENT, CLASS_BIRTH_NON_ELECTIVE_CSECTION |

Obstetric theatre procedures = branch 1 OR branch 2

---
#### Workload derivation

Primary workload object: procedure hours

$$\text{procedure hours} = \text{procedures} \times \frac{\text{procedure time minutes}} {60}$$

---
#### Capacity conversion

$$\text{required obstetric theatres} = \frac{\text{procedure hours}} {\text{annual operational hours} \times \text{utilisation}}$$

---
#### Assumptions

| Subgroup   | Assumption               | Category    | Assumption ID                              |
| ---------- | ------------------------ | ----------- | ------------------------------------------ |
| all groups | procedure time           | workload    | OBSTETRIC_THEATRE_PROC_TIME                |
| all groups | utilisation              | operational | OBSTETRIC_THEATRE_UTIL                     |
| all groups | annual operational hours | operational | OBSTETRIC_THEATRE_ANNUAL_OPERATIONAL_HOURS |

---
#### Known issues / limitations
* Current implementation includes caesarean section activity only.
* Obstetric theatres must be available 24/7 to support emergency activity. For capacity planning purposes, only the assumed planned operating period (14 hours per day) contributes to modelled capacity. Overnight availability is treated as emergency reserve capacity and is excluded from planned throughput calculations.

---
#### Dependencies
* No dependencies.

---
#### Future enhancements
* Extend activity scope beyond caesarean section procedures where suitable obstetric theatre activity data becomes available.

---

