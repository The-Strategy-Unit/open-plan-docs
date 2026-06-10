#### What is a bed on a maternity ward

> A bed on a maternity ward is a hospital bed used for the ongoing care, treatment, recovery, and overnight stay of pregnant or postnatal patients admitted for maternity care.

---
#### Capacity outputs
* MATERNITY_WARD_BEDS
#### Conversion archetype
* bed occupancy — FRM_BED_OCCUPANCY
#### Operational constraint
* Continuous occupancy over 24-hour operational periods

---
#### Activity classification logic

Maternity birth spells typically consist of:

* prenatal admission 
* time in delivery room or time in theatre (C-section)
* postnatal time in ward bed

All spells with a birth episode flag are categorised by type of delivery to one of four groups. Zero-day admissions require special treatment as these admissions don't generate overnight bed-days.

| Subgroup               | Classification IDs                                                     |
| ---------------------- | ---------------------------------------------------------------------- |
| normal delivery        | CLASS_MATERNITY, CLASS_BIRTH_EVENT, CLASS_BIRTH_NORMAL                 |
| assisted delivery      | CLASS_MATERNITY, CLASS_BIRTH_EVENT, CLASS_BIRTH_ASSISTED               |
| elective C-section     | CLASS_MATERNITY, CLASS_BIRTH_EVENT, CLASS_BIRTH_ELECTIVE_C_SECTION     |
| non-elective C-section | CLASS_MATERNITY, CLASS_BIRTH_EVENT, CLASS_BIRTH_NON_ELECTIVE_C_SECTION |

Also included are overnight spells on a maternity ward with no recorded birth event.

| Subgroup                 | Classification IDs                                        |
| ------------------------ | --------------------------------------------------------- |
| overnight no birth event | CLASS_MATERNITY, CLASS_NON_ZERO_LOS, CLASS_NO_BIRTH_EVENT |

---
#### Workload derivation

Primary workload unit: ward bed days

$$\text{zero day bed days} = \text{zero day spells} \times \frac{\text{zero day LOS hours}} {24}$$

$$\text{birth related ward bed days} = \text{birth spell overnight bed days} + \text{zero day bed days} - \text{birth room bed days}$$

$$\text{no birth ward bed days} = \text{no birth spell overnight bed days}$$

$$\text{total ward bed days} = \text{birth related ward bed days} + \text{no birth ward bed days}$$

---
#### Capacity conversion

$$\text{required maternity ward beds} = \frac{\text{total ward bed days}} {\text{annual operational days} \times \text{occupancy}}$$

---
#### Assumptions

| Subgroup               | Assumption              | Category    | Assumption ID                                      |
| ---------------------- | ----------------------- | ----------- | -------------------------------------------------- |
| normal delivery        | zero day LOS            | workload    | MATERNITY_WARD_NORMAL_DELIVERY_ZERO_DAY_LOS        |
| assisted delivery      | zero day LOS            | workload    | MATERNITY_WARD_ASSISTED_DELIVERY_ZERO_DAY_LOS      |
| elective C-section     | zero day LOS            | workload    | MATERNITY_WARD_ELECTIVE_CSECTION_ZERO_DAY_LOS      |
| non-elective C-section | zero day LOS            | workload    | MATERNITY_WARD_NON_ELECTIVE_C_SECTION_ZERO_DAY_LOS |
| all groups             | occupancy               | operational | MATERNITY_WARD_OCC                                 |
| all groups             | annual operational days | operational | MATERNITY_WARD_ANNUAL_OPERATIONAL_DAYS             |

---
#### Known issues / limitations
* LDR/LDRP service models may alter the allocation of time between birthing rooms and maternity ward beds.

---
#### Dependencies
*  Birth room bed-days are calculated in ROOMS_MATERNITY_BIRTH and deducted from birth-related maternity ward workload to avoid double-counting.

---
#### Future enhancements

---
