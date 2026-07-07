---
hide:
  - toc
---

# Assumptions Register

Governed numerical parameters supporting workload derivation and capacity conversion.

<div class="compact-table" markdown="1">

{% set df = pd_read_csv("docs/data/assumptions_register.csv") %}
{{ df.fillna("") | convert_to_md_table }}

</div>