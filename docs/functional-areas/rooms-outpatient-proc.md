#### What is an outpatient procedure room

> An outpatient procedure room is a clinical room where minor diagnostic or therapeutic procedures are performed on patients who do not require hospital admission or an overnight stay.

---
#### Capacity outputs
* OP_PROC_ROOMS
#### Conversion archetype
* appointment utilisation — FRM_APPOINTMENT_UTIL
#### Operational constraint
* Schedulable procedure room time

---
#### Activity classification logic

Outpatient attendances with a valid procedure code.

| Subgroup   | Classification IDs                   |
| ---------- | ------------------------------------ |
| all groups | CLASS_OP_ATTEND, CLASS_HAS_PROCEDURE |

---
#### Workload derivation

Primary workload object: procedure hours

$$\text{effective procedure time minutes} = \text{procedure time minutes} + (\text{DNA rate} \times \text{DNA time minutes})$$

$$\text{procedure hours} = \frac{\text{attendances} \times \text{effective procedure time minutes}} {60}$$

---
#### Capacity conversion

$$\text{required op procedure rooms} = \frac{\text{procedure hours}} {\text{annual operational hours} \times \text{utilisation}}$$

---
#### Assumptions

| Subgroup   | Assumption               | Category    | Assumption ID                    |
| ---------- | ------------------------ | ----------- | -------------------------------- |
| all groups | procedure time           | workload    | OP_PROC_TIME                     |
| all groups | DNA rate                 | workload    | OP_PROC_DNA_RATE                 |
| all groups | DNA time                 | workload    | OP_PROC_DNA_TIME                 |
| all groups | utilisation              | operational | OP_PROC_UTIL                     |
| all groups | annual operational hours | operational | OP_PROC_ANNUAL_OPERATIONAL_HOURS |

---
#### Known issues / limitations
* Outpatient procedure rooms are modelled as appointment-slot capacity rather than theatre-style procedural lists.
* Procedure durations are represented using a global average because procedure type is not currently visible.

---
#### Dependencies
* No dependencies.

---
#### Future enhancements

---
