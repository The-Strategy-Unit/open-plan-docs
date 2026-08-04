---
hide:
  - toc
---

# Converting spell level modelling to episode level capacity estimates

The NHP model operates at a spell level and takes specialty, procedures, and diagnostic information from [the last episode in spell](https://connect.strategyunitwm.nhs.uk/nhp/project_information/data_extraction/inpatients.html#filtering). However, we need to model capacity at an episode level, because working at spell level means that we lose the detail of specialty attribution, procedure activity, and diagnostic information from earlier episodes.

This document outlines how we link spell level outputs from the NHP capacity model to episode level functional areas, so that we can deliver capacity conversion at the required level of detail.

We first work out from the baseline data what percentage of the spell was spent in different functional areas.


<table>
  <caption><strong>Table 1:</strong> Baseline data at episode level</caption>
  <thead>
    <tr>
      <th>Spell ID</th>
      <th>Spell duration in baseline year</th>
      <th>Episodes</th>
      <th>Episode functional area</th>
      <th>Episode duration in baseline year</th>
      <th>Episode proportion of spell duration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A</td>
      <td>6</td>
      <td>A1</td>
      <td>FA1</td>
      <td>6</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="2">B</td>
      <td rowspan="2">10</td>
      <td>B1</td>
      <td>FA1</td>
      <td>2</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>B2</td>
      <td>FA2</td>
      <td>8</td>
      <td>0.8</td>
    </tr>
    <tr>
      <td>C</td>
      <td>0</td>
      <td>C1</td>
      <td>FA3</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

Below is a simplified example of model results in a single iteration of the model (there are usually 256). The NHP model can change the length of a spell, the point of delivery, duplicate spells, or remove them entirely.

* Spell B has been duplicated
* Spell C is not in the modelled horizon year
* Spell A and one of the duplicated spells in Spell B has had its modelled beddays reduced, because of the efficiency TPMAs

<table>
  <caption><strong>Table 2:</strong> Modelled results at spell level</caption>
  <thead>
    <tr>
      <th>Spell ID</th>
      <th>Modelled spell beddays</th>
    </tr>
  </thead>
  <tbody>
    <tr>
    <td>A</td>
    <td>4</td>
    </tr>
    <tr>
    <td>B</td>
    <td>10</td>
    </tr>
    <tr>
    <td>B</td>
    <td>8</td>
    </tr>
  </tbody>
</table>

We can now work out how many beddays to allocate to each functional area:

<table>
  <caption><strong>Table 3:</strong> Modelled functional area beddays at episode level</caption>
  <thead>
    <tr>
      <th>Spell ID</th>
      <th>Modelled spell duration in horizon year</th>
      <th>Episodes</th>
      <th>Episode functional area</th>
      <th>Episode proportion of spell duration</th>
      <th>Modelled functional area beddays for the episode</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A</td>
      <td>4</td>
      <td>A1</td>
      <td>FA1</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <td rowspan="2">B</td>
      <td rowspan="2">10</td>
      <td>B1</td>
      <td>FA1</td>
      <td>0.2</td>
      <td>2</td>
    </tr>
    <tr>
      <td>B2</td>
      <td>FA2</td>
      <td>0.8</td>
      <td>8</td>
    </tr>
    <tr>
      <td rowspan="2">B</td>
      <td rowspan="2">8</td>
      <td>B1</td>
      <td>FA1</td>
      <td>0.2</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td>B2</td>
      <td>FA2</td>
      <td>0.8</td>
      <td>6.4</td>
    </tr>
  </tbody>
</table>

The total modelled beddays for FA1 is 4 + 2 + 1.6 = 7.6

The total modelled beddays for FA2 is 8 + 6.4 = 14.4

Fractional beddays, whilst not possible in the real world, are not an issue in modelling because the beddays are aggregated for each functional area across all 256 model runs, and we are looking at overall patterns instead of specific details.

## Changes of functional area

There may be instances where the functional area changes in the modelling process. This is due to the following TPMAs:

* [Same Day Emergency Care](https://connect.strategyunitwm.nhs.uk/nhp/project_information/modelling_methodology/activity_mitigators/inpatient_activity_mitigators.html#same-day-emergency-care)
* [Planned Day Procedures](https://connect.strategyunitwm.nhs.uk/nhp/project_information/modelling_methodology/activity_mitigators/inpatient_activity_mitigators.html#day-procedures)

When the new functional area is not inpatients – converting to SDEC (currently recorded in A&E) or converting to Outpatients – this is not an issue.

However, where the model converts activity to daycase, this changes the functional area. This is indicated in the model results by a change in the classpat to 2. In these cases we will identify the spell by the Spell ID and change the functional area for all the episodes to the new daycase functional area. The modelled LOS will be 0 so all of the episodes will have a 0 epidur.

<table>
  <caption><strong>Table 4:</strong> Baseline daycase converted data at episode level</caption>
  <thead>
    <tr>
      <th>Spell ID</th>
      <th>Spell duration in baseline year</th>
      <th>Episodes</th>
      <th>Episode functional area</th>
      <th>Episode duration in baseline year</th>
      <th>Episode proportion of spell duration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>C</td>
      <td>0</td>
      <td>C1</td>
      <td>FA3</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="2">D</td>
      <td rowspan="2">2</td>
      <td>D1</td>
      <td>FA3</td>
      <td>1</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>D2</td>
      <td>FA4</td>
      <td>1</td>
      <td>0.5</td>
    </tr>
  </tbody>
</table>

<table>
  <caption><strong>Table 5:</strong> Modelled daycase converted results at spell level</caption>
  <thead>
    <tr>
      <th>Spell ID</th>
      <th>Modelled spell beddays</th>
      <th>Modelled spell beddays</th>
    </tr>
  </thead>
  <tbody>
    <tr>
    <td>C</td>
    <td>DC</td>
    <td>0</td>
    </tr>
    <tr>
    <td>D</td>
    <td>DC</td>
    <td>0</td>
    </tr>
  </tbody>
</table>

<table>
  <caption><strong>Table 6:</strong> Modelled functional area daycase converted beddays at episode level</caption>
  <thead>
    <tr>
      <th>Spell ID</th>
      <th>Modelled spell duration in horizon year</th>
      <th>Episodes</th>
      <th>Modelled episode functional area</th>
      <th>Modelled functional area beddays for the episode</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>C</td>
      <td>0</td>
      <td>C1</td>
      <td>DC</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="2">D</td>
      <td rowspan="2">0</td>
      <td>D1</td>
      <td>DC</td>
      <td>0</td>
    </tr>
    <tr>
      <td>D2</td>
      <td>DC</td>
      <td>0</td>
    </tr>
  </tbody>
</table>