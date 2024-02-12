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
loading, involved although they are variable actions.)


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

One can in many cases distinguish between two kinds of variables (constituents) $F_0$ and $W$ describing
an action $F$ (see also part 1, [Basis of Design](../part-01/introduction.md)).

```{math}
:label: eq_action_F
F = \varphi (F_O, W)
```

- $F_O$ is a basic action variable which is directly associated with the event causing the action and
which should be defined so that it is, as far as possible, independent of the structure. For
example, for snow load $F_O$ is the snow load on ground, on a flat horizontal surface

- $W$ is a kind of conversion factor or model parameter appearing in the transformation from the
basic action to the action $F$ which affects the particular structure. $W$ may depend on the form and size of the structure etc. For the snow load example $W$  is the factor which transforms the snow load on ground to the snow load on roof and which depends on the roof slope, the type of roof surface etc.

- $\varphi$ is a suitable function, often a simple product.

The time variability is normally included in $F_O$, whereas $W$ can often be considered as time
independent. A systematic part of the space variability of an action is in most cases included in $W$,
whereas a possible random part may be included in $F_O$ or in $W$. Eq. {eq}`eq_action_F` should be regarded as a
schematic equation. For one action there may be several variables $F_O$ and several variables $W$.

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

To describe time depended loads, one needs the probability distribution for the "arbitrary point in time values" and a description of the variations in time. Some typical process models are (see figure {numref}`fig-Various-types-of-load-models`):

1. Continuous and differentiable process

2. Random sequence

3. Point pulse process with random intervals

4. Rectangular wave process with random intervals

5. Rectangular wave process with equidistant intervals $\Delta$

If the load intensities in subsequent time intervals of model (e) are independent, the model is referred to as a **FBC model** (Ferry Borges Castanheta model).

In many applications a combination of models is used, e.g. for wind the long term average is often modelled as an FBC model while the short term gust process is a continuous Gaussian process. Such models are referred to as **hierarchical models** (see Part 1, Basis of Design, [Section 5.4](section-5.4)). Each term in such a model describes a specific and independent part of the time variability. For a number of further definitions and notions, reference is made to [Annex 1](annex-1).

```{figure} ../part-02/images/Various-types-of-load-models.jpg 
:name: fig-Various-types-of-load-models

Various types of load models
```

### Distribution of extremes for single processes

At the design the main interest is normally directed to the maximum value of the load in some reference period of time $t_{0}$. A quite general and useful upperbound formula to calculate the distribution of the maximum is given by:

```{math}
:label: eq2.0.4.1
F_{\max F}(a) \cong \exp \left[-t_{0}~v^{+}(a)\right]
```

The upcrossing frequency $v^{+}(a)$ is given by:

```{math}
:label: eq2.0.4.2
v^{+} (a)= P \left \lbrace F_{t} < a \text{ and } F_{t+dt}>a\right\rbrace / dt
```

For the FBC model $v^{+}(a)$ is simply given by: 

```{math}
:label: eq2.0.4.3
v^{+}(a)=\left(1-F_{F}(a)\right) F_{F}(a) / \Delta t \cong\left(1-F_{F}(a)\right) / \Delta t 
```

And for a continuous Gaussian process:

```{math}
:label: eq2.0.4.4
v^{+}(a)=\frac{1}{2 \pi} \sqrt{-\rho^{\prime \prime}(0)} \exp \left(-\beta^{2} / 2\right)
```

where $\beta=(a-\mu(F)) / F(F)$ and $\rho=$ the correlation function.

### Distribution of extremes for hierarchical processes

Consider the case that the load model contains slowly and rapidly varying parts, as well as random variables that are constant in time (see {numref}`fig-Hierarchical-model-for-time-dependent-loads`).

```{math}
:label: eq2.0.4.5
F=R+Q+S
```

$R =$ random variables, constant in time

$Q =$ slow rectangular process with mean renewal rate $\lambda$

$S =$ fast varying process

In that case the following expression (see [Annex 3](annex-3), {eq}`eqA3.5a`) can be used:

```{math}
:label: eq2.0.4.6
F_{\max F}(a)=E_{R}\left[\exp \left[\lambda t_{0}\left[1-E_{Q} \exp \left(-\Delta t~v_{s}^{+}(a \mid R Q)\right)\right]\right]\right]
```

$v_{s}^{+}(a \mid RQ)=$ upcrossing rate of level "$a$" for process $S$, conditional upon $R$ and $Q$ 

$\Delta t=1 / \lambda=$ time interval for the rectangular process $Q$

$E_{R}$ and $E_{Q}$ denote the expectation operator over all variables $R$ and $Q$ respectively.

```{figure} ../part-02/images/Hierarchical-model-for-time-dependent-loads.jpg 
:name: fig-Hierarchical-model-for-time-dependent-loads

Hierarchical model for time dependent loads
```

## Models for Spatial variability

(section-2.0.5.1)=
### Hierarchical model

As an example for the spatial modelling of actions using a hierarchical model consider the live load in an office building:

```{math}
:label: eq2.0.5.1
F=m+\Delta F_{1}+\Delta F_{2}+\Delta F_{3}(x, y)
```

where:

$m$ is a general mean value for the whole population

$\Delta F_{1}$ is a stochastic variable which describes the variation **between** the load on different floors. The distribution function for $\Delta F_{1}$ has the mean value zero and the standard deviation $\sigma_{1}$

$\Delta F_{2}$ is a stochastic variable which describes the variation **between** the load in rooms on the same floor but with different floor areas. The distribution function for $\Delta F_{2}$ has the mean value zero and the standard deviation $\sigma_{2}$

$\Delta F_{3}$ is a random field which describes the spatial variability of the load **within** a room.

The total variability of the samples taken from the total population is described by $\Delta F_{1}+\Delta F_{2}+\Delta F_{3}$. The variability **within** the subpopulation of floors is described by $\Delta F_{2}+\Delta F_{3}$.

### Equivalent uniformly distributed load (EUDL)

Consider a simple hierarchical distribution load model given by:

```{math}
:label: eq2.5.0.2
q(x, y)=q_{o}+q_{loc}(x, y)
```

$q_{o}=$ the variability between the various structures or structural elements

$q_{\text {loc }}=$ the small scale or point to point fluctuation.

In many cases the random field $q$ is replaced by a so called Equivalent Uniformly Distributed Load (EUDL). This load is defined as:

```{math}
:label: eq2.5.0.3
q_{\text {EUDL }}(t)=\frac{\int q(x, y, t) i(xy) dA}{\int i(xy) dA}
```

when $i(x, y)$ is the influence function for some specific load effect (e.g. the midspan bending moment).

For given statistical properties of the load field $q(x, y)$ the mean and standard deviation of $q_{EUDL}$ can be evaluated. For a homogeneous field, that is a random field where the statistical properties of $q(x, y)$ do not depend on the location, we give here the resulting formulas:

```{math}
:label: eq2.5.0.4
\mu(q_{EUDL})=\mu\left(q_{o}\right)
```

```{math}
:label: eq2.5.0.5
\sigma^{2}\left(q_{EUDL}\right)=\sigma^{2}\left(q_{o}\right)+\sigma^{2}\left(q_{loc}\right) \int\int \int\int  i(x, y) i(\xi, \eta) \rho(d) dxdyd \xi d \eta~/\left[\iint i(x, y) dxdy\right]^{2}
```

Here $\rho(d)$ is the correlation function describing the correlation between the small scale load $q_{loc}$, on the two point $(x, y)$ and $(\xi, \eta)$. This function may be of the form:

```{math}
:label: eq2.5.0.6
\rho(\Delta r)=\exp \left\lbrace-\Delta r^{2} / d_{c}^{2}\right\rbrace
```

with $\Delta r^{2}=(x-\xi)^{2}+(y-\eta)^{2}, \Delta r$ being the distance between the two points, and $d_{c}$ some scale distance. The correlation function tends to zero for distances $\Delta r$ much larger than $d_{c}$.

If the field can be schematised as an FBC-field, the formula for $\sigma^{2}\left(q_{EUDL}\right)$ can be simplified to:

```{math}
:label: eq2.5.0.7
\sigma^{2}\left(q_{EUDL}\right)=\sigma^{2}\left(q_{i}\right)+\sigma^{2}\left(q_{loc}\right) \kappa A_{o} / A
```

Here $A_{o}$ is the reference area of the FBC-field and A stands for the total area under consideration, the so called tributary area. The formula is valid only for $A>A_{0}$.

The parameter $\kappa$ is a factor depending on the shape of the influence line $i(x, y)$. Values are presented in {numref}`fig-Random-fields-and-corresponding-kappa-values`. The figure $\kappa=1$ corresponds to a constant value of $i(x, y)$. 

```{figure} ../part-02/images/Random-fields-and-corresponding-kappa-values.jpg 
:name: fig-Random-fields-and-corresponding-kappa-values

Random fields and corresponding $\kappa$-values
```

## Interactions and correlations between actions

For describing dependencies between various actions it is useful to distinguish between:

- actions of the same nature

- actions of different nature

Actions of the same nature are for instance floor loads on different floors in one building or the wind loads on the front and back wall. The combination of wind and snow is a typical example of the combination of action of a differente type. Note that sometimes it may be less clear: it may be difficult to decide whether floor loads of a completely different type in one building (say office loads and storage loads) are loads of the same nature or a different nature.

If the actions are of the *same nature*, one might better consider them as components of one action, The various components are normally described by similar probabilistic models. The basic question is then to model the statistical dependency between the processes. In general this is a purely mathematical problem. Details of the mathematical description of the dependencies depend on the nature of the physical relationship and the nature of the processes themselves. One possibility is to construct a hierarchical model as has been explained in [section 2.0.5.1](section-2.0.5.1). For two stationary continuous Gaussian processes $x(t)$ and $y(t)$ the correlation alternatively may be described by the cross correlation function $R_{xy}(\tau)$ or alternatively by the cross spectrum $S_{xy}(\omega)$ (see [Annex 1](annex-1)). For pulse type processes we may have to distinguish between the correlation in amplitude, arrival time and duration. Floor loads in multi-storey buildings are a good example where all three correlations are of importance.

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

From a mathematical modelling point of view the load on a structure is a joint set $F(t)$ of time varying random fields. This set of loads give a rectorial load effect $E(t)$ in a given cross section or point of the structure at time $t$ as a function of $F(t)$ (i.e. a random process). In the scalar case we have:

```{math}
:label: eq2.0.7.1
E(t)=c_{1} ~F_{1}(t)+c_{2} ~F_{2}(t)+. .
```

The reliability problem related to the considered point is to evaluate the probability $P_{f}$ that $F_{\max }(t)~E~V$ for all future time $V$ is the nonfailure domain defined by the strength properties at the considered point and limit state.

The load combination problem is to formulate a reasonably simple but for the considered engineering purpose sufficiently realistic mathematical model that defines $\mathbf{F}(t)$. The needed level of detailed modelling of $\mathbf{F}(t)$ depends on the filtering effect of the function that maps $\mathbf{F}(t)$ into the load effect $E(t)$. This filtering effect is judged under due consideration of the sensitivity of the probability $P_{f}$ to the detailing of the models. The sensitivity question is tied to the last part of the load combination problem which is actually to compute the value of $P_{f}$. Thus, to be operational, the modelling of $\mathbf{F}(t)$ should be simple enough to enable at least a computer simulation of the scalar process $E(t)$ to an extent that allows an estimation of $P_{f}$.

First the relevant set of different action types is identified. This identification defines the number of elements in the set $\mathbf{F}(t)$ and the subdivision of $\mathbf{F}(t)$ into stochastically independent subsets. The modelling is next concentrated on each of these subsets with dependent components.

The mathematical difficulty to solve probabilities for outcrossing rates of processes of the type {eq}`eq2.0.7.1` is the possible very different nature of the various contributors $F_{i}$. Each of these processes may be of a completely different nature, including all kinds of continuos and intermittent processes. Numerical solutions will often prove to be necessary, but also analytical solutions may prove to be very helpful. Reference is made to [Annex 3](annex-3) and to the literature.

(annex-1)=
## ANNEX 1 - DEFINITIONS

### Covariance function

The covariance function $r\left(t_{1}, t_{2}\right)$ is defined by:

```{math}
\begin{aligned}
& r\left(t_{1}, t_{2}\right)=E\left[\left(F(t=1)-m_{1}\right)\left(F\left(t_{2}\right)-m_{2}\right)\right] \\
& m_{1}=E\left[F\left(t_{1}\right)\right] \quad \quad \quad \quad  m_{2}=E\left[F\left(t_{2}\right)\right]
\end{aligned}
```

### Stationary processes

The process is defined for $-\infty<t<\infty$. If, for all values $t_{1}$ and for all values $\tau$, chosen such that $0 \leq t_{i} \leq t_{o}$ to and $0 \leq t_{i}+\tau \leq t_{o}$, the stochastic variable $x~\left( t_{i} +\tau\right)$ has the same distribution function as the stochastic variable $x\left(t_{i}\right)$ the stochastic process $x(t)$ is stationary.

If the mean value function $m(t)$ is constant and the covariance function $r\left(t_{1}, t_{2}\right)$ depends solely on the difference $\tau=\left(t_{2}-t_{1}\right)$ the process is sold to be wide-sense stationary.

Thus the covariance function for a stationary or a wide sense stationary process may be written as:

```{math}
r(\tau)=E[(F(t+\tau)-m)(F(t)-m)]
```

The concept of stationary applied to action processes should in most cases be interpreted as widesense stationary.

### Ergodic processes

A process is ergodic if averaging over several realisations and averaging with respect to time (or another index parameter) give the same result.

For ergodic processes a relation between the point-in-time value distribution function $F$ and the excursion time $t$ is determined for a chosen reference period $t_{o}$, by

```{math}
1-F_{F}(F)=t / t_{o}
```

### The correlation function

The correlation function for a stationary process is:

```{math}
\rho(\tau)=\frac{r(\tau)}{r(0)}
```

For ergodic processes $\rho(\tau=\infty)=0$

### Spectrum

A stationary stochastic process may be characterised with aid of a spectrum:

```{math}
S(n)=\int_{-\infty}^{\infty} e^{-i 2 \pi n \tau} r(\tau) d \tau
```

$S(n)$ may be regarded as a measure of how the process is built up of components with different frequencies. The total variance of the process is:

```{math}
\operatorname{Var} Q=2 \int_{0}^{\infty} S(n) d n
```

### Gaussian processes

A stochastic process $S(t)$ is a Gaussian process if the multidimensional probability distribution functions for all the stochastic variables $S\left(t_{i}\right)$ are Gaussian. The stochastic properties of a Gaussian process is completely determined by the mean value and the covariance function or by the spectrum.

### Scalar Nataf Processes

A special but important class of non-Gaussian, scalar and differentiable processes are built by a memoryless transformation from a normal process, i.e.

```{math}
S(t)=h(U(t))
```

where $U(t)$ is a standard normal process and $h(u)$ is an arbitrary function. For $S(t)$ any admissible (unimodal) distribution function can be chosen thus defining a certain class of functions $h(u)$. In addition the autocorrelation function $\rho_{s}\left(t_{1}, t_{2}\right)$ has to be specific. However, there are some restrictions on the type of autocorrelation function.

### Scalar Hermite Processes

The Hermite process is a special case of the Nataf process. All marginal distribution must be of Hermite type. For this process the solution of the integral equation occurring for the autocorrelation function of the equivalent (or better generating) standard normal process is analytic. The standard Hermite process has the representation, i.e. a special case of the function $h(u)$ 

```{math}
S(t)=\kappa\left(U(t)+\widetilde{h}_{3, i}\left(U(t)^{2}-1\right)+\widetilde{h}\left(U(t)^{3}-3 U(t)\right)\right)
```

For the coefficients depending on the first four moments of the marginal distribution of the non-normal process. In addition, the Hermite process requires specification of the autocorrelation function of $S(t)$. Again, there are certain restrictions on the moments of the marginal distributions as well as on the autocorrelation function.

### Scalar Rectangular Wave Renewal Processes

Scalar rectangular wave renewal processes are useful models for processes changing their amplitude at random renewal points in a random fashion. A scalar rectangular wave renewal process is characterised by the jump rate $\lambda$, and the distribution function of the amplitude. The renewals occur independently of each other. No specific distribution is assigned to the interarrival times. Therefore, the renewal process characterised only by a jump rate captures only long term statistics. The mean duration of pulses is asymptotically equal to $1 / \lambda$.. For the special case of a Poisson rectangular wave process the interarrival times and so the durations of the pulses are exponentially distributed with parameter $1 / \lambda$.. In the special case of a Ferry Borges-Castanheta process the durations are constant and the repetition number $r=\left(t_{2}-t_{1}\right) / \Delta$ with $\Delta$ the duration of pulses is equal to $\lambda\left(t_{2}-t_{1}\right)$. Also, the sequence of amplitudes is an independent sequence. The jump rate can be a function of time as well as the parameters of the distribution function of the amplitudes.

It is assumed that rectangular wave processes jump from a random value $S(t)$ to a new value $S^{+}(t+\delta)$ with $\delta \rightarrow$ at a renewal without returning to zero. Rectangular wave renewal processes must be regular processes, i.e. the occurrence of any two or more renewals in a small time interval must be negligible (of o-order). Non-stationary rectangular wave renewal processes are processes which have either time-dependent parameters of the amplitude distributions and/or time-dependent jump rates.

### Random fields

A random field may be regarded as a one-, two- or three-dimensional stochastic process. The time $t$ is substituted by the space co-ordinates $x, y, z$.

For the two-dimensional case the covariance function is written (for a stationary random field)

```{math}
r\left(d_{x}, d_{y}\right)=E\left[\left(F\left(x+d_{x}, y+d_{y}\right)-m\right)(F(x, y)-m)\right]
```

The concepts of stationary, ergodicy etc. are in principle the same as for the stochastic processes.

### Vector processes

Two stationary Gaussian processes F1 and F2 are statistically completely described by their mean values, auto-spectra and the cross spectrum. The latter is defined by:

```{math}
\begin{aligned}
& r_{12}(\tau)=E\left[\left(F_{1}(t+\tau)-m_{1}\right)\left(F_{2}(t)-m_{2}\right)\right] \\
& S_{12}(n)=\int_{-\infty}^{\infty} e^{-i 2 \pi n \tau} r_{12}(\tau) d \tau
\end{aligned}
```

A vector of $n$ stationary Gaussian processes can be described by $n$ mean values, $n$ auto-spectra and $n(n-1)$ cross spectra. Note that $S_{i j}$ is the complex conjugate of $S_{j i}$.

(annex-2)=
## ANNEX 2 - DISTRIBUTIONS FUNCTIONS

```{table} 
:name: tbl-annex-2
| Distribution type | Parameters | Moments |
| --- | --- | --- |
| **Rectangular**<br>$\mathrm{a} \leq \mathrm{x} \leq \mathrm{b}$ <br>  $\mathrm{f}_\mathrm{x} (\mathrm{x})=\frac{1}{\mathrm{b}-\mathrm{a}}$ | $1 = \mathrm{a}$<br>$2 = \mathrm{b}$ | $\mathrm{m} = \frac{\mathrm{a} + \mathrm{b}}{2}$<br>$\mathrm{s} = \frac{\mathrm{b} - \mathrm{a}}{\sqrt{12}}$ |
| **Normal**<br>$\sigma > 0$<br> $\mathrm{f}_\mathrm{x} (\mathrm{x})=\frac{1}{\sigma \sqrt{2\pi}}\mathrm{exp}\left(-\frac{1}{2}\left(\frac{\mathrm{x}-\mu}{\sigma}\right)^2\right)$ | $1 = \mu$ <br> $2 = \sigma$ | $\mathrm{m} = \mu$<br>$\mathrm{s} = \sigma$ |
| **Lognormal**<br>$\mathrm{x} > 0$, $\zeta > 0$ <br> $\mathrm{f}_\mathrm{x} (\mathrm{x})=\frac{1}{\mathrm{x} \zeta \sqrt{2\pi}}\mathrm{exp}\left(-\frac{1}{2}\left(\frac{\ln\mathrm{x}-\lambda}{\zeta}\right)^2\right)$ | $1 = \lambda$ <br> $2 = \zeta$ | $\mathrm{m} = \mathrm{exp} \left(\lambda+\frac{\zeta^2}{2}\right)$ <br> $\mathrm{s}= \mathrm{exp} \left(\lambda+\frac{\zeta^2}{2}\right) \sqrt{\mathrm{exp}\left(\zeta^2\right)-1}$ | 
| **Shifted Lognormal**<br>$\mathrm{x} > \varepsilon$, $\zeta > 0$ <br> $\mathrm{f}_\mathrm{x} (\mathrm{x})=\frac{1}{(\mathrm{x} - \varepsilon) \zeta \sqrt{2\pi}}\mathrm{exp}\left(-\frac{1}{2}\left(\frac{\mathrm{ln}(\mathrm{x}-\varepsilon)-\lambda}{\zeta}\right)^2\right)$ | $1 = \lambda$<br>$2 = \zeta$<br>$3 = \varepsilon$ | $\mathrm{m} = \varepsilon + \mathrm{exp} \left(\lambda+\frac{\zeta^2}{2}\right) + \varepsilon$<br>$\mathrm{s}= \mathrm{exp} \left(\lambda+\frac{\zeta^2}{2}\right) \sqrt{\mathrm{exp}\left(\zeta^2\right)-1}$ |
| **Shifted Exponential**<br>$\mathrm{x} \geq \varepsilon$, $\lambda > 0$ <br> $\mathrm{f}_\mathrm{x} (\mathrm{x})= \lambda~\mathrm{exp}\left(-\lambda(\mathrm{x}-\varepsilon)\right)$  | $1 = \lambda$<br>$2 = \varepsilon$ | $\mathrm{m}=\frac{1}{\lambda} + \varepsilon$ <br> $\mathrm{s}=\frac{1}{\lambda}$  |
| **Shifted Gamma**<br>$\mathrm{x} \geq 0$, $\mathrm{b} > 0$, $\mathrm{p} > 0$ <br> $\mathrm{f}_\mathrm{x} (\mathrm{x})= \frac{\mathrm{b}^\mathrm{p}}{\Gamma (\mathrm{p})}\mathrm{exp} \left(-b(\mathrm{x}-\varepsilon)\right)(\mathrm{x}-\varepsilon)^{\mathrm{p}-1}$ | $1 = \mathrm{p}$<br>$2 = \mathrm{b}$<br>$3 = \varepsilon$ | $\mathrm{m} = \frac{\mathrm{p}}{\mathrm{b}} + \varepsilon$<br>$\mathrm{s} = \frac{\sqrt{\mathrm{p}}}{\mathrm{b}}$ |
| **Beta**<br>$\mathrm{a} \leq \mathrm{x} \leq \mathrm{b},~~ \mathrm{r}$, $\mathrm{t} \geq 1$ <br> $\mathrm{f}_\mathrm{x} (\mathrm{x})= \frac{\left(\mathrm{x}-\mathrm{a}\right)^{\mathrm{r}-1} \left(\mathrm{b}-\mathrm{x} \right)^{\mathrm{t}-1}}{\left(\mathrm{b}-\mathrm{a}\right)^{\mathrm{r+t-1}} \mathrm{B} \left(\mathrm{r,t}\right)}$ | $1 = \mathrm{a}$<br>$2 = \mathrm{b}$<br>$3 = \mathrm{r}$<br>$4 = \mathrm{t}$ | $\mathrm{m} = \mathrm{a} + \left(\mathrm{b} - \mathrm{a}\right) \frac{\mathrm{r}}{\mathrm{r+t}}$ <br> $\mathrm{s} = \frac{\mathrm{b - a}}{\mathrm{r+t}} \sqrt{\frac{\mathrm{rt}}{\mathrm{r+t+1}}} $ |
| **Gumbel (Maximum)**<br>$−\infty < \mathrm{x} < +\infty,~\alpha > 0$ <br> $\mathrm{f}_\mathrm{x} (\mathrm{x})=\alpha~\mathrm{exp}\left(-\alpha(\mathrm{x-u}) - \mathrm{exp}\left(-\alpha(\mathrm{x-u})\right)\right)$  | $1 = \mathrm{u}$<br>$2 = \alpha$ | $\mathrm{m} = \mathrm{u} + \frac{0.577216}{\alpha}$<br>$\mathrm{s} = \frac{\pi}{\alpha \sqrt{6}}$ |
| **Frechet (Maximum)**<br>$ \varepsilon \leq \mathrm{x} < +\infty,~~\mathrm{u, k} > 0$ <br> $\mathrm{f}_\mathrm{x} (\mathrm{x})= \frac{\mathrm{k}}{\mathrm{u}-\varepsilon} \left(\frac{\mathrm{x} - \varepsilon}{\mathrm{u} - \varepsilon}\right)^{\mathrm{-k-1}} \mathrm{exp} \left(- \left(\frac{\mathrm{x} - \varepsilon}{\mathrm{u} - \varepsilon}\right)^{\mathrm{-k}} \right)$ | $1 = \mathrm{u}$<br>$2 = \mathrm{k}$<br>$3 = \varepsilon$ | $\mathrm{m} = \varepsilon + (\mathrm{u} - \varepsilon) \Gamma \left(1 - \frac{1}{\mathrm{k}}\right)$ <br> $\mathrm{s} = (\mathrm{u} - \varepsilon) \sqrt{\Gamma \left(1 - \frac{2}{\mathrm{k}} \right) - \Gamma^2 \left(1 - \frac{1}{\mathrm{k}}\right)}$ |
| **Weibull (Maximum)**<br>$\varepsilon \leq \mathrm{x} < +\infty,~~ \mathrm{u, k} > 0$ <br> $\mathrm{f}_\mathrm{x} (\mathrm{x})= \frac{\mathrm{k}}{\mathrm{u}-\varepsilon} \left(\frac{\mathrm{x} - \varepsilon}{\mathrm{u} - \varepsilon}\right)^{\mathrm{-k-1}} \mathrm{exp} \left(- \left(\frac{\mathrm{x} - \varepsilon}{\mathrm{u} - \varepsilon}\right)^{\mathrm{-k}} \right)$ | $1 = \mathrm{u}$<br>$2 = \mathrm{k}$<br>$3 = \varepsilon$ | $\mathrm{m} = \varepsilon + (\mathrm{u} - \varepsilon) \Gamma \left(1 + \frac{1}{\mathrm{k}}\right)$ <br> $\mathrm{s} = (\mathrm{u} - \varepsilon) \sqrt{\Gamma \left(1 + \frac{2}{\mathrm{k}} \right) - \Gamma^2 \left(1 + \frac{1}{\mathrm{k}}\right)}$ |
```

(annex-3)=
## ANNEX 3 - MATHEMATICAL COMBINATION TECHNIQUES

### Combination of two rectangular processes (Ferry Borges-Castanheta model)

Consider the case that two actions $Q_{1}(t)$ and $Q_{2}(t)$ are to be combined. Assume that these actions can be described as rectangular or sqaure wave models ({numref}`fig-square-wave-processes-for-two-actions`). The following assumptions are made about the processes:

- $Q_{1}(t)$ and $Q_{2}(t)$ are stationary ergodic processes
- All intervals $`\tau_{1}$ are equal; all intervals $\tau_{2}$ are equal and $\tau_{1} \geq \tau_{2}$
- $Q_{1}$ and $Q_{2}$ are constant during each interval $\tau_{1}$ and $\tau_{2}$ respectively
- The values of $Q_{1}$ for the different intervals are mutually independent; same for $Q_{2}$
- $Q_{1}$ and $Q_{2}$ are independent

```{figure} ../part-02/images/square-wave-processes-for-two-actions.jpg 
:name: fig-square-wave-processes-for-two-actions

Square wave processes for $Q_{1}(t)$ and $Q_{2}(t)$
```

Define $Q_{2 c}$ as the maximum value of $Q_{2}$ occurring during the interval $\tau_{1}$ with the probability distribution function:

```{math}
:label: eqA3.1
F_{Q 2 C}(Q)=\left[F_{Q^{*}}(Q)\right]^{\tau 2 / \tau 1}
```

$F_{Q}{ }^{*}=$ the arbitrary point in time distribution for $Q_{2}$

Assume a linear relationship between the actions effect $E$ and the actions:

```{math}
:label: eqA3.2
E=c_{1} Q_{1}+c_{2} Q_{2}
```

The maximum action effect $E_{\max }$ from $Q_{1}$ and $Q_{2}$ during the reference period $t_{O}$ can then be written as:

```{math}
:label: eqA3.3
E_{\max }=\max \left\lbracec_{1} Q_{1}+c_{2} Q_{2 c}\right\rbrace
```

The maximum should be taken over all intervals $\tau_{1}$ within the reference period $t_{o}$.

As an approximation, the resulting action effects could be calculated as the maximum of the following two combinations (Turkstra's rule):

- $\quad E\left\lbrace Q_{1 \max }, Q_{2 c}\right\rbrace \quad$ if $Q_{1}$ is considered as the dominating action
- $\quad E\left\lbrace Q_{2 \max }, Q_{1 c}\right\rbrace \quad$ if $Q_{2}$ is considered as the dominating action

Written as a formula for the case $E=c_{1} Q_{1}+c_{2} Q_{2}$

```{math}
:label: eqA3.4
E_{\max }=\max \left\lbrace c_{1} Q_{\max }+c_{2} Q_{2 c}~; c_{1} Q_{1 c}+c_{2} Q_{2, \max }\right\rbrace
```

It should be noted that the Turkstra Rule gives a lower bound for the failure probability.

### Oucrossing approach

Consider the more general event that random state vector $Z(\tau)$ representative for a given problem, enters the failure domain

```{math}
V = \left \lbrace Z(\tau) \mid g(z(\tau), \tau)<0,0<\tau<t \right \rbrace;
```

where $g(.)$ is the limit state function. $Z(\tau)$ may conveniently be separated into three components as:

```{math}
Z(\tau)^{T}=\left(R^{T}, Q(\tau)^{T}, S(\tau)^{T}\right)
```

where $R$ is a vector of random variables independent of time $t$, $Q(\tau)$ is a slowly varying random vector sequence and $S(\tau)$ is a vector of not necessarily stationary but sufficiently mixing random process variables having fast flunctuations as compared to $Q(t)$.

In the general case where all the different types of random variables $R, Q(\tau)$ and $S(\tau)$ are present, the failure probability $P_{f}(t)$ not only must be integrated over the time invariant variables $R$, but an expectation operation must also be performed over the slowly varying variables $Q(\tau)$ :

```{math}
:label: eqA3.5a
P_{f}\left(t_{\text {min }}, t_{\text {max }}\right) \approx 1-E_{R}\left[\exp \left[nE_{Q}\left[1-\exp \left(-E\left[N^{+}(\Delta t, R, Q)\right)\right]\right]\right]\right]
```

$\Delta t$ is the characteristic fluctuation time of $Q$ and $n=\left(t_{\max }-t_{\min }\right) / \Delta t$

Or, one step further simplified:

```{math}
:label: eqA3.5b
P_{f}\left(t_{\text {min }}, t_{\max }\right) \approx 1-E_{R}\left[\exp \left[-E_{Q}\left[E\left[N^{+}\left(t_{\text {min }}, t_{\max } ; R, Q\right)\right]\right]\right]\right]
```

It should be observed that the expectation operation with respect to $Q$ is performed inside the exponent, whereas the expectation operation with respect to $R$ is performed outside the exponent operator. If the point process of exits is a regular process which can be assumed in most cases, the conditional expectation of the number of exits in the time interval $\left[t_{\min }, t_{\max }\right]$ can be determined from:

```{math}
:label: eqA3.6
E\left[N^{+}\left(t_{\min }, t_{\max } ; r, q\right)\right]=\int_{t_{\min }}^{t_{\max }} v^{+}(\tau ; r, q) d \tau
```

where $v^{+}(\tau ; p,r.q)$ is the outcrossing rate defined by:

```{math}
:label: eqA3.7
v^{+}(\tau ; r, q)=\lim _{\Delta \rightarrow 0} \frac{1}{\Delta} P\left(N^{+}(\{S(\tau) \in \overline{V}\} \cap\{S(\tau+\Delta) \in V\} \mid r, q\right)
```

If the vector $\underline{S}$ consists out of $n$ components $\left(S_{1}, \ldots . . S_{n}\right)$, all of rectangular wave type, the following formula can be used:

```{math}
:label: eqA3.8
\left.v^{+}=\sum_{i=1}^{n} v_{i} P\left\lbrace \left( S_{1}, ~S_{2}, \ldots S_{i}, \ldots S_{n}\right) \in \overline{V}\right) \cap\left(S_{1}, ~S_{2}, \ldots S_{i}^{+}, \ldots S_{n}\right) \in V\right\rbrace
```

where $S_{i}^{-}$ and $S_{i}^{+}$ are two realisations of $S_{i}$, one before and one after some particular jump and $v_{i}$ is the jump rate of $S_{i}$.

### Intermittent processes

Intermittent processes are a practically important generalisation for all types of random processes. Although more general forms are known only the simplest type of intermittancies are discussed below. The renewals of times where the process is "on" follow a Poisson renewal process with rate $\kappa$ (or mean interarrival time $l / \kappa$ ). At a renewal the process activates an "on"-state (state "1"). The "off"-states are denoted by "0". The initial durations of "on"-states will have exponential distribution with mean $1 / \mu$ independent of the arrival times. However, we will assume that a "on"-time is also finished if a next renewal occurs so that the durations have a truncated distribution. By assuming random initial conditions the probabilities of the "on/off'-states are then determined by

```{math}
:label: eqA3.9
p_{\text {off }}(t)=\frac{\mu}{\kappa+\mu}+\frac{\kappa-\mu}{\kappa+\mu} \exp [-(\kappa+\mu) t]
```

```{math}
:label: eqA3.10
p_{\text {on }}(t)=\frac{\mu}{\kappa+\mu}+\frac{\kappa-\mu}{\kappa+\mu} \exp [-(\kappa+\mu) t]
```

In general it is assumed that the "on/off"-process is already in its stationary state where the last terms in these equations vanish. In contrast to rectangular wave renewal processes where the duration of the rectangular pulse is exactly until the next renewal and the duration of the rectangular pulse is exponentially distributed with mean $1 / \lambda$ for a Poissonian renewal process the "on"-times are now truncated at the next renewal. It is easily shown that the effective duration of the "on"-times then are also exponential but with mean $`1 /(\kappa+\mu)$. The so-called interarrival-duration intensity is defined by $\rho=$ $\kappa / \mu$. For $\rho=\kappa / \mu \rightarrow \infty$ the processes are almost always active. For $\kappa / \mu \rightarrow 0$ one obtains spike-like processes.

Intermittancies can also be defined for differentiable processes. If this is a dependent vector process the entire vector process must have a common $\rho$, that is all components of the vector must have the same $\kappa$ and $\mu$. Independent differentiable vector processes, however, can have different $\rho$ 's.

In the case of a single intermittent process with $\kappa t_{o}>1$ and $\mu t_{o}<<1$ the periods where the intermittent load are present can conveniently be put together. The failure probability is then approximately given by:

```{math}
:label: eqA3.11
P_{f}\left(t_{\min }, t_{\max }\right)=v_{\text {on }} T+v_{\text {off }}\left(t_{o}-T\right)
```

where $T=\kappa t_{o} / \mu=$ the total expected time that the intermittent load is active and $t_{o}=t_{\max }-t_{\min } ; v_{\text {on }}$ and $v_{\text {off }}$ are the failure rates for present and absent intermittent load respectively.

In the case of two mostly absent uncorrelated intermittent loads, the same approximation principle can be applied, leading to:

```{math}
:label: eqA3.12
\begin{aligned}
P_{f}\left(t_{\text {min }}, t_{\text {max }}\right)= & \left(\frac{\kappa_{1}}{\mu_{1}}\right)\left(\frac{\kappa_{2}}{\mu_{2}}\right) v_{\text {on,on }} t_{o}+ \\
& \left(\frac{\kappa_{1}}{\mu_{1}}\right)\left(1-\frac{\kappa_{2}}{\mu_{2}}\right) v_{\text {on, off }} t_{o}+ \\
& \left(1-\frac{\kappa_{1}}{\mu_{1}}\right)\left(\frac{\kappa_{2}}{\mu_{2}}\right) v_{\text {off ,on }} t_{o}+ \\
& \left(1-\frac{\kappa_{1}}{\mu_{1}}\right)\left(1-\frac{\kappa_{2}}{\mu_{2}}\right) v_{\text {off ,off }} t_{o}
\end{aligned}
```

where $v_{on, on}$ is the failure rate for both intermittent loads present, etc.



