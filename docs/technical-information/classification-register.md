---
hide:
  - toc
---

# Classification Register

Routing logic and cohort/subgroup definitions.


<div class="compact-table" markdown="1">
{{ pd_read_yaml("docs/data/classification_register.yaml").fillna("")
   | format_list_cells
   | convert_to_md_table }}
</div>