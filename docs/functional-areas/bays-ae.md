---
title: Bays A&E
---

#### What is an A&E bay?

> An A&E bay is a treatment space within the Emergency Department used to assess and manage lower-acuity patients requiring ambulatory or chair-based care, typically within the minor injury or illness pathway.

---
#### Capacity outputs
* ADULT_MINOR_AE_BAYS
* CHILD_MINOR_AE_BAYS
#### Conversion archetype
* flow-space occupancy — FRM_FLOW_SPACE
#### Operational constraint
* Concurrent occupancy over operational periods

---
#### Activity classification logic

Department type 01 only (consultant-led 24/7 with full resuscitation facilities).
Minors are defined with: Acuity IN {3,4,5}. Null or unknown acuity values are assumed to belong to the minor pathway.

| Level | Description          |
| ----- | -------------------- |
| 1     | Immediate care level |
| 2     | Very urgent level    |
| 3     | Urgent level         |
| 4     | Standard level       |
| 5     | Low acuity level     |

<div class="compact-table" markdown="1">
{{ pd_read_yaml("docs/data/calculation_traceability_matrix.yaml")
.fillna("")
.query("subgroup in ['adult minor', 'child minor']")
.filter(items=['subgroup', 'classification_ids'])
.rename(columns={'subgroup':'Subgroup','classification_ids':'Classification IDs'}) 
| convert_to_md_table }}
</div>

---
#### Workload derivation

Primary workload object: occupancy hours

$$\text{occupancy hours} = \text{attendances} \times \frac{\text{LOS minutes}} {60}$$

---
#### Capacity conversion

$$\text{required AE bays} = \frac{\text{occupancy hours}}{\text{annual operational hours} \times \text{utilisation}}$$

---
#### Assumptions

<div class="compact-table" markdown="1">
{{ pd_read_csv("docs/data/assumptions_register.csv")
   .fillna("")
   [["Subgroup", "Metric", "Assumption Category", "Assumption ID"]]
   [pd_read_csv("docs/data/assumptions_register.csv").fillna("")["Assumption ID"].str.contains('|'.join(['MINOR', 'BAYS']))]
   | convert_to_md_table }}
</div>

---
#### Known issues / limitations
* Type 02 mono-specialty A&E out-of-scope in current development plan.

---
#### Dependencies
* No dependencies.

---
#### Future enhancements
* Obvious candidate for queueing methods.

---
