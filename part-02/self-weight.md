# Self Weight

**List of symbols:**

{math}`\mathrm{d}=` correlation length

{math}`\mathrm{V}=` volume described by the boundary of the structural part

{math}`\gamma=` weight density of the material.

{math}`\gamma_{\mathrm{av}}=` average weight density for a structural part

{math}`\rho_{0}=` correlation between two far away points in one member

{math}`\Delta \mathrm{r}=` distance between two points within a member

## Introduction

The self weight concerns the weight of structural and non-structural components. The main characteristics of the self weight can be described as follows:

- The probability of occurrence at an arbitrary point-in-time is close to one
- The variability with time is normally negligible
- The uncertainties of the magnitude is normally small in comparison with other kinds of loads.

Concerning the uncertainties one can distinguish between (hierarchical model):

- variability **within** a structural part
- variability **between** different structural parts of the same structure
- variability **between** various structures

The variability within a structural part is normally small and can often be neglected. However, for some types of problem (e.g. static equilibrium) it may be important.

## Basic model

The self weight, {math}`\mathrm{G}`, of a structural part is determined by the relation

```{math}
:label: eq-self-wt-1
\mathrm{G}=\int_{\mathrm{Vol}} \gamma \mathrm{dV}
```

where:

{math}`\mathrm{V}` is the volume described by the boundary of the structural part. The volume of {math}`\mathrm{V}` is Vol.

{math}`\gamma` is the weight density of the material.

For a part where the material can be assumed to be reasonably homogeneous eq. {eq}`eq-self-wt-1` can be written

```{math}
:label: eq-self-wt-2
\mathrm{G}=\gamma_{\mathrm{av}} \mathrm{V}
```

where

{math}`\gamma_{\mathrm{av}}` is an average weight density for the part (see further [section 2.1.4](section-2.1.4)).

## Probability density distribution functions

The weight density and the dimensions of a structural part are assumed to have Gaussian distributions. To simplify the calculations the self weight, {math}`\mathrm{G}`, may as an approximation be assumed to have a Gaussian distribution.

(section-2.1.4)=
## Weight density

### Total variability

Mean values, {math}`\mu_{\gamma}`, and coefficients of variation, {math}`\mathrm{V}_{\gamma}`, for the total variability of the weight density of some common building materials are given in {numref}`tbl2.1.1`.

```{table} Mean value and coefficient of variation for weight density 
:name: tbl2.1.1
| Material | Mean value [{math}`\mathrm{kN/m^3}`] | Coefficient of variation |
| :--- | :--- | :--- |
| **Steel** | 77 | <0.01 |
| **Concrete** |  |  |
| &nbsp;&nbsp;&nbsp;Ordinary concrete {math}`{ }^{2)}` | 24 | 0.04 |
| &nbsp;&nbsp;&nbsp;High strength concrete | 24-26{math}`~{}^{4)}` | 0.03 |
| &nbsp;&nbsp;&nbsp;Lightweight aggregate concrete | {math}`{}^{4)}` | 0.04-0.08 |
| &nbsp;&nbsp;&nbsp;Cellular concrete | {math}`{}^{4)}` | 0.05-0.10 |
| Heavy concrete for special purposes | {math}`{}^{4)}` | 0.01-0.02 |
| **Masonry** | - | {math}`\approx` 0.05 |
| **Timber**{math}`~{}^{3)}` |  |  |
| &nbsp;&nbsp;&nbsp;Spruce, fir (Picea) | 4.4 | 0.10 |
| &nbsp;&nbsp;&nbsp;Pine (Pinus) | 5.1 | 0.10 |
| &nbsp;&nbsp;&nbsp;Larch (Larix) | 6.6 | 0.10 |
| &nbsp;&nbsp;&nbsp;Beech (Fagus) | 6.8 | 0.10 |
| &nbsp;&nbsp;&nbsp;Oak (Quercus) | 6.5 | 0.10 |
```

{math}`{}^{1)}` The values refer to large populations. They are based on data from various sources.  
{math}`{}^{2)}` The values are valid for concrete without reinforcement and with stable moisture content. In case of continuous drying under elevated temperature the stable volume weight after 50 days is {math}`1.0-1.5 \mathrm{kN} / \mathrm{m}^{3}` lower.  
{math}`{}^{3)}` Moisture content {math}`12 \%`. An increase in moisture content from {math}`12 \%` to {math}`22 \%` causes a {math}`10 \%` rise in weight density.  
{math}`{}^{4)}` Depends on mix, composition and treatment

### Spatial correlations

Between densities of two points within one member, the following correlation can considered to be present:

```{math}
:label: eq-self-wt-3
\rho(\Delta \mathrm{r})=\rho_{o}+\left(1-\rho_{0}\right) \exp \left\lbrace-(\Delta \mathrm{r} / \mathrm{d})^{2}\right\rbrace
```

where

{math}`\mathrm{d}~` is a so called correlation length which characterises the correlation structures

{math}`\Delta \mathrm{r}~` is the distance between two points within a member

{math}`\rho_{0}~` correlation between two far away points in one member

Only correlation in the length dimensions of a structural part are of importance. For beams the weight density over the cross section and for plates over the height may be considered as fully correlated.

Between points in two different members, but within one building, a constant correlation {math}`\rho_{\mathrm{m}}` is assumed to be present.  

In the absence of more detailed information the following values can be used:

| d | 10 m (beam/column) <br> 6 m (plate) <br> 3 m (volume) |
| :--- | :--- |
| {math}`\rho_{\mathrm{o}}` | 0.85 |
| {math}`\rho_{\mathrm{m}}` | 0.70 |

Note: For large members the variability of the weight density may be taken as {math}`\mathrm{V} \rho_{\mathrm{o}}`; for a whole structure consisting out of many members the variability may be taken as {math}`\mathrm{V} \rho_{\mathrm{m}}`, where {math}`\mathrm{V}` is the total variability according to {numref}`tbl2.1.1`.

## Volume

In most cases it may be assumed that the mean values of the dimensions are equal to the nominal values i.e. the dimensions given on drawings, in descriptions etc. The mean value of the volume, {math}`\mathrm{V}`, of the structural parts is calculated directly from the mean values of the dimensions.

The standard deviation of the volume, {math}`\mathrm{V}`, is calculated directly from the values of the standard deviation for the dimensions. Standard deviations for cross section dimensions are given in {numref}`tbl2.1.2` for some common building materials and types of structural elements.

```{table} Mean values and standard deviations for deviations of cross-section dimensions from their nominal values 
:name: tbl2.1.2
| Structure or structural member | Mean value | Standard deviation |
| :--- | :--- | :--- |
|  |  |  |
| **Rolled steel** |  |  |
| &nbsp;&nbsp;&nbsp;steel profiles, area A | 0.01 {math}`\mathrm{~A}_{\text {nom }}` | 0.04 {math}`\mathrm{~A}_{\text {nom }}` |
| &nbsp;&nbsp;&nbsp;steel plates, thickness {math}`\mathrm{t}` | 0.01 {math}`\mathrm{t}_{\text {nom }}` | 0.02 {math}`\mathrm{t}_{\text {nom }}` |
| **Concrete members** {math}`{ }^{2)}` |  |  |
| &nbsp;&nbsp;&nbsp;{math}`\mathrm{a}_{\text {nom }} \leq` 1000 mm | 0.003 {math}`\mathrm{a}_{\text {nom }}` | 4+0.006 {math}`\mathrm{a}_{\text {nom }}` |
| &nbsp;&nbsp;&nbsp;{math}`\mathrm{a}_{\text {nom }} \geq` 1000 mm | 3 mm | 10 mm |
| **Masonry members** |  |  |
| &nbsp;&nbsp;&nbsp;unplastered | 0.02 {math}`\mathrm{~a}_{\text {nom }}` | 0.04 {math}`\mathrm{~a}_{\text {nom }}` |
| &nbsp;&nbsp;&nbsp;plastered | 0.02 {math}`\mathrm{~a}_{\text {nom }}` | 0.02 {math}`\mathrm{~a}_{\text {nom }}` |
| **Structural timber** |  |  |
| &nbsp;&nbsp;&nbsp;sawn beam or strut | 0.05 {math}`\mathrm{~a}_{\text {nom }}` | 2 mm |
| &nbsp;&nbsp;&nbsp;laminated beam, planed | {math}`\approx` 0 | 1 mm |
```

{math}`{}^{1)}` The values refer to large populations. They are based on data from various sources and they concern members with currency acceptation dimension accuracy.  
{math}`{}^{2)}` The values are valid for concrete members cast in situ. For concrete members produced in a factory the deviations may be considerably smaller.

The variability within a component (e.g. the variability of the cross section area along a beam) may be treated according to the same principles that is presented for the weight density in [section 2.1.4](section-2.1.4).

**Reference**

CIB W81, Actions on Stuctures, Self weight, Report no. 115, Rotterdam