#### What is an cardiac catheter laboratory

>A cardiac catheter laboratory (cath lab) is a specialised hospital facility where doctors use minimally invasive catheter-based procedures to diagnose and treat heart and blood vessel conditions.

---
#### Capacity outputs
* CARDIAC_CATH_PROC_LABS
#### Conversion archetype
* time utilisation — FRM_TIME_UTIL
#### Operational constraint
* Schedulable procedural operating time

---
#### Activity classification logic

All spells with a valid procedure code in cardiology (320) or paediatric cardiology (321) treatment specialties plus any spells in other specialties with the following primary procedure codes:

* K63 Contrast radiology of heart
* K75 Angioplasty
* K60 Cardiac pacemaker
* K62 Therapeutic transluminal operations on heart
* K59 Cardioverter defibrillator introduced through the vein
* K57 Other therapeutic transluminal operations on heart
* K73 Other cardiac pacemaker system through vein
* K49 Transluminal balloon angioplasty

| Branch             | Classification IDs                 |
| ------------------ | ---------------------------------- |
| cardiology         | CLASS_CARDIOLOGY, CLASS_HAS_PROC   |
| catheter procedure | CLASS_HAS_PROC, CLASS_CARDIAC_CATH |

Cardiac catheter procedure spells = branch 1 OR branch 2.

Branches should be combined as a de-duplicated OR cohort.

---
#### Workload derivation

Primary workload object: procedure hours

$$\text{procedure hours} = \text{procedures} \times \frac{\text{procedure time minutes}} {60}$$

---
#### Capacity conversion

$$\text{required cardiac cath labs} = \frac{\text{procedure hours}} {\text{annual operational hours} \times \text{utilisation}}$$

---
#### Assumptions

| Subgroup   | Assumption               | Category    | Assumption ID                              |
| ---------- | ------------------------ | ----------- | ------------------------------------------ |
| all groups | procedure time           | workload    | LABS_CARDIAC_CATH_PROC_TIME                     |
| all groups | utilisation              | operational | LABS_CARDIAC_CATH_UTIL                     |
| all groups | annual operational hours | operational | LABS_CARDIAC_CATH_ANNUAL_OPERATIONAL_HOURS |

---
#### Known issues / limitations
* Some included procedures, such as pacemaker insertion, may be undertaken outside a cardiac catheter laboratory depending on local service configuration.

---
#### Dependencies
* No dependencies.

---
#### Future enhancements

---
