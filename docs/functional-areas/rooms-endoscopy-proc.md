#### What is an endoscopy procedure room

> An endoscopy procedure room is a specialised clinical room where minimally invasive procedures are performed using an endoscope to examine, diagnose, and sometimes treat conditions inside the body.

---
#### Capacity outputs
* ENDOSCOPY_PROC_ROOMS
#### Conversion archetype
* time utilisation — FRM_TIME_UTIL
#### Operational constraint
* Schedulable procedural operating time

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

Primary workload object: procedure hours

$$\text{procedure hours} = \text{procedures} \times \frac{\text{procedure time minutes}} {60}$$

---
#### Capacity conversion

$$\text{required endoscopy rooms} = \frac{\text{procedure hours}} {\text{annual operational hours} \times \text{utilisation}}$$

---
#### Assumptions

| Subgroup   | Assumption               | Category    | Assumption ID                           |
| ---------- | ------------------------ | ----------- | --------------------------------------- |
| all groups | procedure time           | workload    | ENDOSCOPY_PROC_TIME                     |
| all groups | utilisation              | operational | ENDOSCOPY_PROC_UTIL                     |
| all groups | annual operational hours | operational | ENDOSCOPY_PROC_ANNUAL_OPERATIONAL_HOURS |

---
#### Known issues / limitations

---
#### Dependencies
* Specialist endoscopy procedure activity must be excluded from the general daycase theatres capacity domain to avoid double-counting. Feeds exclusion logic for THEATRES_DAYCASE_PROC.

---
#### Future enhancements

---
