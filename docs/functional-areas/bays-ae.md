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

<!-- This approach has been created to try to programmatically identify the
relevant assumptions for this page from its title and the CTM, then gather their related info
from the assumptions register. Hopefully we can abstract this logic out to apply 
to all the FAs after confirming the restructure approach. -->
<div class="compact-table" markdown="1">

{% set functional_area = page.url
   | replace("functional-areas/", "")
   | replace("/", "")
   | upper
   | replace("-", "_") %}

{% set ctm_data = pd_read_yaml("docs/data/calculation_traceability_matrix.yaml") %}

{% set ctm_rows = ctm_data
   .query("functional_area == '" ~ functional_area ~ "'")
   .to_dict("records") %}

{% set assumptions = [] %}

{% for row in ctm_rows %}
  {% for assumption in row.workload_assumptions %}
    {% if assumption %}
      {% set _ = assumptions.append(assumption) %}
    {% endif %}
  {% endfor %}
  {% for assumption in row.operational_assumptions %}
    {% if assumption %}
      {% set _ = assumptions.append(assumption) %}
    {% endif %}
  {% endfor %}
{% endfor %}

{% set assumptions_register = pd_read_csv("docs/data/assumptions_register.csv").fillna("") %}

{{ assumptions_register
   .filter(items=["Subgroup", "Metric", "Assumption Category", "Assumption ID"])
   [assumptions_register["Assumption ID"].isin(assumptions)]
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
