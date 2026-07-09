---
icon: 
---

## Product overview 

This tool is an accompaniment to the OpenPlan demand model. 
It has been designed to make it easy, clear and consistent to convert the 
predicted hospital activity produced from that model into estimates of the 
capacity needed to supply that activity.

### What happens 'under the hood'?

This tool takes one financial year's worth of hospital activity data, groups it
according to which resources it uses, applies a set of assumptions about how the 
hospital operates, then calculates how many beds, rooms and other resources might 
be needed to meet that demand.

The essential components needed to perform a conversion are:
- A [funtional area](/docs/reference/functional-area-catalogue.md) (a resource and the context in which it is being used 
(e.g. BEDS_DAYCASE_RECOVERY is hospital beds that are being used for the recovery
period following daycase procedures)
- [Subgroups/classifications](/docs/reference/classification-register.md) of the row-level activity data
- Relevant [assumptions](/docs/reference/assumptions-register.md) about how resource is used
- a [conversion formula](/docs/reference/conversion-archetypes-catalogue.md)

For example:
- Functional Area: A&E beds ('BEDS_AE')
- Classification: adult majors
- Assumptions: assumed length of stay per episode and hours per day the ward operates
- Conversion formula (a formula converts this into ADULT_MAJOR_AE_BEDS)

To see how all these elements relate to each other, please see the
[conversion directory]().

### What if my hospital uses its resources differently?

All the activity in the input data is grouped into 'functional areas' that share
particular resources (for example A&E bays are shared by both adult and
paediatric patients, so would be grouped together into a funtional area).
This grouping is not specific to how any individual hospital uses its space and
resources, but is based on the generic setup of a hospital using the Hospital 2.0
Schedule of Accommodation.

In this release, all operational and resource assumptions are set centrally and
based on expert opinion. 
In future we hope to be able to ingest user-supplied assumptions to allow you
to tailor the conversions to your hospital's specific characteristics.