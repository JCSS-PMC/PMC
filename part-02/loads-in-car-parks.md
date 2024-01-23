# Loads In Car Parks

**List of symbols:**


$\mathrm{i}  =\text { influence coefficient }$ 

$\mathrm{t}_{\mathrm{d}}  =\text { busy time per year }$ 

$\mathrm{t}_{\mathrm{y}}  =\text { busy days per year }$ 

$\mathrm{L} =\text { weight of car in } \mathrm{kN}$ 

$\mathrm{S}  =\text { load effect }$ 

$\mathrm{T}  =\text { reference time in years }$ 

$\mathrm{N}  =\text { number of parking places }$ 

$\lambda_{\mathrm{d}}  \text { = renewal rate in [1/d] }$ 

$\tau  =\text { mean dwell time in hours }$


## Basic Model
In car parks the loads on parking areas and drive ways may be distinguished. In general, the loads for regulated parking are dominating the loads for spatially free parking. Further, the entries and parking places are such that only certain categories of vehicles can use the facility. It is sufficient to distinguish between facilities for light vehicles like normal passenger cars, station wagons and vans and for heavy vehicles like trucks and buses. For each parking facility it can conservatively be assumed that the vehicles form an independent sequence each vehicle with random weight remaining the same at arrival and when leaving the place. At the beginning of the busy periods it can conservatively be assumed that parking places left by a car will immediately be occupied by another car. Thus the loading process due to vehicles is a rectangular wave renewal process.

## Stochastic Model

With respect to the temporal fluctuations one can distinguish the following usage categories for light vehicles:

- car parks belonging to residential areas
- car parks belonging to factories, offices etc.
- car parks belonging to commercial areas
- car parks belonging to assembly halls, sport facilities etc.
- car parks connected with railway stations airports etc.

The temporal fluctuations are summarized in table 1. For parking facilities for heavy vehicles similar distinctions can be made.

The mean weight of light vehicles can be assumed to be about {math}`\mathrm{E}[\mathrm{L}] \approx 15 \mathrm{kN}` with coefficient of variation of 15 to 30% depending on the usage of the parking facility and the traffic mixture. The parking place covers an area of about {math}`2.4 \cdot 5.0 \mathrm{~m}^{2}`. A normal distribution can be assumed. In general, light vehicles can be modeled by point loads located in the middle of the parking places.

```{table} Typical temporal fluctuations in car parks
:name: tbl-1-loads -in-car-parks
| Location of car park | Busy days per year <br> {math}`\mathrm{t}_{\mathrm{y}}[\mathrm{d}]` | Busy times per day <br> {math}`\mathrm{t}_{\mathrm{d}}[\mathrm{h}]` | Mean dwell time {math}`\tau[\mathrm{h}]` | Number of cars per day {math}`\lambda_{\mathrm{d}}[1 / \mathrm{d}]` |
| :--- | :---: | :---: | :---: | :---: |
| Commercial areas | 312 |8 <br> 4 | 2.4 | 3.2 |
| Railway stations <br> Airports | 30 | 14 - 18 | 10 - 14 | 1.3 |
| Assembly halls | 50 - 150 | 2.5 | 2.5 | 1.0 |
| Office factories | 260 | 8 - 12 | 8 - 12 | 1.0 |
| Residential areas | 360 | 17 | 8 | 2.1 |
```

Calculation of load effects has to take proper account of influence functions according to

```{math}
:label: eq-loads-in-car-parks-1
\mathrm{S(t)}=\sum_{\mathrm{j=i}}^{\mathrm{n}} \mathrm{i_{j} L_{j}}
```

If the negative parts of the influence functions can be neglected the distribution of extreme load effects can be computed from

```{math}
:label: eq-loads-in-car-parks-2
\mathrm{F}_{\max \{\mathrm{S}\}}(\mathrm{x}) \approx \exp \left[-\lambda_{\mathrm{d}} \mathrm{t_{y}} \mathrm{t_{d}} \mathrm{T P}\left(\sum_{\mathrm{j=1}}^{\mathrm{n}} \mathrm{i_{j} L_{j}} \geq \mathrm{x}\right)\right]
```

with

```{math}
:label: eq-loads-in-car-parks-3
\mathrm{P}\left(\sum_{\mathrm{j=1}}^{\mathrm{n}} \mathrm{i_{j} L_{j}}>\mathrm{x}\right) \approx \Phi\left(-\frac{\mathrm{x}-\left(\sum_{\mathrm{j=1}}^{\mathrm{n}} \mathrm{i_{j} E}\left[\mathrm{L_{j}}\right]\right)}{\left(\sum_{\mathrm{j=1}}^{\mathrm{n}} \mathrm{i_{j}} \operatorname{Var}\left[\mathrm{L_{j}}\right]\right)^{1 / 2}}\right)
```

{math}`\mathrm{T}` is the reference time. On driveways where only one vehicle determines the load effect one has

```{math}
:label: eq-loads-in-car-parks-4
\mathrm{F}_{\max \{\mathrm{S}\}}(\mathrm{x}) \approx \exp \left[-\lambda_{\mathrm{d}} \mathrm{t}_{\mathrm{y}} \mathrm{TN}\left\{1-\Phi\left(\frac{\mathrm{x}-\mathrm{E}[\mathrm{L}]}{(\operatorname{Var}[\mathrm{L}])^{1 / 2}}\right)\right\}\right]
```

where {math}`\mathrm{N}` is the numer of parking places associated with the drive way.

**References**

CIB W81, Actions on Structures: Live Load in Buildings, Rep. N0. 116, Rotterdam, 1989
