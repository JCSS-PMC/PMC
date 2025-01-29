# Self Weight

**List of symbols:**

$\begin{array}{ll} d &= \text {correlation length} \\
V &= \text {volume described by the boundary of the structural part} \\
\gamma &= \text {weight density of the material} \\
\gamma_{av} &= \text {average weight density for a structural part} \\
\rho_{0} &= \text {correlation between two far away points in one member} \\
\Delta r &= \text {distance between two points within a member}\end{array}$

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

The self weight, $G$, of a structural part is determined by the relation

```{math}
:label: eq-self-wt-1
G=\int_{Vol} \gamma dV
```

where:

$V$ is the volume described by the boundary of the structural part. The volume of $V$ is Vol.

$\gamma$ is the weight density of the material.

For a part where the material can be assumed to be reasonably homogeneous eq. {eq}`eq-self-wt-1` can be written

```{math}
:label: eq-self-wt-2
G=\gamma_{av} V
```

where

$\gamma_{av}$ is an average weight density for the part (see further [section 13.4.](section-2.1.4)).

## Probability density distribution functions

The weight density and the dimensions of a structural part are assumed to have Gaussian distributions. To simplify the calculations the self weight, $G$, may as an approximation be assumed to have a Gaussian distribution.

(section-2.1.4)=
## Weight density

### Total variability

Mean values, $\mu_{\gamma}$, and coefficients of variation, $V_{\gamma}$, for the total variability of the weight density of some common building materials are given in {numref}`table-Mean-value-and-coefficient-of-variation-for-weight-density`.

```{table} Mean value and coefficient of variation for weight density${}^{1)}$ 
:name: table-Mean-value-and-coefficient-of-variation-for-weight-density
| Material | Mean value [$kN/m^3$] | Coefficient of variation |
| :--- | :--- | :--- |
| **Steel** | 77 | <0.01 |
| **Concrete** |  |  |
| $\quad$ Ordinary concrete ${ }^{2)}$ | 24 | 0.04 |
| $\quad$ High strength concrete | 24-26$~{}^{4)}$ | 0.03 |
| $\quad$ Lightweight aggregate concrete | ${}^{4)}$ | 0.04-0.08 |
| $\quad$ Cellular concrete | ${}^{4)}$ | 0.05-0.10 |
| Heavy concrete for special purposes | ${}^{4)}$ | 0.01-0.02 |
| **Masonry** | - | $\approx$ 0.05 |
| **Timber**$~{}^{3)}$ |  |  |
| $\quad$ Spruce, fir (Picea) | 4.4 | 0.10 |
| $\quad$ Pine (Pinus) | 5.1 | 0.10 |
| $\quad$ Larch (Larix) | 6.6 | 0.10 |
| $\quad$ Beech (Fagus) | 6.8 | 0.10 |
| $\quad$ Oak (Quercus) | 6.5 | 0.10 |
```


${}^{1)}$ The values refer to large populations. They are based on data from various sources.  
${}^{2)}$ The values are valid for concrete without reinforcement and with stable moisture content. In case of continuous drying under elevated temperature the stable volume weight after 50 days is $1.0-1.5~kN/ m^{3}$ lower.  
${}^{3)}$ Moisture content $12 \%$. An increase in moisture content from $12 \%$ to $22 \%$ causes a $10 \%$ rise in weight density.  
${}^{4)}$ Depends on mix, composition and treatment

### Spatial correlations

Between densities of two points within one member, the following correlation can considered to be present:

```{math}
:label: eq-self-wt-3
\rho(\Delta r)=\rho_{o}+\left(1-\rho_{0}\right) \exp \left\lbrace-(\Delta r / d)^{2}\right\rbrace
```

where

$d~$ is a so called correlation length which characterises the correlation structures

$\Delta r~$ is the distance between two points within a member

$\rho_{0}~$ correlation between two far away points in one member

Only correlation in the length dimensions of a structural part are of importance. For beams the weight density over the cross section and for plates over the height may be considered as fully correlated.

Between points in two different members, but within one building, a constant correlation $\rho_{m}$ is assumed to be present.  

In the absence of more detailed information the following values can be used:

| d | 10 m (beam/column) <br> 6 m (plate) <br> 3 m (volume) |
| :--- | :--- |
| $\rho_{o}$ | 0.85 |
| $\rho_{m}$ | 0.70 |

Note: For large members the variability of the weight density may be taken as $V \rho_{o}$; for a whole structure consisting out of many members the variability may be taken as $V \rho_{m}$, where $V$ is the total variability according to {numref}`table-Mean-value-and-coefficient-of-variation-for-weight-density`.

## Volume

In most cases it may be assumed that the mean values of the dimensions are equal to the nominal values i.e. the dimensions given on drawings, in descriptions etc. The mean value of the volume, $V$, of the structural parts is calculated directly from the mean values of the dimensions.

The standard deviation of the volume, $V$, is calculated directly from the values of the standard deviation for the dimensions. Standard deviations for cross section dimensions are given in {numref}`table-Mean-values-and-standard-deviations-for-deviations-of-cross-section-dimensions` for some common building materials and types of structural elements.

```{table} Mean values and standard deviations for deviations of cross-section dimensions from their nominal values 
:name: table-Mean-values-and-standard-deviations-for-deviations-of-cross-section-dimensions
| Structure or structural member | Mean value | Standard deviation |
| :--- | :--- | :--- |
|  |  |  |
| **Rolled steel** |  |  |
| $\quad$ steel profiles, area A | 0.01 $~A_{\text {nom }}$ | 0.04 $~A_{\text {nom }}$ |
| $\quad$ steel plates, thickness $t$ | 0.01 $t_{\text {nom }}$ | 0.02 $t_{\text {nom }}$ |
| **Concrete members** ${ }^{2)}$ |  |  |
| $\quad$ $a_{\text {nom }} \leq$ 1000 mm | 0.003 $a_{\text {nom }}$ | 4+0.006 $a_{\text {nom }}$ |
| $\quad$ $a_{\text {nom }} \geq$ 1000 mm | 3 mm | 10 mm |
| **Masonry members** |  |  |
| $\quad$ unplastered | 0.02 $~a_{\text {nom }}$ | 0.04 $~a_{\text {nom }}$ |
| $\quad$ plastered | 0.02 $~a_{\text {nom }}$ | 0.02 $~a_{\text {nom }}$ |
| **Structural timber** |  |  |
| $\quad$ sawn beam or strut | 0.05 $~a_{\text {nom }}$ | 2 mm |
| $\quad$ laminated beam, planed | $\approx$ 0 | 1 mm |
```

${}^{1)}$ The values refer to large populations. They are based on data from various sources and they concern members with currency acceptation dimension accuracy.  
${}^{2)}$ The values are valid for concrete members cast in situ. For concrete members produced in a factory the deviations may be considerably smaller.

The variability within a component (e.g. the variability of the cross section area along a beam) may be treated according to the same principles that is presented for the weight density in [section 13.5.](section-2.1.4).

**Reference**

1. CIB W81, Actions on Stuctures, Self weight, Report no. 115, Rotterdam