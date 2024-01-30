# Properties of Timber


**List of most important symbols:**

{math}`R_{m} \quad` bending strength

{math}`E_{m} \quad` bending MOE

{math}`\rho_{\text {den }} \quad` density

{math}`R_{t, 0 / 90} \quad` tension strength

{math}`E_{t, 0 / 90} \quad` tension MOE

{math}`R_{c, 0 / 90} \quad` compression strength

{math}`E_{c, 0 / 90}` compression MOE

{math}`R_{v} \quad` shear strength

{math}`G_{v} \quad` shear modulus

{math}`R_{h, 0 / 90} \quad` embedding strength

{math}`\sigma \quad` stress

{math}`\varepsilon \quad` strain

{math}`E_{t}` tension MOE

{math}`E_{c}` compression MOE

{math}`R_{c} \quad` compression strength

{math}`R_{c, y} \quad` asymptotic final compression strength

{math}`R_{t} \quad` tension strength

{math}`\varepsilon_{u} \quad` ultimate strain

{math}`S(t) \quad` load history

{math}`\omega` humidity

{math}`\tau \quad` temperature

{math}`T \quad` time

{math}`\alpha \quad` strength modification function

{math}`\alpha_{D}, \alpha_{\kappa} \quad` damage state

{math}`\delta \quad` stiffness modification function

{math}`R_{0} \quad` failure stress under short term ramp loading

{math}`X_{M} \quad` model uncertainty

{math}`\hat{x} \quad` tests data

{math}`i \quad` strength indicator

## Introduction

Timber is a rather complex building material. Its properties are highly variable, spatially and in time. In structural engineering, material properties of timber are the stress and stiffness related properties of standard test specimen under given (standard) loading and climate conditions and the timber density. Timber is a graded material. Due to the grading process, the material properties are associated with some control scheme, whereas only the so-called reference material properties are considered explicitly. The so-called other material properties are only assessed implicitly. The distinction between reference properties and other properties is made as illustrated in {numref}`fig-timber-1` . The bending strength {math}`R_{m}`, the bending modulus of elasticity {math}`E_{m}` and the timber density {math}`\rho_{d e n}` are referred to as the reference material properties.

```{figure} ../part-03/images/fig-timber-1.jpg
:name: fig-timber-1

Reference material properties and other material properties.
```

```{figure} ../part-03/images/fig-timber-2.jpg
:name: fig-timber-2

Outline of the modelling of timber material properties.
```

When modelling timber material properties in a structure, i.e. at any generic point, in time and in space, several issues have to be taken into account. As illustrated in {numref}`fig-timber-2` the cornerstone of the modelling of timber material properties are the reference material properties under test conditions. The material property of interest at any generic point may deviate in terms of type ('other material properties'), of dimensions ('scale') and of specific loading and climate conditions ('time (load/moisture)').

The models in this model code relate to solid structural timber and are predominantly based on test programs and investigations considering European and North American softwoods. For some other softwoods and especially for hardwood the underlying assumptions are less appropriate.

## Basic Model

### Stress-strain relationship

```{figure} ../part-03/images/fig-timber-3.jpg
:height: 200px
:name: fig-timber-3

Stress-strain relation according to Glos [1]. A simplified linear elastic-plastic stressstrain curve is shown with thin line.
```

In {numref}`fig-timber-3` an idealised stress-strain relationship under axial load is shown for {math}`\underline{\text{small clear timber specimens}}`, according to Glos, [1]. In tension there is a linear relationship described by the modulus of elasticity {math}`E_{t}`. In compression the relation is described by the initial modulus of elasticity {math}`E_{c}`, the compression strength {math}`R_{c}`, the asymptotic final compression strength {math}`R_{c, y}`, the strain {math}`\varepsilon_{c}` at maximum stress and the ultimate strain {math}`\varepsilon_{u}`. The following empirical relation is assumed:

```{math}
:label: eq-timber-1
\sigma(\varepsilon)=\left\lbrace \begin{array}{ccc}\frac{\varepsilon+k_{1} \varepsilon^{N}}{k_{2}+k_{3} \varepsilon+k_{4} \varepsilon^{N}} & \text { for } & -\varepsilon_{u} \leq \varepsilon \leq 0 \\ \\ E_{t} \varepsilon & \text { for } & 0 \leq \varepsilon \leq \varepsilon_{t}\end{array}\right.
```

where

```{math}
:label: eq-timber-2
k_{1}=\frac{R_{c, y}}{(N-1) \cdot E_{c} \cdot \varepsilon_{c}^{(N-1)}\left(1-R_{c, y} / R_{c}\right)}
```

```{math}
:label: eq-timber-3
k_{2}=\frac{1}{E_{c}}
```

```{math}
:label: eq-timber-4
k_{3}=\frac{1}{R_{c}}-\frac{N}{(N-1) \cdot E_{c} \cdot \varepsilon_{c}}
```

```{math}
:label: eq-timber-5
k_{4}=\frac{k_{1}}{R_{c, y}}
```

Conditions for {eq}`eq-timber-1`:

```{math}
:label: eq-timber-6
R_{c, y} \leq R_{c}-1[\mathrm~{\text{MPa}}] \qquad \varepsilon_{c} \geq \frac{N}{(N-1)} \frac{R_{c}}{E_{c}}
```

Typical values for the parameters are:  
{math}`R_{c, y} / R_{c} \approx 0.8 \qquad \varepsilon_{c}=0.8-1.2 \% \qquad \varepsilon_{u} \approx 3 \varepsilon_{c \qquad }N=7`

For {math}`\underline{\text{structural timber}}`, the force-deformation relationship can be different.

### Basic Material Properties

The reference properties of structural timber determined from standard tests are:

- the bending strength {math}`R_{m, t}` in [MPa] and the

- bending modulus of elasticity {math}`E_{m, t}` in [MPa], <br> both measured on short-term standard test specimens evaluated according to ISO 8375 [3] with symmetrical 4-point bending test, span {math}`18 h(3 \cdot 6 \cdot h)` with {math}`h \approx 150 \mathrm{~mm}`, ramp load test duration {math}`300 \pm 120 \mathrm{~s}`, specimen conditioned at nominal climate, {math}`20 \pm 2^{\circ} \mathrm{C}, 65 \pm 5 \%` relative humidity.

- timber density {math}`\rho_{d e n, t}` in {math}`\left[\mathrm{kg} / \mathrm{m}^{3}\right]`, measured according to ISO 3131 [4] from a disc of full cross section, free of knots and resin pockets.

The reference material properties are sensitive to the deviations from the standard test conditions. The reference material properties of a cross section in situ (i.e. at any generic point in time and in space) are estimated as:

Bending moment capacity in situ, {math}`R_{m}` :

```{math}
:label: eq-timber-7
R_{m}=\alpha(E x(S, \omega, \tau, T)) \mathrm{R}_{m, 0}
```

Bending MOE in bending in situ, {math}`E_{m}` :

```{math}
:label: eq-timber-8
E_{m}=E_{m, 0} /(1+\delta(E x(S, \omega, \tau, T)))
```

Density in situ, {math}`\rho_{\text {den }}` :

```{math}
:label: eq-timber-9
\rho_{d e n}=\rho_{\text {den }, 0}
```

where

{math}`\operatorname{Ex}(S, \omega, \tau, T)` is the exposure of the structure to loads {math}`S`, humidity {math}`\omega` and temperature {math}`\tau`, in the time interval {math}`[0, T]`

{math}`\alpha(E x(.))`  is a strength modification function, in general defined for a particular set of exposures

{math}`\delta(E x(.))`  is a stiffness modification function, in general defined for a particular set of exposures.

{math}`R_{m, 0}, E_{m, 0}` and {math}`\rho_{\text {den, } 0}` are the bending moment capacity, the modulus of elasticity and the density of a cross section under test conditions. It is assumed that these properties are equal to the properties of the corresponding standard test specimen; i.e. it is assumed that within test specimen and within structural components these properties are constant.

Other material properties are estimated based on the reference material properties, see next section.

## Probabilistic model

### Expected values and COV

Expressions for the expected values {math}`E[.]` and the coefficient of variation {math}`\operatorname{COV}[.]` are given in {numref}`tbl-timber-1` for Nordic softwood.

```{table} Relation reference properties - other properties
:name: tbl-timber-1
| Property |  Expected Values {math}`E[X]` |  Coefficient of variation {math}`\operatorname{COV}[X]` |
| :--- | :---: | :---: |
| Tension strength par. to the <br> grain, {math}`R_{t, 0}:` | {math}`E\left[R_{t, 0}\right]=0.6 E\left[R_{m}\right]` | {math}`\operatorname{COV}\left[R_{t, 0}\right]=1.2 \operatorname{COV}\left[R_{m}\right]` |
| Tension strength perpendicular <br> to the grain, {math}`R_{t, 90}:` | {math}`E\left[R_{t, 90}\right\rfloor=0.015 E\left[\rho_{\text {den }}\right]` | {math}`\operatorname{COV}\left[R_{t, 90}\right\rfloor=2.5 \operatorname{COV}\left[\rho_{\text {den }}\right]` |
| MOE - tension par. to the <br> grain, {math}`E_{t, 0}` : | {math}` E\left\lfloor E_{t, 0}\right\rfloor=E\left[E_{m}\right]` | {math}`\operatorname{COV}\left\lfloor E_{t, 0}\right\rfloor=\operatorname{COV}\left[E_{m}\right]` |
| MOE - tension perpendicular <br> to the grain, {math}`E_{t, 90}` : | {math}`E\left[E_{t, 90}\right]=E\left[E_{m}\right] / 30` | {math}`\operatorname{COV}\left[E_{t, 90}\right]=\operatorname{COV}\left[E_{m}\right]` |
| Compression strength parallel <br> to the grain, {math}`R_{c, 0}` : | {math}`E\left[R_{c, 0}\right]=5 E\left[R_{m}\right]^{0.45}` | {math}`\operatorname{COV}\left[R_{c, 0}\right\rfloor=0.8 \operatorname{COV}\left[R_{m}\right]` |
|  Compression strength perpendicular <br> to the grain, {math}`R_{c, 90}:` |  {math}`E\left[R_{c, 90}\right]=0.008 E\left[\rho_{d e n}\right]` | {math}`\operatorname{COV}\left[R_{c, 90}\right]=\operatorname{COV}\left[\rho_{\text {den }}\right]` |
| Shear modulus, {math}`G_{v}:` | {math}`E\left[G_{v}\right]=E\left[E_{m}\right] / 16` | {math}`\operatorname{COV}\left[G_{v}\right]=\operatorname{COV}\left[E_{m}\right]` |
| Shear strength, {math}`R_{v}:` | {math}`E\left[R_{v}\right]=0.2 E\left[R_{m}\right]^{0.8}` | {math}`\operatorname{COV}\left[R_{v}\right]=\operatorname{COV}\left[R_{m}\right]` |
```

The relations are derived for standard test specimen properties tested under reference conditions. However, it is assumed that the relations can be used at any level, i.e. for components of any size and/or for other climate and load conditions.

### Distribution types

The distribution type and the recommended coefficient of variation ( {math}`\mathrm{COV}` ) of the basic material properties for European softwood are given in {numref}`tbl-timber-2` as prior values corresponding to a number of tests equal to 10 .

```{table} Probabilistic models for reference properties for structural timber
:name: tbl-timber-2
|  | Distribution | {math}`\mathrm{COV}` |
| :--- | :--- | :--- |
| Bending strength {math}`R_{m}` | Lognormal | 0.25 |
| Bending MOE: {math}`E_{m}` | Lognormal | 0.13 |
| Density {math}`\rho_{\text {den }}` | Normal | 0.1 |
```

The distribution types for the other basic material properties are given in {numref}`tbl-timber-3`.

```{table} Distribution functions for other material properties for structural timber
:name: tbl-timber-3
| Property | Distribution Function |
| :--- | :--- |
| Tension strength par. to the grain, {math}`R_{t, 0}:` | Lognormal |
| Tension strength perpendicular to the grain, {math}`R_{t, 90}:` | 2-p Weibull |
| MOE - tension par. to the grain, {math}`E_{t, 0}:` | Lognormal |
| MOE - tension perpendicular to the grain, {math}`E_{t, 90}:` | Lognormal |
| Compression strength parallel to the grain, {math}`R_{c, 0}:` | Lognormal |
| Compression strength perpendicular to the grain, {math}`R_{c, 90}:` | Normal |
| Shear modulus, {math}`G_{v}:` | Lognormal |
| Shear strength, {math}`R_{v}:` | Lognormal |
```

### Correlation coefficients

```{table} Correlation coefficient matrix
:name: tbl-timber-4
|  | {math}`E_{m}` | {math}`\rho_{\text {den }}` | {math}`R_{t, 0}` | {math}`R_{t, 90}` | {math}`E_{t, 0}` | {math}`E_{t, 90}` | {math}`R_{c, 0}` | {math}`R_{c, 90}` | {math}`G_{v}` | {math}`R_{v}` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| {math}`R_{m}` | 0.8 | 0.6 | 0.8 | 0.4 | 0.6 | 0.6 | 0.8 | 0.6 | 0.4 | 0.4 |
| {math}`E_{m}` |  | 0.6 | 0.6 | 0.4 | 0.8 | 0.4 | 0.6 | 0.4 | 0.6 | 0.4 |
| {math}`\rho_{d e n}` |  |  | 0.4 | 0.4 | 0.6 | 0.6 | 0.8 | 0.8 | 0.6 | 0.6 |
| {math}`R_{t, 0}` |  |  |  | 0.2 | 0.8 | 0.2 | 0.5 | 0.4 | 0.4 | 0.6 |
| {math}`R_{t, 90}` |  |  |  |  | 0.4 | 0.4 | 0.2 | 0.4 | 0.4 | 0.6 |
| {math}`E_{t, 0}` |  |  |  |  |  | 0.4 | 0.4 | 0.4 | 0.6 | 0.4 |
| {math}`E_{t, 90}` |  |  |  |  |  |  | 0.6 | 0.2 | 0.6 | 0.6 |
| {math}`R_{c, 0}` |  |  |  |  |  |  |  | 0.6 | 0.4 | 0.4 |
| {math}`R_{c, 90}` |  |  |  |  |  |  |  |  | 0.4 | 0.4 |
| {math}`G_{v}` |  |  |  |  |  |  | |  |  | 0.6 |
```

The relations to other material properties are given in {numref}`tbl-timber-1`. Indicative values of the correlation coefficient matrix are given in {numref}`tbl-timber-4` . The values in {numref}`tbl-timber-4` are quantified by judgment (COST E24 [2]), such that {math}`0.8 \leftrightarrow` high correlation, {math}`0.6 \leftrightarrow` medium correlation, {math}`0.4 \leftrightarrow` low correlation, {math}`0.2 \leftrightarrow` very low correlation.

### Failure types

Failure modes related to the different strength parameters are characterized as brittle, ductile or ductile with reserve strength, see {numref}`tbl-timber-5`.

```{table} Failure types for different failure modes for structural timber
:name: tbl-timber-5
| Property | Failure type |
| :--- | :--- |
| Bending, {math}`R_{m}:` | Ductile {math}`{ }^{1)}` |
| Tension parallel to the grain, {math}`R_{t, 0}:` | Brittle |
| Tension perpendicular to the grain, {math}`R_{t, 90}:` | Brittle |
| Compression parallel to the grain, {math}`R_{c, 0}:` | Ductile |
| Compression perpendicular to the grain, {math}`R_{c, 90}:` | Ductile with reserve |
| Shear, {math}`R_{v}:` | Brittle |
```
{math}`1)` for lower grade timber the failure mode can be brittle.

### Strength and Stiffness Modification Functions

Values for the strength modification function {math}`\alpha(.)` are quantified for discrete exposures {math}`\operatorname{Ex}(S, \omega, \tau, T)` as specified in {numref}`tbl-timber-6`. The particular sets of exposures are defined as in EC 5 [5]; different load duration classes and different service classes (sc) depending on the expected moisture content (mc) of the timber (sc 1, 2, 3 is associated with mc {math}`<12 \%,<20 \%` and {math}`>20 \%)`. The values for {math}`\alpha(.)` are taken from EC 5.

```{table} Strength modification function table for constant loads with different duration
:name: tbl-timber-6
| sc | Permanent <br> {math}`(T>10~\text{years} )` | Long term <br> {math}`(10>T>0.5~\text{years}` | Medium term <br> {math}`(6>T>0.25~\text{month}` | Short term <br> {math}`(T<~\text{1 week}` | Instantaneous |
| :--- | :--- | :--- | :--- | :--- | :--- |
| {math}`1 / 2` | {math}`\alpha=0.6` | {math}`\alpha=0.70` | {math}`\alpha=0.80` | {math}`\alpha=0.9` | {math}`\alpha=1.1` |
| {math}`3` | {math}`\alpha=0.5` | {math}`\alpha=0.55` | {math}`\alpha=0.65` | {math}`\alpha=0.7` | {math}`\alpha=0.9` |
```

Values for the stiffness modification function {math}`\delta(.)` are quantified for discrete exposures {math}`\operatorname{Ex}(S, \omega, \tau, T)` as specified in {numref}`tbl-timber-7`. The particular sets of exposures are defined as in EC 5 [5]. The values for {math}`\delta(.)` are taken from EC 5.

```{table} Stiffness modification function table for constant loads with different duration
:name: tbl-timber-7
| sc | Permanent <br> {math}`(T>10~\text{years} )` | Long term <br> {math}`(10>T>0.5~\text{years}` | Medium term <br> {math}`(6>T>0.25~\text{month}` | Short term <br> {math}`(T<~\text{1 week}` | Instantaneous |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | {math}`\delta=0.6` | {math}`\delta=0.5` | {math}`\delta=0.25` | {math}`\delta=0.0` | {math}`\delta=0.0` |
| 2 | {math}`\delta=0.8` | {math}`\delta=0.5` | {math}`\delta=0.25` | {math}`\delta=0.0` | {math}`\delta=0.0` |
| 3 | {math}`\delta=2.0` | {math}`\delta=1.5` | {math}`\delta=0.75` | {math}`\delta=0.3` | {math}`\delta=0.0` |
```

### Glued laminated timber

The stochastic model for glued laminated timber is related to the strength parameters for whole structural elements, and not to the strength parameters for the single laminates and the glue. In {numref}`tbl-timber-8` a prior probabilistic model for the material strength properties is given corresponding to a number of tests equal to 10. In {numref}`tbl-timber-9` failure types for different failure modes are shown.

```{table} Probabilistic models for properties for glued laminated timber
:name: tbl-timber-8
|  | Distribution | {math}`COV` |
| :--- | :--- | :--- | 
| Bending strength: {math}`R_{m}` | Lognormal | 0.15 |
| Bending MOE: {math}`E_{m}` | Lognormal | 0.13 |
| Tension strength par. to the grain: {math}`R_{t, 0}` | Lognormal |  |
| Tension strength perpendicular to the grain: {math}`R_{t, 90}` | 2-p Weibull |  |
| MOE - tension par. to the grain: {math}`E_{t, 0}` | Lognormal |  |
| MOE - tension perpendicular to the grain: {math}`E_{t, 90}` | Lognormal |  |
| Compression strength parallel to the grain: {math}`R_{c, 0}` | Lognormal |  |
| Compression strength perpendicular to the grain: {math}`R_{c, 90}` | Normal |  |
| Shear modulus: {math}`G_{v}` | Lognormal |  |
| Shear strength: {math}`R_{v}` | Lognormal |  |
| Density: {math}`\rho_{d e n}` | Normal | 0.1 |
```

```{table} Probabilistic models for properties for glued laminated timber
:name: tbl-timber-9
| Property | Failure type |
| :--- | :--- |
| Bending: {math}`R_{m}` | Brittle |
| Tension parallel to the grain: {math}`R_{t, 0}` | Brittle |
| Tension perpendicular to the grain: {math}`R_{t, 90}` | Brittle |
| Compression parallel to the grain: {math}`R_{c, 0}` | Ductile |
| Compression perpendicular to the grain: {math}`R_{c, 90}` | Ductile with reserve |
| Shear: {math}`R_{v}` | Brittle |
```

### Model Uncertainties for Different Ultimate Limit States

The model uncertainties cover deviations and simplifications related to the probabilistic modelling and the limit state equations. The reference properties are determined by standardized tests. Therefore, model uncertainties related to estimation of other material parameters (e.g. tension and compression strengths) have to be accounted for. Geometrical deviations from specified dimensions, durations of load and moisture effects (damage accumulation) also contribute to model uncertainties if not explicitly accounted for in the probabilistic modelling. Furthermore, the idealized and simplified limit state equations introduce model uncertainties. In {numref}`tbl-timber-10` values for model uncertainties are shown. The model uncertainty depends on the limit state (bending or e.g. combined stress effects) and how much the actual condition deviates from the standard test conditions.

```{table} Model uncertainties for component load bearing capacity
:name: tbl-timber-10
|  | Mean | Standard deviation | Distribution |
| :--- | :--- | :--- | :--- |
| Without load duration effects | 1 | 0.05 - 0.10 | Lognormal |
| With load duration effects, eq. {eq}`eq-timber-16`-{eq}`eq-timber-17` | 1 | 0.10 | Lognormal |
```

## Refinements of the probabilistic model

### Modeling the Spatial Variation of Timber Properties

**Bending moment capacity**

Following a model proposed by Isaksson [6], the bending strength {math}`R_{m, i j}` at a particular point {math}`j` in the component {math}`i` of a structure/batch is given as:

```{math}
:label: eq-timber-10
R_{m, i j}=\exp \left(v+\varpi_{i}+\chi_{i j}\right)
```

where

{math}`v` is the unknown logarithm of the mean strength of all sections in all components, see {numref}`fig-timber-4`

{math}`\varpi_{i}` is the difference between the logarithm of the mean strength of the sections within a component {math}`i` and {math}`v ; \varpi_{i}` is normal distributed with mean value equal to zero and standard deviation {math}`\sigma_{\sigma}`

{math}`\chi_{i j}` is the difference between the strength weak section {math}`j` in the beam {math}`i` and the value {math}`v+\varpi_{i} ; \chi_{i j}` is normal distributed with mean value equal to zero and standard deviation {math}`\sigma_{\chi}`. {math}`\varpi_{i}` and {math}`\chi_{i j}` are statistically independent.

The bending strength {math}`R_{m, i j}` is the bending strength of a particular cross section. {math}`R_{m, i j}` is lognormal distributed.

```{figure} ../part-03/images/fig-timber-4.jpg
:name: fig-timber-4

Section model for the longitudinal variation of bending strength
```

It is assumed that the bending strength of a cross section is related with the bending strength of a test specimen {math}`R_{m, t}` as:

```{math}
:label: eq-timber-11
R_{m, 0}=R_{m, t}^{\vartheta}
```

where {math}`\vartheta` is a constant depending on the applied bending test standard and the type of timber.

The bending moment capacity {math}`R_{m, 0}` is assumed to be constant within one section. The discrete section transition is assumed to be Poisson distributed, thus the section length {math}`X` follows an exponential distribution with mean value {math}`1 / \lambda`. A realization of {math}`X, x_{j}` is illustrated in {numref}`fig-timber-4`.

For Nordic spruce the following information basis can be given (Isaksson [6]): The variation of the logarithm of the bending capacity {math}`\ln \left(R_{m, 0}\right)` is related by {math}`40 \%` to the variable {math}`\varpi` and by {math}`60 \%` to the variable {math}`\chi`. The expected length of a section is {math}`1 / \lambda=480 \mathrm{~mm}`.

```{table} ϑ -values for the estimation of the strength of weak sections (for Nordic Spruce)
:name: tbl-timber-11
|  | EN | US | AUS |
| :--- | :--- | :--- | :--- |
| {math}`\vartheta=` | 1.05 | 1.03 | 1.02 |
```
Note: {math}`\vartheta`-values should be used in connection with strength values in [MPa].

The different values for {math}`\vartheta` given in {numref}`tbl-timber-11` are due to the different definitions of bending strength of test specimen. The values are derived by simulations, see Köhler [7].

For the bending modulus of elasticity and the density no within component variation is assumed.

### Duration of Load Effect

The mechanism leading to strength reduction of a timber member under sustained load is referred to as creep rupture and is modelled by so-called cumulative damage models with the general form:

```{math}
:label: eq-timber-12
\frac{d \alpha_{D}}{d t}=h\left(S(t), R_{0}, \alpha_{D}, \boldsymbol{\theta}\right) \quad \text { for } \quad 0 \leq \alpha_{D} \leq 1
```

where {math}`t` is time, {math}`\alpha_{D}` is the damage state variable which commonly ranges from 0 (no damage) to 1 (failure), the function {math}`h(.)` contains parameters {math}`\boldsymbol{\theta}` that must be determined from experiment observations, {math}`S(t)` is the applied stress and {math}`R_{0}` the failure stress under short term ramp loading.

Three different models are proposed:

1) The model referred to as the Gerhards model [8]:

```{math}
:label: eq-timber-13
\frac{d \alpha_{D}}{d t}=\exp \left(-a_{D}+b_{D} \frac{S(t)}{R_{0}}\right) \quad \text{for} \quad 0 \leq \alpha_{D} \leq 1
```

2) The model referred to as the Foschi and Yao model [9]:

```{math}
:label: eq-timber-14
\begin{aligned}
\frac{d \alpha_{D}}{d t} & =a_{D}\left(\frac{S(t)}{R_{0}}-\eta_{D}\right)^{b_{D}}+c_{D}\left(\frac{S(t)}{R_{0}}-\eta_{D}\right)^{d_{D}} \alpha_{D}(\mathrm{t}) & & \text { for } \frac{S(t)}{R_{0}} \geq \eta_{D} \\ \\
\frac{d \alpha_{D}}{d t} & =0 & & \text { for } \frac{S(t)}{R_{0}}<\eta_{D}
\end{aligned}
```

3) The model referred to as the Nielsen model [10]:

```{math}
:label: eq-timber-15
\frac{d \alpha_{\kappa}}{d t}=\alpha_{\kappa}\left(\frac{S(t)}{R_{0}}\right)^{2}\left(\left(\alpha_{\kappa}\left(\frac{S(t)}{R_{0}}\right)^{2}\right)^{-1}-1\right)^{-\frac{1}{\mathrm{~b}_{\mathrm{D}}}} \text { for } 0 \leq \alpha_{\kappa} \leq\left(\frac{S(t)}{R_{0}}\right)^{-2}
```

where {math}`\alpha_{D}, \alpha_{\kappa}` are the damage state variables, {math}`a_{D}, b_{D}, c_{D}, d_{D}, \eta_{D}` are model parameters fitted to experimental results e.g. as in Sørensen et al. [11] and Köhler and Svensson [12].

For model 1) and 2) a time invariant limit state function can be formulated:

```{math}
:label: eq-timber-16
g(T)=1-X_{M} \alpha_{D}(S(T))
```

where {math}`X_{M}` is the model uncertainty, see {numref}`tbl-timber-10`. {math}`\alpha_{D}(S(T))` at time {math}`T` is obtained using the damage accumulation models 1 ) or 2) with the load time history {math}`S(t), 0 \leq t \leq T`.

For model 3) a time variant limit state function has to be used:

```{math}
:label: eq-timber-17
g(T)=\min _{0 \leq t \leq T}\left\lbrace \left(S(t) / R_{0}\right)^{-2}-X_{M} \alpha_{\kappa}\left(S(t) / R_{0}\right)\right\rbrace
```

where {math}`X_{M}` is the model uncertainty, see {numref}`tbl-timber-10` .

### Updating Scheme for the Basic Properties

When information has been collected about the basic material properties the new knowledge implicit in that information might be applied to improve any previous (prior) estimate of the material property. Dependent on the type of information, it can be differentiated between direct and indirect information. Direct information can e.g. be in the form of test results of a material property. Indirect information can be in the form of measurements of some indicator of the property, e.g. information from grading indications. In the following updating is illustrated with three different methods based on Bayesian updating as described in JCSS Probabilistic Model Code, [section 23.](section-part-3-general-principles-annex-A).

### Updating - Direct Information

The bending strength {math}`R_{m}` and the bending modulus of elasticity {math}`E_{m}` are modelled by lognormal distributed random variables which can be represented through the normal distributed random variables {math}`R_{m}^{*}=\ln \left(R_{m}\right)` and {math}`E_{m}^{*}=\ln \left(E_{m}\right)`. All basic properties may be represented with the uncertain mean value {math}`M` and standard deviation {math}`\Sigma` as illustrated by:

```{math}
:label: eq-timber-18
R_{m}=\exp \left(R_{m}^{*}\right) \rightarrow R_{m}^{*}: N\left(M_{R}, \Sigma_{R}\right) 
```

```{math}
:label: eq-timber-19
E_{m}=\exp \left(E_{m}^{*}\right) \rightarrow E_{m}^{*}: N\left(M_{E}, \Sigma_{E}\right) 
```

```{math}
:label: eq-timber-20
\rho_{d e n}: N\left(M_{\rho}, \Sigma_{\rho}\right)
```

The parameters {math}`M` and {math}`\Sigma` of {math}`R_{m}^{*}, E_{m}^{*}` and {math}`\rho_{\text {den }}` are quantified with a Normal-Inverse-Gamma-2 distribution with the parameters {math}`m, s, n, v` which is equivalent to the natural conjugate prior of a normal distribution with unknown mean and standard deviation. Given the parameters {math}`m, s, n, v` the predictive distribution of {math}`R_{m}^{*}, E_{m}^{*}` and {math}`\rho_{d e n}` can be derived as:

```{math}
:label: eq-timber-21
F_{X \mid \hat{\mathbf{x}}}(x \mid m, n, s, v)=T_{v}\left(\frac{x-m}{s} \sqrt{\frac{n}{n+1}}\right)
```

where {math}`T_{v}(.)` is the student-t-distribution with {math}`v` degrees of freedom.

The prior predictive distribution can be quantified with parameters {math}`(m, s, n, v)=\left(m^{\prime}, s^{\prime}, n^{\prime}, v^{\prime}\right)`

New measurements on the material properties can be used for updating the parameters given above. For a sample of {math}`n` observations {math}`\left(\hat{x}_{1}, \hat{x}_{2}, \ldots, \hat{x}_{n}\right)`, the posterior predictive distribution function of {math}`X` is obtained using the JCSS Probabilistic Model Code, [section 23.](../part-03/general-principles.md).

### Updating - Indirect Information I - machine grading

In this section a simple model for updating the statistical parameters of the Lognormal distribution for e.g. the bending strength of a given timber grade when new information becomes available in the form of machine grading results is described.

The Lognormal distributed strength parameter {math}`R` is assumed to have a coefficient of variation {math}`C O V_{R}`. Then {math}`X=\ln R` is Normal distributed with expected value {math}`M_{X}` and standard deviation {math}`\sigma_{X}^{2}=\ln \left(C O V_{R}^{2}+1\right) . \sigma_{X}` is assumed to be known and {math}`M_{X}` is assumed to be Normal distributed with expected value {math}`\mu_{0}` and standard deviation {math}`\sigma_{0}`.

When machine grading is based on a measured indicator {math}`i`, typically related to the stiffness of a timber test specimen, the following relation between the indicator {math}`i` and the strength parameter can initially be fitted to tests results where both the indicator value and the strength {math}`R` are measured:

```{math}
:label: eq-timber-22
i=b_{0} \cdot R^{b_{1}} \cdot \varepsilon
```

where {math}`b_{0}` and {math}`b_{1}` are constants and {math}`\varepsilon` is an error term which is assumed Lognormal distributed. {math}`\ln (\varepsilon)` is then Normal distributed and is assumed to have zero mean value and standard deviation {math}`\sigma_{\ln (\varepsilon)}`. The parameters {math}`b_{0}, b_{1}` and {math}`\sigma_{\ln (\varepsilon)}` can be estimated from the tests using the Maximum Likelihood method.

Next, it is assumed that {math}`n` new observations {math}`\hat{i}_{1}, \hat{i}_{2}, \ldots, \hat{i}_{n}` of the indicator is obtained from {math}`n` specimens from a given timber grade. The mean value of these can be estimated as {math}`\ln \bar{i}=1 / n \sum_{i=1}^{n} \ln \hat{i}_{i}` and the updated (predictive) distribution function for {math}`X=\ln R` is then Normal with expected value {math}`\mu^{\prime \prime}` and standard deviation {math}`\sigma^{\prime \prime \prime}` :

```{math}
:label: eq-timber-23
\mu^{\prime \prime}=\frac{\frac{n}{\ln b_{1}}\left(\ln \bar{i}-b_{0}\right) \sigma_{0}^{2}+\mu_{0} \sigma_{X}^{2}}{n \sigma_{0}^{2}+\sigma_{X}^{2}}$ and $\sigma^{\prime \prime \prime}=\sqrt{\sigma_{X}^{2}+\frac{\sigma_{0}^{2} \sigma_{X}^{2}}{n \sigma_{0}^{2}+\sigma_{X}^{2}}+\left(\frac{\left(n / \ln b_{1}\right) \sigma_{0}^{2}}{n \sigma_{0}^{2}+\sigma_{X}^{2}}\right)^{2} \sigma_{\ln (\varepsilon)}^{2}}
```

The updated predictive distribution for the strength {math}`R` is then Lognormal with expected value {math}`\mu_{R}^{\prime \prime}=\exp \left(\mu^{\prime \prime}+0.5 \sigma^{\prime \prime \prime 2}\right)` and standard deviation {math}`\sigma_{R}^{\prime \prime \prime}=\mu_{R}^{\prime \prime} \sqrt{\exp \left(\sigma^{\prime \prime 2}\right)-1}`.

### Updating - Indirect Information II - calibration of grading rules

The probabilistic model for bending strength described in this section can be used for machine graded timber and is based on the model described in Faber et al. [14]. The probabilistic model can be described by the following steps:

For a given geographic region and a given type of specie (e.g. Nordic Spruce) an initial (prior) distribution function {math}`F_{R_{m}}(x)` can be established for the bending strength {math}`R_{m}` for non-graded timber. The recommended distribution function is Lognormal. The statistical parameters in the distribution function can be obtained using e.g. the Maximum Likelihood method. For the identification of lower grades it is recommended to fit the initial (prior) distribution function {math}`F_{R_{m}}(x)` to the data in the lower end (e.g. {math}`30 \%` of the data with lowest strengths); in order to obtain good models in the lower tail of the distribution function for the graded timber strength. This can be done using the Maximum Likelihood method, see e.g. in Faber et al. [14].

Machine grading is based on a measured indicator {math}`i`, typically related to the stiffness of a timber test specimen. For each grading technique the following linear relation with the bending strength is assumed:

```{math}
:label: eq-timber-24
i(r)=a_{0}+a_{1} r+\varepsilon
```

where {math}`a_{0}` and {math}`a_{1}` are constants and {math}`\varepsilon` is the lack-of-fit quantity which is assumed Normal distributed with zero mean value and standard deviation {math}`\sigma_{\varepsilon}`. The parameters {math}`a_{0}, a_{1}` and {math}`\sigma_{\varepsilon}` can be estimated using the Maximum Likelihood method which also gives the statistical uncertainty in form of standard deviations and correlation coefficients of the parameters {math}`a_{0}, a_{1}` and {math}`\sigma_{\varepsilon}`. It is noted that in {eq}`eq-timber-22` the logarithms are fitted with a Lognormal distributed lack-of-fit error, whereas in {eq}`eq-timber-24` a linear model with a Normal distributed lack-of-fir error is used.

After grading the updated (predictive) distribution function for the bending strength in grade no. {math}`j` is obtained from:

```{math}
:label: eq-timber-25
F_{R_{m, j}}^{U}(x)=P\left(R_{m} \leq x \mid b_{L, j} \leq i(x) \leq b_{U, j}\right)
```

where {math}`b_{L, j}` and {math}`b_{U, j}` are lower and upper limits of the grading indicator {math}`i` for grading no. {math}`j`. The updated distribution function {math}`F_{R_{m, j}}^{U}(x)` can then be used in reliability analyses. A detailed description of the method can be found in Faber et al. [14] and Köhler [15].

## Remarks

The presented document does not cover all aspects of the design of timber structures. For timber structures, the structural performance depends to a considerable part on the connections between different timber structural members; connections can govern the overall strength, serviceability and fire resistance. Beside solid timber other timber materials are utilized in timber engineering.

**References**

[1] Glos P. (1981). Zur Modellierung des Festigkeitsverhaltens von Bauholz bei Druck-, Zug- und Biegebeanspruchung. Berichte zur Zuverlässigkeitstheorie der Bauwerke, SFB 96, Munich, Germany.

[2] COST Action E 24, Reliability of timber structures. Several meetings and Publications, Internet Publication: http://www.km.fgg.uni-lj.si/coste24/coste24.htm, 2005.

[3] ISO 8375: Solid timber in structural sizes - determination of some physical and mechanical properties. International Organisation for Standardisation, 1985.

[4] ISO 3131: Wood - Determination of density for physical and mechanical tests. International Organisation for Standardisation, 1975.

[5] EN 1995-1-1, Eurocode 5: Design of timber structures; part 1-1: general rules and rules for buildings. Comité Européen de Normalisation, Brussels, Belgium, 2004.

[6] Isaksson T. Modelling the Variability of Bending Strength in Structural Timber. PhDthesis, Lund Institute of Technology, Report TVBK-1015, 1999.

[7] Köhler, J. Reliability of Timber Structures. PhD-thesis, Swiss Federal Institute of Technology, submitted for approval, 2005.

[8] Gerhards, C. C. Time-related effects of loads of wood strength. A linear cumulative damage theory. Wood Science. 19(2), pp. 139-144, 1979.

[9] Foschi R. O. and Yao Z. C. Another look at three duration of load models. Proceedings of the 19th Meeting, International Council for Research and Innovation in Building and Construction, Working Commission W18 - Timber Structures, CIB-W18, Florence, Italy, 1986.

[10] Nielsen L.F. Lifetime and Residual Strength of wood subjected to static and variable load - Part I +II. Holz als Roh- und Werkstoff. Vol. 58, pp. 81-90 and 141-152, 2000.

[11] Sørensen J.D., Svensson S. \& Stang B.D. Reliability-based calibration of load duration factors for timber structures. Structural Safety, Vol. 27, 2005, pp. 153-169, 2005.

[12] Köhler J., Svensson S. Probabilistic Modeling of Duration of Load Effects in Timber Structures. Proceedings of the 35th Meeting, International Council for Research and In-
novation in Building and Construction, Working Commission W18 - Timber Structures, CIB-W18, Paper No. 35-17-1, Kyoto, Japan, 2002.

[13] Raiffa H. and Schlaifer R. Applied statistical decision theory. John Wiley \& Sons Ltd. Chichester, UK, 1960.

[14] Faber M. H., Köhler J. and Sørensen, J. D. Probabilistic modelling of graded timber material properties. Journal of Structural Safety, 26(3), pp. 295-309, 2004.

[15] Köhler J., Faber M. H. A probabilistic approach to cost optimal timber grading. Proceedings of the 36th Meeting, International Council for Research and Innovation in Building and Construction, Working Commission W18 - Timber Structures, CIB-W18, Paper No. 36-5-2, Colorado, USA, 2003.

