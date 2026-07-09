---
icon: lucide/file-digit
---

# Explain my results

Results are delivered as an Excel workbook.
The cover sheet explains the contents of each sheet in the workbook.

The results are contained in the `estimated_capacity_needs.xlsx` file.

In this sheet, each row describes a type of resource.

Because the demand model is _probabilistic_ it generates a range of plausible 
activity predictions, each of which we convert into capacity estimates. 
This results in many different plausible capacity estimates which we summarise
for you into a mean (the average value for that resource across all the estimates) 
and a _prediction interval_ (via a `p10` and a `p90`) which describes the range 
of capacity values that contain 80% of capacity estimates generated.

For more information on this vital 'uncertainty', see [the explanation here](../user-guide/methodology.md).

Let's say for surgical beds you get the following results

|                                 | mean | p10 | p90 |
|---------------------------------|------|-----|-----|
| adult_elective_surgical_beddays | 30   | 23  | 32  |



You can interpret this as
> On average, we'd expect to need about 30 adult surgical beds. Most of the time (8 days out of 10), that need would fall somewhere between 23 and 32 beds.

To see an example results workbook, click here.
<Example file for download>
