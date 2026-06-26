#### What is an outpatient virtual consultation room

> An outpatient virtual consultation room is a digital or technology-enabled space used for remote consultations between patients and healthcare professionals without requiring an in-person hospital visit.

---
#### Capacity outputs
* OP_VIRTUAL_CONSULT_ROOMS
#### Conversion archetype
* appointment utilisation — FRM_APPOINTMENT_UTIL
#### Operational constraint
* Schedulable clinic consultation time

---
#### Activity classification logic

Outpatient virtual consultations.

| Subgroup   | Classification IDs                |
| ---------- | --------------------------------- |
| all groups | CLASS_OP_ATTEND, CLASS_OP_VIRTUAL |

---
#### Workload derivation

Primary workload object: consultation hours

$$\text{effective consult time minutes} = \text{consult time minutes} + (\text{DNA rate} \times \text{DNA time minutes})$$

$$\text{consultation hours} = \frac{\text{attendances} \times \text{effective consult time minutes}} {60}$$

---
#### Capacity conversion

$$\text{required op virtual consultation rooms} = \frac{\text{consultation hours}} {\text{annual operational hours} \times \text{utilisation}}$$

---
#### Assumptions

| Subgroup   | Assumption               | Category    | Assumption ID                               |
| ---------- | ------------------------ | ----------- | ------------------------------------------- |
| all groups | consult time             | workload    | OP_VIRTUAL_CONSULT_TIME                     |
| all groups | DNA rate                 | workload    | OP_VIRTUAL_CONSULT_DNA_RATE                 |
| all groups | DNA time                 | workload    | OP_VIRTUAL_CONSULT_DNA_TIME                 |
| all groups | utilisation              | operational | OP_VIRTUAL_CONSULT_UTIL                     |
| all groups | annual operational hours | operational | OP_VIRTUAL_CONSULT_ANNUAL_OPERATIONAL_HOURS |

---
#### Known issues / limitations
* Consultation durations are represented using subgroup-level averages and may not reflect variation between specialties.

---
#### Dependencies
* No dependencies.

---
#### Future enhancements
* Explore specialty-specific consultation times and DNA assumptions.
* Assess whether clinician capacity rather than virtual-room capacity provides a more appropriate representation of the service.

---
