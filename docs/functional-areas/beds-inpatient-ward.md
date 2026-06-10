#### What is an inpatient ward bed

> An inpatient ward bed is a hospital bed used for the ongoing care, treatment, and overnight stay of patients admitted to a hospital ward.

---
#### Capacity outputs
* ADULT_ELECTIVE_INPATIENT_WARD_BEDS (SUM of adult elective medical and surgical ward beds)
* ADULT_NON_ELECTIVE_INPATIENT_WARD_BEDS (SUM of adult non-elective medical and surgical ward beds)
* PAEDIATRIC_INPATIENT_WARD_BEDS (SUM of all paediatric ward beds)
#### Conversion archetype
* bed occupancy — FRM_BED_OCCUPANCY
#### Operational constraint
* Continuous occupancy over 24-hour operational periods

---
#### Activity classification logic

Ward bed requirements are calculated from inpatient bed-days remaining after workload allocated to specialist settings such as assessment beds and critical care has been removed. Ward beds also include an adjustment for zero day admissions as these admissions don't generate overnight bed-days.

| Subgroup                         | Classification IDs                                  |
| -------------------------------- | --------------------------------------------------- |
| adult elective medical           | CLASS_AGE_ADULT, CLASS_ELECTIVE, CLASS_MEDICAL      |
| adult elective surgical          | CLASS_AGE_ADULT, CLASS_ELECTIVE, CLASS_SURGICAL     |
| adult non-elective medical       | CLASS_AGE_ADULT, CLASS_NON_ELECTIVE, CLASS_MEDICAL  |
| adult non-elective surgical      | CLASS_AGE_ADULT, CLASS_NON_ELECTIVE, CLASS_SURGICAL |
| paediatric elective medical      | CLASS_AGE_CHILD, CLASS_ELECTIVE, CLASS_MEDICAL      |
| paediatric elective surgical     | CLASS_AGE_CHILD, CLASS_ELECTIVE, CLASS_SURGICAL     |
| paediatric non-elective medical  | CLASS_AGE_CHILD, CLASS_NON_ELECTIVE, CLASS_MEDICAL  |
| paediatric non-elective surgical | CLASS_AGE_CHILD, CLASS_NON_ELECTIVE, CLASS_SURGICAL |

---
#### Workload derivation

Primary workload object: ward bed days

For each subgroup:

$$\text{zero day bed days} = \text{zero day spells} \times \frac{\text{zero day los hours}} {24}$$

$$\text{ward bed days} = \text{overnight bed days} + \text{zero day bed days} - \text{assessment bed days} - \text{critical care bed days}$$

Assessment bed-days are deducted only from non-elective subgroups. Critical care bed-days are deducted where workload has been allocated to critical care.

---
#### Capacity conversion
Required ward beds are aggregated for (1) adult elective, (2) adult non-elective, and (3) all paediatric subgroups.

$$\text{required ward beds} = \frac{\text{ward bed days}} {\text{annual operational days} \times \text{occupancy}}$$

---
#### Assumptions

| Subgroup                         | Assumption              | Category    | Assumption ID                                 |
| -------------------------------- | ----------------------- | ----------- | --------------------------------------------- |
| adult elective medical           | zero day LOS            | workload    | WARD_ADULT_ELECTIVE_MEDICAL_ZERO_DAY_LOS      |
| adult elective surgical          | zero day LOS            | workload    | WARD_ADULT_ELECTIVE_SURGICAL_ZERO_DAY_LOS     |
| adult non-elective medical       | zero day LOS            | workload    | WARD_ADULT_NON_ELECTIVE_MEDICAL_ZERO_DAY_LOS  |
| adult non-elective surgical      | zero day LOS            | workload    | WARD_ADULT_NON_ELECTIVE_SURGICAL_ZERO_DAY_LOS |
| paediatric elective medical      | zero day LOS            | workload    | WARD_PAED_ELECTIVE_MEDICAL_ZERO_DAY_LOS       |
| paediatric elective surgical     | zero day LOS            | workload    | WARD_PAED_ELECTIVE_SURGICAL_ZERO_DAY_LOS      |
| paediatric non-elective medical  | zero day LOS            | workload    | WARD_PAED_NON_ELECTIVE_MEDICAL_ZERO_DAY_LOS   |
| paediatric non-elective surgical | zero day LOS            | workload    | WARD_PAED_NON_ELECTIVE_SURGICAL_ZERO_DAY_LOS  |
| adult elective                   | occupancy               | operational | WARD_ADULT_ELECTIVE_OCC                       |
| adult non-elective               | occupancy               | operational | WARD_ADULT_NON_ELECTIVE_OCC                   |
| paediatric                       | occupancy               | operational | WARD_PAEDIATRIC_OCC                           |
| all groups                       | annual operational days | operational | WARD_ANNUAL_OPERATIONAL_DAYS                  |

---
#### Known issues / limitations
* Ward capacity is dependent on the correctness of upstream assessment bed-day and critical care bed-day allocations.
* Zero-day admissions require explicit conversion into fractional bed-days because they do not generate overnight bed-days.
* Spell-level modelling may not fully capture transfers between assessment, ward and critical care settings. This may understate capacity requirements where transfer-day overlap results in simultaneous occupancy of multiple capacity domains.

---
#### Dependencies
* Depends on assessment bed-day and critical care bed-day allocations.

---
#### Future enhancements

---
