---
title: Bays A&E
---

#### :lucide-circle-question-mark: What is an A&E bay?

> An A&E bay is a treatment space within the Emergency Department used to assess and manage lower-acuity patients requiring ambulatory or chair-based care, typically within the minor injury or illness pathway.

---
#### :lucide-shopping-cart: Capacity outputs

* ADULT_MINOR_AE_BAYS
* CHILD_MINOR_AE_BAYS

---
#### :lucide-shapes: Activity classification logic

Department type 01 only (consultant-led 24/7 with full resuscitation facilities).
Minors are defined with: Acuity IN {3,4,5}. Null or unknown acuity values are assumed to belong to the minor pathway.

<div class="compact-table" markdown="1">
{{ pd_read_csv("docs/data/AAE_acuity.csv").fillna("") | convert_to_md_table }}
</div>

<div class="compact-table" markdown="1">
{{ pd_read_csv("docs/data/AAE_subgroup_classification.csv").fillna("") | convert_to_md_table }}
</div>

---
#### :lucide-puzzle: Assumptions

<div class="compact-table" markdown="1">
{{ pd_read_csv("docs/data/AAE_assumptions.csv").fillna("") | convert_to_md_table }}
</div>

---
#### :lucide-replace: Conversion archetype

* flow-space occupancy — FRM_FLOW_SPACE

#### :lucide-scan: Operational constraint

* Concurrent occupancy over operational periods

---
#### :lucide-square-sigma: Formulae

##### Workload derivation

Primary workload object: occupancy hours

$$\text{occupancy hours} = \text{attendances} \times \frac{\text{LOS minutes}} {60}$$

##### Capacity conversion

$$\text{required AE bays} = \frac{\text{occupancy hours}}{\text{annual operational hours} \times \text{utilisation}}$$

---

#### :lucide-triangle-alert: Known issues / limitations

* Type 02 mono-specialty A&E currently out-of-scope.

---
#### :lucide-file-stack: Dependencies

* No dependencies.


