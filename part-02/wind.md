# Wind

**List of symbols:**

$\mathrm{f_c}$ = Coriolis parameter (= 2 $\Omega \sin \phi$)

$\mathrm{f_0}$ = mean frequency of zero upcrossing, in Hz

$\mathrm{g}$ = peak factor (no dimension)

$\mathrm{G_u(n), G_v(n), G_w(n)}$ = half-sided power spectral density for longitudinal, transversal and vertical components of velocity fluctuations

$\mathrm{I_u(z)}$ = turbulence intensity of longitudinal velocity fluctuations (dimensionless)

$\mathrm{k}$ = von Karman`s constant (= 0.4)

$\mathrm{L_u(z)}$ = integral length scale for longitudinal velocity fluctuations, in m

$\mathrm{L_v(z)}$ = integral length scale for transversal velocity fluctuations, in m

$\mathrm{L_w(z)}$ =integral length scale for vertical velocity fluctuations, in m

$\mathrm{N}$ = number of reference time, in years

$\mathrm{n}$ = frequency, in Hertz

$\mathrm{n_u,n_v,n_w}$ = dimensionless frequency of fluctuations in longitudinal, transversal and vertical direction

$\mathrm{\overline{Q}_{ref}}$ = reference wind velocity pressure

$\mathrm{\overline{Q}_z}$ = mean velocity pressure at height $z = \left((1/2) \rho \mathrm{\overline{U}^2} (\mathrm{z})\right)$ 

$\mathrm{S_{ij}(n)}$ = cross spectral power density

$\mathrm{T}$ = reference time

$\mathrm{\overline{T}(u_p)}$ = mean recurrence interval of maximum annual mean velocity, in years

$\mathrm{\overline{U}_{ref}}$ = reference wind velocity, in m/s

$\mathrm{\overline{U}(z)}$ = mean longitudinal velocity of the wind at height $\mathrm{z}$

$\mathrm{u_1}$ = mode of the maximum annual mean wind speed in Gumbel distribution

$\mathrm{u(x,z,t)=u}$ = longitudinal component of the wind velocity fluctuations, in m/s

$\mathrm{v(y,z,t)=v}$ = transversal component of wind velocity fluctuations, in m/s

$\mathrm{w(z,t)=w}$ = vertical component of wind velocity fluctuations, in m/s

$\mathrm{z}$ = height above ground, in m

$\mathrm{z_0}$  = roughness length, in m

$\mathrm{z_r}$ = a reference height above ground, in m

$\mathrm{z_{ref}}$ = the reference height above ground (10 - 30 m)

$\mathrm{\alpha_1}$ = dispersion parameter for the maximum annual mean wind speed in
Gumbel distribution

$\mathrm{\delta}$ = height of the atmospheric boundary layer

$\mathrm{\kappa}$ = surface drag coefficient (dimensionless) $\left(=\left[k/ln(\mathrm{z_{ref}/z_0} \right)\right]^2 )$

$\mathrm{\lambda_{\kappa}}$ = k-th moment of spectral density

$\mathrm{ν(x)}$ = mean upcrossing rate for level x

$\phi$ = geographical latitude

$\rho$ = air density (= 1.25 $\mathrm{kg/m^3}$ )

$\sigma_{\mathrm{u}}, \sigma_{\mathrm{v}},\sigma_{\mathrm{w}}$ = standard deviation of velocity fluctuations in x-, y- and z-direction, in m/s

## Introduction

Wind effects on buildings and structures depend on the general wind climate, the exposure of buildings, structures and their elements to the natural wind, the dynamic properties, the shape and dimensions of the building (structure). The section presents basic data and procedures for the estimation of wind loads on buildings and structures. Tropical cyclones, tornados, thunderstorms and orographic wind phenomena require separate treatment.

The field of wind velocities over horizontal terrain is decomposed into a mean wind (average over 10 minutes) in the direction of general air flow (x-direction) averaged over a specified time interval and a fluctuating, turbulent part with zero mean and components in the longitudinal (x) direction, the transversal (y-) direction and the vertical (z-) direction

(section-2.13.2)=
## Wind forces

The wind force acting per unit area of structure is determined with the relations:

1) For rigid structures of smaller dimensions:

```{math}
:label: eq-wind-1
\mathrm{w}=\mathrm{c}_{\mathrm{a}} \mathrm{c}_{\mathrm{g}} \mathrm{c}_{\mathrm{r}} \overline{\mathrm{Q}}_{\mathrm{ref}}=\mathrm{c}_{\mathrm{a}} \mathrm{c}_{\mathrm{e}} \overline{\mathrm{Q}}_{\mathrm{ref}}
```

2) For structures sensitive to dynamic effects (natural frequency {math}`<1 \mathrm{~Hz}`) and for large rigid structures:

```{math}
:label: eq-wind-2
\mathrm{w}=\mathrm{c}_{\mathrm{d}} \mathrm{c}_{\mathrm{a}} \mathrm{c}_{\mathrm{e}} \overline{\mathrm{Q}}_{\mathrm{ref}}
```

where:

{math}`\overline{\mathrm{Q}}_{\mathrm{ref}}`  = the reference (mean) velocity pressure   
{math}`\mathrm{c}_{\mathrm{r}}`  = roughness factor    
{math}`\mathrm{c}_{\mathrm{g}}`  = gust factor    
{math}`\mathrm{c}_{\mathrm{a}}`  = aerodynamic shape factor    
{math}`\mathrm{c}_{\mathrm{d}}`  = dynamic factor.   

## Mean wind velocity

The reference wind velocity, {math}`\overline{\mathrm{U}}_{\text {ref }}` is the mean velocity of the wind averaged over a time interval of 10 {math}`\min =600 \mathrm{~s}`, determined at an elevation of {math}`10 \mathrm{~m}` above ground, in horizontal open terrain exposure {math}`\left(\mathrm{z}_{0}=0.03\right.` {math}`\mathrm{m})^{1}`

The distribution of the mean wind velocities (for any terrain category, height above ground and averaging time interval) is the Weibull distribution:

```{math}
:label: eq-wind-3
\mathrm{F}_{\overline{\mathrm{U}}}(\mathrm{x})=1-\exp \left[-\frac{1}{2}\left(\frac{\mathrm{x}}{\sigma}\right)^{\mathrm{k}}\right]
```

with {math}`\mathrm{k}` close to 2.

{math}`{ }^{1}` For other than 10 min averaging intervals, in open terrain exposure, the following relationships may be used: {math}`1.05 \overline{\mathrm{U}}^{1 \mathrm{~h}}=1.0 \overline{\mathrm{U}}^{10 \mathrm{~min}}=0.84 \overline{\mathrm{U}}^{1 \mathrm{~min}(\text { fastest mile) }}=0.67 \overline{\mathrm{U}}^{3 \mathrm{sec}}`.  

The same distribution is valid for direction dependent mean wind flows. Generally, it can not be assumed that the mean wind direction is uniformly distributed over the circle.

Mean wind velocities vary over the year. If no data are available it can be assumed in the northern hemisphere that {math}`\sigma(\mathrm{t}) \approx \sigma\left[1+a \cos \left(2 \pi\left(\mathrm{t}-\mathrm{t}_{0}\right) / 365\right]\right.` with the constant {math}`a` between {math}`1 / 3` and {math}`1 / 2` and {math}`\mathrm{t}_{0} \approx 15` to 45 , with {math}`\mathrm{t}` in days.

The mean wind velocities are highly autocorrelated. Mean wind velocities with separation of about 4 to 12 (8 on average) hours can be considered as independent in most practical applications.

If seasonal variations are neglected, the mean period the mean wind velocities are between levels {math}`\mathrm{x}_{1}` and {math}`\mathrm{x}_{2}\left(\mathrm{x}_{2} \geq \mathrm{x}_{1}\right)` is asymptotically

```{math}
:label: eq-wind-4
\mathrm{E}\left[\mathrm{T}_{\mathrm{x}_{1}, \mathrm{x}_{2}}\right]=\mathrm{T}\left[\mathrm{F}_{\overline{\mathrm{U}}}\left(\mathrm{x}_{2}\right)-\mathrm{F}_{\overline{\mathrm{U}}}\left(\mathrm{x}_{1}\right)\right]
```

with {math}`\mathrm{T}` the reference time. For higher levels of {math}`\mathrm{x}_{2}` the distribution of individual times above {math}`\mathrm{x}` is approximately {math}`\left[1-\mathrm{F}_{\overline{\mathrm{U}}}(\mathrm{x})\right] / \mathrm{v}(\mathrm{x})` with {math}`\mathrm{v}(\mathrm{x})` the mean upcrossing rate for level {math}`\mathrm{x}`.

The maximum mean wind speeds for longer periods follows a Gumbel distribution for maxima. Generally, it is not possible to infer the maxima over more years from observations covering only a few years. If the annual maxima are used, provided that the maximum annual data are homogenous as exposure and averaging time, the distribution function is:

```{math}
:label: eq-wind-5
\mathrm{F}_{\max \overline{\mathrm{U}}}(\mathrm{x})=\exp \left\lbrace-\exp \left[-\alpha_{1}\left(\mathrm{x}-\mathrm{u}_{1}\right)\right]\right\rbrace
```

The mode {math}`\mathrm{u}` and the parameter {math}`\alpha_{1}` of the distribution are determined from the mean {math}`\mathrm{m}_{1}` and the standard deviation {math}`\sigma_{1}` of the set of maximum annual velocities: {math}`\mathrm{u}_{1}=\mathrm{m}_{1}-0.577 / \alpha_{1}, \alpha_{1}=1.282 / \sigma_{1}`. The coefficient of variation of maximum annual wind speed, {math}`\mathrm{V}_{1}=\sigma_{1} / \mathrm{m}_{1}` depends on the climate and is normally between 0.10 and 0.35. For reliable results, the number of the years of available records must be of the same order of magnitude like the required mean recurrence interval.

The lifetime ( {math}`\mathrm{N}` years) maxima of wind velocity is also Gumbel distributed and the mean and the standard deviation of lifetime maxima are functions of the mean and of the standard deviation of annual maxima: {math}`\mathrm{m}_{\mathrm{N}}+0.78 \sigma_{1} \ln \mathrm{N}, \sigma_{\mathrm{N}}=\sigma_{1}`.

Under special climatic conditions, the distribution of mean wind speeds is a mixed distribution reflecting different meteorological phenomena.

For load combination purposes it is proposed to model storms, for example those wind regimes where a mean velocity >10 m/s lasts for some time, as an intermittent rectangular wave renewal process. The number of storms per year is approximately 50 corresponding to the frequency with which weather systems pass by, at least in middle Europe. The mean duration of the storm is approximately 8 hours. Consecutive storms are independent. The representative mean wind velocity in a storm can also be modeled by a Weibull distribution. The exponent of the Weibull distribution should be around 2. The location parameter should be based on local data.

## Terrain roughness (category)

The roughness of the ground surface is aerodynamically described by the roughness length {math}`\mathrm{z}_{0}`, which is a measure of the size and spacing of obstacles on the ground surface. Alternatively, the terrain roughness can be described by the surface drag coefficient, {math}`\kappa` corresponding to the roughness length {math}`\mathrm{z}_{0}` :

```{math}
:label: eq-wind-6
\kappa^{2}=\frac{k}{\ln \frac{z_{r e f}}{z_{0}}}
```

where {math}`k \cong 0.4` is von Karman's constant and {math}`\mathrm{z}_{\text {ref }}` is the reference height ({numref}`tbl2-wind`, {numref}`tbl3-wind`). Various terrain categories are classified in {numref}`tbl1-wind` according to their approximate roughness lengths. The distribution of the surface roughness with wind direction must be considered.

```{table} Roughness length, in meters, for various terrain categories
:name: tbl1-wind
| Terrain category | Terrain description | Range of {math}`\mathrm{z}_{0}` | Recommended value |
| :---: | :--- | :---: | :---: |
| A. Open sea. Smooth flat country | Areas exposed to the wind coming from large bodies of water; snow surface; Smooth flat terrain with cut grass and rare obstacles. | 0.0001 <br> {math}`\mid` <br> 0.0005 | 0.003 |
| B. Open country | High grass (60 cm) hedges, and farmland with isolated trees; <br> Terrain with occasional obstructions having heights less than 10m (some trees and some buildings) | 0.01 <br> {math}`\mid` <br> 0.1 | 0.03 |
| C. Sparsely built-up urban areas. Wooded areas | Sparsely built-up areas, suburbs, fairly wooded areas (many trees) | 0.1 <br> {math}`\mid` <br> 0.7 | 0.3 |
| D. Densely built-up urban areas. Forests | Dense forests in which the mean height of trees is about 15m; Densely built-up urban areas; towns in which at least 15% of the surface is covered with buildings having heights over 15m | 0.7 <br> {math}`\mid` <br> 1.2 | 1.0 |
| E. Centers of very large cities | Numerous large high closely spaced obstructions: more than 50% of the buildings have a height over 20m | 1.0  <br> {math}`\geq` 2.0 | 2.0 |
```

{math}`{ }^{1)}` Smaller values of {math}`\mathrm{z}_{0}` provoke higher mean velocities of the wind

{math}`{ }^{2)}` For the full development of the roughness category, the terrains of types A to D must prevail in the up wind direction for a distance of at least of 1000 m, respectively. For category E this distance is more than 5 km.

## Variation of the mean wind with height

The variation of the mean wind velocity with height over horizontal terrain of homogenous roughness can be described by the logarithmic law. The logarithmic profile is valid for moderate and strong winds (mean hourly velocity $>10 \mathrm{~m} / \mathrm{s}$ ) in neutral atmosphere (where the vertical thermal convection of the air may be neglected).

```{math}
:label: eq-wind-7
\overline{\mathrm{U}}(\mathrm{z})=\frac{1}{\mathrm{k}} \mathrm{u}_{*}\left(\mathrm{z}_{0}\right)\left(\ln \frac{\mathrm{z}}{\mathrm{z}_{0}}+5.75 \frac{\mathrm{z}}{\delta}-1.87\left(\frac{\mathrm{z}}{\delta}\right)^{2}-1.33\left(\frac{\mathrm{z}}{\delta}\right)^{3}+0.25\left(\frac{\mathrm{z}}{\delta}\right)^{4}\right) \quad\left(\mathrm{z}>\mathrm{d}_{0}>>\mathrm{z}_{0}\right)
```

where: 

{math}`\mathrm{u(z_0)}=\frac{\overline{U}(z)}{2.5 \ln \frac{z}{z_{0}}}=` friction velocity in {math}`\mathrm{m} / \mathrm{s}`

{math}`\delta \quad=\frac{u_{*}\left(z_{0}\right)}{6 f_{c}}=` depth of boundary layer in {math}`\mathrm{m}`

{math}`\overline{\mathrm{U}}(\mathrm{z})` = mean velocity of the wind at height {math}`\mathrm{z}` above ground in {math}`\mathrm{m} / \mathrm{s}`

{math}`\mathrm{z} \quad=` height above ground in {math}`\mathrm{m}`

{math}`\mathrm{z}_{0} \quad=` roughness length in {math}`\mathrm{m}`

{math}`\mathrm{k}=` von Karman's constant {math}`(\mathrm{k} \cong 0.4)`

{math}`\mathrm{d}_{0} \quad=` the lowest height of validity of Eq.{eq}`eq-wind-7` in {math}`\mathrm{m}`

{math}`\mathrm{f}_{\mathrm{c}} \quad=2 \Omega \sin (\phi)=` Coriolis parameter in 1/s

{math}`\Omega \quad=0.726~10^{-4}=` angular rotation velocity in {math}`\mathrm{rad} / \mathrm{s}`

{math}`\phi \quad=$ latitude of location in degree

For lowest 0.1 {math}`\delta` or 200 m of the boundary layer only the first term needs to be taken into account (Harris and Deaves, 1981). The lowest height of validity for Eq.{eq}`eq-wind-7`, {math}`\mathrm{d}_{0}`, is close to the average height of dominant roughness elements : i.e. from less than 1 m, for smooth flat country to more than 15 m, for centers of cities. For {math}`\mathrm{z}_{0} \leq \mathrm{z} \leq \mathrm{d}_{0}` a linear interpolation is recommended. In engineering practice, Eq.{eq}`eq-wind-7` is conservatively used with {math}`\mathrm{d}_{0}=0`.

With respect to the reference (open terrain) exposure, the relation between wind velocities in two different roughness categories at two different heights can be written approximately as (Bietry, 1976, Simiu, 1986):

```{math}
:label: eq-wind-8
\frac{\overline{U}(z)}{\overline{U}_{\text {ref }}}=\frac{\ln \frac{Z}{Z_{0}}}{\ln \frac{Z_{\text {ref }}}{Z_{0, \text { ref }}}}\left(\frac{z_{0}}{z_{0, r e f}}\right)^{0.07}
```

At the reference height {math}`\mathrm{z}_{\mathrm{ref}}`, the ratio of the mean wind velocity in various terrain categories to the mean wind velocity in open terrain is given by the factor {math}`\mathrm{p}` in {numref}`tbl2-wind` . The corresponding ratio for the mean velocity pressure is {math}`\mathrm{p}^{2}`.

Table 2. Scale factors for the mean velocity (and the mean velocity pressure) at reference height in various terrain exposure

```{table} Scale factors for the mean velocity (and the mean velocity pressure) at reference height in various terrain exposure
:name: tbl2-wind
| Terrain category | A. Open sea. Smooth flat country | B. Open country | C. Sparsely built-up urban areas. Wooded areas | D. Densely built-up urban areas. Forests | E. Centers of large cities |
| :---: | :---: | :---: | :---: | :---: | :---: |
| {math}`\mathrm{z}_{\text {ref }}, \mathrm{m}` | 10 | 10 | 10 | 15 | 30 |
| {math}`\mathrm{p}` | 1.19 | 1.00 | 0.71 | 0.56 | 0.39 |
```

## Intensity of turbulence

The turbulent fluctuations of the wind velocity can be assumed to be normally distributed with mean zero. The root mean squared value of the velocity fluctuations in the airflow, deviating from the longitudinal mean velocity, may be normalised to the friction velocity as follows:

```{math}
:label: eq-wind-9a
\frac{\sigma_{\mathrm{u}}}{\mathrm{u}_{*}}=\beta_{\mathrm{u}}\left(1-\frac{\mathrm{z}}{\delta}\right)  \quad \text { Longitudinal } 
```

```{math}
:label: eq-wind-9b
\frac{\sigma_{\mathrm{v}}}{\mathrm{u}_{*}}=\beta_{\mathrm{v}}\left(1-\frac{\mathrm{z}}{\delta}\right)  \quad \text { Transversal } 
```

```{math}
:label: eq-wind-9c
\frac{\sigma_{\mathrm{w}}}{\mathrm{u}_{*}}=\beta_{\mathrm{w}}\left(1-\frac{\mathrm{z}}{\delta}\right)  \quad \text { Vertical }
```

The approximate linear variation with height (Hanna, 1982) can be used only in moderate and strong winds. For neutral atmosphere, the ratios{math}`\sigma_{\mathrm{v}} / \sigma_{\mathrm{u}}` and {math}`\sigma_{\mathrm{w}} / \sigma_{\mathrm{u}}` near the ground are constant irrespective of the roughness of the terrain (ESDU 1993):

```{math}
:label: eq-wind-10a
\frac{\sigma_{v}}{\sigma_{u}}=1-0.25 \cos ^{4}\left(\frac{\pi}{2} \frac{z}{\delta}\right) 
```

```{math}
:label: eq-wind-10b
\frac{\sigma_{w}}{\sigma_{u}}=1-0.55 \cos ^{4}\left(\frac{\pi}{2} \frac{z}{\delta}\right)
```

For {math}`\mathrm{z}<<\delta` the variance of the velocity fluctuations can be assumed independent of height above ground :

```{math}
:label: eq-wind-11a
\sigma_{\mathrm{u}}=\beta_{\mathrm{u}} \mathrm{u}_{*}
```

```{math}
:label: eq-wind-11b
\sigma_{\mathrm{v}}=\beta_{\mathrm{v}} \mathrm{u}_{*}
```

```{math}
:label: eq-wind-11c
\sigma_{\mathrm{w}}=\beta_{\mathrm{w}} \mathrm{u}_{*}
```

and, for {math}`\mathrm{z}<0.1 \delta` :

```{math}
:label: eq-wind-12a
\frac{\sigma_{v}}{\sigma_{u}} \cong 0.75
```

```{math}
:label: eq-wind-12b
\frac{\sigma_{w}}{\sigma_{u}} \cong 0.505
```

The variance of the longitudinal velocity fluctuations can also be expressed from non-linear regression of measurement data, as function of terrain roughness (Solari, 1987):

```{math}
:label: eq-wind-13
4.5 \leq \beta_{\mathrm{u}}^{2}=4.5-0.856 \ln \mathrm{z}_{0} \leq 7.5
```

The longitudinal intensity of turbulence is the ratio of the root mean squared value of the longitudinal velocity fluctuations to the mean wind velocity at height {math}`\mathrm{z}` (i.e. the coefficient of variation of the velocity fluctuations at height {math}`\mathrm{z}` :

```{math}
:label: eq-wind-14
\mathrm{I_u (z)} = \frac{\overline{\mathrm{u(z,t)^2}}^{1/2}}{\mathrm{\overline{U}(z)}}= \frac{\sigma_\mathrm{u} \mathrm{z}}{\mathrm{\overline{U}(z)}}
```

The turbulence intensity at height {math}`\mathrm{z}` can be approximated by:

```{math}
:label: eq-wind-15
I(z)=\frac{\beta_{u}}{2.5 \ln \frac{z}{z_{0}}} \approx \frac{1}{\ln \frac{z}{z_{0}}}
```

The transversal and vertical intensities of turbulence can be determined by multiplication of the longitudinal intensity {math}`\mathrm{I}_{\mathrm{u}}(\mathrm{z})` by the ratios {math}`\sigma_{\mathrm{v}} / \sigma_{\mathrm{u}}` and {math}`\sigma_{\mathrm{w}} / \sigma_{\mathrm{u}}`. Representative values for intensity of turbulence at the reference height are given in {numref}`tbl3-wind`.

```{table} Wind parameters depending on terrain category
:name: tbl3-wind
| Terrain category | A. Open sea. Smooth flat country | B.Open country | C. Sparsely built-up urban areas. Wooded areas | D. Densely built-up urban areas.Forests | E. Centers of large cities |
| :---: | :---: | :---: | :---: | :---: | :---: |
| {math}`\mathrm{z}_{0}[\mathrm{~m}]` | 0.01 | 0.05 | 0.3 | 1.0 | 2.0 |
| {math}`\mathrm{d}_{0}[\mathrm{~m}]` | 0 | 2 | 8 | 15 | 30 |
| {math}`\kappa` | 0.0024 | 0.0047 | 0.013 | 0.022 | 0.022 |
| {math}`\beta_{\mathrm{u}}` | 3.1 | 2.7 | 2.3 | 2.1 | 2.0 |
| {math}`\beta_{\mathrm{v}}` | 2.3 | 2.1 | 1.8 | 1.6 | 1.5 |
| {math}`\beta_{\mathrm{w}}` | 1.55 | 1.35 | 1.15 | 1.05 | 1.0 |
| {math}`\mathrm{Z}_{\mathrm{ref}}[\mathrm{m}]` | 10 | 10 | 10 | 15 | 30 |
| {math}`\mathrm{I}\left(\mathrm{z}_{\mathrm{ref}}\right)` | 0.15 | 0.19 | 0.26 | 0.31 | 0.39 |
```

## Power spectral density and autocorrelation function of gustiness

The normalised half-sided von Karman power spectral densities and autocorrelation functions of gust velocity are given in {numref}`tbl4-wind`.

```{table} The von Karman model of isotropic turbulence
:name: tbl4-wind
| Component of gust velocity | Normalised spectral density <br> {math}`\frac{\mathrm{nG}_{\mathrm{i}}(\mathrm{n})}{\sigma_{\mathrm{i}}^{2}}` | Normalised autocorrelation function <br> {math}`\rho_{\mathrm{i}}\left(\tau_{\mathrm{i}}\right)` |
| :---: | :---: | :---: |
| Longitudinal <br> {math}`\text{I = u}` | {math}`\frac{4 \mathrm{n}_{\mathrm{u}}}{\left(1+70.8 \mathrm{n}_{\mathrm{u}}^{2}\right)^{5 / 6}}` | {math}`\frac{2^{2 / 3}}{\Gamma(1 / 3)} \bar{\tau}_{\mathrm{u}}^{1 / 3} \mathrm{~K}_{1 / 3}\left(\bar{\tau}_{\mathrm{u}}\right)` |
| Transversal <br> {math}`\mathrm{I}=\mathrm{v}` <br> <br> Vertical <br> {math}`\mathrm{i}=\mathrm{w}` | <br> <br> {math}`\frac{2 \mathrm{n}_{\mathrm{i}}\left(1+188.6 \mathrm{n}_{\mathrm{i}}^{2}\right)}{\left(1+70.8 \mathrm{n}_{\mathrm{i}}^{2}\right)^{11 / 6}}` | <br> <br> {math}`\frac{2^{2 / 3}}{\Gamma(1 / 3)} \bar{\tau}_{\mathrm{i}}^{1 / 3}\left[K_{1 / 3}\left(\bar{\tau}_{\mathrm{i}}\right)-\frac{1}{2} \bar{\tau}_{\mathrm{i}} K_{2 / 3}\left(\bar{\tau}_{\mathrm{i}}\right)\right]` |
```

The notations in {numref}`tbl4-wind` are as follows:

{math}`\sigma_{\mathrm{i}}^{2}` = variance of velocity fluctuations in direction {math}`\mathrm{i}`, {math}`\mathrm{m}^{2} / \mathrm{s}^{2}` ; {math}`\mathrm{i}=\mathrm{u}, \mathrm{v}` or {math}`\mathrm{w}`

{math}`\mathrm{n}_{\mathrm{i}}  = \mathrm{n}_{\mathrm{i}}(\mathrm{z}) = \frac{\mathrm{n} \mathrm{L}_{\mathrm{i}}(\mathrm{z})}{\overline{\mathrm{U}}(\mathrm{z})}` = is a non-dimensional height dependent frequency

{math}`\mathrm{n}` = frequency, in Hertz 

{math}`\overline{\mathrm{U}}(\mathrm{z})` = longitudinal mean velocity at height {math}`\mathrm{z}` , in {math}`\mathrm{m} / \mathrm{s}`

{math}`\mathrm{L}_{\mathrm{i}}(\mathrm{z})`  = length of integral scale of turbulence in direction {math}`\mathrm{i}` , in {math}`\mathrm{m} / \mathrm{s}` 

{math}`\bar{\tau}_{\mathrm{i}}=\frac{\tau \overline{\mathrm{U}}(\mathrm{z})}{\mathrm{a} \mathrm{L}_{\mathrm{i}}(\mathrm{z})}` = non-dimensional time {math}`(\mathrm{a}=1.339)`

{math}`\mathrm{K}_{\mu}()` = modified Bessel function of second kind of order {math}`\mu`

{math}`\tau` = time lag, in {math}`\mathrm{s}`

The integral length scale of turbulence in direction {math}`\mathrm{i}` at the height {math}`\mathrm{z}` is:

```{math}
:label: eq-wind-16
\mathrm{L}_{\mathrm{i}}(\mathrm{z})=\mathrm{U}(\mathrm{z}) \int_{0}^{\infty} \rho_{\mathrm{i}} (\tau_{\mathrm{i}}) \mathrm{d} \tau_{\mathrm{i}}
```

where the autocorrelation {math}`\rho_{\mathrm{i}}\left(\tau_{\mathrm{i}}\right)` is the Fourier transform of spectral density. An estimation of the length of the integral scale of longitudinal turbulence, for heights up to 300 m is given by ESDU (1993), as:

```{math}
:label: eq-wind-17
\mathrm{L}_{\mathrm{u}}(\mathrm{z})=\frac{\mathrm{A}^{3 / 2}\left(\sigma_{\mathrm{u}} / \mathrm{u}_{*}\right)^{3} \mathrm{z}}{2.5 \mathrm{~K}_{\mathrm{z}}^{3 / 2}(1-\mathrm{z} / \mathrm{h})^{2}(1+5.75 \mathrm{z} / \mathrm{h})}
```

where

{math}`A=0.115\left[1+0.315\left(1-\frac{\mathrm{z}}{\delta}\right)^{6}\right]^{2 / 3}`

{math}`\mathrm{K}_{\mathrm{z}}=0.188\left[1-\left(1-\mathrm{z} / \mathrm{z}_{\mathrm{c}}\right)^{2}\right]^{1 / 2}`

{math}`\mathrm{z}_{\mathrm{c}} / \delta=0.39\left[\frac{\mathrm{u}_{*}}{\mathrm{f}_{\mathrm{c}} \mathrm{z}_{0}}\right]^{-1 / 8}`

For the lateral and vertical direction (ESDU, 1993):

```{math}
:label: eq-wind-18a
\mathrm{L}_{\mathrm{v}}(\mathrm{z})=0.5\left(\sigma_{\mathrm{v}} / \sigma_{\mathrm{u}}\right)^{3} \mathrm{~L}_{\mathrm{u}}(\mathrm{z})
``` 

```{math}
:label: eq-wind-18b
\mathrm{L}_{\mathrm{w}}(\mathrm{z})=0.5\left(\sigma_{\mathrm{w}} / \sigma_{\mathrm{u}}\right)^{3} \mathrm{~L}_{\mathrm{u}}(\mathrm{z})
``` 

```{math}
:label: eq-wind-18c
\mathrm{L}_{\mathrm{v}}(\mathrm{z}) \cong 0.24 \mathrm{~L}_{\mathrm{u}}(\mathrm{z}
``` 

```{math}
:label: eq-wind-18d
\mathrm{L}_{\mathrm{w}}(\mathrm{z}) \cong 0.08 \mathrm{~L}_{\mathrm{u}}(\mathrm{z})
``` 
(section-2.13.8)=
## Coherence function

The cross-spectral density for two separated points {math}`\mathrm{P}_{1}` and {math}`\mathrm{P}_{2}` with distance {math}`\mathrm{r}` perpendicular to direction {math}`\mathrm{i}` are given in terms of the point spectra and the coherence function by:

```{math}
:label: eq-wind-19
\mathrm{S}_{\mathrm{ij}}\left(\mathrm{n}, \mathrm{P}_{1}, \mathrm{P}_{2}\right) \approx \mathrm{S}_{\mathrm{ii}}^{1 / 2}\left(\mathrm{n}, \mathrm{P}_{1}, \mathrm{P}_{2}\right) \mathrm{S}_{\mathrm{jj}}^{1 / 2}\left(\mathrm{n}, \mathrm{P}_{1}, \mathrm{P}_{2}\right) \cdot \operatorname{Coh}_{\mathrm{ij}}^{1 / 2}\left(\mathrm{n}, \mathrm{P}_{1}, \mathrm{P}_{2}\right)
``` 

with:

```{math}
:label: eq-wind-20a
\text{Longitudinal} \quad \operatorname{Coh}_{u u}^{1 / 2}(r, \bar{k})=\frac{\left(\frac{\psi_{u}}{2}\right)^{5 / 6}}{\Gamma(5 / 6)}\left[2 K_{5 / 6}\left(\psi_{u}\right)-\psi_{u} K_{1 / 6}\left(\psi_{u}\right)\right] \approx \exp \left(-1.15 \psi_{u}^{1.5}\right)
``` 

```{math}
:label: eq-wind-20b
\text{Transversal} \quad \operatorname{Coh}_{v v}^{1 / 2}(r, \bar{k})=\frac{\left(\frac{\psi_{v}}{2}\right)^{5 / 6}}{\Gamma(5 / 6)}\left[2 K_{5 / 6}\left(\psi_{v}\right)+\frac{6(r \bar{k})^{2}}{3 \psi_{v}^{2}+5(r \bar{k})^{2}} \psi_{v} K_{1 / 6}\left(\psi_{v}\right)\right] \approx \exp \left(-0.65 \psi_{v}^{1.3}\right)
``` 

```{math}
:label: eq-wind-20c
\text{Vertical} \quad \operatorname{Coh}_{w w}^{1 / 2}(r, \bar{k})=\frac{\left(\frac{\psi_{w}}{2}\right)^{5 / 6}}{\Gamma(5 / 6)}\left[2 K_{5 / 6}\left(\psi_{w}\right)-\frac{6(r L)^{2}}{3 \psi_{w}^{2}+5(r \bar{k})^{2}} \psi_{w} K_{1 / 6}\left(\psi_{w}\right)\right] \approx \exp \left(-0.65 \psi_{w}^{1.3}\right)
``` 

where {math}`\overline{\mathrm{k}}=\frac{2 \pi \mathrm{n}}{\overline{\mathrm{U}}_{\mathrm{m}}}` and {math}`\psi_{\mathrm{i}}^{2}=\left(\mathrm{r}^{2} \overline{\mathrm{k}}^{2}+\mathrm{r}^{2} / \mathrm{L}_{\mathrm{i}}^{2}\right)`. All coherence function {math}`\operatorname{Coh}_{i j}^{1 / 2}\left(n, P_{1}, P_{2}\right)` with {math}`\mathrm{i} \neq \mathrm{j}` can be assumed to vanish.

The longitudinal coherence can also be approximated by (Kareem, 1987):

```{math}
:label: eq-wind-21
\operatorname{Coh}_{\mathrm{uu}}^{1 / 2}(\mathrm{n}, \mathrm{r}) \approx \exp \left[-\left\lbrace \left(\frac{\mathrm{r}}{\mathrm{L}_{\mathrm{u}}}\right)^{2}+\left(\frac{\mathrm{nr}}{\overline{\mathrm{U}}_{\mathrm{m}}}\right)^{2}\left(12+\frac{11 \mathrm{r}}{\mathrm{z}_{\mathrm{m}}}\right)^{2}\right\rbrace^{1 / 2}\right]
```

implying a coherence coefficient of {math}`\mathrm{C}=12+11 \mathrm{r} / \mathrm{z}_{\mathrm{m}}` and where

{math}`\mathrm{z}_{\mathrm{m}}=\sqrt{\mathrm{z}_{1} \mathrm{z}_{2}}` 

{math}`\overline{\mathrm{U}}_\mathrm{m} = \sqrt{\overline{\mathrm{U}}_1 \left(\mathrm{z}_1\right) \overline{\mathrm{U}}_2 \left(\mathrm{z}_2\right)}`

For structures of small dimension, i.e. {math}`\mathrm{r}` much smaller than {math}`\mathrm{L}_{\mathrm{w}}`, {math}`\mathrm{r}` can be taken as zero.

## Peak velocities

Spectral moments, {math}`\lambda_{\mathrm{i}}` of higher than the {math}`\mathrm{i}` = 0 order formally do not exist for turbulence spectra (including von Karman and other spectra) fulfilling the Kolmogorov asymptote (asymptotic {math}`\mathrm{f}^{-5 / 3}` behaviour). However, for high frequencies the spectra fall off more rapidly so that truncation of these spectra at frequencies of 5 {math}`\div` 20 Hz makes them finite. Also, filtering by finite areas on which the wind blows removes this mathematical inconvenience. Then, the distribution of extreme gust velocities, {math}`\mathrm{u}_{\max }` is asymptotically a Gumbel distribution with mean:

```{math}
:label: eq-wind-22
\mathrm{E}\left[\mathrm{u}_{\max } \mid \lambda_{0}, \lambda_{2}, \mathrm{t}\right]=\left(\sqrt{2 \ln v_{0} \mathrm{t}}+\gamma / \sqrt{2 \ln v_{0} \mathrm{t}}\right) \sqrt{\lambda_{0}}
```

and variance:

```{math}
:label: eq-wind-23
\operatorname{Var}\left[\mathrm{u}_{\max } \mid \lambda_{0}, \lambda_{2}, \mathrm{t}\right]=\left[\left(\pi^{2} / 6\right) / 2 \ln \mathrm{v}_{0} \mathrm{t}\right] \lambda_{0}
```

{math}`\gamma` = 0.5772 is Euler's constant, {math}`\mathrm{t}` = 600 s and {math}`v_{0}` is the mean frequency of zero upcrossing, in Hz:

```{math}
:label: eq-wind-24
v_{0}=\sqrt{\lambda_{2} / \lambda_{0}}
```

The mean and standard deviation of the random peak factor for gust velocities, {math}`\mathrm{g}` are defined as:

```{math}
:label: eq-wind-25
g =\sqrt{2 \ln v_{0} t}+0.577 / \sqrt{2 \ln v_{0} t} 
```

```{math}
:label: eq-wind-26
\sigma_{\mathrm{g}} =\frac{\pi}{6} \frac{1}{\sqrt{2 \ln v_{0} \mathrm{t}}}
```

The calculation of {math}`\mathrm{g}` from turbulence spectra is sensitive to the choice of cut-off frequency (5-20 Hz). Empirically and theoretically one can assume that the mean of {math}`\mathrm{g}` is about 3.2 for 1 hour (3.8 for 8 hours) and its standard deviation about 0.4 . Since the fluctuating velocity pressure is a linear function of fluctuating velocity of gusts, the above values of {math}`\mathrm{g}` and {math}`\sigma_{\mathrm{g}}` also apply to the peak pressure.

## Mean velocity pressure and the roughness factor

The mean wind velocity pressure {math}`{ }^{2)}` at height {math}`\mathrm{z}` is defined by:

```{math}
:label: eq-wind-27
\overline{\mathrm{Q}}(\mathrm{z})=\frac{1}{2} \rho \overline{\mathrm{U}}^{2}(\mathrm{z})
```

where {math}`\rho` is the air density ( {math}`\rho=1.25 \mathrm{~kg} / \mathrm{m}^{3}` for standard air).

${ }^{2}$ Conversion of the open country velocity pressure for different averaging time intervals can be guided by the following values obtained from [Section 17.2.](section-2.13.2):

$1.1 \overline{\mathrm{Q}}^{1 \mathrm{~h}}=\overline{\mathrm{Q}}^{10 \mathrm{~min}}=0.7 \overline{\mathrm{Q}}^{1 \mathrm{~min}(\text { fastest mile) }}=0.44 \overline{\mathrm{Q}}^{3 \mathrm{~s}}$



The coefficient of variation of the maximum annual velocity pressure is approximately the double of the coefficient of variation of the maximum annual velocity, {math}`\mathrm{V}_{1}` : {math}`\mathrm{V}_{\mathrm{Q}} \cong 2 \mathrm{~V}_{1}`.

The roughness factor describes the variation of the mean velocity pressure with height above ground and terrain roughness as function of the reference velocity pressure. From Eq. {eq}`eq-wind-13` one gets:

```{math}
:label: eq-wind-28
\mathrm{c}_{\mathrm{r}}(\mathrm{z})=\frac{\overline{\mathrm{Q}}(\mathrm{z})}{\overline{\mathrm{Q}}_{\text {ref }}}=\frac{\overline{\mathrm{U}}(\mathrm{z})^{2}}{\overline{\mathrm{U}}_{\text {ref }}^{2}}=\left[\frac{\left(\frac{\mathrm{z}}{\mathrm{z}_{0, \text { ref }}}\right)^{0.07}}{\ln \frac{\mathrm{z}_{\text {ref }}}{\mathrm{z}_{0, \text { ref }}}}\right]^{2}\left(\ln \frac{\mathrm{z}}{\mathrm{z}_{0}}\right)^{2}{z})
```

and {math}`\overline{\mathrm{Q}}(\mathrm{z})=\mathrm{c}_{\mathrm{r}}(\mathrm{z}) \overline{\mathrm{Q}}_{\mathrm{ref}}`

## Gust factor for velocity pressure

The gust factor for velocity pressure is the ratio of the peak velocity pressure to the mean velocity pressure of the wind:

```{math}
:label: eq-wind-29
\mathrm{c}_{\mathrm{g}}(\mathrm{z})=\frac{\mathrm{q}_{\text {peak }}(\mathrm{z})}{\overline{\mathrm{Q}}(\mathrm{z})}=\frac{\overline{\mathrm{Q}}(\mathrm{z})+\mathrm{g} \cdot \sigma_{\mathrm{q}}}{\overline{\mathrm{Q}}(\mathrm{z})}=1+\mathrm{g} \cdot \mathrm{V}_{\mathrm{q}}=1+\mathrm{g}\left[2 \cdot \mathrm{I}_{\mathrm{u}}(\mathrm{z})\right]
```

where:

{math}`\overline{\mathrm{Q}}(\mathrm{z}) \quad=` the mean velocity pressure of the wind

{math}`\sigma_\mathrm{q} \quad=\bar{q}(z, t)^{2^{1 / 2}}=` the root mean squared value of the longitudinal velocity pressure fluctuations from the mean

{math}`\mathrm{V}_{\mathrm{Q}} \quad=` coefficient of variation of the velocity pressure fluctuations (approximately equal to the double of the coefficient of variation of the velocity fluctuations):

{math}`\mathrm{V}_{\mathrm{Q}} \cong 2~\mathrm{I}(\mathrm{z})`

{math}`\mathrm{g} \quad=` the peak factor for velocity pressure.

Approximately, the longitudinal velocity pressure fluctuation, $\mathrm{q}(\mathrm{z}, \mathrm{t})$ is a linear function of the velocity fluctuation. Since:

```{math}
\frac{1}{2} \rho\left[\overline{U}(z)^{2}+u(z, t)\right]^{2}=\frac{1}{2} \rho \overline{U}(z)^{2}+\rho \overline{U}(z) u(z, t)+\frac{1}{2} \rho u(z, t)^{2} \cong \frac{1}{2} \rho \overline{U}(z)^{2}+\rho \overline{U}(z) u(z, t)
```

it is:

{math}`\overline{Q}(z)=\frac{1}{2} \rho \overline{U}(z)^{2}`

{math}`q(z, t) \cong \rho \overline{U}(z) u(z, t)`

and consequently, the mean value and the standard deviation of the peak factor for 10 min. velocity pressure are the same like that for the gust velocity g {math}`\cong` 3.2 and {math}`\sigma_{\mathrm{g}} \cong` 0.4. The values of the peak factor depend on the averaging time interval of the reference velocity. {math}`{ }^{3}`

{math}`{ }^{3}` Since: {math}`\mathrm{q}_{\text {peak }}=\mathrm{c}_{\mathrm{g}}^{1 \min }\left(\mathrm{c}_{\mathrm{r}} \mathrm{Q}_{\text {ref }}^{1 \min }\right)=\mathrm{c}_{\mathrm{g}}^{10 \min }\left(\mathrm{c}_{\mathrm{r}} \mathrm{Q}_{\text {ref }}^{10 \mathrm{~min}}\right)=\mathrm{c}_{\mathrm{g}}^{1 \mathrm{~h}}\left(\mathrm{c}_{\mathrm{r}} \mathrm{Q}_{\text {ref }}^{1 \mathrm{~h}}\right)` from [Section 17.8.](section-2.13.8), the following approximate relations hold: {math}`\mathrm{c}_{\mathrm{g}}^{1 \mathrm{~min}}=0.7 \mathrm{c}_{\mathrm{g}}^{10 \mathrm{~min}}=\mathrm{c}_{\mathrm{g}}^{1 \mathrm{~h}}`

## Exposure factor for peak velocity pressure

The peak velocity pressure at the height $\mathrm{z}$ above ground is the product of the gust factor: the roughness factor and the reference velocity pressure;

```{math}
:label: eq-wind-30
\mathrm{Q}_{\mathrm{g}}(\mathrm{z})=\mathrm{c}_{\mathrm{g}}(\mathrm{z}) \mathrm{c}_{\mathrm{r}}(\mathrm{z}) \mathrm{Q}_{\mathrm{ref}}
```

The exposure factor is defined as the product of the gust and roughness factors:

```{math}
:label: eq-wind-31
\mathrm{c}_{\mathrm{e}}(\mathrm{z})=\mathrm{c}_{\mathrm{g}}(\mathrm{z}) \mathrm{c}_{\mathrm{r}}(\mathrm{z}) 
```

## Aerodynamic shape factors

The aerodynamic shape factor, {math}`\mathrm{c}_{\mathrm{a}}` is the ratio of the aerodynamic pressure exerted by the wind on the surface of a structure and its components to the velocity pressure. The aerodynamic pressure is acting normal to the surface. By convention {math}`\mathrm{c}_{\mathrm{a}}` is assumed positive for pressures and negative for suctions.

As the pressure exerted on a surface is not uniformly distributed over the whole area of the surface or on the different faces of a building, the aerodynamic coefficients should be assessed separately for the different parts and faces of a building.

The aerodynamic shape factors refer either to the mean pressure or to the peak pressure of the wind.

The shape factors are dependent on the geometry and the dimensions of building, the angle of attack of the wind i.e. the relative position of the body in the airflow, terrain category, Reynolds number, etc.

In certain cases the aerodynamic factors for external pressure must be combined with those for internal pressure.

There are two different approaches to the practical assessment of wind effects on rigid structures: using pressure coefficients and using force coefficients.

- In the former case the wind force is the result of the summation of the aerodynamic forces normal to a certain surface. It is intended for parts of the structure.
- In the later case, the wind force is the product of the velocity pressure multiplied by the overall force coefficient times the frontal area of the building. This approach is used within the procedures for calculating the structural response.

Typical values of the aerodynamic shape factors can be selected from appropriate national and international documents or from wind tunnel tests. The aerodynamic shape factors should be determined in wind tunnels capable of modelling the atmospheric boundary layer.

## Uncertainties consideration

The factors involved in the assessment of the wind forces on structures contain uncertainties.

The mean and the coefficient of variation of the wind forces expressed through the product of uncorrelated variables in Eq. {eq}`eq-wind-1` or Eq. {eq}`eq-wind-2` may be written as follows:

```{math}
:label: eq-wind-32
\mathrm{E}(\mathrm{w})=\mathrm{E}\left(\mathrm{c}_{\mathrm{g}}\right) \mathrm{E}\left(\mathrm{c}_{\mathrm{a}}\right) \mathrm{E}\left(\mathrm{c}_{\mathrm{r}}\right) \mathrm{E}\left(\mathrm{Q}_{\mathrm{ref}}\right) 
```

```{math}
:label: eq-wind-33
\mathrm{V}_{\mathrm{w}}^{2}=\mathrm{V}_{\mathrm{c}_{\mathrm{g}}}^{2}+\mathrm{V}_{\mathrm{c}_{\mathrm{a}}}^{2}+\mathrm{V}_{\mathrm{c}_{\mathrm{r}}}^{2}+\mathrm{V}_{\overline{\mathrm{Q}}_{\mathrm{ref}}}^{2}
```

and

```{math}
:label: eq-wind-34
\mathrm{E}(\mathrm{w})=\mathrm{E}\left(\mathrm{c}_{\mathrm{d}}\right) \mathrm{E}\left(\mathrm{c}_{\mathrm{a}}\right) \mathrm{E}\left(\mathrm{c}_{\mathrm{r}}\right) \mathrm{E}\left(\mathrm{Q}_{\mathrm{ref}}\right)
```

```{math}
:label: eq-wind-35
\mathrm{V}_{\mathrm{w}}^{2}=\mathrm{V}_{\mathrm{c}_{\mathrm{d}}}^{2}+\mathrm{V}_{\mathrm{c}_{\mathrm{a}}}^{2}+\mathrm{V}_{\mathrm{c}_{\mathrm{r}}}^{2}+\mathrm{V}_{\overline{\mathrm{Q}}_{\mathrm{ref}}}^{2}
```

Statistics of the above factors are suggested in {numref}`tbl5-wind`. 

```{table} Statistics of random variables involved in the assessment of the wind loading
:name: tbl5-wind
| Variable | Ratio $\frac{\text { Expected }}{\text { Computed }}$ | Coefficient of variation, V | Reference |
| :--- | :---: | :---: | :---: |
| $\overline{\mathrm{Q}}_{\text {ref }}$ <br> $\mathrm{c}_{\mathrm{r}}$ <br> $\mathrm{c}_{\mathrm{a}}$ - pressure coefficients <br> $\quad$ - force coefficients <br> $\mathrm{c}_{\mathrm{g}}$ <br> $\mathrm{c}_{\mathrm{d}}$  | 0.8 <br> 0.8 <br> 1.0 <br> 1.0 <br> 1.0 <br> 1.0  | 0.2 - 0.3 <br> 0.1 - 0.2 <br> 0.1 - 0.3 <br> 0.1 - 0.15 <br> 0.1 - 0.15 <br> 0.1 - 0.2 | Davenport, 1987 |
| Structure period <br> $\quad$ - small amplitudes <br> $\quad$ - large amplitudes <br> Structure damping <br> $\quad$ - small amplitudes <br> $\quad$ - large amplitudes | <br> 0.85 <br> 1.15 <br> <br> 0.8 <br> 1.2 | <br> 0.3 - 0.35 <br> 0.3 - 0.35 <br> <br> 0.4 - 0.6 <br> 0.4 - 0.6 | Vanmarcke, 1992 |
```

Generally, but not necessarily, the lognormal distribution is the recommended probability distribution function for each of the partial factors involved in Eq. {eq}`eq-wind-32` and Eq. {eq}`eq-wind-34`.

**Relevant Literature and References**

Arya S.P., 1993. Atmospheric boundary layer and its parametrization. Proceedings of the NATO Advanced Study Institute on Wind Climate in Cities, Waldbronn, Germany, July 5-16, Kluwer Academic Publishers, Dordrecht/Boston/London, p.41-66

ASCE 7-93, 1993 and Draft of ASCE7-95, 1995. Minimum design loads for buildings and other structures. American Society of Civil Engineers, New York

CIB W81 Commission, 1994. Actions on structures. Wind loads, 6th draft, May

Davenport N.G., 1995. The response of slender structures to wind. In the wind climate and cities. Kluwer Academic Publishers, p.209-239

Davenport A.G., 1987. Proposed new international (ISO) wind load standard. High winds and building codes. Proceedings of the WERC/NSF Wind engineering symposium. Kansas City, Missouri, Nov., p.373-388

Davenport A.G., 1967. Gust loading factors. Journal of the Structural Division, ASCE, Vol.93, No.3, p.1295-1313

Davenport A.G., 1964. Note on the distribution of the largest value of a random function with application to gust loading. Proceedings. Institution of Civil Engineering, London, England, Vol. 28 June, p.187-195

Davenport A.G., 1961. The application of statistical concepts to the wind loading of structures. Proceedings, Institution of Civil Engineering, London, England, Vol.19, Aug., p.449-472

ESDU 85020, Characteristics of atmospheric turbulence near the ground. Part II: single point data for strong winds (neutral atmosphere), April 1993, 36 p. London, U.K.

ESDU 86010, Characteristics of atmospheric turbulence near the ground. Part III: variation in space and time for strong winds (neutral atmosphere), Sept. 1991, 33 p., London, U.K.

European Prestandard ENV 1991-2-4, 1994. EUROCODE 1: Basis of design and actions on structures, Part 2.4 : Wind actions, CEN

Gerstoft P., 1986. An assessment of wind loading on tower shaped structures. Technical University of Denmark, Lingby, Serie R, No.213

Ghiocel D., Lungu D., 1975. Wind, snow and temperature effects on structures, based on probability. Abacus Press, Tunbridge Wells, Kent, U.K.

Harris R.I., Deaves D.M., 1980. The structure of strong winds. The wind engineering in the eighties. Proceedings of CIRIA Conference 12/13 Nov., Construction Industry, Research and Information Association, London, p.4.1-4.93

ISO / TC 98 / SC3 Draft International Standard 4354, 1990. Wind actions on structures. International Organisation for Standardisation

Joint Committee on Structural Safety CEB-CECM-CIB-FIP-IABSE, 1974. Basic data on loads. Second draft. Lisbon Kareem, A., Wind Effects on Structures, Prob. Eng. Mech., 2, 4, 1987, pp. 166-200

Karman v., T., 1948. Progress in statistical theory of turbulence. Proceedings, National Academy of Science, Washington D.C., p.530-539 Lumley J.L., Panofsky H.A., 1964. The structure of atmospheric turbulence. J.Wiley \\& Sons

Lungu D., Gelder P., Trandafir R., 1995. Comparative study of Eurocode 1, ISO and ASCE procedures for calculating wind loads. IABSE Colloquium, Basis of design and actions on structures, Background and application of Eurocode 1, Delft, The Netherlands, 1996

NBC of Canada, 1990. Code National du Bâtiment du Canada, 1990 and Supplement du Code, Comité Associé du Code National du Bâtiment, Conseil National de Recherche, Canada

Plate E.J., 1993. Urban climates and urban climate modelling: An introduction. Proceedings of the NATO Advanced Study Institute on Wind Climate in Cities, Waldbronn, Germany, July 5-16, Kluwer Academic Publishers, Dordrecht/Boston/London, p.23-40

Plate E.J., Davenport A.G., 1993. The risk of wind effects in cities. Proceedings of the NATO Advanced Study Institute on Wind Climate in Cities, Waldbronn, Germany, July 5-16, Kluwer Academic Publishers, Dordrecht/Boston/London, p.1-20 Ruscheweyh H., 1995. Wind loads on structures from Eurocode 1, ENV 1991-2-3. In Wind climate in cities. Kluwer Academic Publishers, p.241-258

Schroers H., Lösslein H., Zilch K., 1990. Untersuchung der Windstructur bei Starkwind und Sturm. Meteorol. Rdsch., 42, Oct., p.202-212

Simiu E., Scanlan R.H., 1986. Wind effects on structures. Second edition. J. Wiley \\& Sons

Simiu E., 1980. Revised procedure for estimating along-wind response. Journal of the Structural Division, ASCE, Vol.106, No.1, p.1-10

Simiu E., 1974. Wind spectra and dynamic along-wind response. Journal of the Structural Division, ASCE, Vol.100, No.9, p.1897-1910

Solari G., 1993. Gust buffeting. I Peak wind velocity and equivalent pressure. Journal of Structural Engineering, ASCE, Vol.119, No.2, p.365-382

Solari G., 1993. Gust buffeting. II Dynamic along-wind response. Journal of Structural Engineering, Vol.119, No.2, p.383398

Solari G., 1988. Equivalent wind spectrum technique: theory and applications. Journal of Structural Engineering ASCE, Vol.114, No.6, p.1303-1323

Solari G., 1987. Turbulence modelling for gust loading. Journal of Structural Engineering, ASCE, Vol.113, No.7, p.11501569

Theurer W., Bachlin W., Plate E.J., 1992. Model study of the development of boundary layer above urban areas. Journal of Wind Engineering and Industrial Aerodynamics, Vol. 41-44, p.437-448, Elsevier

Uniform Building Code, 1991 Edition. International Conference of Building Officials, Whittier, California

Vellozi J., Cohen E., 1968. Gust response factors. Journal of the Structural Division, ASCE, Vol.97, No.6, p.1295-1313

Vickery B.J., 1994. Across - wind loading on reinforced concrete chimneys of circular cross-section. ACI Structural Journal, May-June, p.355-356

Vickery B.J., Basu R., 1983. Simplified approaches to the evaluation of the across-wind response of chimneys. Journal of Wind Engineering and Industrial Aerodynamics, Vol.14, p. 153-166.

Vickery B.J., 1970. On the reliability of gust loading factors. Proceedings, Technical meeting concerning wind loads on buildings and structures, Building Science Series 30, National Bureau of Standards, Washington D.C., p.93-104

Vickery B.J., 1969. Gust response factors. Discussion. Journal of the Structural Division, ASCE, ST3, March, p.494-501

Wieringa J., 1993. Representative roughness parameters for homogenous terrain. Boundary Layer Meteorology, Vol.63, No.4, p.323-364

Wind loading and wind-induced structural response, 1987. State of the art report prepared by the Committee on Wind effects of the Structural Division of ASCE. ASCE, N.Y.