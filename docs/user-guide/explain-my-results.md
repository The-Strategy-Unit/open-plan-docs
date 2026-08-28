---
icon: lucide/file-digit
---

# Explain my results

Results are delivered as an Excel workbook.
The cover sheet explains the contents of each sheet in the workbook.

The results are contained in the `estimated_capacity_needs` sheet of the results 
workbook.

In this sheet, each row describes a type of resource.

Because the [demand model](https://connect.strategyunitwm.nhs.uk/nhp/project_information/) is _probabilistic_ it generates a range of 
activity predictions, each of which we convert into capacity projections. 
This results in many different capacity estimates which we summarise
for you into a mean (the average value for that resource across all the estimates) 
and a _prediction interval_ (via a `p10` and a `p90`) which describes the range 
of capacity values that contain 80% of capacity estimates generated.

For more information on uncertainty, see [the explanation here](../user-guide/methodology.md).

Let's say for surgical beds you get the following results

|                                 | mean | p10 | p90 |
|---------------------------------|------|-----|-----|
| adult_elective_surgical_beddays | 30   | 23  | 32  |



You could interpret this as
> On average, we'd expect to need about 30 adult surgical beds. Given the inputs
you submitted, we can be 80% sure that the true need will fall somewhere between 
23 and 32 beds.

Here is [an example results workbook](/docs/assets/capacity_conversion_results_formatted.xlsx).

!!! note
    Each column in this example workbook is independent, so the expected relationships
    between cells in any one row is not preserved. This workbook is included for
    illustrative purposes only.