---
icon: lucide/boxes
---
# Methodology
 
This tool is an accompaniment to the OpenPlan demand model.
It has been designed to make it easy, clear and consistent to convert the
predicted hospital activity produced from that model into estimates of the
capacity needed to supply that activity.
 
## What happens 'under the hood'?
 
This tool takes one financial year's worth of hospital activity data, groups it
according to which resources it uses, applies a set of assumptions about how the
hospital operates, then calculates how many beds, rooms and other resources might
be needed to meet that demand.
 
The essential components needed to perform a conversion are:

- A [funtional area](../technical-information/functional-area-catalogue) (a resource and the context in which it is being used
(e.g. `BEDS_DAYCASE_RECOVERY` is hospital beds that are being used for the recovery
period following daycase procedures)
- [Subgroups/classifications](../technical-information/classification-register) of the row-level activity data
- Relevant [assumptions](../technical-information/assumptions-register) about how resource is used
- a [conversion formula](../technical-information/conversion-archetypes-catalogue)
 
For example:

- Functional Area: A&E beds (`BEDS_AE`)
- Classification: adult majors
- Assumptions: assumed length of stay per episode and hours per day the ward operates
- Conversion formula (a formula converts this into `ADULT_MAJOR_AE_BEDS`)
 
To see how all these elements relate to each other, please see the
[calculation traceability matrix](../technical-information/calculation-traceability-matrix.md).
 


