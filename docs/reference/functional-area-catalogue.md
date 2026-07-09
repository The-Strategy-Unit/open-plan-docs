---
hide:
  - toc
---

# Functional Area Catalogue

Inventory of capacity domains, operational constraints and associated conversion archetypes.

<div class="compact-table" markdown="1">

{{ pd_read_csv("docs/data/fun_area_catalog.csv").fillna("") | convert_to_md_table }}

</div>

For three functional areas there is a plausible argument for a different archetype.

**BEDS_INPATIENT_ASSESSMENT** hinges on whether an assessment unit is operationally best viewed as a temporary flow-through area or an inpatient bed base. Given many assessment units keep patients overnight, accommodate stays exceeding 24 hours, and function as admission avoidance wards, the **bed occupancy** archetype was selected as the safer default (rather than **recovery occupancy**). This does make it out-of-step  with BEDS_MATERNITY_ASSESSMENT, although average maternity assessment stays are likely to be shorter in duration.

**ROOMS_MATERNITY_BIRTH** could be represented using a flow-space occupancy approach, as birth activity is naturally expressed as spells multiplied by labour duration. However, birthing rooms are typically occupied continuously by an individual patient, occupancy commonly spans shifts and midnight boundaries, and operational discussions are usually framed in terms of room occupancy rather than throughput. For these reasons the bed occupancy archetype was selected as the most natural operational representation.

**BEDS_DAYCASE_RENAL** could potentially be modelled using a treatment-time utilisation archetype. However, current service planning assumptions are expressed in terms of treatment sessions per bed/chair per day and annual session throughput. As capacity discussions are typically framed around session capacity rather than treatment duration and utilisation, the session capacity archetype was selected.
