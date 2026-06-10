#### What is an renal daycase bed

> A renal daycase bed is a treatment space used to provide scheduled same-day renal therapies and monitoring, typically within dedicated dialysis or renal daycase units without an overnight stay.

---
#### Capacity outputs
* DAYCASE_RENAL_BEDS
#### Conversion archetype
* session capacity — FRM_SESSION_CAPACITY
#### Operational constraint
* Treatment session throughput per bed per operational day

---
#### Activity classification logic

Elective inpatient (excl. non-zero LOS spells) or regular day/night spells in treatment specialty renal medicine (361).

Renal daycase activity is identified as activity meeting either of the following logic branches:

| Branch                  | Classification IDs                          |
| ----------------------- | ------------------------------------------- |
| renal elective          | CLASS_RENAL, CLASS_ELECTIVE, CLASS_ZERO_LOS |
| renal regular day/night | CLASS_RENAL, CLASS_REGULAR_DAY_NIGHT        |

Renal daycase spells = branch 1 OR branch 2

---
#### Workload derivation

One renal daycase spell is assumed to represent one treatment session.

Primary workload object: treatment sessions

$$\text{treatment sessions} = \text{renal daycase spells}$$

---
#### Capacity conversion

$$\text{required renal daycase beds} =  \frac{\text{treatment sessions}} {\text{annual session capacity per bed}}$$

---
#### Assumptions

| Subgroup   | Assumption                      | Category    | Assumption ID                                 |
| ---------- | ------------------------------- | ----------- | --------------------------------------------- |
| all groups | annual session capacity per bed | operational | DAYCASE_RENAL_ANNUAL_SESSION_CAPACITY_PER_BED |

---
#### Known issues / limitations
* Specialist renal treatment activity must be excluded from the general daycase recovery capacity domain to avoid double-counting.
* Annual session capacity per bed is supplied directly and represents the assumed annual treatment throughput achievable by a renal daycase bed. The parameter implicitly incorporates operational factors such as session scheduling, operational days and utilisation. A very common planning assumption for dialysis services is two treatment slots per day per chair/bed. This already incorporates treatment duration, cleaning, setup, turnover, etc.

---
#### Dependencies
* Feeds exclusion logic for BEDS_DAYCASE_RECOVERY.

---
#### Future enhancements
* Current approach models capacity using scheduled treatment session throughput. The supplied session-capacity assumptions implicitly incorporate treatment duration, turnover and operational utilisation. Future work should assess whether a more explicit occupancy- or utilisation-based representation offers additional planning value.

---
