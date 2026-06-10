#### What is a maternity assessment bed

> A maternity assessment bed is a hospital bed used for the assessment, monitoring, and short-term care of pregnant or postnatal patients requiring evaluation before admission, transfer, or discharge decisions are made.

---
#### Capacity outputs
* MATERNITY_ASSESSMENT_BEDS
#### Conversion archetype
* recovery occupancy — FRM_RECOVERY_OCCUPANCY
#### Operational constraint
* Temporary occupancy with intra-day turnover

---
#### Activity classification logic

Maternity assessment activity is defined as zero-day maternity spells without a recorded birth event. Zero-day admissions require special treatment as these admissions don't generate overnight bed-days.

| Subgroup   | Classification IDs                                   |
| ---------- | ---------------------------------------------------- |
| all groups | CLASS_MATERNITY, CLASS_ZERO_DAY, CLASS_NO_BIRTH_FLAG |

---
#### Workload derivation

Primary workload object: occupancy hours

$$\text{occupancy hours} = \text{zero day spells} \times \text{zero day LOS hours}$$

Equivalent to converting fractional zero-day bed-days back into hours.

---
#### Capacity conversion

$$\text{required maternity assessment beds} = \frac{\text{occupancy hours}} {\text{annual operational hours} \times \text{occupancy}}$$

---
#### Assumptions

| Subgroup   | Assumption               | Category    | Assumption ID                                 |
| ---------- | ------------------------ | ----------- | --------------------------------------------- |
| all groups | zero day LOS             | workload    | MATERNITY_ASSESSMENT_ZERO_DAY_LOS             |
| all groups | occupancy                | operational | MATERNITY_ASSESSMENT_OCC                      |
| all groups | annual operational hours | operational | MATERNITY_ASSESSMENT_ANNUAL_OPERATIONAL_HOURS |

---
#### Known issues / limitations

---
#### Dependencies
* No dependencies.

---
#### Future enhancements

---
