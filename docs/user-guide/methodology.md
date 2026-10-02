---
icon: lucide/route
---

# Understand the model

The OpenPlan Capacity Model translates future activity estimated by the [OpenPlan Hospital Demand Model&nbsp;↗](https://connect.strategyunitwm.nhs.uk/nhp/project_information/) into estimates of the physical capacity required to deliver that activity. This includes inpatient beds, theatres, outpatient consultation rooms and other types of clinical capacity.

The estimates depend on assumptions about how future services will be delivered and operated. These assumptions are fully documented, allowing users to understand how they affect capacity requirements. Support for configuring assumptions and testing alternative service models is planned for a future release.

??? info "How the Demand Model estimates future activity"

    The Demand Model starts with baseline hospital activity and applies
    changes reflecting future population needs, demand and supply
    imbalances, unmet need and planned changes to hospital activity and
    resource use.

    The resulting estimates of future activity provide the starting point
    for the Capacity Model.

    <figure markdown="span">

    ![Demand Model architecture, showing how baseline hospital activity is transformed into estimates of future activity](../assets/images/demand-model-light.svg#only-light)
    ![Demand Model architecture, showing how baseline hospital activity is transformed into estimates of future activity](../assets/images/demand-model-dark.svg#only-dark)

    <figcaption>
    How the Demand Model estimates future activity
    <span class="caption-note">(click to enlarge)</span>
    </figcaption>

    </figure>

    Learn more about the
    [Demand Model&nbsp;↗](https://connect.strategyunitwm.nhs.uk/nhp/project_information/).

## From activity to capacity

The Capacity Model converts activity into capacity through three linked
stages: **classification**, **pathway** and **operating model**.

<figure markdown="span">

![Capacity Model architecture, showing how future activity from the Demand Model is translated into capacity through classification, pathway and operating model](../assets/images/capacity-model-light.svg#only-light)
![Capacity Model architecture, showing how future activity from the Demand Model is translated into capacity through classification, pathway and operating model](../assets/images/capacity-model-dark.svg#only-dark)

<figcaption>How the Capacity Model translates future activity into capacity
<span class="caption-note">(click to enlarge)</span>
</figcaption>

</figure>

### 1. Classification — what type of capacity does the activity require?

The model first classifies activity according to the type or types of
capacity required to deliver it. A single episode of care may require more
than one type of capacity, such as a theatre and a recovery bed.

The level of detail available in the activity data determines how precisely
activity can be classified. Where the data cannot reliably distinguish
between different resource requirements, estimates may need to remain at a
more aggregate level.

For outpatient consultation rooms, the model identifies face-to-face
consultations and separates first and follow-up attendances.

### 2. Pathway — how is future care expected to be delivered?

The model then translates activity into **workload** for each capacity type.
Workload represents the amount of use required, such as occupied bed-days,
theatre hours or consultation hours.

This calculation uses pathway assumptions about how future care will be
delivered, including length of stay, appointment or procedure duration and
recovery requirements. These assumptions are intended to reflect an agreed
future model of care.

For outpatient consultation rooms, the model uses consultation durations
for first and follow-up attendances, together with an allowance for time
lost to missed appointments, to estimate the total consultation hours
required.

### 3. Operating model — how is capacity expected to operate?

Finally, the model translates workload into an estimate of the physical
capacity required. This calculation uses operational assumptions about how
capacity will be used, such as operating hours, occupancy, utilisation and
availability.

For outpatient consultation rooms, the model divides the required
consultation hours by the usable time available per room. This depends on
annual operating hours and the assumed utilisation of that time.

Each [functional area](../functional-areas/)
has its own methods page, explaining the activity included, the pathway
and operating model calculations, the assumptions used and any known
limitations. See the
[outpatient consultation rooms methods](../functional-areas/rooms-outpatient-consult/)
for the complete example.

## The assumptions behind the estimates

Pathway and operational assumptions connect future activity to capacity
requirements:

| Assumption type | What it describes                                         | Examples                                                                    |
| --------------- | --------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Pathway**     | How care is delivered and the workload it creates         | Length of stay, consultation duration, procedure duration and recovery time |
| **Operational** | How capacity operates and the workload it can accommodate | Operating hours, occupancy, utilisation and availability                    |

Changing these assumptions changes the estimated capacity requirement.
For example, longer consultations increase the consultation hours
required, while longer operating hours increase the workload each room can
accommodate.

The assumptions should therefore be considered together as a description
of how future services are expected to work. Reviewing them is an
essential part of assessing whether the estimates reflect the service
model being planned.

The [assumptions register](../technical-information/assumptions-register/)
provides the complete list of assumptions. The functional-area methods
pages explain how they are used in each calculation.

## How the model handles uncertainty

The Demand Model uses
[Monte Carlo simulation&nbsp;↗](https://en.wikipedia.org/wiki/Monte_Carlo_method)
to produce a range of possible future activity estimates. The Capacity
Model converts each of these into a corresponding capacity estimate,
carrying the uncertainty in demand through to the capacity results.

Pathway and operational assumptions are held fixed for each conversion.
The Capacity Model does not simulate additional uncertainty in these
assumptions. The resulting range therefore reflects uncertainty in
modelled demand under the selected capacity assumptions.

The distribution of capacity estimates is summarised using the mean, p10
and p90 for each capacity output. See
[Understand your results](../user-guide/understand-results/)
for an explanation of these values and how to interpret them.
