# General Principles

## Introduction

The environment in which structural systems function gives rise to internal forces, deformations, material deterioration and other short-term or long-term effects in these systems. The causes of these effects are termed actions. The environment from which the actions originate can be of a natural
character, for example, snow, wind and earthquake. lt can also be associated with human activities such as living in a domestic house, working in a factory, etc.

The following concepts of actions are used in this document.

1. An action is an assembly of concentrated or distributed forces acting on the structure. This kind of action is also denoted by "load".
2. An action is the cause of imposed displacements or thermal effects in the structure. This kind of action is often denoted by "indirect action".
3. An action is an environmental influence which may cause changes with time in the material properties or in the dimensions of a structure.

Action descriptions are in most cases based on suitably simple mathematical models, describing the temporal, spatial and directional properties of the action across the structure. The choice of the level of richness of details is guided by a balance between the quality of the available or obtainable information and a reasonably accurate modelling of the action effect. The choice of the level of realism and accuracy in predicting the relevant action effects is, in time, guided by the sensitivity of the implied design decisions to variations of this level and the economical weight of these decisions.
Thus the same action phenomenon may give rise to several very different action models dependent on the effect and structure under investigation.

## Classifications

Loads can be classified according to a number of characteristics. With respect to the type of the loads, the following subdivision can be made:

- self weight of structures
- occupancy loads in buildings, e.g. loads from persons and equipment
- actions caused by industrial activities, e.g. silo loads
- actions caused by transport: traffic, liquids in pipelines, cranes, impact, etc.
- climatic actions, e.g. snow, wind, outdoor temperature etc.
- hydraulic actions, e.g. water and ground water pressures
- actions from soil or rock, including earth quake

This classification does not cover all possible actions but most of the common types of actions can be included in one or more classes. Some of the classes belong as a whole either to uncontrollable actions or to controllable actions. Other actions may belong to both e.g. water pressure.

With respect to the variations in time the following classification can be made:

- **permanent actions** , whose variations in time around their mean is small and slow (e.g. self weight, earth pressure) or which monotonically a limiting value (e.g. prestressing, imposed deformation from construction processes, effects from temperature, shrinkage, creep or settlements)
- **variable actions**, whose variations in time are frequent and large (e.g. all actions caused by the use of the structure and by most of the external actions such as wind and snow)
- **exceptional actions**, whose magnitude can be considerable but whose probability of occurrence for a given structure is small related to the anticipated time of use. Frequently the duration is short (e.g. impact loads, explosions, earth and snow avalanches).

As far as the spatial fluctuations are concerned it is useful to distinguish between fixed and free
actions. **Fixed actions** have a given spatial intensity distribution over the structure. They are
completely defined if the intensity is specified in a particular point of the structure (e.g. earth or water
pressure). For **free actions** the spatial intensity distribution is variable (e.g. regular occupancy
loading, involved although they are variable actions.


## Modelling of actions

There are two main aspects of the description of an action: one is the physical aspect, the other is the
statistical aspect. In most cases these aspects can be clearly separated. Then the physical description
gives the type of physical data which characterise the action model, for example, vertical forces
distributed over a given area. The statistical description gives the statistical properties of the
variables, for example, a probability distribution function. In some cases the physical and statistical
aspects are so integrated that they cannot be considered separately.

A complete action model consists in general, of several constituents which describe the magnitude,
the position, the direction, the duration etc. of the action. Sometimes there is an interaction between
the components. There may in certain cases also be an interaction between the action and the
response of the structure.

One can in many cases distinguish between two kinds of variables (constituents) {math}`F_0` and {math}`W` describing
an action {math}`F` (see also part 1, [Basis of Design](../part-01/introduction.md)).

```{math}
:label: eq_action_F
F = φ (F_O, W)
```

- {math}`F_O` is a basic action variable which is directly associated with the event causing the action and
which should be defined so that it is, as far as possible, independent of the structure. For
example, for snow load {math}`F_O` is the snow load on ground, on a flat horizontal surface

- {math}`W` is a kind of conversion factor or model parameter appearing in the transformation from the
basic action to the action {math}`F` which affects the particular structure. {math}`W` may depend on the form
and size of the structure etc. For the snow load example {math}`W`  is the factor which transforms the
snow load on ground to the snow load on roof and which depends on the roof slope, the type
of roof surface etc.
- {math}`\varphi` is a suitable function, often a simple product.

The time variability is normally included in {math}`F_O`, whereas {math}`W` can often be considered as time
independent. A systematic part of the space variability of an action is in most cases included in {math}`W`,
whereas a possible random part may be included in {math}`F_O` or in {math}`W`. Eq. {eq}`eq_action_F` should be regarded as a
schematic equation. For one action there may be several variables {math}`F_O` and several variables {math}`W`.

Any action model contains a set of parameters and variables that must be evaluated before the model
can be used. In probabilistic modelling all action variables are in principle assumed to be random
variables or processes while other parameters may be time or spatial co-ordinates, directions etc.
Sometimes parameters may themselves be random variables, for example when the model allows for
statistical uncertainty due to small sample sizes.

An action model often includes two or more variables of different character as is described by eq. {eq}`eq_action_F`
For each variable a suitable model should be chosen so that the complete action model
consists of a number of models for the individual variables.

These models may be described in terms of:

- stochastic processes or random fields
- sequences of random variables
- individual random variables
- deterministic values or functions

The definition of the models for these quantities require probability distributions (see [annex 2](annex-2)) and a
description of the correlation patterns.


## Models for fluctuations in time

### Types of models

To describe time depended loads, one needs the probability distribution for the "arbitrary point in time values" and a description of the variations in time. Some typical process models are (see figure {numref}`fig2.0.4.1`):

1. Continuous and differentiable process

2. Random sequence

3. Point pulse process with random intervals

4. Rectangular wave process with random intervals

5. Rectangular wave process with equidistant intervals {math}`\Delta`

If the load intensities in subsequent time intervals of model (e) are independent, the model is referred to as a **FBC model** (Ferry Borges Castanheta model).

In many applications a combination of models is used, e.g. for wind the long term average is often modelled as an FBC model while the short term gust process is a continuous Gaussian process. Such models are referred to as **hierarchical models** (see Part 1, Basis of Design, [Section 5.4](section-5.4)). Each term in such a model describes a specific and independent part of the time variability. For a number of further definitions and notions, reference is made to [Annex 1](annex-1).

```{figure} ../part-02/images/Figure-2.0.4.1.jpg
:name: fig2.0.4.1

Various types of load models
```

### Distribution of extremes for single processes

At the design the main interest is normally directed to the maximum value of the load in some reference period of time {math}`t_{0}`. A quite general and useful upperbound formula to calculate the distribution of the maximum is given by:

```{math}
:label: eq2.0.4.1
\mathrm{F}_{\max F}(\mathrm{a}) \cong \exp \left[-\mathrm{t}_{0}~v^{+}(\mathrm{a})\right]
```

The upcrossing frequency {math}`v^{+}(a)` is given by:

```{math}
:label: eq2.0.4.2
v^{+}(\mathrm{a})=\mathrm{P}\left\lbrace\mathrm{F}_{\mathrm{t}}<\mathrm{a} \text { and } \mathrm{F}_{\mathrm{t}+\mathrm{dt}}>\mathrm{a}\right\rbrace / \mathrm{dt}
```

For the FBC model {math}`v^{+}(a)` is simply given by: 

```{math}
:label: eq2.0.4.3
v^{+}(a)=\left(1-F_{F}(a)\right) F_{F}(a) / \Delta t \cong\left(1-F_{F}(a)\right) / \Delta t 
```

And for a continuous Gaussian process:

```{math}
:label: eq2.0.4.4
v^{+}(a)=\frac{1}{2 \pi} \sqrt{-\rho^{\prime \prime}(0)} \exp \left(-\beta^{2} / 2\right)
```

where {math}`\beta=(a-\mu(F)) / F(F)` and {math}`\rho=` the correlation function.

### Distribution of extremes for hierarchical processes

Consider the case that the load model contains slowly and rapidly varying parts, as well as random variables that are constant in time (see {numref}`fig2.0.4.2`).

```{math}
:label: eq2.0.4.5
\mathrm{F}=\mathrm{R}+\mathrm{Q}+\mathrm{S}
```

{math}`\mathrm{R} =` random variables, constant in time

{math}`\mathrm{Q} =` slow rectangular process with mean renewal rate $\lambda$

{math}`\mathrm{S} =` fast varying process

In that case the following expression (see Annex 3, {eq}`eqA3.5a`) can be used:

```{math}
:label: eq2.0.4.6
F_{\max F}(a)=E_{R}\left[\exp \left[\lambda t_{0}\left[1-E_{Q} \exp \left(-\Delta t~v_{s}^{+}(a \mid R Q)\right)\right]\right]\right]
```

{math}`v_{\mathrm{s}}^{+}(\mathrm{a} \mid \mathrm{RQ})=` upcrossing rate of level "a" for process {math}`\mathrm{S}`, conditional upon {math}`\mathrm{R}` and {math}`\mathrm{Q}` 

{math}`\Delta t=1 / \lambda=` time interval for the rectangular process {math}`\mathrm{Q}`

{math}`E_{R}` and {math}`E_{Q}` denote the expectation operator over all variables {math}`R` and {math}`Q` respectively.

```{figure} ../part-02/images/Figure-2.0.4.2.jpg
:name: fig2.0.4.2

Hierarchical model for time dependent loads
```

## Models for Spatial variability

(section-2.0.5.1)=
### Hierarchical model

As an example for the spatial modelling of actions using a hierarchical model consider the live load in an office building:

```{math}
:label: eq2.0.5.1
\mathrm{F}=\mathrm{m}+\Delta \mathrm{F}_{1}+\Delta \mathrm{F}_{2}+\Delta \mathrm{F}_{3}(\mathrm{x}, \mathrm{y})
```

where:

{math}`\mathrm{m}` is a general mean value for the whole population

{math}`\Delta \mathrm{F}_{1}` is a stochastic variable which describes the variation **between** the load on different floors. The distribution function for {math}`\Delta \mathrm{F}_{1}` has the mean value zero and the standard deviation {math}`\sigma_{1}`

{math}`\Delta \mathrm{F}_{2}` is a stochastic variable which describes the variation **between** the load in rooms on the same floor but with different floor areas. The distribution function for {math}`\Delta \mathrm{F}_{2}` has the mean value zero and the standard deviation {math}`\sigma_{2}`

{math}`\Delta \mathrm{F}_{3}` is a random field which describes the spatial variability of the load **within** a room.

The total variability of the samples taken from the total population is described by {math}`\Delta \mathrm{F}_{1}+\Delta \mathrm{F}_{2}+\Delta \mathrm{F}_{3}`. The variability **within** the subpopulation of floors is described by {math}`\Delta \mathrm{F}_{2}+\Delta \mathrm{F}_{3}`.

### Equivalent uniformly distributed load (EUDL)

Consider a simple hierarchical distribution load model given by:

```{math}
:label: eq2.5.0.2
\mathrm{q}(\mathrm{x}, \mathrm{y})=\mathrm{q}_{\mathrm{o}}+\mathrm{q}_{\mathrm{loc}}(\mathrm{x}, \mathrm{y})
```

{math}`\mathrm{q}_{\mathrm{o}}=` the variability between the various structures or structural elements

{math}`\mathrm{q}_{\text {loc }}=` the small scale or point to point fluctuation.

In many cases the random field {math}`\mathrm{q}` is replaced by a so called Equivalent Uniformly Distributed Load (EUDL). This load is defined as:

```{math}
:label: eq2.5.0.3
\mathrm{q}_{\text {EUDL }}(\mathrm{t})=\frac{\int \mathrm{q}(\mathrm{x}, \mathrm{y}, \mathrm{t}) \mathrm{i}(\mathrm{xy}) \mathrm{dA}}{\int \mathrm{i}(\mathrm{xy}) \mathrm{dA}}
```

when {math}`\mathrm{i}(\mathrm{x}, \mathrm{y})` is the influence function for some specific load effect (e.g. the midspan bending moment).

For given statistical properties of the load field {math}`\mathrm{q}(\mathrm{x}, \mathrm{y})` the mean and standard deviation of {math}`\mathrm{q}_{\mathrm{EUDL}}` can be evaluated. For a homogeneous field, that is a random field where the statistical properties of {math}`\mathrm{q}(\mathrm{x}, \mathrm{y})` do not depend on the location, we give here the resulting formulas:

```{math}
:label: eq2.5.0.4
\mu(\mathrm{q}_{\mathrm{EUDL}})=\mu\left(\mathrm{q}_{\mathrm{o}}\right)
```

```{math}
:label: eq2.5.0.5
\sigma^{2}\left(\mathrm{q}_{\mathrm{EUDL}}\right)=\sigma^{2}\left(\mathrm{q}_{\mathrm{o}}\right)+\sigma^{2}\left(\mathrm{q}_{\mathrm{loc}}\right) \int\int \int\int  \mathrm{i}(\mathrm{x}, \mathrm{y}) \mathrm{i}(\xi, \eta) \rho(\mathrm{d}) \mathrm{dxdyd} \xi \mathrm{d} \eta~/\left[\iint \mathrm{i}(\mathrm{x}, \mathrm{y}) \mathrm{dxdy}\right]^{2}
```

Here {math}`\rho(\mathrm{d})` is the correlation function describing the correlation between the small scale load {math}`\mathrm{q}_{\mathrm{loc}}`, on the two point {math}`(\mathrm{x}, \mathrm{y})` and {math}`(\xi, \eta)`. This function may be of the form:

```{math}
:label: eq2.5.0.6
\rho(\Delta r)=\exp \left\lbrace-\Delta \mathrm{r}^{2} / \mathrm{d}_{\mathrm{c}}^{2}\right\rbrace
```

with {math}`\Delta \mathrm{r}^{2}=(\mathrm{x}-\xi)^{2}+(\mathrm{y}-\eta)^{2}, \Delta \mathrm{r}` being the distance between the two points, and {math}`\mathrm{d}_{\mathrm{c}}` some scale distance. The correlation function tends to zero for distances {math}`\Delta \mathrm{r}` much larger than {math}`\mathrm{d}_{\mathrm{c}}`.

If the field can be schematised as an FBC-field, the formula for {math}`\sigma^{2}\left(\mathrm{q}_{\mathrm{EUDL}}\right)` can be simplified to:

```{math}
:label: eq2.5.0.7
\sigma^{2}\left(\mathrm{q}_{\mathrm{EUDL}}\right)=\sigma^{2}\left(\mathrm{q}_{\mathrm{i}}\right)+\sigma^{2}\left(\mathrm{q}_{\mathrm{loc}}\right) \kappa \mathrm{A}_{\mathrm{o}} / \mathrm{A}
```

Here {math}`A_{o}` is the reference area of the FBC-field and A stands for the total area under consideration, the so called tributary area. The formula is valid only for {math}`A>A_{0}`.

The parameter {math}`\kappa` is a factor depending on the shape of the influence line {math}`\mathrm{i}(\mathrm{x}, \mathrm{y})`. Values are presented in {numref}`fig2.5.0.1`. The figure {math}`\kappa=1` corresponds to a constant value of {math}`\mathrm{i}(\mathrm{x}, \mathrm{y})`. 

```{figure} ../part-02/images/Figure-2.5.0.1.jpg
:name: fig2.5.0.1

Random fields and corresponding {math}`\kappa`-values
```

## Interactions and correlations between actions

For describing dependencies between various actions it is useful to distinguish between:

- actions of the same nature

- actions of different nature

Actions of the same nature are for instance floor loads on different floors in one building or the wind loads on the front and back wall. The combination of wind and snow is a typical example of the combination of action of a differente type. Note that sometimes it may be less clear: it may be difficult to decide whether floor loads of a completely different type in one building (say office loads and storage loads) are loads of the same nature or a different nature.

If the actions are of the *same nature*, one might better consider them as components of one action, The various components are normally described by similar probabilistic models. The basic question is then to model the statistical dependency between the processes. In general this is a purely mathematical problem. Details of the mathematical description of the dependencies depend on the nature of the physical relationship and the nature of the processes themselves. One possibility is to construct a hierarchical model as has been explained in [section 2.0.5.1](section-2.0.5.1). For two stationary continuous Gaussian processes {math}`\mathrm{x}(\mathrm{t})` and {math}`\mathrm{y}(\mathrm{t})` the correlation alternatively may be described by the cross correlation function {math}`\mathrm{R}_{\mathrm{xy}}(\tau)` or alternatively by the cross spectrum {math}`\mathrm{S}_{\mathrm{xy}}(\omega)` (see [Annex 1](annex-1)). For pulse type processes we may have to distinguish between the correlation in amplitude, arrival time and duration. Floor loads in multi-storey buildings are a good example where all three correlations are of importance.

If the actions are *of a different nature*, they sometimes may show quite complex physical interactions. Typical examples are:

*Snow and wind*  
If snow and wind act together, the result may be that the wind reduces the accumulated snow load on the roof. For some building configuration, however, the combined action by wind and snow may result in much higher loads on some specific locations. This dependency between wind and snow is present even if wind and snow are statistically completely independent processes (which is not the case). In such cases we need a more complex model {eq}`eq_action_F` where the final load is calculated as a function of both wind speed and snow intensity. In addition one may need a statistical correlation between wind and snow as components of the same multicomponent atmospheric system.

*Earthquake and fire*  
Earthquakes are often followed by fire: due to the damage of the pipes and heating systems gas may come free and a fire may be started. The earth quake is said to act as a trigger mechanism for fire. In order to treat this interaction properly, one should consider

1. the probability of a fire starting given an earth quake has occured and
2. the probability of collapse, given earth quake and fire

The second analysis should take into account that all extinction devices may not be working and that the structure may already be damaged by the earth quake.

Additional to that, of course, one still needs to consider the standard cases of collapse under earth quake alone and collapse under fire alone.

*Wind and traffic on bridges*  
Traffic on bridges enlarges the wind load, but heavy wind will reduce the traffic. One may need a model expressing the wind force given the traffic and wind speed and a model expressing the conditional probabability density of the traffic intensity as a function of wind speed.

So in all above examples one need to build a more advanced physical model on the one hand and conditional probability models of one load given the (extreme) condition of the other. In most cases it may be convenient to define one of the processes as the "leading one" and describe arrival times and amplitudes of the second process conditional upon the occurrence and amplitude of the first one.

In this model code none or little guidance is presented to this matter. However, the user of this model code is always entitled to be aware of these possible correlations and interactions. It is stressed that these interactions may be of great importance to the reliability of the structure.

## Combination of actions

From a mathematical modelling point of view the load on a structure is a joint set {math}`\mathrm{F}(\mathrm{t})` of time varying random fields. This set of loads give a rectorial load effect {math}`\mathrm{E}(\mathrm{t})` in a given cross section or point of the structure at time {math}`t` as a function of {math}`\mathrm{F}(\mathrm{t})` (i.e. a random process). In the scalar case we have:

```{math}
:label: eq2.0.7.1
\mathrm{E}(\mathrm{t})=\mathrm{c}_{1} \mathrm{~F}_{1}(\mathrm{t})+\mathrm{c}_{2} \mathrm{~F}_{2}(\mathrm{t})+. .
```

The reliability problem related to the considered point is to evaluate the probability {math}`P_{f}` that {math}`F_{\max }(t)~E~V` for all future time {math}`\mathrm{V}` is the nonfailure domain defined by the strength properties at the considered point and limit state.

The load combination problem is to formulate a reasonably simple but for the considered engineering purpose sufficiently realistic mathematical model that defines {math}`\mathbf{F}(\mathrm{t})`. The needed level of detailed modelling of {math}`\mathbf{F}(\mathrm{t})` depends on the filtering effect of the function that maps {math}`\mathbf{F}(\mathrm{t})` into the load effect {math}`\mathrm{E}(\mathrm{t})`. This filtering effect is judged under due consideration of the sensitivity of the probability {math}`\mathrm{P}_{\mathrm{f}}` to the detailing of the models. The sensitivity question is tied to the last part of the load combination problem which is actually to compute the value of {math}`\mathrm{P}_{\mathrm{f}}`. Thus, to be operational, the modelling of {math}`\mathbf{F}(\mathrm{t})` should be simple enough to enable at least a computer simulation of the scalar process {math}`\mathrm{E}(\mathrm{t})` to an extent that allows an estimation of {math}`\mathrm{P}_{\mathrm{f}}`.

First the relevant set of different action types is identified. This identification defines the number of elements in the set {math}`\mathbf{F}(\mathrm{t})` and the subdivision of {math}`\mathbf{F}(\mathrm{t})` into stochastically independent subsets. The modelling is next concentrated on each of these subsets with dependent components.

The mathematical difficulty to solve probabilities for outcrossing rates of processes of the type {eq}`eq2.0.7.1` is the possible very different nature of the various contributors {math}`F_{i}`. Each of these processes may be of a completely different nature, including all kinds of continuos and intermittent processes. Numerical solutions will often prove to be necessary, but also analytical solutions may prove to be very helpful. Reference is made to [Annex 3](annex-3) and to the literature.

(annex-1)=
## ANNEX 1 - DEFINITIONS

### Covariance function

The covariance function {math}`\mathrm{r}\left(\mathrm{t}_{1}, \mathrm{t}_{2}\right)` is defined by:

```{math}
\begin{aligned}
& \mathrm{r}\left(\mathrm{t}_{1}, \mathrm{t}_{2}\right)=\mathrm{E}\left[\left(\mathrm{F}(\mathrm{t}=1)-\mathrm{m}_{1}\right)\left(\mathrm{F}\left(\mathrm{t}_{2}\right)-\mathrm{m}_{2}\right)\right] \\
& \mathrm{m}_{1}=\mathrm{E}\left[\mathrm{F}\left(\mathrm{t}_{1}\right)\right] \quad \quad \quad \quad  \mathrm{m}_{2}=\mathrm{E}\left[\mathrm{F}\left(\mathrm{t}_{2}\right)\right]
\end{aligned}
```

### Stationary processes

The process is defined for {math}`-\infty<\mathrm{t}<\infty`. If, for all values {math}`\mathrm{t}_{1}` and for all values {math}`\tau`, chosen such that {math}`0 \leq \mathrm{t}_{\mathrm{i}} \leq \mathrm{t}_{\mathrm{o}}` to and {math}`0 \leq \mathrm{t}_{\mathrm{i}}+\tau \leq \mathrm{t}_{\mathrm{o}}`, the stochastic variable {math}`\mathrm{x}~\left( \mathrm{t}_{\mathrm{i}} +\tau\right)` has the same distribution function as the stochastic variable {math}`\mathrm{x}\left(\mathrm{t}_{\mathrm{i}}\right)` the stochastic process {math}`\mathrm{x}(\mathrm{t})` is stationary.

If the mean value function {math}`\mathrm{m}(\mathrm{t})` is constant and the covariance function {math}`\mathrm{r}\left(\mathrm{t}_{1}, \mathrm{t}_{2}\right)` depends solely on the difference {math}`\tau=\left(\mathrm{t}_{2}-\mathrm{t}_{1}\right)` the process is sold to be wide-sense stationary.

Thus the covariance function for a stationary or a wide sense stationary process may be written

```{math}
\mathrm{r}(\tau)=\mathrm{E}[(\mathrm{F}(\mathrm{t}+\tau)-\mathrm{m})(\mathrm{F}(\mathrm{t})-\mathrm{m})]
```

The concept of stationary applied to action processes should in most cases be interpreted as widesense stationary.

### Ergodic processes

A process is ergodic if averaging over several realisations and averaging with respect to time (or another index parameter) give the same result.

For ergodic processes a relation between the point-in-time value distribution function {math}`\mathrm{F}` and the excursion time {math}`\mathrm{t}` is determined for a chosen reference period {math}`\mathrm{t}_{\mathrm{o}}`, by

```{math}
1-\mathrm{F}_{\mathrm{F}}(\mathrm{F})=\mathrm{t} / \mathrm{t}_{\mathrm{o}}
```

### The correlation function

The correlation function for a stationary process is:

```{math}
\rho(\tau)=\frac{\mathrm{r}(\tau)}{\mathrm{r}(0)}
```

For ergodic processes {math}`\rho(\tau=\infty)=0`

### Spectrum

A stationary stochastic process may be characterised with aid of a spectrum:

```{math}
\mathrm{S}(\mathrm{n})=\int_{-\infty}^{\infty} e^{-i 2 \pi n \tau} \mathrm{r}(\tau) \mathrm{d} \tau
```

{math}`\mathrm{S}(\mathrm{n})` may be regarded as a measure of how the process is built up of components with different frequencies. The total variance of the process is:

```{math}
\operatorname{Var} \mathrm{Q}=2 \int_{0}^{\infty} \mathrm{S}(\mathrm{n}) \mathrm{d} \mathrm{n}
```

### Gaussian processes

A stochastic process {math}`\mathrm{S}(\mathrm{t})` is a Gaussian process if the multidimensional probability distribution functions for all the stochastic variables {math}`\mathrm{S}\left(\mathrm{t}_{\mathrm{i}}\right)` are Gaussian. The stochastic properties of a Gaussian process is completely determined by the mean value and the covariance function or by the spectrum.

### Scalar Nataf Processes

A special but important class of non-Gaussian, scalar and differentiable processes are built by a memoryless transformation from a normal process, i.e.

```{math}
\mathrm{S}(\mathrm{t})=\mathrm{h}(\mathrm{U}(\mathrm{t}))
```

where {math}`\mathrm{U}(\mathrm{t})` is a standard normal process and {math}`\mathrm{h}(\mathrm{u})` is an arbitrary function. For {math}`\mathrm{S}(\mathrm{t})` any admissible (unimodal) distribution function can be chosen thus defining a certain class of functions {math}`\mathrm{h}(\mathrm{u})`. In addition the autocorrelation function {math}`\rho_{\mathrm{s}}\left(\mathrm{t}_{1}, \mathrm{t}_{2}\right)` has to be specific. However, there are some restrictions on the type of autocorrelation function.

### Scalar Hermite Processes

The Hermite process is a special case of the Nataf process. All marginal distribution must be of Hermite type. For this process the solution of the integral equation occurring for the autocorrelation function of the equivalent (or better generating) standard normal process is analytic. The standard Hermite process has the representation, i.e. a special case of the function {math}`\mathrm{h}(\mathrm{u})` 

```{math}
\mathrm{S}(\mathrm{t})=\kappa\left(\mathrm{U}(\mathrm{t})+\widetilde{\mathrm{h}}_{3, \mathrm{i}}\left(\mathrm{U}(\mathrm{t})^{2}-1\right)+\widetilde{\mathrm{h}}\left(\mathrm{U}(\mathrm{t})^{3}-3 \mathrm{U}(\mathrm{t})\right)\right)
```

For the coefficients depending on the first four moments of the marginal distribution of the non-normal process. In addition, the Hermite process requires specification of the autocorrelation function of {math}`\mathrm{S}(\mathrm{t})`. Again, there are certain restrictions on the moments of the marginal distributions as well as on the autocorrelation function.

### Scalar Rectangular Wave Renewal Processes

Scalar rectangular wave renewal processes are useful models for processes changing their amplitude at random renewal points in a random fashion. A scalar rectangular wave renewal process is characterised by the jump rate {math}`\lambda`, and the distribution function of the amplitude. The renewals occur independently of each other. No specific distribution is assigned to the interarrival times. Therefore, the renewal process characterised only by a jump rate captures only long term statistics. The mean duration of pulses is asymptotically equal to {math}`1 / \lambda`.. For the special case of a Poisson rectangular wave process the interarrival times and so the durations of the pulses are exponentially distributed with parameter {math}`1 / \lambda`.. In the special case of a Ferry Borges-Castanheta process the durations are constant and the repetition number {math}`\mathrm{r}=\left(\mathrm{t}_{2}-\mathrm{t}_{1}\right) / \Delta` with {math}`\Delta` the duration of pulses is equal to {math}`\lambda\left(\mathrm{t}_{2}-\mathrm{t}_{1}\right)`. Also, the sequence of amplitudes is an independent sequence. The jump rate can be a function of time as well as the parameters of the distribution function of the amplitudes.

It is assumed that rectangular wave processes jump from a random value {math}`\mathrm{S}(\mathrm{t})` to a new value {math}`\mathrm{S}^{+}(\mathrm{t}+\delta)` with {math}`\delta \rightarrow` at a renewal without returning to zero. Rectangular wave renewal processes must be regular processes, i.e. the occurrence of any two or more renewals in a small time interval must be negligible (of o-order). Non-stationary rectangular wave renewal processes are processes which have either time-dependent parameters of the amplitude distributions and/or time-dependent jump rates.

### Random fields

A random field may be regarded as a one-, two- or three-dimensional stochastic process. The time {math}`\mathrm{t}` is substituted by the space co-ordinates {math}`\mathrm{x}, \mathrm{y}, \mathrm{z}`.

For the two-dimensional case the covariance function is written (for a stationary random field)

```{math}
\mathrm{r}\left(\mathrm{d}_{\mathrm{x}}, \mathrm{d}_{\mathrm{y}}\right)=\mathrm{E}\left[\left(\mathrm{F}\left(\mathrm{x}+\mathrm{d}_{\mathrm{x}}, \mathrm{y}+\mathrm{d}_{\mathrm{y}}\right)-\mathrm{m}\right)(\mathrm{F}(\mathrm{x}, \mathrm{y})-\mathrm{m})\right]
```

The concepts of stationary, ergodicy etc. are in principle the same as for the stochastic processes.

### Vector processes

Two stationary Gaussian processes F1 and F2 are statistically completely described by their mean values, auto-spectra and the cross spectrum. The latter is defined by:

```{math}
\begin{aligned}
& \mathrm{r}_{12}(\tau)=\mathrm{E}\left[\left(\mathrm{F}_{1}(\mathrm{t}+\tau)-\mathrm{m}_{1}\right)\left(\mathrm{F}_{2}(\mathrm{t})-\mathrm{m}_{2}\right)\right] \\
& \mathrm{S}_{12}(\mathrm{n})=\int_{-\infty}^{\infty} \mathrm{e}^{-\mathrm{i} 2 \pi \mathrm{n} \tau} \mathrm{r}_{12}(\tau) \mathrm{d} \tau
\end{aligned}
```

A vector of {math}`\mathrm{n}` stationary Gaussian processes can be described by {math}`\mathrm{n}` mean values, {math}`\mathrm{n}` auto-spectra and {math}`\mathrm{n}(\mathrm{n}-1)` cross spectra. Note that {math}`\mathrm{S}_{\mathrm{i j}}` is the complex conjugate of {math}`\mathrm{S_{j i}}`.

(annex-2)=
## ANNEX 2 - DISTRIBUTIONS FUNCTIONS

```{table} 
:name: tbl-annex-2
| Distribution type | Parameters | Moments |
| --- | --- | --- |
| **Rectangular**<br>{math}`\mathrm{a} \leq \mathrm{x} \leq \mathrm{b}` <br>  {math}`\mathrm{f}_\mathrm{x} (\mathrm{x})=\frac{1}{\mathrm{b}-\mathrm{a}}` | {math}`1 = \mathrm{a}`<br>{math}`2 = \mathrm{b}` | {math}`\mathrm{m} = \frac{\mathrm{a} + \mathrm{b}}{2}`<br>{math}`\mathrm{s} = \frac{\mathrm{b} - \mathrm{a}}{\sqrt{12}}` |
| **Normal**<br>{math}`\sigma > 0`<br> {math}`\mathrm{f}_\mathrm{x} (\mathrm{x})=\frac{1}{\sigma \sqrt{2\pi}}\mathrm{exp}\left(-\frac{1}{2}\left(\frac{\mathrm{x}-\mu}{\sigma}\right)^2\right)` | {math}`1 = \mu` <br> {math}`2 = \sigma` | {math}`\mathrm{m} = \mu`<br>{math}`\mathrm{s} = \sigma` |
| **Lognormal**<br>{math}`\mathrm{x} > 0`, {math}`\zeta > 0` <br> {math}`\mathrm{f}_\mathrm{x} (\mathrm{x})=\frac{1}{\mathrm{x} \zeta \sqrt{2\pi}}\mathrm{exp}\left(-\frac{1}{2}\left(\frac{\ln\mathrm{x}-\lambda}{\zeta}\right)^2\right)` | {math}`1 = \lambda` <br> {math}`2 = \zeta` | {math}`\mathrm{m} = \mathrm{exp} \left(\lambda+\frac{\zeta^2}{2}\right)` <br> {math}`\mathrm{s}= \mathrm{exp} \left(\lambda+\frac{\zeta^2}{2}\right) \sqrt{\mathrm{exp}\left(\zeta^2\right)-1}` | 
| **Shifted Lognormal**<br>{math}`\mathrm{x} > \varepsilon`, {math}`\zeta > 0` <br> {math}`\mathrm{f}_\mathrm{x} (\mathrm{x})=\frac{1}{(\mathrm{x} - \varepsilon) \zeta \sqrt{2\pi}}\mathrm{exp}\left(-\frac{1}{2}\left(\frac{\mathrm{ln}(\mathrm{x}-\varepsilon)-\lambda}{\zeta}\right)^2\right)` | {math}`1 = \lambda`<br>{math}`2 = \zeta`<br>{math}`3 = \varepsilon` | {math}`\mathrm{m} = \varepsilon + \mathrm{exp} \left(\lambda+\frac{\zeta^2}{2}\right) + \varepsilon`<br>{math}`\mathrm{s}= \mathrm{exp} \left(\lambda+\frac{\zeta^2}{2}\right) \sqrt{\mathrm{exp}\left(\zeta^2\right)-1}` |
| **Shifted Exponential**<br>{math}`\mathrm{x} \geq \varepsilon`, {math}`\lambda > 0` <br> {math}`\mathrm{f}_\mathrm{x} (\mathrm{x})= \lambda~\mathrm{exp}\left(-\lambda(\mathrm{x}-\varepsilon)\right)`  | {math}`1 = \lambda`<br>{math}`2 = \varepsilon` | {math}`\mathrm{m}=\frac{1}{\lambda} + \varepsilon` <br> {math}`\mathrm{s}=\frac{1}{\lambda}`  |
| **Shifted Gamma**<br>{math}`\mathrm{x} \geq 0`, {math}`\mathrm{b} > 0`, {math}`\mathrm{p} > 0` <br> {math}`\mathrm{f}_\mathrm{x} (\mathrm{x})= \frac{\mathrm{b}^\mathrm{p}}{\Gamma (\mathrm{p})}\mathrm{exp} \left(-b(\mathrm{x}-\varepsilon)\right)(\mathrm{x}-\varepsilon)^{\mathrm{p}-1}` | {math}`1 = \mathrm{p}`<br>{math}`2 = \mathrm{b}`<br>{math}`3 = \varepsilon` | {math}`\mathrm{m} = \frac{\mathrm{p}}{\mathrm{b}} + \varepsilon`<br>{math}`\mathrm{s} = \frac{\sqrt{\mathrm{p}}}{\mathrm{b}}` |
| **Beta**<br>{math}`\mathrm{a} \leq \mathrm{x} \leq \mathrm{b},~~ \mathrm{r}`, {math}`\mathrm{t} \geq 1` <br> {math}`\mathrm{f}_\mathrm{x} (\mathrm{x})= \frac{\left(\mathrm{x}-\mathrm{a}\right)^{\mathrm{r}-1} \left(\mathrm{b}-\mathrm{x} \right)^{\mathrm{t}-1}}{\left(\mathrm{b}-\mathrm{a}\right)^{\mathrm{r+t-1}} \mathrm{B} \left(\mathrm{r,t}\right)}` | {math}`1 = \mathrm{a}`<br>{math}`2 = \mathrm{b}`<br>{math}`3 = \mathrm{r}`<br>{math}`4 = \mathrm{t}` | {math}`\mathrm{m} = \mathrm{a} + \left(\mathrm{b} - \mathrm{a}\right) \frac{\mathrm{r}}{\mathrm{r+t}}` <br> {math}`\mathrm{s} = \frac{\mathrm{b - a}}{\mathrm{r+t}} \sqrt{\frac{\mathrm{rt}}{\mathrm{r+t+1}}} ` |
| **Gumbel (Maximum)**<br>{math}`−\infty < \mathrm{x} < +\infty,~\alpha > 0` <br> {math}`\mathrm{f}_\mathrm{x} (\mathrm{x})=\alpha~\mathrm{exp}\left(-\alpha(\mathrm{x-u}) - \mathrm{exp}\left(-\alpha(\mathrm{x-u})\right)\right)`  | {math}`1 = \mathrm{u}`<br>{math}`2 = \alpha` | {math}`\mathrm{m} = \mathrm{u} + \frac{0.577216}{\alpha}`<br>{math}`\mathrm{s} = \frac{\pi}{\alpha \sqrt{6}}` |
| **Frechet (Maximum)**<br>{math}` \varepsilon \leq \mathrm{x} < +\infty,~~\mathrm{u, k} > 0` <br> {math}`\mathrm{f}_\mathrm{x} (\mathrm{x})= \frac{\mathrm{k}}{\mathrm{u}-\varepsilon} \left(\frac{\mathrm{x} - \varepsilon}{\mathrm{u} - \varepsilon}\right)^{\mathrm{-k-1}} \mathrm{exp} \left(- \left(\frac{\mathrm{x} - \varepsilon}{\mathrm{u} - \varepsilon}\right)^{\mathrm{-k}} \right)` | {math}`1 = \mathrm{u}`<br>{math}`2 = \mathrm{k}`<br>{math}`3 = \varepsilon` | {math}`\mathrm{m} = \varepsilon + (\mathrm{u} - \varepsilon) \Gamma \left(1 - \frac{1}{\mathrm{k}}\right)` <br> {math}`\mathrm{s} = (\mathrm{u} - \varepsilon) \sqrt{\Gamma \left(1 - \frac{2}{\mathrm{k}} \right) - \Gamma^2 \left(1 - \frac{1}{\mathrm{k}}\right)}` |
| **Weibull (Maximum)**<br>{math}`\varepsilon \leq \mathrm{x} < +\infty,~~ \mathrm{u, k} > 0` <br> {math}`\mathrm{f}_\mathrm{x} (\mathrm{x})= \frac{\mathrm{k}}{\mathrm{u}-\varepsilon} \left(\frac{\mathrm{x} - \varepsilon}{\mathrm{u} - \varepsilon}\right)^{\mathrm{-k-1}} \mathrm{exp} \left(- \left(\frac{\mathrm{x} - \varepsilon}{\mathrm{u} - \varepsilon}\right)^{\mathrm{-k}} \right)` | {math}`1 = \mathrm{u}`<br>{math}`2 = \mathrm{k}`<br>{math}`3 = \varepsilon` | {math}`\mathrm{m} = \varepsilon + (\mathrm{u} - \varepsilon) \Gamma \left(1 + \frac{1}{\mathrm{k}}\right)` <br> {math}`\mathrm{s} = (\mathrm{u} - \varepsilon) \sqrt{\Gamma \left(1 + \frac{2}{\mathrm{k}} \right) - \Gamma^2 \left(1 + \frac{1}{\mathrm{k}}\right)}` |
```

(annex-3)=
## ANNEX 3 - MATHEMATICAL COMBINATION TECHNIQUES

### Combination of two rectangular processes (Ferry Borges-Castanheta model)

Consider the case that two actions {math}`\mathrm{Q}_{1}(\mathrm{t})` and {math}`\mathrm{Q}_{2}(\mathrm{t})` are to be combined. Assume that these actions can be described as rectangular or sqaure wave models ({numref}`figA-3.1`). The following assumptions are made about the processes:

- {math}`\mathrm{Q}_{1}(\mathrm{t})` and {math}`\mathrm{Q}_{2}(\mathrm{t})` are stationary ergodic processes
- All intervals {math}`\tau_{1}` are equal; all intervals {math}`\tau_{2}` are equal and {math}`\tau_{1} \geq \tau_{2}`
- {math}`\mathrm{Q}_{1}` and {math}`\mathrm{Q}_{2}` are constant during each interval {math}`\tau_{1}` and {math}`\tau_{2}` respectively
- The values of {math}`\mathrm{Q}_{1}` for the different intervals are mutually independent; same for {math}`\mathrm{Q}_{2}`
- {math}`\mathrm{Q}_{1}` and {math}`\mathrm{Q}_{2}` are independent

```{figure} ../part-02/images/Figure-A.3.1.jpg
:name: figA-3.1

Square wave processes for {math}`\mathrm{Q}_{1}(\mathrm{t})` and {math}`\mathrm{Q}_{2}(\mathrm{t})`
```

Define {math}`\mathrm{Q}_{2 c}` as the maximum value of {math}`\mathrm{Q}_{2}` occurring during the interval {math}`\tau_{1}` with the probability distribution function:

```{math}
:label: eqA3.1
\mathrm{F}_{\mathrm{Q} 2 \mathrm{C}}(\mathrm{Q})=\left[\mathrm{F}_{\mathrm{Q}^{*}}(\mathrm{Q})\right]^{\tau 2 / \tau 1}
```

{math}`\mathrm{F}_{\mathrm{Q}}{ }^{*}=` the arbitrary point in time distribution for {math}`\mathrm{Q}_{2}`

Assume a linear relationship between the actions effect {math}`\mathrm{E}` and the actions:

```{math}
:label: eqA3.2
\mathrm{E}=\mathrm{c}_{1} \mathrm{Q}_{1}+\mathrm{c}_{2} \mathrm{Q}_{2}
```

The maximum action effect {math}`\mathrm{E}_{\max }` from {math}`\mathrm{Q}_{1}` and {math}`\mathrm{Q}_{2}` during the reference period {math}`\mathrm{t}_{\mathrm{O}}` can then be written as:

```{math}
:label: eqA3.3
\mathrm{E}_{\max }=\max \left\lbrace\mathrm{c}_{1} \mathrm{Q}_{1}+\mathrm{c}_{2} \mathrm{Q}_{2 \mathrm{c}}\right\rbrace
```

The maximum should be taken over all intervals {math}`\tau_{1}` within the reference period {math}`\mathrm{t}_{\mathrm{o}}`.

As an approximation, the resulting action effects could be calculated as the maximum of the following two combinations (Turkstra's rule):

- {math}`\quad \mathrm{E}\left\lbrace \mathrm{Q}_{1 \max }, \mathrm{Q}_{2 \mathrm{c}}\right\rbrace \quad` if {math}`\mathrm{Q}_{1}` is considered as the dominating action
- {math}`\quad \mathrm{E}\left\lbrace \mathrm{Q}_{2 \max }, \mathrm{Q}_{1 \mathrm{c}}\right\rbrace \quad` if {math}`\mathrm{Q}_{2}` is considered as the dominating action

Written as a formula for the case {math}`\mathrm{E}=\mathrm{c}_{1} \mathrm{Q}_{1}+\mathrm{c}_{2} \mathrm{Q}_{2}`

```{math}
:label: eqA3.4
\mathrm{E}_{\max }=\max \left\lbrace \mathrm{c}_{1} \mathrm{Q}_{\max }+\mathrm{c}_{2} \mathrm{Q}_{2 \mathrm{c}}~; \mathrm{c}_{1} \mathrm{Q}_{1 \mathrm{c}}+\mathrm{c}_{2} \mathrm{Q}_{2, \max }\right\rbrace
```

It should be noted that the Turkstra Rule gives a lower bound for the failure probability.

### Oucrossing approach

Consider the more general event that random state vector {math}`\mathrm{Z}(\tau)` representative for a given problem, enters the failure domain

```{math}
\mathrm{V} = \left \lbrace \mathrm{Z}(\tau) \mid \mathrm{g}(\mathrm{z}(\tau), \tau)<0,0<\tau<\mathrm{t} \right \rbrace;
```

where {math}`\mathrm{g}(.)` is the limit state function. {math}`\mathrm{Z}(\tau)` may conveniently be separated into three components as:

```{math}
\mathrm{Z}(\tau)^{\mathrm{T}}=\left(\mathrm{R}^{\mathrm{T}}, \mathrm{Q}(\tau)^{\mathrm{T}}, \mathrm{S}(\tau)^{\mathrm{T}}\right)
```

where {math}`R` is a vector of random variables independent of time {math}`\mathrm{t}`, {math}`Q(\tau)` is a slowly varying random vector sequence and {math}`S(\tau)` is a vector of not necessarily stationary but sufficiently mixing random process variables having fast flunctuations as compared to {math}`\mathrm{Q}(\mathrm{t})`.

In the general case where all the different types of random variables {math}`\mathrm{R}, \mathrm{Q}(\tau)` and {math}`\mathrm{S}(\tau)` are present, the failure probability {math}`\mathrm{P}_{\mathrm{f}}(\mathrm{t})` not only must be integrated over the time invariant variables {math}`\mathrm{R}`, but an expectation operation must also be performed over the slowly varying variables {math}`\mathrm{Q}(\tau)` :

```{math}
:label: eqA3.5a
\mathrm{P}_{\mathrm{f}}\left(\mathrm{t}_{\text {min }}, \mathrm{t}_{\text {max }}\right) \approx 1-\mathrm{E}_{\mathrm{R}}\left[\exp \left[\mathrm{nE}_{\mathrm{Q}}\left[1-\exp \left(-\mathrm{E}\left[\mathrm{N}^{+}(\Delta \mathrm{t}, \mathrm{R}, \mathrm{Q})\right)\right]\right]\right]\right]
```

{math}`\Delta \mathrm{t}` is the characteristic fluctuation time of {math}`\mathrm{Q}` and {math}`\mathrm{n}=\left(\mathrm{t}_{\max }-\mathrm{t}_{\min }\right) / \Delta \mathrm{t}`

Or, one step further simplified:

```{math}
:label: eqA3.5b
\mathrm{P}_{\mathrm{f}}\left(\mathrm{t}_{\text {min }}, \mathrm{t}_{\max }\right) \approx 1-\mathrm{E}_{\mathrm{R}}\left[\exp \left[-\mathrm{E}_{\mathrm{Q}}\left[\mathrm{E}\left[\mathrm{N}^{+}\left(\mathrm{t}_{\text {min }}, \mathrm{t}_{\max } ; \mathrm{R}, \mathrm{Q}\right)\right]\right]\right]\right]
```

It should be observed that the expectation operation with respect to {math}`\mathrm{Q}` is performed inside the exponent, whereas the expectation operation with respect to {math}`\mathrm{R}` is performed outside the exponent operator. If the point process of exits is a regular process which can be assumed in most cases, the conditional expectation of the number of exits in the time interval {math}`\left[\mathrm{t}_{\min }, \mathrm{t}_{\max }\right]` can be determined from:

```{math}
:label: eqA3.6
\mathrm{E}\left[\mathrm{N}^{+}\left(\mathrm{t}_{\min }, \mathrm{t}_{\max } ; \mathrm{r}, \mathrm{q}\right)\right]=\int_{\mathrm{t}_{\min }}^{\mathrm{t}_{\max }} \mathrm{v}^{+}(\tau ; \mathrm{r}, \mathrm{q}) \mathrm{d} \tau
```

where {math}`v^{+}(\tau ; \mathrm{p,r.q})` is the outcrossing rate defined by:

```{math}
:label: eqA3.7
v^{+}(\tau ; \mathrm{r}, \mathrm{q})=\lim _{\Delta \rightarrow 0} \frac{1}{\Delta} \mathrm{P}\left(\mathrm{N}^{+}(\{\mathrm{S}(\tau) \in \overline{\mathrm{V}}\} \cap\{\mathrm{S}(\tau+\Delta) \in \mathrm{V}\} \mid \mathrm{r}, \mathrm{q}\right)
```

If the vector {math}`\underline{\mathrm{S}}` consists out of {math}`\mathrm{n}` components {math}`\left(\mathrm{S}_{1}, \ldots . . \mathrm{S}_{n}\right)`, all of rectangular wave type, the following formula can be used:

```{math}
:label: eqA3.8
\left.v^{+}=\sum_{\mathrm{i}=1}^{\mathrm{n}} v_{\mathrm{i}} \mathrm{P}\left\lbrace \left( \mathrm{S}_{1}, \mathrm{~S}_{2}, \ldots \mathrm{S}_{\mathrm{i}}, \ldots \mathrm{S}_{\mathrm{n}}\right) \in \overline{\mathrm{V}}\right) \cap\left(\mathrm{S}_{1}, \mathrm{~S}_{2}, \ldots \mathrm{S}_{\mathrm{i}}^{+}, \ldots \mathrm{S}_{\mathrm{n}}\right) \in \mathrm{V}\right\rbrace
```

where {math}`\mathrm{S}_{\mathrm{i}}^{-}` and {math}`\mathrm{S}_{\mathrm{i}}^{+}` are two realisations of {math}`\mathrm{S}_{\mathrm{i}}`, one before and one after some particular jump and {math}`v_{\mathrm{i}}` is the jump rate of {math}`\mathrm{S}_{\mathrm{i}}`.

### Intermittent processes

Intermittent processes are a practically important generalisation for all types of random processes. Although more general forms are known only the simplest type of intermittancies are discussed below. The renewals of times where the process is "on" follow a Poisson renewal process with rate {math}`\kappa` (or mean interarrival time {math}`\mathrm{l} / \kappa` ). At a renewal the process activates an "on"-state (state "1"). The "off"-states are denoted by "0". The initial durations of "on"-states will have exponential distribution with mean {math}`\mathrm{1} / \mu` independent of the arrival times. However, we will assume that a "on"-time is also finished if a next renewal occurs so that the durations have a truncated distribution. By assuming random initial conditions the probabilities of the "on/off'-states are then determined by

```{math}
:label: eqA3.9
\mathrm{p}_{\text {off }}(\mathrm{t})=\frac{\mu}{\kappa+\mu}+\frac{\kappa-\mu}{\kappa+\mu} \exp [-(\kappa+\mu) \mathrm{t}]
```

```{math}
:label: eqA3.10
\mathrm{p}_{\text {on }}(\mathrm{t})=\frac{\mu}{\kappa+\mu}+\frac{\kappa-\mu}{\kappa+\mu} \exp [-(\kappa+\mu) \mathrm{t}]
```

In general it is assumed that the "on/off"-process is already in its stationary state where the last terms in these equations vanish. In contrast to rectangular wave renewal processes where the duration of the rectangular pulse is exactly until the next renewal and the duration of the rectangular pulse is exponentially distributed with mean {math}`1 / \lambda` for a Poissonian renewal process the "on"-times are now truncated at the next renewal. It is easily shown that the effective duration of the "on"-times then are also exponential but with mean {math}`1 /(\kappa+\mu)`. The so-called interarrival-duration intensity is defined by {math}`\rho=` {math}`\kappa / \mu`. For {math}`\rho=\kappa / \mu \rightarrow \infty` the processes are almost always active. For {math}`\kappa / \mu \rightarrow 0` one obtains spike-like processes.

Intermittancies can also be defined for differentiable processes. If this is a dependent vector process the entire vector process must have a common {math}`\rho`, that is all components of the vector must have the same {math}`\kappa` and {math}`\mu`. Independent differentiable vector processes, however, can have different {math}`\rho` 's.

In the case of a single intermittent process with {math}`\kappa\mathrm{t}_{\mathrm{o}}>1` and {math}`\mu \mathrm{t}_{\mathrm{o}}<<1` the periods where the intermittent load are present can conveniently be put together. The failure probability is then approximately given by:

```{math}
:label: eqA3.11
\mathrm{P}_{\mathrm{f}}\left(\mathrm{t}_{\min }, \mathrm{t}_{\max }\right)=v_{\text {on }} \mathrm{T}+v_{\text {off }}\left(\mathrm{t}_{\mathrm{o}}-\mathrm{T}\right)
```

where {math}`\mathrm{T}=\kappa \mathrm{t}_{\mathrm{o}} / \mu=` the total expected time that the intermittent load is active and {math}`\mathrm{t}_{\mathrm{o}}=\mathrm{t}_{\max }-\mathrm{t}_{\min } ; v_{\text {on }}` and {math}`v_{\text {off }}` are the failure rates for present and absent intermittent load respectively.

In the case of two mostly absent uncorrelated intermittent loads, the same approximation principle can be applied, leading to:

```{math}
:label: eqA3.12
\begin{aligned}
\mathrm{P}_{\mathrm{f}}\left(\mathrm{t}_{\text {min }}, \mathrm{t}_{\text {max }}\right)= & \left(\frac{\kappa_{1}}{\mu_{1}}\right)\left(\frac{\kappa_{2}}{\mu_{2}}\right) v_{\text {on,on }} \mathrm{t}_{\mathrm{o}}+ \\
& \left(\frac{\kappa_{1}}{\mu_{1}}\right)\left(1-\frac{\kappa_{2}}{\mu_{2}}\right) v_{\text {on, off }} \mathrm{t}_{\mathrm{o}}+ \\
& \left(1-\frac{\kappa_{1}}{\mu_{1}}\right)\left(\frac{\kappa_{2}}{\mu_{2}}\right) v_{\text {off ,on }} \mathrm{t}_{\mathrm{o}}+ \\
& \left(1-\frac{\kappa_{1}}{\mu_{1}}\right)\left(1-\frac{\kappa_{2}}{\mu_{2}}\right) v_{\text {off ,off }} \mathrm{t}_{\mathrm{o}}
\end{aligned}
```

where {math}`v_{\mathrm{on, on}}` is the failure rate for both intermittent loads present, etc.



