#### What is a maternity birthing room

> A maternity birthing room is a specialised hospital room where patients receive care and support during labour, childbirth, and the immediate postnatal period.

---
#### Capacity outputs
* NORMAL_DELIVERY_MATERNITY_BIRTH_ROOMS  
* ASSISTED_DELIVERY_MATERNITY_BIRTH_ROOMS  
* NON_ELECTIVE_C_SECTION_MATERNITY_BIRTH_ROOMS
#### Conversion archetype
* bed occupancy — FRM_BED_OCCUPANCY
#### Operational constraint
* Continuous occupancy of birthing rooms over 24-hour operational periods

---
#### Activity classification logic

Maternity birth spells typically consist of:

* prenatal admission 
* time in delivery room or time in theatre (C-section)
* postnatal time in ward bed

All spells with a birth episode flag are categorised by type of delivery to one of four groups. Only three groups are used here as elective C-sections generate no time in birth room.

| Subgroup               | Classification IDs                                                    |
| ---------------------- | --------------------------------------------------------------------- |
| normal delivery        | CLASS_MATERNITY, CLASS_BIRTH_EVENT, CLASS_BIRTH_NORMAL                |
| assisted delivery      | CLASS_MATERNITY, CLASS_BIRTH_EVENT, CLASS_BIRTH_ASSISTED              |
| non-elective C-section | CLASS_MATERNITY, CLASS_BIRTH_EVENT, CLASS_BIRTH_NONELECTIVE_C_SECTION |

---
#### Workload derivation

Primary workload object: birth room bed days

$$\text{birth room bed days} = \text{birth spells} \times \frac{\text{birth room LOS minutes}} {1440}$$

---
#### Capacity conversion

$$\text{required birthing rooms} = \frac{\text{birth room bed days}} {\text{annual operational days} \times \text{occupancy}}$$

---
#### Assumptions

| Subgroup               | Assumption              | Category    | Assumption ID                                  |
| ---------------------- | ----------------------- | ----------- | ---------------------------------------------- |
| normal delivery        | LOS                     | workload    | MATERNITY_NORMAL_DELIVERY_BIRTH_ROOM_LOS       |
| assisted delivery      | LOS                     | workload    | MATERNITY_ASSISTED_DELIVERY_BIRTH_ROOM_LOS     |
| non-elective C-section | LOS                     | workload    | MATERNITY_NONELECTIVE_C_SECTION_BIRTH_ROOM_LOS |
| all groups             | occupancy               | operational | MATERNITY_BIRTH_ROOM_OCC                       |
| all groups             | annual operational days | operational | MATERNITY_BIRTH_ROOM_ANNUAL_OPERATIONAL_DAYS   |

---
#### Known issues / limitations
* LDR/LDRP service models may alter the allocation of time between birthing rooms and maternity ward beds.

---
#### Dependencies
* Birth spells also generate capacity in BEDS_MATERNITY_WARD.
* Separate modelling of obstetric theatre capacity for C-section activity.

---
#### Future enhancements

---
