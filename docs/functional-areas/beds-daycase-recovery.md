#### What is a daycase recovery bed

> A daycase recovery bed is a short-stay recovery space used to monitor and care for patients following daycase procedures before discharge, typically within dedicated surgical or procedural recovery areas.

---
#### Capacity outputs
* ADULT_MEDICAL_DAYCASE_RECOVERY_BEDS
* ADULT_SURGICAL_DAYCASE_RECOVERY_BEDS
* PAEDIATRIC_MEDICAL_DAYCASE_RECOVERY_BEDS
* PAEDIATRIC_SURGICAL_DAYCASE_RECOVERY_BEDS
#### Conversion archetype
* recovery occupancy — FRM_RECOVERY_OCCUPANCY
#### Operational constraint
* Temporary occupancy with intra-day turnover

---
#### Activity classification logic

Daycase spells by medical/surgical treatment specialties. Specialist renal, endoscopy, and haematology/oncology daycase activity is excluded.

| Subgroup            | Classification IDs                             |
| ------------------- | ---------------------------------------------- |
| adult medical       | CLASS_DAYCASE, CLASS_AGE_ADULT, CLASS_MEDICAL  |
| adult surgical      | CLASS_DAYCASE, CLASS_AGE_ADULT, CLASS_SURGICAL |
| paediatric medical  | CLASS_DAYCASE, CLASS_AGE_CHILD, CLASS_MEDICAL  |
| paediatric surgical | CLASS_DAYCASE, CLASS_AGE_CHILD, CLASS_SURGICAL |

---
#### Workload derivation

Primary workload object: occupancy hours

$$\text{occupancy hours} = \text{daycase spells} \times \frac{\text{recovery time minutes}} {60}$$

---
#### Capacity conversion

$$\text{required daycase recovery beds} = \frac{\text{occupancy hours}} {\text{annual operational hours} \times \text{occupancy}}$$

---
#### Assumptions

| Subgroup            | Assumption               | Category    | Assumption ID                             |
|---------------------|--------------------------|-------------|-------------------------------------------|
| adult medical       | recovery LOS             | workload    | DAYCASE_RECOVERY_ADULT_MEDICAL_LOS        |
| adult medical       | occupancy                | operational | DAYCASE_RECOVERY_ADULT_MEDICAL_OCC        |
| adult surgical      | recovery LOS             | workload    | DAYCASE_RECOVERY_ADULT_SURGICAL_LOS       |
| adult surgical      | occupancy                | operational | DAYCASE_RECOVERY_ADULT_SURGICAL_OCC       |
| paediatric medical  | recovery LOS             | workload    | DAYCASE_RECOVERY_PAEDIATRIC_MEDICAL_LOS   |
| paediatric medical  | occupancy                | operational | DAYCASE_RECOVERY_PAEDIATRIC_MEDICAL_OCC   |
| paediatric surgical | recovery LOS             | workload    | DAYCASE_RECOVERY_PAEDIATRIC_SURGICAL_TIME |
| paediatric surgical | occupancy                | operational | DAYCASE_RECOVERY_PAEDIATRIC_SURGICAL_OCC  |
| all groups          | annual operational hours | operational | DAYCASE_RECOVERY_ANNUAL_OPERATIONAL_HOURS |

---
#### Known issues / limitations
* Exclusions must be applied consistently to avoid double-counting with renal, endoscopy and haematology/oncology daycase capacity domains.

---
#### Dependencies
* Requires exclusion of specialist activity in renal, endoscopy, and haematology/oncology daycase capacity domains.

---
#### Future enhancements

---
