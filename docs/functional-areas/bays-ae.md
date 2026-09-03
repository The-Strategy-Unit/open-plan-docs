---
title: Bays A&E
---

#### What is an A&E bay?

> An A&E bay is a treatment space within the Emergency Department used to assess and manage lower-acuity patients requiring ambulatory or chair-based care, typically within the minor injury or illness pathway.

---

#### Capacity outputs

- ADULT_MINOR_AE_BAYS
- CHILD_MINOR_AE_BAYS

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
{{ pd_read_csv("docs/data/calculation_traceability_matrix.csv")
   .fillna("")
   [["subgroup", "classification_ids"]]
   [pd_read_csv("docs/data/calculation_traceability_matrix.csv").fillna("")["subgroup"].str.contains("minor")]
   | convert_to_md_table }}
</div>

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
#### Conversion archetype

- flow-space occupancy — FRM_FLOW_SPACE

#### Operational constraint

- Concurrent occupancy over operational periods

---
#### Formulae

##### Workload derivation

Primary workload object: occupancy hours

$$
\text{occupancy hours} = 
\text{attendances} \times 
\frac{\text{LOS minutes}} {60}
$$

##### Capacity conversion

$$
\text{required AE bays} = 
\frac{\text{occupancy hours}}
{\text{annual operational hours} \times \text{utilisation}}
$$

---
#### Dependencies

- No dependencies.

---
#### Known issues / limitations

- Type 02 mono-specialty A&E currently out-of-scope.
