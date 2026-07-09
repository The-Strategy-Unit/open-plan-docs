---
icon: lucide/file-digit
---

# Explain my results

Results are delivered as an Excel workbook.
The cover sheet explains the contents of each sheet in the workbook.

The 'results' are contained in the 'estimated_capacity_needs' sheet.

In this sheet, each row describes a type of resource.

Because the demand model is _probabilistic_ it generates a range of plausible 
activity predictions, each of which we convert into capacity estimates. 
This results in many different plausible capacity estimates which we summarise
for you into a mean (the average value for that resource across all the estimates) 
and a 'confidence interval' (via a 'p10 and a 'p90') which describes the range 
of capacity values that contain 80% of capacity estimates generated.

For more information on this vital 'uncertainty', see [the explanation here](../user-guide/methodology.md).

To interpret these figures, you could say:
"Given the inputs I gave to the demand model, the predicted activity would
require on average 30 ['mean'] adult surgical beds, but 80% of the time the predicted
activity suggested the need for between 23 ['p10'] and 32 ['p90']beds"
** This is horrible - someone rewrite this in English for me please!!

To see an example results workbook, click here.
<Example file for download>
