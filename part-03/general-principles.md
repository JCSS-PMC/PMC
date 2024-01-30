# General Principles

**List of symbols:**

{math}`\mathrm{f}_{\mathrm{x}}(\mathrm{x} \mid \mathrm{q})=` the variability of property {math}`\mathrm{x}` within a given lot

{math}`\mathrm{f}_{\mathrm{q}}(\mathrm{q})=` the variability of the parameters {math}`\mathrm{q}` from lot to lot; statistical description of the production

{math}`\mathrm{f}^{\prime}(\mathrm{q})=` prior distribution of {math}`\mathrm{q}`

{math}`\mathrm{f}^{\prime \prime}(\mathrm{q})=` posterior distribution of {math}`\mathrm{q}`

{math}`\mathrm{L}(` data {math}`\mid` {math}`\mathrm{q})=` likelihood function

{math}`\mathrm{q}=` vector of distribution parameters (e.g. mean and std. dev.)

{math}`\mathrm{C}=` normalising constant

{math}`\mathrm{d}=` decision rule

## Introduction

The description of each material property consists of a mathematical model (e.g. elastic-plastic model, creep model, etc.) and random variables or random fields (e.g. modulus of elasticity, creep coefficient). Functional relationships between the various variables may be part of the material model (e.g. the relation between tensile stress and compressive stress for concrete).  

In general, it is the response to static and time dependent mechanical loading that matters for structural design. However, also the response to physical, chemical and biological actions is important as it may affect the mechanical properties and behaviour.

It is understood that modelling is an art of reasonable simplification of reality such that the outcome is sufficiently explanatory and predictive in an engineering sense. An important aspect of an engineering model is also its operationability, i.e. the ease in handling it in applications.

Models and values should follow from (standardised) tests, representing the actual
environmental and loading conditions as good as possible. The set of tested specimen should be representative for the production of the relevant fabrication sites, cover a sufficient long period of time
and may include the effect of standard quality control measures. Allowance should be made for possible differences between test circumstances and structural environment (conversion).

For the classical building materials, knowledge about the various properties is generally available from
experience and from tests in the past. For new materials, models and values should be obtained from an
extensive and well defined testing program.

## Material properties

Material properties are defined as the properties of material specimens of defined size and conditioning, sampled according to given rules, subjected to an agreed testing procedure, the results of which are evaluated according to specified procedures.

The main characteristics of the mechanical behaviour is described by the one dimensional {math}`\sigma-\varepsilon-` diagram, as presented in {numref}`fig-stress-strain-diagram`. As an absolute minimum for structural design the

- modulus of elasticity
- the strength of the material

both for tensile and compression should be known. Other important parameters in the one-dimensional {math}`\sigma-\varepsilon-` diagram are:

- yield stress (if present)
- limit of proportionality
- strain at rupture and strain at maximum stress

The strain at rupture is a local phenomenon and the value obtained may heavily depend on the shape and dimensions of the test specimen.

```{figure} ../part-03/images/fig-stress-strain-diagram.jpg
:name: fig-stress-strain-diagram

Stress strain relationship 
```

Additional to the one dimensional {math}`\sigma-\varepsilon-` diagram, information about a number of other quantities and effects is of importance, such as:

- Multi-axial stress condition
- Duration and strain rate effects
- Temperature effects
- Humidity effects
- Effects of notches and flaws
- Effects of chemical influences

In general, the various properties of one material may be correlated.

In the present version of this JCSS model code not all properties will be considered.

## Uncertainties in material modelling

Material properties vary randomly in space: The strength in one point of a structure will not be the same as the strength in another point of the same structure or another one. This item will be further developed in the sections [3.04](../part-03/model-uncertainties.md) and [3.05](../part-03/dimensions.md). 

Additional to spatial variations of materials, the following uncertainties between measured properties of specimen and properties of the real structure should be accounted for.

1. Systematic deviations identified in laboratory testing by relating the observed structural property to the predicted property, suggesting some bias in prediction.

2. Random deviations between the observed and predicted structural property, generally suggesting some lack of completeness in the variables considered in the model.

3. Uncertainties in the relation between the material incorporated in the structural sample and the corresponding material samples. 

4. Different qualities of workmanship affecting the properties of (fictitious) material samples, i.e. when modelling the material supply as a supply of material samples.

5. The effect of different qualities of workmanship when incorporating the material in actual structures, not reflected in corresponding material samples.

6. Uncertainties related to alterations in time, predictable only by laboratory testing, field observations, etc.

## Scales of modelling variations

Material properties vary locally in space and, possibly, in time. As far as the spacial variations are concerned, it is useful to distinguish between three hierarchical levels of variation: global (macro), local (meso) and micro (see {numref}`tbl-general-principles-3.0.1`).

For example, the variability of the mean and standard deviation of concrete cylinder strength per job or construction unit as shown in {numref}`fig-general-principles-3.0.2` is a typical form of global parameter variation. This variation primarily is the result of production technology and production strategy of the concrete producers. Parameter variations between objects are conveniently denoted as macroscale variations. The unit of that scale is in the order of a structure or a construction unit. Parameter variations may also be due to statistical uncertainties.

Given a certain parameter realisation in a system the next step is to model the local variations within the system in terms of random processes or fields. Characteristically, spatial correlations (dependencies) become negligible at distances comparable to the size of the system. This is a direct consequence of the hierarchical modelling procedure where it is natural to assume that the variation within the system is conditional on the variations between systems and the first type of variation is conditionally independent of the second. At this level one may speak of meso-scale variations. Examples are the spatial variation of soils within a given (not too large) foundation site or the number, size and spatial distribution of flaws along welding lines given a welding factory (or welding operator). The unit of this scale is in the order of the size of the structural elements and probably most conveniently measured in meters.

At the third level, the micro-level, one focuses on rapidly fluctuating variations and inhomogenities which basically are uncontrollable as they originate from physical facts such as the random distribution of spacing and size of aggregates, pores or particles in concrete, metals or other materials. The scale of these variations is measured in particle sizes, i.e. in centimeters down to the size of crystals.

The modelling process normally uses physical arguments as far as possible. Quite generally, the object is taken as an arrangement of a large number of small elements. The statistical properties of these elements usually can only be assessed qualitatively as well as their type of interaction. This, however, is sufficient to perform some basic operations such as extreme value, summation or intersection operations which describe the overall performance. The large number of elements greatly facilitates such operations because one can make use of certain limit theorems in probability theory. The advantage of using asymptotic concepts rests on the fact that the description of the element properties can then be reduced to some few essential characteristics. The central limit theorem of probability theory, asymptotic extreme value concepts, convergence theorems to the Poisson distribution, etc. will play an important role. In particular, size effects have to be taken into account at this level. 

A useful concept is to introduce a reference volume of the material which in general is chosen on rather practical grounds. It most frequently corresponds to some specified test specimen volume at which material testing is carried out. This volume generally neither corresponds to the volume of the virtual strength elements introduced at the micro-scale modelling level nor to a characteristic volume for in situ strength. It eds to be related to the latter one and these operations can involve not only simple size scaling but more complicated functional relationships if the material produced is subject to further uncertain factors once put in place. Concrete is the most obvious example for the necessity of such additional consideration. Of course, scale effects may also be present at the meso-scale level of modelling.

The reason for this concept of modelling at several levels (steps) is the requirement for operationability not only in the probabilistic manipulations but also in sampling, estimation and quality control. This way of modelling and the considerations below are, of course, only valid under certain technical standards for production and its control. At the macro-scale level it is assumed that the production process is under control. This simply means that the outcome of production is stationary in some sense. Should a trend develop, production control corrects for it immediately or with some sufficiently small delay. Therefore, it is assumed that at least for some time interval (or spatial region) whose length (size) is to be selected carefully, approximate stationarity on the meso- and micro-scale is guaranteed. Quite frequently, the operational, mathematical models available so far even require ergodicity. Variations at the macro scale level, therefore, can be described by stationary sequences. If the sequences are or can be assumed independent, it is possible to handle macro-scale variations by the concept of random variables. Stationarity is also assumed at the lower levels. However, it may be necessary to use the theory of random processes (fields) at the lower levels, especially in order to take into account of significant effects of dependencies in time or space.

## Hierarchical modelling

Consider a random material property {math}`\mathrm{X}` which is described by a probability density function {math}`f_{\mathrm{x}}(\mathrm{x} \mid \mathbf{q})`, where {math}`\mathbf{q}=\left(\mathrm{q_{1}}, \mathrm{q_{2}}, \ldots\right)` is the statistical parameter vector, e.g. {math}`\mathrm{q_{1}}` is the mean and {math}`\mathrm{q_{2}}` the standard deviation. The density function {math}`\mathrm{f}_{\mathrm{x}}(\mathrm{x} \mid \mathbf{q})` applies to the property of a *finite reference volume*, identical with or clearly related to the volume of the test specimen within a given unit of material. Guidance on the type of distribution may be obtained by assessing the performance of the reference volume under testing conditions in terms of some *micro system* behaviour. The performance of test specimens, regarded as a system of micro elements, can usually be interpreted by one of the following strength models

- Weakest link model
- Full plasticity model
- Daniel’s bundle of threads model

When applying these models to systems with increasing number of elements, they generally lead to specific distributions for the properties of the system at the meso-scale level. The weakest link model leads to a Weibull distribution, the other two models to a normal distribution. For larger coefficients of variation the normal distribution must be replaced by a lognormal distribution in order to avoid physically impossible, negative strength values.

In the next step (see {numref}`tbl-general-principles-3.0.1`) a *unit* (a structural member) is considered as *meso-scale* (local variations). The respective unit is regarded as being constituted from a sequence of finite volumes. Hence, a property in this unit is modelled by a random sequence {math}`\mathrm{X}_{1}, \mathrm{X}_{2}, \mathrm{X}_{3} \ldots` of reference volume properties. The {math}`\mathrm{X_{i}}` may have to be considered as correlated, with a coefficient of correlation depending on the distance {math}`\Delta \mathrm{r}_{\mathrm{ij}}` and a correlation parameters {math}`\rho_{\mathrm{o}}` and {math}`\mathrm{d}_{\mathrm{c}}`, for example:

```{math}
:label: eq-general-principles-3.0.1
\rho\left(\Delta \mathrm{r_{i j}}\right)=\rho_{o}+\left(1-\rho_{o}\right) \exp \left[-\left(\Delta \mathrm{r_{i j}} / \mathrm{d_{c}}\right)^{2}\right]
```

In general {math}`\rho_{0}=0`.

In the subsequent step the complete structure or some relevant part of it is considered as a lot. A lot is defined as a set of units, produced by one producer, in a relatively short period, with no obvious changes in production circumstances and intended for one building site. In practice lots correspond to e.g.:

- the production of ready-mix concrete for a set of elements
- structural steel from one melt processed according to the same conditions
- foundation piles for a specific site

As a lot is a set of units it can also be conceived as a set of reference volumes {math}`\mathrm{X}_{\mathrm{i}}`. Normally the parameters {math}`\mathrm{q}` defined before are defined on the lot level. The correlation between the {math}`\mathrm{X}_{\mathrm{i}}` values within different members normally can be modelled by a single parameter

```{math}
:label: eq-general-principles-3.0.2
\rho_{\mathrm{ij}}=\rho_{0}
```

Finally, at the highest *macro scale* level, we have a sequence of lots, represented by a random sequence of lot parameters (in space or in time). Here we are concerned with the estimation of the distribution of lot parameters, either from one source or several sources. The individual lots may be interpreted as random samples taken from the enlarged population or *gross supply*. The gross supply comprises all materials produced (and controlled) according to given specifications, within a country or groups of countries. The *macro-scale* model may be used if the number of producers and structures is large or differences between producers can be considered as approximately random.

```{table} Scales of fluctuation
:name: tbl-general-principles-3.0.1
| Scale | Population | Reference name | Description |
| :--- | :--- | :--- | :--- |
| macro (global) | set of structures | gross supply | {math}`\mathbf{X}` |
| meso | set of elements | lot | {math}`\mathbf{X} \mid \mathbf{q}` and {math}`\boldsymbol{\rho}_{\mathbf{o}}` |
| meso (local) | one element | unit | {math}`\mathbf{X} \mid \mathbf{q}` and {math}`\boldsymbol{\rho}(\Delta \mathbf{r})` |
| micro | aggregate level | reference volume | type of distribution |
```

```{figure} ../part-03/images/fig-general-principles-3.0.2.jpg
:name: fig-general-principles-3.0.2

Figure a) production description {math}`\mathrm{f}_{\mathrm{q}}(\mathrm{q})`

Figure b) lot description {math}`\mathrm{f}_{\mathrm{x}}(\mathrm{x} \mid \mathrm{q})` 

Figure c) total supply {math}`\mathrm{f_{x}(x)}` 

Description of production parameters, lots and total supply 
```

The gross supply is described by {math}`\mathrm{f}(\mathrm{q})`. Type and parameters should follow from a statistical survey of the fluctuations of the various lots which belong to the production under consideration. It will be assumed here that {math}`\mathrm{f}(\mathrm{q})` is known without statistical uncertainty. If statistical uncertainties cannot be neglected, they can be incorporated. The distribution {math}`\mathrm{f}(\mathrm{q})` should be monitored more or less continuously to find possible changes in production characteristics.

The probability density function (predictive density function) for an arbitrary unit (arbitrary means that the lot is not explicitly identified) can be found from the total probability theorem:

```{math}
:label: eq-general-principles-3.0.3
\mathrm{f_{x}(x)}=\int \mathrm{f_{x}}(\mathrm{x \mid q})~\mathrm{f_{q}(q)~d q}
```

The density function {math}`\mathrm{f}(\mathrm{x})` may be conceived as the statistical description of {math}`\mathrm{x}` within a large number of randomly selected lots. For some purposes one could also identify {math}`\mathrm{f}(\mathrm{x})` directly.

## Definition of characteristic value

The characteristic value of a material with respect to a given property {math}`\mathrm{X}` is defined as the {math}`\mathrm{p}_{\mathrm{x}}` - quantile in the predictive distribution, i.e.

```{math}
:label: eq-general-principles-3.0.4
\mathrm{x}_{\mathrm{c}}=\mathrm{F}_{\mathrm{x}}^{-1}(\mathrm{p})
```

Examples for predictive distributions can be found in [Annex A](section-part-3-general-principles-annex-A). Others may be found in [1](section-part-3-general-principles-references), [2](section-part-3-general-principles-references) and [3](section-part-3-general-principles-references).

## Quality control strategies

### *Types of strategies*

Normally the statistical parameters of the material properties are based on general tests, taking into account standard production methods. For economic reasons it might be advantageous to have more specific forms of quality control for a particular work or a particular factory.

Quality control may be of a total (all units are tested) or a statistical nature (a sample is tested). Quality control will lead to more economical solutions, but has in general the disadvantage that the result is not available at the time of design. In those cases, the design value has to be based on the combination of the unfiltered production characteristics and the expected effect of the quality control selection rules.

Various quality control procedures can be activated, each one leading to a different design value. In {numref}`fig-general-principles-3.0.3` an overview is presented. The easiest procedure is to perform no additional activities (option "no tests"). This means that the units, lots, production should be defined, their descriptions {math}`\mathrm{f}(\mathrm{x} \mid \mathrm{q})` and {math}`\mathrm{f}(\mathrm{q})` should be established and only {math}`\mathrm{f}(\mathrm{q})` should be checked for long term changes in production characteristics.

If on the other hand tests are performed one may distinguish between a total (unit by unit) control and sampling on the one hand and between selection and updating on the other hand. The various options will be discussed.

```{figure} ../part-03/images/fig-general-principles-3.0.3.jpg
:name: fig-general-principles-3.0.3

Strategies for Quality Control
```

### *Total testing versus Sampling*

Both for updating and for selection one may test all units which go into a structure (total testing) or one may test a (random) sample only (statistical testing).

If the control is total, every produced unit is inspected. The acceptance rules imply that a unit is judged as good (accepted) or bad (not accepted). This type of control is also referred to as unit by unit control. Typically, testing all units requires a non-destructive testing technique. Therefore some kind of measurement error has to be included resulting in a smooth truncation of the distribution.

If the control is statistical only a limited member of units is tested. The procedure generally consists of the following parts:

- batching the products;
- sampling within each lot;
- testing the samples;
- statistical judgement of the results;
- decision regarding acceptance.

One normally takes a random sample. In a random sample each unit of the lot has the same probability of being sampled. Where knowledge on the inherent structure of the lot is available, this could be utilised, rendering more efficient sampling techniques, e.g.:

- sampling at weak points, when trends are known;
- sampling at specified intervals;
- stratified sampling; 

The larger efficiency results in smaller sample sizes for obtaining the same filtering capability of a test. No further guidance, however, will be given here.

### *Updating versus selecting*

Testing can be done with two purposes:

1) to update the probability density function {math}`\mathrm{f}(\mathrm{x})` or {math}`\mathrm{f}(\mathrm{q})` of some particular lot or item (updating);

2) to identify and reject inadequate lots or units on the basis of predefined sampling procedures and selection rules (selection).

The basic formula for the first option is given by:

```{math}
:label: eq-general-principles-3.0.5
\mathrm{f}^{\prime \prime}(\mathrm{q})=\mathrm{C}~\mathrm{L}(\text{data} \left.\mid \mathrm{q})\right) \mathrm{f}^{\prime}(\mathrm{q})
```

where:

{math}`\mathrm{f}^{\prime \prime}(\mathrm{q})  =` posterior distribution of q

{math}`\mathrm{f}^{\prime}(\mathrm{q})  =` prior distribution of q

{math}`\mathrm{L}(\text { data/q })  =` likelihood of the data 

{math}`\mathrm{q}  =` vector of distribution parameters (e.g. mean and std. dev.)

{math}`\mathrm{C} =` normalising constant = {math}`\int \left.\mathrm{L}(\text { data } \mid \mathrm{q})\right) \mathrm{f}^{\prime}(\mathrm{q}) d q`

For the normal case more detailed information is presented in [Annex A](section-part-3-general-principles-annex-A).

The first option can only be used after production of the lot or item under consideration. This data may not be known at the time of the design (e.g. ready mix concrete). The second option, on the other hand, offers the possibility to predict the posterior {math}`\mathrm{f}^{\prime \prime}(\mathrm{q})` for the filtered supply for a given combination of {math}`\mathrm{f(x \mid q), f(q)}` and a selection rule {math}`\mathrm{d}`. In such a case the control may lead to two possible outcomes:

- the lot (or unit) is rejected {math}`\qquad: \mathrm{d} \notin \mathrm{A}`
- the lot (or unit) is accepted {math}`\qquad: \mathrm{d} \in \mathrm{A}`

Here {math}`\mathrm{d}` is a function of the test result of a single unit or of the combined test result of the units in a sample and {math}`\mathrm{A}` is the acceptance domain. 

One may then calculate the posterior distributions for an arbitrary accepted lot:

```{math}
:label: eq-general-principles-3.0.6
\mathrm{f}^{\prime}(\mathrm{q} \mid \mathrm{d} \in \mathrm{A})=\mathrm{C}~\mathrm{P}(\mathrm{d} \in \mathrm{A} \mid \mathrm{q})~\mathrm{f}^{\prime}(\mathrm{q})
```

Here {math}`\mathrm{f}(\mathrm{q})` is the distribution function for the unfiltered supply and the acceptance probability {math}`\mathrm{P}(\mathrm{d} \in \mathrm{A} \mid \mathrm{q})` should be calculated from the decision rule.

The updated distribution for {math}`\mathrm{X}` can be obtained through {eq}`eq-general-principles-3.0.3` with {math}`\mathrm{f}(\mathrm{q})` replaced by {math}`\mathrm{f}^{\prime \prime}(\mathrm{q})`.

More information about the effect of quality cobntrol on the distribution of material properties can be found in [4](section-part-3-general-principles-references). 

(section-part-3-general-principles-annex-A)=
## Annex A: *Bayesian evaluation procedure for the normal and lognormal distribution - characteristic values*

If {math}`\mathrm{X}` has a normal distribution with parameters {math}`\mathrm{q}_{1}=\mu` and {math}`\mathrm{q}_{2}=\sigma` it is convenient to assume a prior distribution for {math}`\mu` and {math}`\sigma` according to:

```{math}
:label: eq-general-principles-annex-A-1
\mathrm{f}^{\prime}(\mu, \sigma)=\mathrm{k} \sigma^{-\left(\nu^{\prime}+\delta\left(\mathrm{n}^{\prime}\right)+1\right)} \exp \left\lbrace-\frac{1}{2 \sigma^{2}}\left\lbrace \nu^{\prime} \mathrm{s}^{\prime 2}+\mathrm{n}^{\prime}\left(\mu-\mathrm{m}^{\prime}\right)^{2}\right\rbrace \right\rbrace
```

{math}`\mathrm{k}=` normalizing constant  
{math}`\delta\left(\mathrm{n}^{\prime}\right)=` 0 for {math}`\mathrm{n}^{\prime}=0`  
{math}`\delta\left(\mathrm{n}^{\prime}\right)=` for {math}`\mathrm{n}^{\prime}>0`

This special choice enables a further analytical treatment of the various operations. The prior distribution {eq}`eq-general-principles-annex-A-1` contains four parameters: {math}`\mathrm{m}^{\prime}, \mathrm{n}^{\prime}, \mathrm{s}^{\prime 2}` and {math}`\nu^{\prime}`.

Using equation {eq}`eq-general-principles-3.0.4` one may combine the prior information characterised by {eq}`eq-general-principles-annex-A-1` and a test result of {math}`\mathrm{n}` observations with sample mean {math}`\mathrm{m}` and sample standard deviation {math}`\mathrm{s}`. The result is a posterior distribution for the unknown mean and standard deviation of {math}`\mathrm{X}`, which is again given by {eq}`eq-general-principles-annex-A-1`, but with parameters given by the following updating formula's:

```{math}
:label: eq-general-principles-annex-A-2
\mathrm{n}^{\prime \prime}=\mathrm{n}^{\prime}+\mathrm{n}
```

```{math}
:label: eq-general-principles-annex-A-3
\nu^{\prime \prime}=\nu^{\prime}+\nu+\delta\left(\mathrm{n}^{\prime}\right)
```

```{math}
:label: eq-general-principles-annex-A-4
\mathrm{m}^{\prime \prime}\mathrm{n}^{\prime \prime} =\mathrm{n}^{\prime} \mathrm{m}^{\prime}+ \mathrm{nm}
```

```{math}
:label: eq-general-principles-annex-A-5
{\left[\nu^{\prime \prime} \mathrm{s}^{\prime \prime 2}+\mathrm{n}^{\prime \prime} \mathrm{m}^{\prime \prime 2}\right]=\left[\nu^{\prime} \mathrm{s}^{, 2}+\mathrm{n}^{\prime} \mathrm{m}^{\prime 2}\right]+\left[\nu \mathrm{s}^{2}+\mathrm{n m}^{2}\right]}
```

Then, using equation {eq}`eq-general-principles-3.0.3` the predictive value of {math}`\mathrm{X}` can be found from:

```{math}
:label: eq-general-principles-annex-A-6
X=\mathrm{m}^{\prime \prime}+\mathrm{t}_{\mathrm{v}^{\prime \prime}}~\mathrm{s}^{\prime \prime}\left(1+\frac{1}{\mathrm{n}^{\prime \prime}}\right)^{0.5}
```

where {math}`\mathrm{t}_{\mathrm{v}^{\prime \prime}}` has a central t-distribution.

In case of known standard deviation {math}`\sigma` eq. {eq}`eq-general-principles-3.0.2` and {eq}`eq-general-principles-3.0.4` still hold for the posterior mean. The predictive value of {math}`\mathrm{X}` is

```{math}
:label: eq-general-principles-annex-A-7
X=\mathrm{m}^{\prime \prime}+u \sigma\left(1+\frac{1}{\mathrm{n}^{\prime \prime}}\right)^{0.5}
```

where {math}`\mathrm{u}` has a standard normal distribution.

The characteristic value is thus defined as

```{math}
:label: eq-general-principles-annex-A-8
x_{c}=\left\{\begin{array}{ccc}
m^{\prime \prime}+u\left(p_{x}\right) \sigma\left(1+\frac{1}{n^{\prime \prime}}\right)^{0.5} & \text { for } & \sigma \text { known } \\ \\
m^{\prime \prime}+t_{v^{\prime \prime}}\left(p_{x}\right) s^{\prime \prime}\left(1+\frac{1}{n^{\prime \prime}}\right)^{0.5} & \text { for } & \sigma \text { unknown }
\end{array}\right.
```

For {math}`\mathrm{n}^{\prime \prime} \nu^{\prime \prime} \rightarrow \infty~~\mathrm{x}_{\mathrm{c}}=\mathrm{m}^{\prime \prime} + \mathrm{u}\left(\mathrm{p}_{\mathrm{x}}\right) \mathrm{s}^{\prime \prime}` in both cases with {math}`\mathrm{s}^{\prime \prime}=\sigma`.

If {math}`\mathrm{X}` has a lognormal distribution, {math}`\mathrm{Y}=\ln (\mathrm{X})` has a normal distribution. One may then use the former formula's on {math}`\mathrm{Y}` and use {math}`\mathrm{X}=\exp (\mathrm{Y})` for results on {math}`\mathrm{X}`. 

## Annex B: *Bayesian evaluation procedure for regression - characteristic value*

If only indirect measurements for the quantity of interest are possible and a linear regression model {math}`\mathrm{y}=\mathrm{a}_{0}+\mathrm{a}_{1} \mathrm{x}` is suitable the predictive value of {math}`\mathrm{y}` has also a t-distribution given by

```{math}
y=a_{0}+a_{1} x+t_{\nu}~s \left(1 + \frac{1}{n}+\frac{\left(\bar{x}-x_{0}\right)^{2}}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}}\right)^{1/2}
```

where

{math}`a_{0}=\bar{y}-a_{1} \bar{x}`

{math}`a_{1}=\frac{\sum_{i=1}^{n} x_{i} y_{i}-n \overline{x y}}{\sum_{i=1}^{n} x_{i}^{2}-n \bar{x}^{2}}`

{math}`\bar{x}=\frac{1}{n} \sum_{i=1}^{n} x_{i}`

{math}`\bar{y}=\frac{1}{n} \sum_{i=1}^{n} y_{i}`

{math}`s^{2}=\frac{1}{n-2} \sum_{i=1}^{n} \left(y_{i}-a_{0}-a_{1} x_{i} \right)^2`

{math}`\nu=n-2`

The characteristic value corresponding to the quantile {math}`\mathrm{p}` is

```{math}
y_{c}=a_{0}+a_{1} x+T^{-1}(p, \nu)~s \left(1 + \frac{1}{n}+\frac{\left(\bar{x}-x_{0}\right)^{2}}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}}\right)^{1/2}
```

For example, for S-N curves, it is $\mathrm{y}=\ln (\mathrm{N}), \mathrm{x}=\ln (\Delta \sigma), \mathrm{a}_{1}=-\mathrm{m}$ and $\mathrm{a}_{0}=\ln \mathrm{a}$. The characteristic value of $\mathrm{N}$ for given $\ln \left(\Delta \sigma_{\mathrm{E}}\right)=\mathrm{x}_{0}$ is $\mathrm{N}_{\mathrm{c}}=\exp \left[\mathrm{y}_{\mathrm{c}}\right]$.


(section-part-3-general-principles-references)=
**References**

[1] Aitchison, J., Dunsmore, I.R., Statistical Prediction Analysis, Cambridge University Press, Cambridge, 1975

[2] Raiffa, H., Schlaifer, R., Applied Statistical Decision Theory, MIT Press, Cambridge, 1968

[3] Engelund, S., Rackwitz, R., On Predictive Distribution Functions for the Three Asymptotic Extreme Value Distributions, Structural Safety, Vol. 11, 1992, pp. 255-258

[4] Kersken-Bradley, M., Rackwitz, R., Stochastic Modeling of Material Properties and Quality Control, JCSS Working Document, IABSE-publication, March 1991