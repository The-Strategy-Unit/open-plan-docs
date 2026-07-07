#### What is an endoscopy daycase recovery bed?

> An endoscopy daycase recovery bed is a short-stay recovery space used to monitor and care for patients following endoscopic procedures before discharge, typically within dedicated endoscopy recovery areas.

---
#### Capacity outputs
* DAYCASE_ENDOSCOPY_RECOVERY_BEDS
#### Conversion archetype
* recovery occupancy — FRM_RECOVERY_OCCUPANCY
#### Operational constraint
* Temporary occupancy with intra-day turnover

---
#### Activity classification logic

Daycase spells with the following primary procedure codes:

* Oesophagoscopy G14, G15, G16, G17, G18, G19, G20
* OGD G42, G43, G44, G45, G46
* Duodenoscopy G54, G55
* Jejunoscopy G64, G65
* Ileoscopy G79,G80
* Sigmoidoscopy H23, H24, H25, H26, H27, H28, H37, H69, H70, H71
* ERCP J38, J39, J40, J41, J42, J43, J44, J45
* Colonoscopy H20, H21, H22, H68
* Bronchoscopy E48, E49, E50, E51

| Subgroup   | Classification IDs             |
| ---------- | ------------------------------ |
| all groups | CLASS_DAYCASE, CLASS_ENDOSCOPY |

---
#### Workload derivation

Primary workload object: occupancy hours

$$\text{occupancy hours} = \text{daycase spells} \times \frac{\text{recovery time minutes}} {60}$$

----
#### Capacity conversion

$$\text{required daycase endoscopy recovery beds} = \frac{\text{occupancy hours}} {\text{annual operational hours} \times \text{occupancy}}$$

---
#### Assumptions

| Subgroup   | Assumption               | Category    | Assumption ID                                       |
|------------|--------------------------|-------------|-----------------------------------------------------|
| all groups | recovery LOS             | workload    | DAYCASE_ENDOSCOPY_RECOVERY_LOS                      |
| all groups | occupancy                | operational | DAYCASE_ENDOSCOPY_RECOVERY_OCC                      |
| all groups | annual operational hours | operational | DAYCASE_ENDOSCOPY_RECOVERY_ANNUAL_OPERATIONAL_HOURS |

---
#### Known issues / limitations
* Specialist endoscopy recovery activity must be excluded from the general daycase recovery capacity domain to avoid double-counting.

---
#### Dependencies
* Feeds exclusion logic for BEDS_DAYCASE_RECOVERY.

---
#### Future enhancements

---
