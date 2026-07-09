---
hide:
  - toc
---

# QA Templates

**SUMMARY**

* **Flow-space:** _concurrent occupancy_
* **Recovery occupancy:** _temporary occupancy capacity_
* **Bed occupancy:** _overnight bed stock_
* **Time utilisation:** _procedural time_
* **Appointment utilisation:** _appointment slots_
* **Session capacity:** _treatment throughput_

<div class="compact-table" markdown="1">

| Conversion Archetype    | Core QA Themes                                                           | Example Validation Tests                                                                           | Expected Monotonic Behaviour                                                                                 | Primary Bottleneck            |
|-------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|-------------------------------|
| Flow-space occupancy    | workload scaling, operational sensitivity, peak occupancy behaviour      | LOS scaling, utilisation sensitivity, annual hours consistency, zero-activity test                 | Longer LOS → more spaces; reduced operational hours → more spaces; higher utilisation → fewer spaces         | concurrent space availability |
| Recovery occupancy      | LOS and occupancy sensitivity, turnover assumptions                      | LOS scaling, occupancy monotonicity, operational hours consistency, zero-activity test             | Longer LOS → more beds; reduced operational hours → more beds; higher occupancy → fewer beds                 | recovery space availability   |
| Bed occupancy           | bed-day annualisation, occupancy behaviour, residual workload allocation | 365-day denominator test, occupancy monotonicity, bed-day reconciliation, zero-activity test       | More bed-days → more beds; higher occupancy → fewer beds                                                     | staffed beds                  |
| Time utilisation        | duration and utilisation sensitivity                                     | procedure-time scaling, utilisation monotonicity, annual hours consistency, zero-activity test     | Longer procedure time → more rooms; reduced operational hours → more rooms; higher utilisation → fewer rooms | schedulable procedural time   |
| Appointment utilisation | appointment duration, DNA assumptions, utilisation sensitivity           | appointment-time scaling, DNA-rate sensitivity, utilisation monotonicity, annual hours consistency | Longer appointment time → more rooms; higher DNA rate → more rooms; higher utilisation → fewer rooms         | schedulable appointment time  |
| Session capacity        | throughput assumptions and annual session capacity                       | session-capacity sensitivity, annual throughput consistency, zero-activity test                    | More treatment sessions → more beds; higher annual session capacity per bed → fewer beds                     | treatment session throughput  |

</div>