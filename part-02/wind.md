# Wind

**List of symbols:**

$\begin{array}{ll}f_c &= \text { Coriolis parameter} (= 2 \Omega \sin \phi)\\
f_0 &= \text { mean frequency of zero upcrossing, in} Hz\\
g &= \text { peak factor (no dimension)}\\
G_u(n), G_v(n), G_w(n) &= \text { half-sided power spectral density for longitudinal, transversal and vertical components of velocity fluctuations}\\
I_u(z) &= \text { turbulence intensity of longitudinal velocity fluctuations (dimensionless)}\\
k &= \text { von Karman`s constant} (= 0.4)\\
L_u(z) &= \text { integral length scale for longitudinal velocity fluctuations, in} m\\
L_v(z) &= \text { integral length scale for transversal velocity fluctuations, in} m\\
L_w(z) &= \text { integral length scale for vertical velocity fluctuations, in} m\\
N &= \text { number of reference time, in years}\\
n &= \text { frequency, in Hertz}\\
n_u,n_v,n_w &= \text { dimensionless frequency of fluctuations in longitudinal, transversal and vertical direction}\\
\overline{Q}_{ref} &= \text { reference wind velocity pressure}\\
\overline{Q}_z &= \text { mean velocity pressure at height z} = \left((1/2) \rho \overline{U}^2 (z)\right) \\
S_{ij}(n) &= \text { cross spectral power density}\\
T &= \text { reference time}\\
\overline{T}(u_p) &= \text { mean recurrence interval of maximum annual mean velocity, in years}\\
\overline{U}_{ref} &= \text { reference wind velocity, in} m/s\\
\overline{U}(z) &= \text { mean longitudinal velocity of the wind at height} z\\
u_1 &= \text { mode of the maximum annual mean wind speed in Gumbel distribution}\\
u(x,z,t) &=u = \text { longitudinal component of the wind velocity fluctuations, in} m/s\\
v(y,z,t) &=v = \text { transversal component of wind velocity fluctuations, in} m/s\\
w(z,t) &=w = \text { vertical component of wind velocity fluctuations, in} m/s\\
z &= \text { height above ground, in} m\\
z_0  &= \text { roughness length, in} m\\
z_r &= \text { a reference height above ground, in} m\\
z_{ref} &= \text { the reference height above ground} (10 - 30 m)\\
\alpha_1 &= \text { dispersion parameter for the maximum annual mean wind speed in
Gumbel distribution}\\
\delta &= \text { height of the atmospheric boundary layer}\\
\kappa &= \text { surface drag coefficient (dimensionless)} \left(=\left[k/ln(z_{ref}/z_0 \right)\right]^2 )\\
\lambda_{\kappa} &= \text { k-th moment of spectral density}\\
ν(x) &= \text { mean upcrossing rate for level} x\\
\phi &= \text { geographical latitude}\\
\rho &= \text { air density} (= 1.25 kg/m^3 )\\
\sigma_{u}, \sigma_{v},\sigma_{w} &= \text { standard deviation of velocity fluctuations in x-, y- and z-direction, in}~m/s\end{array}$

## Introduction

Wind effects on buildings and structures depend on the general wind climate, the exposure of buildings, structures and their elements to the natural wind, the dynamic properties, the shape and dimensions of the building (structure). The section presents basic data and procedures for the estimation of wind loads on buildings and structures. Tropical cyclones, tornados, thunderstorms and orographic wind phenomena require separate treatment.

The field of wind velocities over horizontal terrain is decomposed into a mean wind (average over 10 minutes) in the direction of general air flow (x-direction) averaged over a specified time interval and a fluctuating, turbulent part with zero mean and components in the longitudinal (x) direction, the transversal (y-) direction and the vertical (z-) direction

(section-2.13.2)=
## Wind forces

The wind force acting per unit area of structure is determined with the relations:

1) For rigid structures of smaller dimensions:

```{math}
:label: eq-wind-1
w=c_{a} c_{g} c_{r} \overline{Q}_{ref}=c_{a} c_{e} \overline{Q}_{ref}
```

2) For structures sensitive to dynamic effects (natural frequency $<1 ~Hz$) and for large rigid structures:

```{math}
:label: eq-wind-2
w=c_{d} c_{a} c_{e} \overline{Q}_{ref}
```

where:

$\overline{Q}_{ref}$  = the reference (mean) velocity pressure   
$c_{r}$  = roughness factor    
$c_{g}$  = gust factor    
$c_{a}$  = aerodynamic shape factor    
$c_{d}$  = dynamic factor.   

## Mean wind velocity

The reference wind velocity, $\overline{U}_{\text {ref }}$ is the mean velocity of the wind averaged over a time interval of 10 $\min =600 ~s$, determined at an elevation of $10 ~m$ above ground, in horizontal open terrain exposure $\left(z_{0}=0.03\right.$ $m)^{1}$

The distribution of the mean wind velocities (for any terrain category, height above ground and averaging time interval) is the Weibull distribution:

```{math}
:label: eq-wind-3
F_{\overline{U}}(x)=1-\exp \left[-\frac{1}{2}\left(\frac{x}{\sigma}\right)^{k}\right]
```

with $k$ close to 2.

${ }^{1}$ For other than 10 min averaging intervals, in open terrain exposure, the following relationships may be used: $1.05 \overline{U}^{1 ~h}=1.0 \overline{U}^{10 ~min}=0.84 \overline{U}^{1 ~min(\text { fastest mile) }}=0.67 \overline{U}^{3 sec}$.  

The same distribution is valid for direction dependent mean wind flows. Generally, it can not be assumed that the mean wind direction is uniformly distributed over the circle.

Mean wind velocities vary over the year. If no data are available it can be assumed in the northern hemisphere that $\sigma(t) \approx \sigma\left[1+a \cos \left(2 \pi\left(t-t_{0}\right) / 365\right]\right.$ with the constant $a$ between $1 / 3$ and $1 / 2$ and $t_{0} \approx 15$ to 45 , with $t$ in days.

The mean wind velocities are highly autocorrelated. Mean wind velocities with separation of about 4 to 12 (8 on average) hours can be considered as independent in most practical applications.

If seasonal variations are neglected, the mean period the mean wind velocities are between levels $x_{1}$ and $x_{2}\left(x_{2} \geq x_{1}\right)$ is asymptotically

```{math}
:label: eq-wind-4
E\left[T_{x_{1}, x_{2}}\right]=T\left[F_{\overline{U}}\left(x_{2}\right)-F_{\overline{U}}\left(x_{1}\right)\right]
```

with $T$ the reference time. For higher levels of $x_{2}$ the distribution of individual times above $x$ is approximately $\left[1-F_{\overline{U}}(x)\right] / v(x)$ with $v(x)$ the mean upcrossing rate for level $x$.

The maximum mean wind speeds for longer periods follows a Gumbel distribution for maxima. Generally, it is not possible to infer the maxima over more years from observations covering only a few years. If the annual maxima are used, provided that the maximum annual data are homogenous as exposure and averaging time, the distribution function is:

```{math}
:label: eq-wind-5
F_{\max \overline{U}}(x)=\exp \left\lbrace-\exp \left[-\alpha_{1}\left(x-u_{1}\right)\right]\right\rbrace
```

The mode $u$ and the parameter $\alpha_{1}$ of the distribution are determined from the mean $m_{1}$ and the standard deviation $\sigma_{1}$ of the set of maximum annual velocities: $u_{1}=m_{1}-0.577 / \alpha_{1}, \alpha_{1}=1.282 / \sigma_{1}$. The coefficient of variation of maximum annual wind speed, $V_{1}=\sigma_{1} / m_{1}$ depends on the climate and is normally between 0.10 and 0.35. For reliable results, the number of the years of available records must be of the same order of magnitude like the required mean recurrence interval.

The lifetime ( $N$ years) maxima of wind velocity is also Gumbel distributed and the mean and the standard deviation of lifetime maxima are functions of the mean and of the standard deviation of annual maxima: $m_{N}+0.78 \sigma_{1} \ln N, \sigma_{N}=\sigma_{1}$.

Under special climatic conditions, the distribution of mean wind speeds is a mixed distribution reflecting different meteorological phenomena.

For load combination purposes it is proposed to model storms, for example those wind regimes where a mean velocity >10 m/s lasts for some time, as an intermittent rectangular wave renewal process. The number of storms per year is approximately 50 corresponding to the frequency with which weather systems pass by, at least in middle Europe. The mean duration of the storm is approximately 8 hours. Consecutive storms are independent. The representative mean wind velocity in a storm can also be modeled by a Weibull distribution. The exponent of the Weibull distribution should be around 2. The location parameter should be based on local data.

## Terrain roughness (category)

The roughness of the ground surface is aerodynamically described by the roughness length $z_{0}$, which is a measure of the size and spacing of obstacles on the ground surface. Alternatively, the terrain roughness can be described by the surface drag coefficient, $\kappa$ corresponding to the roughness length $z_{0}$ :

```{math}
:label: eq-wind-6
\kappa^{2}=\frac{k}{\ln \frac{z_{r e f}}{z_{0}}}
```

where $k \cong 0.4$ is von Karman's constant and $z_{\text {ref }}$ is the reference height ({numref}`table-Scale-factors-for-the-mean-velocity`, {numref}`table-Wind-parameters-depending-on-terrain-category`). Various terrain categories are classified in {numref}`table-Roughness-length-for-various-terrain-categories` according to their approximate roughness lengths. The distribution of the surface roughness with wind direction must be considered.

```{table} Roughness length, in meters, for various terrain categories${}^{1)~2)}$ 
:name: table-Roughness-length-for-various-terrain-categories
| Terrain category | Terrain description | Range of $z_{0}$ | Recommended value |
| :---: | :--- | :---: | :---: |
| A. Open sea. Smooth flat country | Areas exposed to the wind coming from large bodies of water; snow surface; Smooth flat terrain with cut grass and rare obstacles. | 0.0001 <br> $\mid$ <br> 0.0005 | 0.003 |
| B. Open country | High grass (60 cm) hedges, and farmland with isolated trees; <br> Terrain with occasional obstructions having heights less than 10m (some trees and some buildings) | 0.01 <br> $\mid$ <br> 0.1 | 0.03 |
| C. Sparsely built-up urban areas. Wooded areas | Sparsely built-up areas, suburbs, fairly wooded areas (many trees) | 0.1 <br> $\mid$ <br> 0.7 | 0.3 |
| D. Densely built-up urban areas. Forests | Dense forests in which the mean height of trees is about 15m; Densely built-up urban areas; towns in which at least 15% of the surface is covered with buildings having heights over 15m | 0.7 <br> $\mid$ <br> 1.2 | 1.0 |
| E. Centers of very large cities | Numerous large high closely spaced obstructions: more than 50% of the buildings have a height over 20m | 1.0  <br> $\geq$ 2.0 | 2.0 |
```

${ }^{1)}$ Smaller values of $z_{0}$ provoke higher mean velocities of the wind

${ }^{2)}$ For the full development of the roughness category, the terrains of types A to D must prevail in the up wind direction for a distance of at least of 1000 m, respectively. For category E this distance is more than 5 km.

## Variation of the mean wind with height

The variation of the mean wind velocity with height over horizontal terrain of homogenous roughness can be described by the logarithmic law. The logarithmic profile is valid for moderate and strong winds (mean hourly velocity $>10 ~m / s$ ) in neutral atmosphere (where the vertical thermal convection of the air may be neglected).

```{math}
:label: eq-wind-7
\overline{U}(z)=\frac{1}{k} u_{*}\left(z_{0}\right)\left(\ln \frac{z}{z_{0}}+5.75 \frac{z}{\delta}-1.87\left(\frac{z}{\delta}\right)^{2}-1.33\left(\frac{z}{\delta}\right)^{3}+0.25\left(\frac{z}{\delta}\right)^{4}\right) \quad\left(z>d_{0}>>z_{0}\right)
```

where: 

$u(z_0)=\frac{\overline{U}(z)}{2.5 \ln \frac{z}{z_{0}}}=$ friction velocity in $m / s$

$\delta \quad=\frac{u_{*}\left(z_{0}\right)}{6 f_{c}}=$ depth of boundary layer in $m$

$\overline{U}(z)$ = mean velocity of the wind at height $z$ above ground in $m / s$

$z \quad=$ height above ground in $m$

$z_{0} \quad=$ roughness length in $m$

$k=$ von Karman's constant $(k \cong 0.4)$

$d_{0} \quad=$ the lowest height of validity of Eq.{eq}`eq-wind-7` in $m$

$f_{c} \quad=2 \Omega \sin (\phi)=$ Coriolis parameter in 1/s

$\Omega \quad=0.726~10^{-4}=$ angular rotation velocity in $rad / s$

$\phi \quad=$ latitude of location in degree

For lowest 0.1 $\delta$ or 200 m of the boundary layer only the first term needs to be taken into account {cite}`Harris1980`. The lowest height of validity for Eq.{eq}`eq-wind-7`, $d_{0}$, is close to the average height of dominant roughness elements : i.e. from less than 1 m, for smooth flat country to more than 15 m, for centers of cities. For $z_{0} \leq z \leq d_{0}$ a linear interpolation is recommended. In engineering practice, Eq.{eq}`eq-wind-7` is conservatively used with $d_{0}=0$.

With respect to the reference (open terrain) exposure, the relation between wind velocities in two different roughness categories at two different heights can be written approximately as (Bietry, 1976, Simiu, {cite}`Simiu1986`):

```{math}
:label: eq-wind-8
\frac{\overline{U}(z)}{\overline{U}_{\text {ref }}}=\frac{\ln \frac{Z}{Z_{0}}}{\ln \frac{Z_{\text {ref }}}{Z_{0, \text { ref }}}}\left(\frac{z_{0}}{z_{0, r e f}}\right)^{0.07}
```

At the reference height $z_{ref}$, the ratio of the mean wind velocity in various terrain categories to the mean wind velocity in open terrain is given by the factor $p$ in {numref}`table-Scale-factors-for-the-mean-velocity`. The corresponding ratio for the mean velocity pressure is $p^{2}$.

Table 2. Scale factors for the mean velocity (and the mean velocity pressure) at reference height in various terrain exposure

```{table} Scale factors for the mean velocity (and the mean velocity pressure) at reference height in various terrain exposure
:name: table-Scale-factors-for-the-mean-velocity
| Terrain category | A. Open sea. Smooth flat country | B. Open country | C. Sparsely built-up urban areas. Wooded areas | D. Densely built-up urban areas. Forests | E. Centers of large cities |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $z_{\text {ref }}, m$ | 10 | 10 | 10 | 15 | 30 |
| $p$ | 1.19 | 1.00 | 0.71 | 0.56 | 0.39 |
```

## Intensity of turbulence

The turbulent fluctuations of the wind velocity can be assumed to be normally distributed with mean zero. The root mean squared value of the velocity fluctuations in the airflow, deviating from the longitudinal mean velocity, may be normalised to the friction velocity as follows:

```{math}
:label: eq-wind-9a
\frac{\sigma_{u}}{u_{*}}=\beta_{u}\left(1-\frac{z}{\delta}\right)  \quad \text { Longitudinal } 
```

```{math}
:label: eq-wind-9b
\frac{\sigma_{v}}{u_{*}}=\beta_{v}\left(1-\frac{z}{\delta}\right)  \quad \text { Transversal } 
```

```{math}
:label: eq-wind-9c
\frac{\sigma_{w}}{u_{*}}=\beta_{w}\left(1-\frac{z}{\delta}\right)  \quad \text { Vertical }
```

The approximate linear variation with height (Hanna, 1982) can be used only in moderate and strong winds. For neutral atmosphere, the ratios$`\sigma_{v} / \sigma_{u}$ and $\sigma_{w} / \sigma_{u}$ near the ground are constant irrespective of the roughness of the terrain {cite}`ESDU85020`:

```{math}
:label: eq-wind-10a
\frac{\sigma_{v}}{\sigma_{u}}=1-0.25 \cos ^{4}\left(\frac{\pi}{2} \frac{z}{\delta}\right) 
```

```{math}
:label: eq-wind-10b
\frac{\sigma_{w}}{\sigma_{u}}=1-0.55 \cos ^{4}\left(\frac{\pi}{2} \frac{z}{\delta}\right)
```

For $z<<\delta$ the variance of the velocity fluctuations can be assumed independent of height above ground :

```{math}
:label: eq-wind-11a
\sigma_{u}=\beta_{u} u_{*}
```

```{math}
:label: eq-wind-11b
\sigma_{v}=\beta_{v} u_{*}
```

```{math}
:label: eq-wind-11c
\sigma_{w}=\beta_{w} u_{*}
```

and, for $z<0.1 \delta$ :

```{math}
:label: eq-wind-12a
\frac{\sigma_{v}}{\sigma_{u}} \cong 0.75
```

```{math}
:label: eq-wind-12b
\frac{\sigma_{w}}{\sigma_{u}} \cong 0.505
```

The variance of the longitudinal velocity fluctuations can also be expressed from non-linear regression of measurement data, as function of terrain roughness {cite}`Solari1987`:

```{math}
:label: eq-wind-13
4.5 \leq \beta_{u}^{2}=4.5-0.856 \ln z_{0} \leq 7.5
```

The longitudinal intensity of turbulence is the ratio of the root mean squared value of the longitudinal velocity fluctuations to the mean wind velocity at height $z$ (i.e. the coefficient of variation of the velocity fluctuations at height $z$) :

```{math}
:label: eq-wind-14
I_u (z) = \frac{\overline{u(z,t)^2}^{1/2}}{\overline{U}(z)}= \frac{\sigma_u z}{\overline{U}(z)}
```

The turbulence intensity at height $z$ can be approximated by:

```{math}
:label: eq-wind-15
I(z)=\frac{\beta_{u}}{2.5 \ln \frac{z}{z_{0}}} \approx \frac{1}{\ln \frac{z}{z_{0}}}
```

The transversal and vertical intensities of turbulence can be determined by multiplication of the longitudinal intensity $I_{u}(z)$ by the ratios $\sigma_{v} / \sigma_{u}$ and $\sigma_{w} / \sigma_{u}$. Representative values for intensity of turbulence at the reference height are given in {numref}`table-Wind-parameters-depending-on-terrain-category`.

```{table} Wind parameters depending on terrain category
:name: table-Wind-parameters-depending-on-terrain-category
| Terrain category | A. Open sea. Smooth flat country | B.Open country | C. Sparsely built-up urban areas. Wooded areas | D. Densely built-up urban areas.Forests | E. Centers of large cities |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $z_{0}[~m]$ | 0.01 | 0.05 | 0.3 | 1.0 | 2.0 |
| $d_{0}[~m]$ | 0 | 2 | 8 | 15 | 30 |
| $\kappa$ | 0.0024 | 0.0047 | 0.013 | 0.022 | 0.022 |
| $\beta_{u}$ | 3.1 | 2.7 | 2.3 | 2.1 | 2.0 |
| $\beta_{v}$ | 2.3 | 2.1 | 1.8 | 1.6 | 1.5 |
| $\beta_{w}$ | 1.55 | 1.35 | 1.15 | 1.05 | 1.0 |
| $Z_{ref}[m]$ | 10 | 10 | 10 | 15 | 30 |
| $I\left(z_{ref}\right)$ | 0.15 | 0.19 | 0.26 | 0.31 | 0.39 |
```

## Power spectral density and autocorrelation function of gustiness

The normalised half-sided von Karman power spectral densities and autocorrelation functions of gust velocity are given in {numref}`table-von-Karman-model-of-isotropic-turbulence`.

```{table} The von Karman model of isotropic turbulence
:name: table-von-Karman-model-of-isotropic-turbulence
| Component of gust velocity | Normalised spectral density <br> $\frac{nG_{i}(n)}{\sigma_{i}^{2}}$ | Normalised autocorrelation function <br> $\rho_{i}\left(\tau_{i}\right)$ |
| :---: | :---: | :---: |
| Longitudinal <br> $I = u$ | $\frac{4 n_{u}}{\left(1+70.8 n_{u}^{2}\right)^{5 / 6}}$ | $\frac{2^{2 / 3}}{\Gamma(1 / 3)} \bar{\tau}_{u}^{1 / 3} ~K_{1 / 3}\left(\bar{\tau}_{u}\right)$ |
| Transversal <br> $I=v$ <br> <br> Vertical <br> $i=w$ | <br> <br> $\frac{2 n_{i}\left(1+188.6 n_{i}^{2}\right)}{\left(1+70.8 n_{i}^{2}\right)^{11 / 6}}$ | <br> <br> $\frac{2^{2 / 3}}{\Gamma(1 / 3)} \bar{\tau}_{i}^{1 / 3}\left[K_{1 / 3}\left(\bar{\tau}_{i}\right)-\frac{1}{2} \bar{\tau}_{i} K_{2 / 3}\left(\bar{\tau}_{i}\right)\right]$ |
```

The notations in {numref}`table-von-Karman-model-of-isotropic-turbulence` are as follows:

$\sigma_{i}^{2}$ = variance of velocity fluctuations in direction $i$, $m^{2} / s^{2}$ ; $~~~i=u, v$ or $w$

$n_{i}  = n_{i}(z) = \frac{n L_{i}(z)}{\overline{U}}(z)$ = is a non-dimensional height dependent frequency

$n$ = frequency, in Hertz 

$\overline{U}(z)$ = longitudinal mean velocity at height $z$ , in $m / s$

$L_{i}(z)$  = length of integral scale of turbulence in direction $i$ , in $m / s$ 

$\bar{\tau}_{i}=\frac{\tau \overline{U}(z)}{a L_{i}(z)}$ = non-dimensional time $(a=1.339)$

$K_{\mu}()$ = modified Bessel function of second kind of order $\mu$

$\tau$ = time lag, in $s$

The integral length scale of turbulence in direction $i$ at the height $z$ is:

```{math}
:label: eq-wind-16
L_{i}(z)=U(z) \int_{0}^{\infty} \rho_{i} (\tau_{i}) d \tau_{i}
```

where the autocorrelation $\rho_{i}\left(\tau_{i}\right)$ is the Fourier transform of spectral density. An estimation of the length of the integral scale of longitudinal turbulence, for heights up to 300 m is given by {cite}`ESDU85020`, as:

```{math}
:label: eq-wind-17
L_{u}(z)=\frac{A^{3 / 2}\left(\sigma_{u} / u_{*}\right)^{3} z}{2.5 ~K_{z}^{3 / 2}(1-z / h)^{2}(1+5.75 z / h)}
```

where

$A=0.115\left[1+0.315\left(1-\frac{z}{\delta}\right)^{6}\right]^{2 / 3}$

$K_{z}=0.188\left[1-\left(1-z / z_{c}\right)^{2}\right]^{1 / 2}$

$z_{c} / \delta=0.39\left[\frac{u_{*}}{f_{c} z_{0}}\right]^{-1 / 8}$

For the lateral and vertical direction {cite}`ESDU85020`:

```{math}
:label: eq-wind-18a
L_{v}(z)=0.5\left(\sigma_{v} / \sigma_{u}\right)^{3} ~L_{u}(z)
``` 

```{math}
:label: eq-wind-18b
L_{w}(z)=0.5\left(\sigma_{w} / \sigma_{u}\right)^{3} ~L_{u}(z)
``` 

```{math}
:label: eq-wind-18c
L_{v}(z) \cong 0.24 ~L_{u}(z
``` 

```{math}
:label: eq-wind-18d
L_{w}(z) \cong 0.08 ~L_{u}(z)
``` 
(section-2.13.8)=
## Coherence function

The cross-spectral density for two separated points $P_{1}$ and $P_{2}$ with distance $r$ perpendicular to direction $i$ are given in terms of the point spectra and the coherence function by:

```{math}
:label: eq-wind-19
S_{ij}\left(n, P_{1}, P_{2}\right) \approx S_{ii}^{1 / 2}\left(n, P_{1}, P_{2}\right) S_{jj}^{1 / 2}\left(n, P_{1}, P_{2}\right) \cdot \operatorname{Coh}_{ij}^{1 / 2}\left(n, P_{1}, P_{2}\right)
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

where $\overline{k}=\frac{2 \pi n}{\overline{U}_{m}}$ and $\psi_{i}^{2}=\left(r^{2} \overline{k}^{2}+r^{2} / L_{i}^{2}\right)$. All coherence function $\operatorname{Coh}_{i j}^{1 / 2}\left(n, P_{1}, P_{2}\right)$ with $i \neq j$ can be assumed to vanish.

The longitudinal coherence can also be approximated by {cite}`JointCommittee1974`:

```{math}
:label: eq-wind-21
\operatorname{Coh}_{uu}^{1 / 2}(n, r) \approx \exp \left[-\left\lbrace \left(\frac{r}{L_{u}}\right)^{2}+\left(\frac{nr}{\overline{U}_{m}}\right)^{2}\left(12+\frac{11 r}{z_{m}}\right)^{2}\right\rbrace^{1 / 2}\right]
```

implying a coherence coefficient of $C=12+11 r / z_{m}$ and where

$z_{m}=\sqrt{z_{1} z_{2}}$ 

$\overline{U}_m = \sqrt{\overline{U}_1 \left(z_1\right) \overline{U}_2 \left(z_2\right)}$

For structures of small dimension, i.e. $r$ much smaller than $L_{w}$, $r$ can be taken as zero.

## Peak velocities

Spectral moments, $\lambda_{i}$ of higher than the $i$ = 0 order formally do not exist for turbulence spectra (including von Karman and other spectra) fulfilling the Kolmogorov asymptote (asymptotic $f^{-5 / 3}$ behaviour). However, for high frequencies the spectra fall off more rapidly so that truncation of these spectra at frequencies of 5 $\div$ 20 Hz makes them finite. Also, filtering by finite areas on which the wind blows removes this mathematical inconvenience. Then, the distribution of extreme gust velocities, $u_{\max }$ is asymptotically a Gumbel distribution with mean:

```{math}
:label: eq-wind-22
E\left[u_{\max } \mid \lambda_{0}, \lambda_{2}, t\right]=\left(\sqrt{2 \ln v_{0} t}+\gamma / \sqrt{2 \ln v_{0} t}\right) \sqrt{\lambda_{0}}
```

and variance:

```{math}
:label: eq-wind-23
\operatorname{Var}\left[u_{\max } \mid \lambda_{0}, \lambda_{2}, t\right]=\left[\left(\pi^{2} / 6\right) / 2 \ln v_{0} t\right] \lambda_{0}
```

$\gamma$ = 0.5772 is Euler's constant, $t$ = 600 s and $v_{0}$ is the mean frequency of zero upcrossing, in $Hz$:

```{math}
:label: eq-wind-24
v_{0}=\sqrt{\lambda_{2} / \lambda_{0}}
```

The mean and standard deviation of the random peak factor for gust velocities, $g$ are defined as:

```{math}
:label: eq-wind-25
g =\sqrt{2 \ln v_{0} t}+0.577 / \sqrt{2 \ln v_{0} t} 
```

```{math}
:label: eq-wind-26
\sigma_{g} =\frac{\pi}{6} \frac{1}{\sqrt{2 \ln v_{0} t}}
```

The calculation of $g$ from turbulence spectra is sensitive to the choice of cut-off frequency (5-20 Hz). Empirically and theoretically one can assume that the mean of $g$ is about 3.2 for 1 hour (3.8 for 8 hours) and its standard deviation about 0.4 . Since the fluctuating velocity pressure is a linear function of fluctuating velocity of gusts, the above values of $g$ and $\sigma_{g}$ also apply to the peak pressure.

## Mean velocity pressure and the roughness factor

The mean wind velocity pressure ${ }^{2)}$ at height $z$ is defined by:

```{math}
:label: eq-wind-27
\overline{Q}(z)=\frac{1}{2} \rho \overline{U}^{2}(z)
```

where $\rho$ is the air density ( $\rho=1.25 ~kg / m^{3}$ for standard air).

${ }^{2}$ Conversion of the open country velocity pressure for different averaging time intervals can be guided by the following values obtained from [Section 17.2.](section-2.13.2):

$1.1 \overline{Q}^{1 ~h}=\overline{Q}^{10 ~min}=0.7 \overline{Q}^{1 ~min(\text { fastest mile) }}=0.44 \overline{Q}^{3 ~s}$



The coefficient of variation of the maximum annual velocity pressure is approximately the double of the coefficient of variation of the maximum annual velocity, $V_{1}$ : $V_{Q} \cong 2~V_{1}$.

The roughness factor describes the variation of the mean velocity pressure with height above ground and terrain roughness as function of the reference velocity pressure. From Eq. {eq}`eq-wind-13` one gets:

```{math}
:label: eq-wind-28
c_{r}(z)=\frac{\overline{Q}(z)}{\overline{Q}_{\text {ref }}}=\frac{\overline{U}(z)^{2}}{\overline{U}_{\text {ref }}^{2}}=\left[\frac{\left(\frac{z}{z_{0, \text { ref }}}\right)^{0.07}}{\ln \frac{z_{\text {ref }}}{z_{0, \text { ref }}}}\right]^{2}\left(\ln \frac{z}{z_{0}}\right)^{2}{z})
```

and $\overline{Q}(z)=c_{r}(z) \overline{Q}_{ref}$

## Gust factor for velocity pressure

The gust factor for velocity pressure is the ratio of the peak velocity pressure to the mean velocity pressure of the wind:

```{math}
:label: eq-wind-29
c_{g}(z)=\frac{q_{\text {peak }}(z)}{\overline{Q}(z)}=\frac{\overline{Q}(z)+g \cdot \sigma_{q}}{\overline{Q}(z)}=1+g \cdot V_{q}=1+g\left[2 \cdot I_{u}(z)\right]
```

where:

$\overline{Q}(z) \quad=$ the mean velocity pressure of the wind

$\sigma_q \quad=\bar{q}(z, t)^{2^{1 / 2}}=$ the root mean squared value of the longitudinal velocity pressure fluctuations from the mean

$V_{Q} \quad=$ coefficient of variation of the velocity pressure fluctuations (approximately equal to the double of the coefficient of variation of the velocity fluctuations):

$V_{Q} \cong 2~I(z)$

$g \quad=$ the peak factor for velocity pressure.

Approximately, the longitudinal velocity pressure fluctuation, $q(z, t)$ is a linear function of the velocity fluctuation. Since:

```{math}
\frac{1}{2} \rho\left[\overline{U}(z)^{2}+u(z, t)\right]^{2}=\frac{1}{2} \rho \overline{U}(z)^{2}+\rho \overline{U}(z) u(z, t)+\frac{1}{2} \rho u(z, t)^{2} \cong \frac{1}{2} \rho \overline{U}(z)^{2}+\rho \overline{U}(z) u(z, t)
```

it is:

$\overline{Q}(z)=\frac{1}{2} \rho \overline{U}(z)^{2}$

$q(z, t) \cong \rho \overline{U}(z) u(z, t)$

and consequently, the mean value and the standard deviation of the peak factor for 10 min. velocity pressure are the same like that for the gust velocity g $\cong$ 3.2 and $\sigma_{g} \cong$ 0.4. The values of the peak factor depend on the averaging time interval of the reference velocity. ${ }^{3}$

${ }^{3}$ Since: $q_{\text {peak }}=c_{g}^{1 \min }\left(c_{r} Q_{\text {ref }}^{1 \min }\right)=c_{g}^{10 \min }\left(c_{r} Q_{\text {ref }}^{10 ~min}\right)=c_{g}^{1 ~h}\left(c_{r} Q_{\text {ref }}^{1 ~h}\right)$ from [Section 17.8.](section-2.13.8), the following approximate relations hold: $c_{g}^{1 ~min}=0.7 c_{g}^{10 ~min}=c_{g}^{1 ~h}$

## Exposure factor for peak velocity pressure

The peak velocity pressure at the height $z$ above ground is the product of the gust factor: the roughness factor and the reference velocity pressure;

```{math}
:label: eq-wind-30
Q_{g}(z)=c_{g}(z) c_{r}(z) Q_{ref}
```

The exposure factor is defined as the product of the gust and roughness factors:

```{math}
:label: eq-wind-31
c_{e}(z)=c_{g}(z) c_{r}(z) 
```

## Aerodynamic shape factors

The aerodynamic shape factor, $c_{a}$ is the ratio of the aerodynamic pressure exerted by the wind on the surface of a structure and its components to the velocity pressure. The aerodynamic pressure is acting normal to the surface. By convention $c_{a}$ is assumed positive for pressures and negative for suctions.

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
E(w)=E\left(c_{g}\right) E\left(c_{a}\right) E\left(c_{r}\right) E\left(Q_{ref}\right) 
```

```{math}
:label: eq-wind-33
V_{w}^{2}=V_{c_{g}}^{2}+V_{c_{a}}^{2}+V_{c_{r}}^{2}+V_{\overline{Q}_{ref}}^{2}
```

and

```{math}
:label: eq-wind-34
E(w)=E\left(c_{d}\right) E\left(c_{a}\right) E\left(c_{r}\right) E\left(Q_{ref}\right)
```

```{math}
:label: eq-wind-35
V_{w}^{2}=V_{c_{d}}^{2}+V_{c_{a}}^{2}+V_{c_{r}}^{2}+V_{\overline{Q}_{ref}}^{2}
```

Statistics of the above factors are suggested in {numref}`table-Statistics-of-random-variables-involved-in-the-assessment-of-the-wind-loading`. 

```{table} Statistics of random variables involved in the assessment of the wind loading
:name: table-Statistics-of-random-variables-involved-in-the-assessment-of-the-wind-loading
| Variable | Ratio $\frac{\text { Expected }}{\text { Computed }}$ | Coefficient of variation, $V$ | Reference |
| :--- | :---: | :---: | :---: |
| $\overline{\mathrm{Q}}_{\text {ref }}$ <br> $\mathrm{c}_{\mathrm{r}}$ <br> $\mathrm{c}_{\mathrm{a}}$ - pressure coefficients <br> $\quad$ - force coefficients <br> $\mathrm{c}_{\mathrm{g}}$ <br> $\mathrm{c}_{\mathrm{d}}$  | 0.8 <br> 0.8 <br> 1.0 <br> 1.0 <br> 1.0 <br> 1.0  | 0.2 - 0.3 <br> 0.1 - 0.2 <br> 0.1 - 0.3 <br> 0.1 - 0.15 <br> 0.1 - 0.15 <br> 0.1 - 0.2 | {cite}`Davenport1987` |
| Structure period <br> $\quad$ - small amplitudes <br> $\quad$ - large amplitudes <br> Structure damping <br> $\quad$ - small amplitudes <br> $\quad$ - large amplitudes | <br> 0.85 <br> 1.15 <br> <br> 0.8 <br> 1.2 | <br> 0.3 - 0.35 <br> 0.3 - 0.35 <br> <br> 0.4 - 0.6 <br> 0.4 - 0.6 | Vanmarcke, 1992 |
```

Generally, but not necessarily, the lognormal distribution is the recommended probability distribution function for each of the partial factors involved in Eq. {eq}`eq-wind-32` and Eq. {eq}`eq-wind-34`.

**References**

```{bibliography}
:filter: docname in docnames
```

**Additional References**

1. Arya S.P., 1993. Atmospheric boundary layer and its parametrization. Proceedings of the NATO Advanced Study Institute on Wind Climate in Cities, Waldbronn, Germany, July 5-16, Kluwer Academic Publishers, Dordrecht/Boston/London, p.41-66

2. ASCE 7-93, 1993 and Draft of ASCE7-95, 1995. Minimum design loads for buildings and other structures. American Society of Civil Engineers, New York

3. CIB W81 Commission, 1994. Actions on structures. Wind loads, 6th draft, May

4. Davenport N.G., 1995. The response of slender structures to wind. In the wind climate and cities. Kluwer Academic Publishers, p.209-239

5. Davenport A.G., 1967. Gust loading factors. Journal of the Structural Division, ASCE, Vol.93, No.3, p.1295-1313

6. Davenport A.G., 1964. Note on the distribution of the largest value of a random function with application to gust loading. Proceedings. Institution of Civil Engineering, London, England, Vol. 28 June, p.187-195

7. Davenport A.G., 1961. The application of statistical concepts to the wind loading of structures. Proceedings, Institution of Civil Engineering, London, England, Vol.19, Aug., p.449-472

8. ESDU 86010, Characteristics of atmospheric turbulence near the ground. Part III: variation in space and time for strong winds (neutral atmosphere), Sept. 1991, 33 p., London, U.K.

9. European Prestandard ENV 1991-2-4, 1994. EUROCODE 1: Basis of design and actions on structures, Part 2.4 : Wind actions, CEN

10. Gerstoft P., 1986. An assessment of wind loading on tower shaped structures. Technical University of Denmark, Lingby, Serie R, No.213

11. Ghiocel D., Lungu D., 1975. Wind, snow and temperature effects on structures, based on probability. Abacus Press, Tunbridge Wells, Kent, U.K.

12. ISO / TC 98 / SC3 Draft International Standard 4354, 1990. Wind actions on structures. International Organisation for Standardisation

13. Karman v., T., 1948. Progress in statistical theory of turbulence. Proceedings, National Academy of Science, Washington D.C., p.530-539 Lumley J.L., Panofsky H.A., 1964. The structure of atmospheric turbulence. J.Wiley \\& Sons

14. Lungu D., Gelder P., Trandafir R., 1995. Comparative study of Eurocode 1, ISO and ASCE procedures for calculating wind loads. IABSE Colloquium, Basis of design and actions on structures, Background and application of Eurocode 1, Delft, The Netherlands, 1996

15. NBC of Canada, 1990. Code National du Bâtiment du Canada, 1990 and Supplement du Code, Comité Associé du Code National du Bâtiment, Conseil National de Recherche, Canada

16. Plate E.J., 1993. Urban climates and urban climate modelling: An introduction. Proceedings of the NATO Advanced Study Institute on Wind Climate in Cities, Waldbronn, Germany, July 5-16, Kluwer Academic Publishers, Dordrecht/Boston/London, p.23-40

17. Plate E.J., Davenport A.G., 1993. The risk of wind effects in cities. Proceedings of the NATO Advanced Study Institute on Wind Climate in Cities, Waldbronn, Germany, July 5-16, Kluwer Academic Publishers, Dordrecht/Boston/London, p.1-20 Ruscheweyh H., 1995. Wind loads on structures from Eurocode 1, ENV 1991-2-3. In Wind climate in cities. Kluwer Academic Publishers, p.241-258

18. Schroers H., Lösslein H., Zilch K., 1990. Untersuchung der Windstructur bei Starkwind und Sturm. Meteorol. Rdsch., 42, Oct., p.202-212

19. Simiu E., 1980. Revised procedure for estimating along-wind response. Journal of the Structural Division, ASCE, Vol.106, No.1, p.1-10

20. Simiu E., 1974. Wind spectra and dynamic along-wind response. Journal of the Structural Division, ASCE, Vol.100, No.9, p.1897-1910

21. Solari G., 1993. Gust buffeting. I Peak wind velocity and equivalent pressure. Journal of Structural Engineering, ASCE, Vol.119, No.2, p.365-382

22. Solari G., 1993. Gust buffeting. II Dynamic along-wind response. Journal of Structural Engineering, Vol.119, No.2, p.383398

23. Solari G., 1988. Equivalent wind spectrum technique: theory and applications. Journal of Structural Engineering ASCE, Vol.114, No.6, p.1303-1323

24. Theurer W., Bachlin W., Plate E.J., 1992. Model study of the development of boundary layer above urban areas. Journal of Wind Engineering and Industrial Aerodynamics, Vol. 41-44, p.437-448, Elsevier

25. Uniform Building Code, 1991 Edition. International Conference of Building Officials, Whittier, California

26. Vellozi J., Cohen E., 1968. Gust response factors. Journal of the Structural Division, ASCE, Vol.97, No.6, p.1295-1313

27. Vickery B.J., 1994. Across - wind loading on reinforced concrete chimneys of circular cross-section. ACI Structural Journal, May-June, p.355-356

28. Vickery B.J., Basu R., 1983. Simplified approaches to the evaluation of the across-wind response of chimneys. Journal of Wind Engineering and Industrial Aerodynamics, Vol.14, p. 153-166.

29. Vickery B.J., 1970. On the reliability of gust loading factors. Proceedings, Technical meeting concerning wind loads on buildings and structures, Building Science Series 30, National Bureau of Standards, Washington D.C., p.93-104

30. Vickery B.J., 1969. Gust response factors. Discussion. Journal of the Structural Division, ASCE, ST3, March, p.494-501

31. Wieringa J., 1993. Representative roughness parameters for homogenous terrain. Boundary Layer Meteorology, Vol.63, No.4, p.323-364

32. Wind loading and wind-induced structural response, 1987. State of the art report prepared by the Committee on Wind effects of the Structural Division of ASCE. ASCE, N.Y.

