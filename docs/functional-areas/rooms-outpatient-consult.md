#### What is an outpatient consultation room

> An outpatient consultation room is a clinical space where patients meet healthcare professionals for assessments, advice, diagnosis, follow-up care, and treatment planning without being admitted to hospital.

---
#### Capacity outputs
* FIRST_OP_CONSULT_ROOMS  
* FOLLOW_UP_OP_CONSULT_ROOMS
#### Conversion archetype
* appointment utilisation — FRM_APPOINTMENT_UTIL
#### Operational constraint
* Schedulable clinic consultation time

---
#### Activity classification logic

Outpatient face-to-face consultations sub-divided by first and follow-up.

| Subgroup             | Classification IDs                                         |
| -------------------- | ---------------------------------------------------------- |
| first attendance     | CLASS_OP_ATTEND, CLASS_OP_FACE_TO_FACE, CLASS_OP_FIRST     |
| follow-up attendance | CLASS_OP_ATTEND, CLASS_OP_FACE_TO_FACE, CLASS_OP_FOLLOW_UP |

---
#### Workload derivation

Primary workload object: consultation hours

$$\text{effective consult time minutes} = \text{consult time minutes} + (\text{DNA rate} \times \text{DNA time minutes})$$

$$\text{consultation hours} = \frac{\text{attendances} \times \text{effective consult time minutes}} {60}$$

---
#### Capacity conversion

$$\text{required op consultation rooms} = \frac{\text{consultation hours}} {\text{annual operational hours} \times \text{utilisation}}$$

---
#### Assumptions

| Subgroup             | Assumption               | Category    | Assumption ID                       |
| -------------------- | ------------------------ | ----------- | ----------------------------------- |
| first attendance     | consult time             | workload    | OP_CONSULT_FIRST_TIME               |
| first attendance     | DNA rate                 | workload    | OP_CONSULT_FIRST_DNA_RATE           |
| first attendance     | DNA time                 | workload    | OP_CONSULT_FIRST_DNA_TIME           |
| follow-up attendance | consult time             | workload    | OP_CONSULT_FOLLOW_UP_TIME           |
| follow-up attendance | DNA rate                 | workload    | OP_CONSULT_FOLLOW_UP_DNA_RATE       |
| follow-up attendance | DNA time                 | workload    | OP_CONSULT_FOLLOW_UP_DNA_TIME       |
| all groups           | utilisation              | operational | OP_CONSULT_UTIL                     |
| all groups           | annual operational hours | operational | OP_CONSULT_ANNUAL_OPERATIONAL_HOURS |

---
#### Known issues / limitations
* Consultation durations are represented using subgroup-level averages and may not reflect variation between specialties.

---
#### Dependencies
* No dependencies.

---
#### Future enhancements
* Explore specialty-specific consultation times and DNA assumptions.

---
