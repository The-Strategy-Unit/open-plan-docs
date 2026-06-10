#### What is a space in SDEC

> A space in SDEC (Same Day Emergency Care) is a clinical area used to assess, diagnose, monitor, and treat patients who require urgent care without needing an overnight hospital admission.

---
#### Capacity outputs
* SDEC_SPACES
#### Conversion archetype
* flow-space occupancy — FRM_FLOW_SPACE
#### Operational constraint
* Concurrent occupancy over operational periods

---
#### Activity classification logic

Department type = 05 in ECDS.

| Subgroup   | Classification IDs |
| ---------- | ------------------ |
| all groups | CLASS_SDEC         |

---
#### Workload derivation

Primary workload object: occupancy hours

$$\text{occupancy hours} = \text{attendances} \times \frac{\text{LOS minutes}} {60}$$

---
#### Capacity conversion

$$\text{required SDEC spaces} = \frac{\text{occupancy hours}} {\text{annual operational hours} \times \text{utilisation}}$$

---
#### Assumptions

| Subgroup   | Assumption               | Category    | Assumption ID                        |
| ---------- | ------------------------ | ----------- | ------------------------------------ |
| all groups | LOS                      | workload    | SDEC_SPACES_LOS                      |
| all groups | utilisation              | operational | SDEC_SPACES_UTIL                     |
| all groups | annual operational hours | operational | SDEC_SPACES_ANNUAL_OPERATIONAL_HOURS |

---
#### Known issues / limitations
* Type 2 mono-specialty A&E activity is excluded from the initial release
* Demand is likely to be highly variable across the day; average occupancy methods may understate peak capacity requirements.

---
#### Dependencies
* No dependencies.

---
#### Future enhancements
* Explore temporal demand profiles and peak-period adjustments (e.g. 80% of attendances within a 12-hour 08:00–20:00 window)
* Obvious candidate for queueing methods.

---
