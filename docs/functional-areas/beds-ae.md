---
title: Beds A&E
---

#### What is an AE bed?

> An A&E bed is a trolley-based treatment space within the Emergency Department used to assess, monitor and manage patients requiring higher-acuity or more prolonged emergency care.

---
#### Capacity outputs
* ADULT_MAJOR_AE_BEDS
* CHILD_MAJOR_AE_BEDS
* RESUS_AE_BEDS
#### Conversion archetype
* flow-space occupancy — FRM_FLOW_SPACE
#### Operational constraint
* Concurrent occupancy over operational periods

---
#### Activity classification logic

Department type 01 only (consultant-led 24/7 with full resuscitation facilities).
Majors are defined with: Acuity = 2.
Resuscitation cases are defined with: Acuity = 1.

| Level | Description          |
| ----- | -------------------- |
| 1     | Immediate care level |
| 2     | Very urgent level    |
| 3     | Urgent level         |
| 4     | Standard level       |
| 5     | Low acuity level     |

| Subgroup    | Classification IDs                        |
| ----------- | ----------------------------------------- |
| adult major | CLASS_AE, CLASS_AGE_ADULT, CLASS_AE_MAJOR |
| child major | CLASS_AE, CLASS_AGE_CHILD, CLASS_AE_MAJOR |
| resus       | CLASS_AE, CLASS_AE_RESUS                  |

---
#### Workload derivation

Primary workload object: occupancy hours

$$\text{occupancy hours} = \text{attendances} \times \frac{\text{LOS minutes}} {60}$$

---
#### Capacity conversion

$$\text{required A&E beds} = \frac{\text{occupancy hours}} {\text{annual operational hours} \times \text{utilisation}}$$

---
#### Assumptions

| Subgroup      | Assumption               | Category    | Assumption ID                    |
| ------------- | ------------------------ | ----------- | -------------------------------- |
| adult major   | LOS                      | workload    | AE_ADULT_MAJOR_LOS               |
| adult major   | utilisation              | operational | AE_ADULT_MAJOR_UTIL              |
| child major   | LOS                      | workload    | AE_CHILD_MAJOR_LOS               |
| child major   | utilisation              | operational | AE_CHILD_MAJOR_UTIL              |
| resuscitation | LOS                      | workload    | AE_RESUS_LOS                     |
| resuscitation | utilisation              | operational | AE_RESUS_UTIL                    |
| all groups    | annual operational hours | operational | AE_BEDS_ANNUAL_OPERATIONAL_HOURS |

---
#### Known issues / limitations
* Type 02 mono-specialty A&E out-of-scope in current development plan.

---
#### Dependencies
* No dependencies.

---
#### Future enhancements
* Obvious candidate for queueing methods.

---
