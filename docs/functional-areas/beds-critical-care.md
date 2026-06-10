#### What is a critical care bed?

> A critical care bed is a specialised high-acuity treatment space used to provide continuous monitoring and advanced organ support for critically ill patients within intensive care, high dependency or neonatal intensive care settings.

---
#### Capacity outputs
* ADULT_CRITICAL_CARE_BEDS
* PAEDIATRIC_CRITICAL_CARE_BEDS
* NEONATAL_CRITICAL_CARE_BEDS
#### Conversion archetype
* bed occupancy — FRM_BED_OCCUPANCY
#### Operational constraint
* Continuous occupancy over 24-hour operational periods

---
#### Activity classification logic

Critical care activity is not disaggregated in the main APC dataset. As a stopgap, a fixed percentage (3%) of total inpatient overnight bed-days is used as an estimate of critical care bed-days. It is envisaged that access to the critical care dataset will permit a more refined approach in the future.

| Subgroup   | Classification IDs   |
| ---------- | -------------------- |
| adult      | CLASS_AGE_ADULT      |
| paediatric | CLASS_AGE_PAEDIATRIC |
| neonatal   | CLASS_AGE_NEONATAL   |

---
#### Workload derivation

Primary workload object: critical care bed days

$$\text{critical care bed days} = \text{total inpatient overnight bed days} \times \text{critical care subgroup percent overnight bed days}$$

---
#### Capacity conversion

$$\text{required critical care beds} = \frac{\text{critical care bed days}} {\text{annual operational days} \times \text{occupancy}}$$

---
#### Assumptions

| Subgroup   | Assumption                     | Category    | Assumption ID                                       |
| ---------- | ------------------------------ | ----------- | --------------------------------------------------- |
| adult      | % inpatient overnight bed-days | other       | CRITICAL_CARE_ADULT_PERCENT_OVERNIGHT_BED_DAYS      |
| adult      | occupancy                      | operational | CRITICAL_CARE_ADULT_OCC                             |
| paediatric | % inpatient overnight bed-days | other       | CRITICAL_CARE_PAEDIATRIC_PERCENT_OVERNIGHT_BED_DAYS |
| paediatric | occupancy                      | operational | CRITICAL_CARE_PAEDIATRIC_OCC                        |
| neonatal   | % inpatient overnight bed-days | other       | CRITICAL_CARE_NEONATAL_PERCENT_OVERNIGHT_BED_DAYS   |
| neonatal   | occupancy                      | operational | CRITICAL_CARE_NEONATAL_OCC                          |
| all groups | annual operational days        | operational | CRITICAL_CARE_ANNUAL_OPERATIONAL_DAYS               |

---
#### Known issues / limitations
* Definition of total inpatient overnight bed-days requires clarification.
* Stopgap method future releases should use the critical care dataset.
* Understates CC need due to double-occupancy at transfer. ICU step-down transfers may temporarily consume both: a critical care bed and a downstream ward bed due to transfer timing and operational delays.
- Overstates neonatal CC need because *transitional care* is missing. Assumes 100% of neonatal bed-days are CC but some days will be transitional care, which does not require specialist neonatal CC capacity. Explore whether critical care dataset supports identification of NICU, HDU, SCBU, and transitional care.

In descending order of intensity:

* NICU = neonatal ICU
* HDU = high dependency unit
* SCBU = special care baby unit
* TC = transitional care

----
#### Dependencies
* Depends on total inpatient overnight bed-days.

---
#### Future enhancements
* Use critical care dataset to replace percentage allocation approach.

---
