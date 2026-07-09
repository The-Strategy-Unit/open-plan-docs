#### What is an inpatient assessment bed

> An inpatient assessment bed is a hospital bed used for the short-term assessment, monitoring, and initial management of patients who require evaluation before admission, transfer, or discharge decisions are made.

---
#### Capacity outputs
* ADULT_INPATIENT_ASSESSMENT_BEDS  
* PAEDIATRIC_INPATIENT_ASSESSMENT_BEDS
#### Conversion archetype
* bed occupancy — FRM_BED_OCCUPANCY
#### Operational constraint
* Continuous occupancy over 24-hour operational periods

---
#### Activity classification logic

All non-elective inpatient spells are assumed to consume assessment-bed capacity prior to transfer to downstream inpatient services.

| Subgroup                         | Classification IDs                                       |
| -------------------------------- | -------------------------------------------------------- |
| adult non-elective medical       | CLASS_AGE_ADULT, CLASS_NON_ELECTIVE, CLASS_MEDICAL       |
| adult non-elective surgical      | CLASS_AGE_ADULT, CLASS_NON_ELECTIVE, CLASS_SURGICAL      |
| paediatric non-elective medical  | CLASS_AGE_PAEDIATRIC, CLASS_NON_ELECTIVE, CLASS_MEDICAL  |
| paediatric non-elective surgical | CLASS_AGE_PAEDIATRIC, CLASS_NON_ELECTIVE, CLASS_SURGICAL |

---
#### Workload derivation

Primary workload object: assessment bed days

$$\text{assessment bed days} = \text{non elective spells} \times \frac{\text{assessment los minutes}} {1440}$$

---
#### Capacity conversion

$$\text{required assessment beds} =  \frac{\text{assessment bed days}} {\text{annual operational days} \times \text{occupancy}}$$

---
#### Assumptions

| Subgroup                         | Assumption              | Category    | Assumption ID                                             |
| -------------------------------- | ----------------------- | ----------- | --------------------------------------------------------- |
| adult non-elective medical       | assessment LOS          | workload    | INPATIENT_ASSESSMENT_ADULT_NON_ELECTIVE_MEDICAL_LOS       |
| adult non-elective surgical      | assessment LOS          | workload    | INPATIENT_ASSESSMENT_ADULT_NON_ELECTIVE_SURGICAL_LOS      |
| paediatric non-elective medical  | assessment LOS          | workload    | INPATIENT_ASSESSMENT_PAEDIATRIC_NON_ELECTIVE_MEDICAL_LOS  |
| paediatric non-elective surgical | assessment LOS          | workload    | INPATIENT_ASSESSMENT_PAEDIATRIC_NON_ELECTIVE_SURGICAL_LOS |
| adult                            | occupancy               | operational | INPATIENT_ASSESSMENT_ADULT_OCC                            |
| paediatric                       | occupancy               | operational | INPATIENT_ASSESSMENT_PAEDIATRIC_OCC                       |
| all groups                       | annual operational days | operational | INPATIENT_ASSESSMENT_ANNUAL_OPERATIONAL_DAYS              |

---
#### Known issues / limitations
* All non-elective inpatient spells are assumed to consume assessment-bed capacity prior to transfer to downstream inpatient services.

---
#### Dependencies
* Assessment bed-days are deducted from downstream inpatient ward workload to avoid double-counting.

---
#### Future enhancements
* Assessment-bed utilisation is currently inferred from non-elective inpatient activity. Future work should assess whether dedicated assessment-unit activity datasets can support direct estimation of assessment workload.

---
