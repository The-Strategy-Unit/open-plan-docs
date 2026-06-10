---
hide:
  - toc
  - navigation
---

# Functional Area Catalogue

Inventory of capacity domains, operational constraints and associated conversion archetypes.

<div class="compact-table" markdown="1">

| Row | Functional Area                  | Conversion Archetype       | Operational Constraint                                   | Primary Workload Object | Output Type  |
|-----|----------------------------------|----------------------------|----------------------------------------------------------|-------------------------|--------------|
| 1   | BAYS_AE                          | flow-space occupancy       | concurrent occupancy over operational periods            | occupancy_hours         | bays         |
| 2   | BEDS_AE                          | flow-space occupancy       | concurrent occupancy over operational periods            | occupancy_hours         | beds         |
| 3   | BEDS_CRITICAL_CARE               | bed occupancy              | continuous occupancy over 24-hour operational periods    | critical_care_bed_days  | beds         |
| 4   | BEDS_DAYCASE_ENDOSCOPY_RECOVERY  | recovery occupancy         | temporary occupancy with intra-day turnover              | occupancy_hours         | beds         |
| 5   | BEDS_DAYCASE_RECOVERY            | recovery occupancy         | temporary occupancy with intra-day turnover              | occupancy_hours         | beds         |
| 6   | BEDS_DAYCASE_RENAL               | session capacity           | treatment session throughput per bed per operational day | treatment_sessions      | beds         |
| 7   | BEDS_INPATIENT_ASSESSMENT        | bed occupancy              | continuous occupancy over 24-hour operational periods    | assessment_bed_days     | beds         |
| 8   | BEDS_INPATIENT_WARD              | bed occupancy              | continuous occupancy over 24-hour operational periods    | ward_bed_days           | beds         |
| 9   | BEDS_MATERNITY_ASSESSMENT        | recovery occupancy         | temporary occupancy with intra-day turnover              | occupancy_hours         | beds         |
| 10  | BEDS_MATERNITY_WARD              | bed occupancy              | continuous occupancy over 24-hour operational periods    | ward_bed_days           | beds         |
| 12  | LABS_CARDIAC_CATH_PROC           | time utilisation           | schedulable procedural operating time                    | procedure_hours         | laboratories |
| 13  | ROOMS_ENDOSCOPY_PROC             | time utilisation           | schedulable procedural operating time                    | procedure_hours         | rooms        |
| 14  | ROOMS_INT_RADIOLOGY_PROC         | time utilisation           | schedulable procedural operating time                    | procedure_hours         | rooms        |
| 15  | ROOMS_MATERNITY_BIRTH            | bed occupancy              | continuous occupancy over 24-hour operational periods    | birth_room_bed_days     | rooms        |
| 16  | ROOMS_OUTPATIENT_CONSULT         | appointment utilisation    | schedulable clinic consultation time                     | consultation_hours      | rooms        |
| 17  | ROOMS_OUTPATIENT_PROC            | appointment utilisation    | schedulable procedure room time                          | procedure_hours         | rooms        |
| 18  | ROOMS_OUTPATIENT_VIRTUAL_CONSULT | appointment utilisation    | schedulable clinic consultation time                     | consultation_hours      | rooms        |
| 19  | SPACES_HAEM_ONC                  | treatment-time utilisation | schedulable treatment-space time                         | treatment_hours         | spaces       |
| 20  | SPACES_SDEC                      | flow-space occupancy       | concurrent occupancy over operational periods            | occupancy_hours         | spaces       |
| 21  | THEATRES_DAYCASE_PROC            | time utilisation           | schedulable procedural operating time                    | procedure_hours         | theatres     |
| 22  | THEATRES_INPATIENT_PROC          | time utilisation           | schedulable procedural operating time                    | procedure_hours         | theatres     |
| 23  | THEATRES_OBSTETRIC_PROC          | time utilisation           | schedulable procedural operating time                    | procedure_hours         | theatres     |

</div>

For three functional areas there is a plausible argument for a different archetype.

**BEDS_INPATIENT_ASSESSMENT** hinges on whether an assessment unit is operationally best viewed as a temporary flow-through area or an inpatient bed base. Given many assessment units keep patients overnight, accommodate stays exceeding 24 hours, and function as admission avoidance wards, the **bed occupancy** archetype was selected as the safer default (rather than **recovery occupancy**). This does make it out-of-step  with BEDS_MATERNITY_ASSESSMENT, although average maternity assessment stays are likely to be shorter in duration.

**ROOMS_MATERNITY_BIRTH** could be represented using a flow-space occupancy approach, as birth activity is naturally expressed as spells multiplied by labour duration. However, birthing rooms are typically occupied continuously by an individual patient, occupancy commonly spans shifts and midnight boundaries, and operational discussions are usually framed in terms of room occupancy rather than throughput. For these reasons the bed occupancy archetype was selected as the most natural operational representation.

**BEDS_DAYCASE_RENAL** could potentially be modelled using a treatment-time utilisation archetype. However, current service planning assumptions are expressed in terms of treatment sessions per bed/chair per day and annual session throughput. As capacity discussions are typically framed around session capacity rather than treatment duration and utilisation, the session capacity archetype was selected.
