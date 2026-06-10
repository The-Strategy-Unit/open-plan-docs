#### What is an interventional radiology procedure room

> An interventional radiology procedure room is a specialised clinical room where image-guided minimally invasive procedures are performed to diagnose and treat medical conditions using techniques such as X-ray, ultrasound, CT, or MRI guidance.

---
#### Capacity outputs
* INT_RADIOLOGY_PROC_ROOMS
#### Conversion archetype
* time utilisation — FRM_TIME_UTIL
#### Operational constraint
* Schedulable procedural operating time

---
#### Activity classification logic

All spells in treatment specialty interventional radiology (811) or paediatric interventional radiology (280) with a valid procedure.

| Subgroup   | Classification IDs                  |
| ---------- | ----------------------------------- |
| all groups | CLASS_INT_RADIOLOGY, CLASS_HAS_PROC |

---
#### Workload derivation

Primary workload object: procedure hours

$$\text{procedure hours} = \text{procedures} \times \frac{\text{procedure time minutes}} {60}$$

---
#### Capacity conversion

$$\text{required interventional radiology rooms} = \frac{\text{procedure hours}} {\text{annual operational hours} \times \text{utilisation}}$$

---
#### Assumptions

| Subgroup   | Assumption               | Category    | Assumption ID                               |
| ---------- | ------------------------ | ----------- | ------------------------------------------- |
| all groups | procedure time           | workload    | INT_RADIOLOGY_PROC_TIME                     |
| all groups | utilisation              | operational | INT_RADIOLOGY_PROC_UTIL                     |
| all groups | annual operational hours | operational | INT_RADIOLOGY_PROC_ANNUAL_OPERATIONAL_HOURS |

---
#### Known issues / limitations

---
#### Dependencies
* No dependencies.

---
#### Future enhancements

---
