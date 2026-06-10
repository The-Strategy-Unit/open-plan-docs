#### What is a haematology/oncology treatment space

> A haematology/oncology treatment space is a specialised clinical area where patients receive diagnostic procedures and treatments related to blood disorders and cancer, such as chemotherapy, transfusions, biopsies, or supportive care.

---
#### Capacity outputs
* HAEM_ONC_TRT_SPACES
#### Conversion archetype
* treatment time utilisation — FRM_TIME_UTIL
#### Operational constraint
* Schedulable treatment-space time

---
#### Activity classification logic

Daycase spells with a valid procedure code in haematology (253, 303) or oncology (260, 370, 800) treatment specialties.

| Subgroup   | Classification IDs                                 |
| ---------- | -------------------------------------------------- |
| all groups | CLASS_DAYCASE, CLASS_HAEM_ONC, CLASS_HAS_PROCEDURE |

---
#### Workload derivation

One eligible daycase procedure is assumed to represent one treatment-space attendance.

Primary workload object: treatment hours

$$\text{treatment hours} = \text{procedures} \times \frac{\text{treatment time minutes}} {60}$$

---
#### Capacity conversion

$$\text{required haem onc treatment spaces} = \frac{\text{treatment hours}} {\text{annual operational hours} \times \text{utilisation}}$$

---
#### Assumptions

| Subgroup   | Assumption               | Category    | Assumption ID                     |
| ---------- | ------------------------ | ----------- | --------------------------------- |
| all groups | treatment time           | workload    | HAEM_ONC_TREATMENT_TIME           |
| all groups | utilisation              | operational | HAEM_ONC_TREATMENT_UTIL           |
| all groups | annual operational hours | operational | HAEM_ONC_ANNUAL_OPERATIONAL_HOURS |

---
#### Known issues / limitations
* Current implementation identifies activity using haematology and oncology treatment specialties with a valid procedure code. Further validation is required to determine whether the intended scope is broader haematology/oncology daycase activity or specifically Systemic Anti-Cancer Therapy (SACT).

---
#### Dependencies
* No dependencies.

---
#### Future enhancements

---
