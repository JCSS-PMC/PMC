# Annex C: Reliability Analysis Principles

## Introduction

In recent years, practical reliability methods have been developed to help engineers tackle the analysis, quantification, monitoring and assessment of structural risks, undertake sensitivity analysis of inherent uncertainties and make appropriate decisions about the performance of a structure. The structure may be at the design stage, under construction or in actual use.

This Annex C summarizes the principles and procedures used in formulating and solving risk related problems via reliability analysis. It is neither as broad nor as detailed as available textbooks on this subject, some of which are included in the bibliography. Its purpose is to underpin the updating and decision-making methodologies presented in [part 2](../part-02/general-principles.md) of this document.

Starting from the principles of limit state analysis and its application to codified design, the link is made between unacceptable performance and probability of failure. It is important, especially in assessment, to distinguish between components and systems. System concepts are introduced and important results are summarized. The steps involved in carrying out a reliability analysis, whose main objective is to estimate the failure probability, are outlined and alternative techniques available for such an analysis are presented. Some recommendations on formulating stochastic models for commonly used variables are also included.

## Concepts

### {math}`\underline{\text {Limit States}}`

The structural performance of a whole structure or part of it may be described with reference to a set of limit states which separate acceptable states of the structure from unacceptable states. The limit states are divided into the following two categories:

- ultimate limit states, which relate to the maximum load carrying capacity.
- serviceability limit states, which relate to normal use.

The boundary between acceptable (safe) and unacceptable (failure) states may be distinct or diffuse but, at present, deterministic codes of practice assume the former. Thus, verification of a structure with respect to a particular limit state is carried out via a model describing the limit state in terms of a function (called the limit state function) whose value depends on all relevant design parameters. In general terms, attainment of the limit state can be expressed as:

```{math}
:label: eqC1
g(\mathbf{s}, \mathbf{r})=0
```

where {math}`\mathbf{s}` and {math}`\mathbf{r}` represent sets of load (actions) and resistance variables. Conventionally, {math}`g(\mathbf{s}, \mathbf{r}) \leq 0` represents failure; in other words, an adverse state.

The limit state function, {math}`g(\mathbf{s}, \mathbf{r})`, can often be separated into one resistance function, {math}`r(.)`, and one loading (or action effect) function, {math}`s(.)` , in which case equation {eq}`eqC1` can be expressed as:

```{math}
:label: eqC2
r(\mathbf{r})-s(\mathbf{s})=0
```

### {math}`\underline{\text{Structural Reliability}}`

Load, material and geometry parameters are subject to uncertainties, which can be classified according to their nature, see [section 3](../part-03/general-principles.md). They can, thus, be represented by random variables (this being the simplest possible probabilistic representation, whereas more advanced models might be appropriate in certain situations, such as random fields). The variables {math}`\mathbf{S}` and {math}`\mathbf{R}` are often referred to as "basic random variables" (where the upper case letter is used for denoting random variables) and may be collectively represented by a random vector {math}`\mathbf{X}`.

In this context, failure is a probabilistic event and its probability of occurrence, {math}`P_{f}`, is given by:

```{math}
:label: eqC3a
P_{f}=\text{Prob}~ \left\lbrace g(\mathbf{X}) \leq 0 \right\rbrace =\text{Prob}~ \left\lbrace \mathrm{M} \leq 0 \right\rbrace
```

where, {math}`\mathrm{M}=g(\mathbf{X})`. Note that {math}`\mathrm{M}` is also a random variable, called the safety margin.

If the limit state function is expressed in the form of {eq}`eqC2`, {eq}`eqC3a` can be written as

$$
P_{f}=\text{Prob}~ \left\lbrace r~(\mathbf{R}) \leq s~(\mathbf{S})\right\rbrace =\text{Prob}~ \left\lbrace \mathrm{R} \leq \mathrm{S}\right\rbrace
$$

where {math}`\mathrm{R}=r~(\mathbf{R})` and {math}`\mathrm{S}=s~(\mathbf{S})` are random variables associated with resistance and loading respectively. This expression is useful in the context of the discussion in [section 2.2](section-2.2) on code formats and partial safety factors but will not be further used herein.

The failure probability defined in eqn {eq}`eqC3a` can also be expressed as follows:

```{math}
:label: eqC3b
P_{f}=\int_{g(\mathbf{x}) \leq 0} f_{\mathbf{X}}(\mathbf{x}) \mathrm{d} \mathbf{x}
```

where {math}`f_{\mathbf{X}}(\mathbf{x})` is the joint probability density function of {math}`\mathbf{X}`.

The reliability, {math}`P_{S}`, associated with the particular limit state considered is the complementary event, i.e.

```{math} 
:label: eqC4
P_{S}=1-P_{f}
```

In recent years, a standard reliability measure, the reliability index {math}`\beta`, has been adopted which has the following relationship with the failure probability

```{math}
:label: eqC5
\beta=-\Phi^{-1}(P_f)=\Phi^{-1}\left(P_{S}\right)
```

where {math}`\Phi^{-1}(.)` is the inverse of the standard normal distribution function, see {numref}`tblC1`

```{table} Relationship between β and Probability of occurance of failure
:name: tblC1
| {math}`P_{f}` | {math}`10^{-1}` | {math}`10^{-2}` | {math}`10^{-3}` | {math}`10^{-4}` | {math}`10^{-5}` | {math}`10^{-6}` | {math}`10^{-7}` |
| :-----------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| {math}`\beta` |       1.3       |       2.3       |       3.1       |       3.7       |       4.2       |       4.7       |       5.2       |
```

In most engineering applications, complete statistical information about the basic random variables {math}`\mathbf{X}` is not available and, furthermore, the function {math}`g(.)` is a mathematical model which idealizes the limit state. In this respect, the probability of failure evaluated from eqn {eq}`eqC3a` or {eq}`eqC3b` is a point estimate given a particular set of assumptions regarding probabilistic modelling and a particular mathematical model for {math}`g(.)`. The uncertainties associated with these models can be represented in terms of a vector of random parameters {math}`\mathbf{Q}`, and hence the limit state function may be re-written as {math}`g(\mathbf{X}, \mathbf{Q})`. It is important to note that the nature of uncertainties represented by the basic random variables {math}`\mathbf{X}` and the parameters {math}`\mathbf{Q}` is different. Whereas uncetainties in {math}`\mathbf{X}` cannot be influenced without changing the physical characteristics of the problem (e.g. changing the steel grade), uncertainties in {math}`\mathbf{Q}` can be influenced by the use of alternative methods and collection of additional data.

In this context, eqn {eq}`eqC3b` may be recast as follows

```{math}
:label: eqC6
P_{f}(\boldsymbol{\theta})=\int_{g(\mathbf{x}, \theta) \leq 0} f_{\mathbf{X} \mid \Theta}~(\mathbf{x} \mid \boldsymbol{\theta}) \mathrm{d} \mathbf{x}
```

where {math}`P_{f}(\boldsymbol{\theta})` is the conditional probability of failure for a given set of values of the parameters {math}`\boldsymbol{\theta}` and {math}`f_{\mathbf{X} \mid \Theta}~(\mathbf{x} \mid \boldsymbol{\theta})` is the conditional probability density function of {math}`\mathbf{X}` for given {math}`\boldsymbol{\theta}`.  

In order to account for the influence of parameter uncertainty on failure probability, one may evaluate the expected value of the conditional probability of failure, i.e.

```{math}
:label: eqC7a
\overline{P_{f}}=\mathrm{E}\left[P_{f}(\boldsymbol{\theta})\right]=\int_{\theta} P_{f}(\boldsymbol{\theta}) f_{\Theta}(\boldsymbol{\theta}) \mathrm{d} \boldsymbol{\theta}
```

where {math}`f_{\theta}(\theta)` is the joint probability density function of {math}`\theta`. The corresponding reliability index is given by

```{math}
:label: eqC7b
\bar{\beta}=-\Phi^{-1}\left(\overline{P_{f}}\right)
```

The main objective of reliability analysis is to estimate the failure probability (or, the reliability index). Hence, it replaces the deterministic safety check with a probabilistic assessment of the safety of the structure, e.g. eqn {eq}`eqC3a` or eqn {eq}`eqC7a`. Depending on the nature of the limit state considered, the uncertainty sources and their implications for probabilistic modeling, the characteristics of the calculation model and the degree of accuracy required, an appropriate methodology has to be developed. In many respects, this is similar to the considerations made in formulating a methodology for deterministic structural analysis but the problem is now set in a probabilistic framework.

### {math}`\underline{\text{System Concepts}}`

Structural design is, at present, primarily concerned with component behaviour. Each limit state equation is, in most cases, related to a single mode of failure of a single component.

However, most structures are an assembly of structural components and even individual components may be susceptible to a number of possible failure modes. In deterministic terms, the former can be tackled through a progressive collapse analysis (particularly appropriate in redundant structures), whereas the latter is usually dealt with by checking a number of limit state equations.

However, the system behaviour of structures is not well quantified in limit state codes and requires considerable innovation and initiative from the engineer. A probabilistic approach provides a better platform from which system behaviour can be explored and utilised. This can be of benefit in assessment of existing structures where strength reserves due to system effects can alleviate the need for expensive strengthening.

There are two fundamental systems, see {numref}`figC1`:

1) A series system is a system which fails if one or more of its components fail.

2) A parallel system is a system which fails when all its components have failed. 

The probability of system failure is given by

```{math}
:label: eqC8a
P_{f, sys}=\mathrm{P} \left[\mathrm{E_1} \cup \mathrm{E_2} \cup \ldots \cup \mathrm{E_n} \right] \quad \text{for a series system}
```

```{math}
:label: eqC8b
P_{f, sys}=\mathrm{P} \left[\mathrm{E_1} \cap \mathrm{E_2} \cap \ldots \cap \mathrm{E_n} \right] \quad \text{for a parallel system}
```

where {math}`\mathrm{E}_{i}(i=1, \ldots n)` is the event corresponding to failure of the {math}`i` th component. In the case of parallel systems, which are designed to provide some redundancy, it is important to define the state of the component after failure. In structures, this can be described in terms of a characteristic load-displacement response, see {numref}`figC2`, for which two convenient idealisations are the 'brittle' and the 'fully ductile' case. Intermediate, often more realistic, cases can also be defined.

The above expressions can be difficult to evaluate in the case of large systems with stochastically dependent components and, for this reason, upper and lower bounds have been developed, which may be used in practical applications. In order to appreciate the effect of system behaviour on failure probabilities, results for two special systems comprising equally correlated components with the same failure probability for each component are shown in [Fig. 10.3(a)](figC3) and [Fig. 10.3(b)](figC3). Note that in the case of the parallel system, it is assumed that the components are fully ductile.

More general systems can be constructed by combining the two fundamental types. It is fair to say that system methods are more developed for skeletal rather than continuous structures. Important results from system reliability theory are summarized in [section 4](../part-01/basis-of-uncerainty-modelling.md).

## Component Reliability Analysis

The framework for probabilistic modeling and reliability evaluation is outlined in this section. The focus is on the procedure to be followed in assessing the reliability of a critical component with respect to a particular failure mode.

#### {math}`\underline{\text{General Steps}}`

The main steps in a component reliability analysis are the following:

1) select appropriate limit state function

2) specify appropriate time reference

3) identify basic variables and develop appropriate probabilistic models

4) compute reliability index and failure probability 

5) perform sensitivity studies

Step (1) is essentially the same as for deterministic analysis. Step (2) should be considered carefully, since it affects the probabilistic modeling of many variables, particularly live loading. Step (3) is perhaps the most important because the considerations made in developing the probabilistic models have a major effect on the results obtained, see [section 3.2](section-3.2). Step (4) should be undertaken with one of the methods summarized in [section 3.3](section-3.3), depending on the application. Step (5) is necessary insofar as the sensitivity of any results (deterministic or probabilistic) should be assessed before a decision is taken.

### {math}`\underline{\text{Probabilistic Modelling}}` 

For the particular failure mode under consideration, uncertainty modeling must be undertaken with respect to those variables in the corresponding limit state function whose variability is judged to be important (basic random variables). Most engineering structures are affected by the following types of uncertainty:

- intrinsic physical or mechanical uncertainty; when considered at a fundamental level, this uncertainty source is often best described by stochastic processes in time and space, although it is often modelled more simply in engineering applications through random variables.

- measurement uncertainty; this may arise from random and systematic errors in the measurement of these physical quantities

- statistical uncertainty; due to reliance on limited information and finite samples

- model uncertainty; related to the predictive accuracy of calculation models used

The physical uncertainty in a basic random variable is represented by adopting a suitable probability distribution, described in terms of its type and relevant distribution parameters. The results of the reliability analysis can be very sensitive to the tail of the probability distribution, which depends primarily on the type of distribution adopted. A proper choice of distribution type is therefore important.

For most commonly encountered basic random variables there have been studies (of varying detail) that contain guidance on the choice of distribution and its parameters. If direct measurements of a particular quantity are available, then existing, so-called *a priori*, information (e.g. probabilistic models found in published studies) should be used as prior statistics with a relatively large equivalent sample size {math}`\left(n^{\prime} \approx 50\right)`.

The following comments may also be helpful in selecting a suitable probabilistic model.

{math}`\underline{\text{Material properties}}`

- frequency of negative values is normally zero
- log-normal distribution can often be used
- distribution type and parameters should, in general, be derived from large homogeneous samples and with due account of established distributions for similar variables (e.g. for a new high strength steel grade, the information on properties of existing grades should be consulted); tests should be planned so that they are, as far as possible, a realistic description of the potential use of the material in real applications.


{math}`\underline{\text{Geometric parameters}}`

- variability in structural dimensions and overall geometry tends to be small
- dimensional variables can be adequately modelled by the normal or log-normal distribution
- if the variable is physically bounded, a truncated distribution may be appropriate (e.g. location of reinforcement); such bounds should always be carefully considered to avoid entering into physically inadmissible ranges
- variables linked to manufacturing can have large coefficients of variation (e.g. imperfections, misalignments, residual stresses, weld defects).


{math}`\underline{\text{Load variables}}`

- loads should be divided according to their time variation (permanent, variable, accidental)
- in certain cases, permanent loads consist of the sum of many individual elements; they may be represented by a normal distribution
- for single variable loads, the form of the point-in-time distribution is seldom of immediate relevance; often the important random variable is the magnitude of the largest extreme load that occurs during a specified reference period for which the probability of failure is calculated (e.g. annual, lifetime)
- the probability distribution of the largest extreme could be approximated by one of the asymptotic extreme-value distributions (Gumbel, sometimes Frechet)
- when more than one variable loads act in combination, load modelling is often undertaken using simplified rules suitable for FORM/SORM analysis.

In selecting a distribution type to account for physical uncertainty of a basic random variable afresh, the following procedure may be followed:

- based on experience from similar type of variables and physical knowledge, choose a set of possible distributions
- obtain a reasonable sample of observations ensuring that, as far as possible, the sample points are from a homogeneous group (i.e. avoid systematic variations within the sample) and that the sampling reflects potential uses and applications 
- evaluate by an appropriate method the parameters of the candidate distributions using the sample data; the method of maximum likelihood is recommended but evaluation by alternative methods (moment estimates, least-square fit, graphical methods) may also be carried out for comparison.
- compare the sample data with the resulting distributions; this can be done graphically (histogram vs. pdf, probability paper plots) or through the use of goodness-of-fit tests (Chi-square, Kolmogorov-Smirnov tests)

If more than one distribution gives equally good results (or if the goodness-of-fit tests are acceptable to the same significance level), it is recommended to choose the distribution that will result in the smaller reliability. This implies choosing distributions with heavy left tails for resistance variables (material properties, geometry excluding tolerances) and heavy right tails for loading variables (manufacturing tolerances, defects and loads).

Capturing the essential features of physical uncertainty in a load or in a structure property through a random variable model is perhaps the simplest way of modeling uncertainty and quantifying its effect on failure probability. In general, loads are functions of both time and position on any particular structure. Equally, material properties and dimensions of even a single structural member, e.g. a RC floor slab, are functions which vary both in time and in space. Such random functions are usually denoted as random (or stochastic) processes when time variation is the most important factor and as random fields when spatial variation is considered.

[Fig. 10.4(a)](figC4) shows schematically a continuous stochastic process, e.g. wind pressure at a particular point on a wall of a structure. The trace of this process over time is obtained through successive realisations of the underlying phenomenon, in this case wind speed, which is clearly a random variable taking on different values within each infinitesimally small time interval, {math}`\delta t`.

[Fig. 10.4(b)](figC4) depicts a two-dimensional random field, e.g. the spatial variation of concrete strength in a floor slab just after construction. Once again, a random variable, in this case describing the possible outcomes of, say, a core test obtained from any given small area, {math}`\delta A`, is the basic kernel from which the random field is built up.

In considering either a random process or a random field, it is clear that, apart from the characteristics associated with the random variable describing uncertainty within a small unit (interval or area), laws describing stochastic dependence (or, in simpler terms, correlation) between outcomes in time and/or in space are very important. 

The other three types of uncertainty mentioned above (measurement, statistical, model) also play an important role in the evaluation of reliability. As mentioned in [section 2.3](section-2.3), these uncertainties are influenced by the particular method used in, for example, strength analysis and by the collection of additional (possibly, directly obtained) data. These uncertainties could be rigorously analysed by adopting the approach outlined by eqns {eq}`eqC8a`, {eq}`eqC8b` and {eq}`eqC9`. However, in many practical applications a simpler approach has been adopted insofar as model (and measurement) uncertainty is concerned based on the differences between results predicted by the mathematical model adopted for {math}`g(\mathrm{x})` and some more elaborate model believed to be a closer representation of actual conditions. In such cases, a model uncertainty basic random variable {math}`X_{m}` is introduced where

```{math}
\mathrm{X}_{\mathrm{m}}=\frac{\text { actual value }}{\text { predicted value }}
```

and the following comments offer some general guidance in estimating the statistics of {math}`\mathrm{X_{m}}` :

- the mean value of the model uncertainty associated with code calculation models can be larger than unity, reflecting the in-built conservatism of code models
- the model uncertainty parameters of a particular calculation model may be evaluated vis-à-vis physical experiments or by comparing the calculation model with a more detailed model (e.g. finite element model)
- when experimental results are used, use of measured rather than nominal or characteristic quantities is preferred in calculating the predicted value
- the use of numerical experiments (e.g. finite element models) has some advantages over physical experiments, since the former ensures well-controlled input.
- the choice of a suitable probability distribution for {math}`\mathrm{X}_{\mathrm{m}}` is often governed by mathematical convenience and a normal distribution has been used extensively.


### {math}`\underline{\text{Computation of Failure Probability}}`

As mentioned above, the failure probability of a structural component with respect to a single failure mode is given by

$$
P_{f}=\int_{g(\mathbf{x}) \leq 0} f_{\mathbf{X}}(\mathbf{x}) \mathrm{d} \mathbf{x} \tag{10.4}
$$

where {math}`\mathbf{X}` is the vector of basic random variables, {math}`g(\boldsymbol{x})` is the limit state (or failure) function for the failure mode considered and {math}`f_{\mathbf{X}}(\mathbf{x})` is the joint probability density function of {math}`\mathbf{X}`.

An important class of limit states are those for which all the variables are treated as time independent, either by neglecting time variations in cases where this is considered acceptable or by transforming time-dependent processes into time-invariant variables (e.g. by using extreme value distributions). The methods commonly used for calculating {math}`P_{f}` in such cases are outlined below. Guidelines on how to deal with time-dependent problems are given in [section 5](../part-01/models-for-physical-behaviour.md). Note that after calculating {math}`P_{f}` via one of the methods outlined below, or any other valid method, a reliability index may be obtained from equation {eq}`eqC5`, for comparative or other purposes.

{math}`\underline{\text{Asymptotic approximate methods}}`

Although these methods first emerged with basic random variables described through 'second-moment' information (i.e. with their mean value and standard deviation, but without assigning any probability distributions), it is nowadays possible in many cases to have a full description of the random vector {math}`\mathbf{X}` (as a result of data collection and probabilistic modelling studies). In such cases, the probability of failure could be calculated via first or second order reliability methods (FORM and SORM respectively). Their implementation relies on:

*(1) Transformation techniques*:

```{math}
:label: eqC9
\mathbf{T}: \quad \mathbf{X}=\left(X_{1}, X_{2}, \ldots X_{n}\right) \quad \rightarrow \quad \mathbf{U}=\left(U_{1}, U_{2}, \ldots U_{n}\right)
```

where {math}`U_{1}, U_{2}, \ldots U_{n}` are independent standard normal variables (i.e. with zero mean value and unit standard deviation). Hence, the basic variable space (including the limit state function) is transformed into a standard normal space, see {numref}`figC5`. The special properties of the standard normal space lead to several important results, as discussed below.

*(2) Search techniques*:

In standard normal space, the objective is to determine a suitable checking point: this is shown to be the point on the limit-state surface which is closest to the origin, the so-called 'design point'. In this rotationally symmetric space, it is the most likely failure point, in other words its co-ordinates define the combination of variables that are most likely to cause failure. This is because the joint standard normal density function, whose bell-shaped peak lies directly above the origin, decreases exponentially as the distance from the origin increases. To determine this point, a search procedure is required in all but the most simple of cases (the Rackwitz-Fiessler algorithm is commonly used).

Denoting the co-ordinates of this point by

```{math}
\mathbf{u}^{*}=\left(u_{1}^{*}, u_{2}^{*}, \ldots u_{n}^{*}\right)
```

its distance from the origin is clearly equal to

$$
\left(\sum_{i=1}^{n} u_{i}^{*2}\right)^{1 / 2}
$$

This scalar quantity is known as the Hasofer-Lind reliability index, {math}`\beta_{\mathrm{HL}}`, i.e.

```{math}
:label: eqC10
\beta_{H L}=\left(\sum_{i=1}^{n} u_{i}^{* 2}\right)^{1 / 2}
```

Note that {math}`\mathbf{u}^{*}` can also be written as

```{math}
:label: eqC11a
\mathbf{u}^{*}=\beta_{\mathrm{HL}}~ \mathbf{\alpha}
```

where {math}`\alpha=\left(\alpha_{1}, \alpha_{2}, \ldots \alpha_{n}\right)` is the unit normal vector to the limit state surface at {math}`\mathbf{u}^{*}`, and, hence, {math}`\alpha_{i}(i=1, \ldots n)` represent the direction cosines at the design point. These are also known as the sensitivity factors, as they provide an indication of the relative importance of the uncertainty in basic random variables on the computed reliability. Their absolute value ranges between zero and unity and the closer this is to the upper limit, the more significant the influence of the respective random variable is to the reliability. The following expression is valid for independent variables

```{math}
:label: eqC11b
\sum_{i=1}^{n} \alpha_{1}^{2}=1
```

*(3) Approximation techniques*:

Once the checking point is determined, the failure probability can be approximated using results applicable to the standard normal space. Thus, in a first-order approximation, the limit state surface is approximated by its tangent hyperplane at the design point. The probability content of the failure set is then given by

```{math}
:label: eqC12a
P_{f \mathrm{FORM}}=\Phi\left(-\beta_{\mathrm{HL}}\right)
```

In some cases, a higher order approximation of the limit state surface at the design point is merited, if only to check the accuracy of FORM. The result for the probability of failure assuming a quadratic (second-order) approximation of the limit state surface is asymptotically given by

```{math}
:label: eqC12b
P_{f S O R M}=\Phi\left(-\beta_{H L}\right) \prod_{j=1}^{n-1}\left(1-\beta_{H L}~ \kappa_{j}\right)^{-1 / 2}
```

for {math}`\beta_{\mathrm{HL}} \rightarrow \infty`, where {math}`\kappa_{j}` are the principal curvatures of the limit state surface at the design point. An expression applicable to finite values of {math}`\beta_{\mathrm{HL}}` is also available.

{math}`\underline{\text{Simulation Methods}}`

In this approach, random sampling is employed to simulate a large number of (usually numerical) experiments and to observe the result. In the context of structural reliability, this means, in the simplest approach, sampling the random vector {math}`\mathbf{X}` to obtain a set of sample values. The limit state function is then evaluated to ascertain whether, for this set, failure (i.e. {math}`g(\mathbf{x}) \leq 0)` has occurred. The experiment is repeated many times and the probability of failure, {math}`P_{f}`, is estimated from the fraction of trials leading to failure divided by the total number of trials. This so-called Direct or Crude Monte Carlo method is not likely to be of use in practical problems because of the large number of trials required in order to estimate with a certain degree of confidence the failure probability. Note that the number of trials increases as the failure probability decreases. Simple rules may be found, of the form {math}`N>\mathrm{C} / P_{f}`, where {math}`N` is the required sample size and {math}`\mathrm{C}` is a constant related to the confidence level and the type of function being evaluated.

Thus, the objective of more advanced simulation methods, currently used for reliability evaluation, is to reduce the variance of the estimate of {math}`P_{f}`. Such methods can be divided into two categories, namely indicator function methods and conditional expectation methods. An example of the former is Importance Sampling, where the aim is to concentrate the distribution of the sample points in the vicinity of likely failure points, such as the design point obtained from FORM/SORM analysis. This is done by introducing a sampling function, whose choice would depend on *a priori* information available, such as the co-ordinates of the design point and/or any estimates of the failure probability. In this way, the success rate (defined here as a probability of obtaining a result in the failure region in any particular trial) is improved compared to Direct Monte Carlo. Importance Sampling is often used following an initial FORM/SORM analysis. A variant of this method is Adaptive Sampling, in which the sampling density is updated as the simulation proceeds. Importance Sampling could be performed in basic variable or standard normal space, depending on the problem and the form of prior information.

A powerful method belonging to the second category is Directional Simulation. It achieves variance reduction using conditional expectation in the standard normal space, where a special result applies pertaining to the probability bounded by a hypersphere centred at the origin. Its efficiency lies in that each random trial generates precise information on where the boundary between safety and failure lies. However, the method does generally require some iterative calculations. It is particularly suited to problems where it is difficult to identify 'important' regions (perhaps due to the presence of multiple local design points).

The two methods outlined above have also been used in combination, which indicates that when simulation is chosen as the basic approach for reliability assessment, there is scope to adapt the detailed methodology to suit the particular problem in hand.

### {math}`\underline{\text{Recommendations}}`

As with any other analysis, choosing a particular method must be justified through experience and/or verification. Experience shows that FORM/SORM estimates are adequate for a wide range of problems. However, these approximate methods have the disadvantage of not being quantified by error estimates, except for few special cases. As indicated, simulation may be used to verify FORM/SORM results, particularly in situations where multiple design points might be suspected. Simulation results should include the variance of the estimated probability of failure, though good estimates of the variance could increase the computations required. When using FORM/SORM, attention should be given to the ordering of dependent random variables and the choice of initial points for the search algorithm. Not least, the results for the design point should be assessed to ensure that they do not contradict physical reasoning.

## System Reliability Analysis

As discussed in [section 3](../part-01/principles-of-limit-state-design.md), individual component failure events can be represented by failure boundaries in basic variable or standard normal space. System failure events can be similarly represented, see {numref}`figC6a` and {numref}`figC6b`, and, once more, certain approximate results may be derived as an extension to FORM/SORM analysis of individual components. In addition, system analysis is sometimes performed using bounding techniques and some relevant results are given below.

### {math}`\underline{\text{Series systems}}`

The probability of failure of a series system with $m$ components is defined as

```{math}
:label: eqC13
P_{f s y s}=\mathrm{P}\left[\bigcup_{j=1}^{\mathrm{m}} \mathrm{F}_{j}\right]
```

where, {math}`\mathrm{F}_{j}` is the event corresponding to the failure of the {math}`j` th component. By describing this event in terms of a safety margin {math}`\mathrm{M}_{j}`

```{math}
:label: eqC14
P\left[F_{j}\right]=P\left[M_{j} \leq 0\right] \approx \Phi\left(-\beta_{j}\right)
```

where {math}`\beta_{j}` is its corresponding FORM reliability index, it can be shown that in a first-order approximation

```{math}
:label: eqC15a
P_{f s y s}=1-\Phi_{\mathrm{m}}[\widetilde{\beta} ; \widetilde{\widetilde{\rho}}]
```

where {math}`\Phi_{\mathrm{m}}[.]` is the multi-variate standard normal distribution function, {math}`\widetilde{\boldsymbol{\beta}}` is the {math}`(m \times 1)` vector of component reliability indices and {math}`\widetilde{\widetilde{\rho}}{ }` is the {math}`(m \times m)` correlation matrix between safety margins with elements given by

```{math}
:label: eqC15b
\rho_{j k}=\sum_{i=1}^{n} \alpha_{i j} \alpha_{i k} \quad, j, k=1,2, \ldots, \mathrm{m}
```

where {math}`\alpha_{i j}` is the sensitivity factor corresponding to the {math}`i` th random variable in the {math}`j` th margin. In some cases, especially when the number of components becomes large, evaluation of equation {eq}`eqC15a` becomes cumbersome and bounds to the system failure probability may prove sufficient.

Simple first-order linear bounds are given by

```{math}
:label: eqC16a
\overset{m}{\underset{j=1}{Max}}\left[P\left(F_{j}\right)\right] \leq P_{f s y s} \leq Min \left[\left(\sum_{j=1}^{m} P\left(F_{j}\right)\right), 1\right]
```

but these are likely to be rather wide, especially for large {math}`m`, in which case second-order linear bounds (Ditlevsen bounds) may be needed. These are given by

```{math}
:label: eqC16b
P\left[F_{1}\right]+\sum_{j=2}^{m} Max \left\lbrace\left[P\left(F_{j}\right)-\sum_{k=1}^{j-1} P\left(F_{j} \cap F_{k}\right)\right], 0\right\rbrace \leq P_{f s y s} \leq \\ P\left[F_{1}\right]+\sum_{j=2}^{m}\left\lbrace P \left(F_{j} \right) - \underset{k < j}{Max} \left[P\left(F_{j} \cap F_{k}\right)\right] \right\rbrace 
```

The narrowness of these bounds depends in part on the ordering of the events. The optimal ordering may differ between the lower and the upper bound. In general, these bounds are much narrower than the simple first-order linear bounds given by equation {eq}`eqC16a`. The bisections of events may be calculated using a first-order approximation, which appears below in the presentation of results for parallel systems.

### {math}`\underline{\text{Parallel systems}}`

Following the same approach and notation as above, the failure probability of a parallel system with {math}`m$ components is given by

```{math}
:label: eqC17
P_{\text {fsys }}=P\left[\overset{m}{\underset{j=1}{\cap}}\left(F_{j}\right)\right]=P\left[\overset{m}{\underset{j=1}{\cap}}\left(M_{j} \leq 0\right)\right]
```

and the corresponding first-order approximation is

```{math}
:label: eqC18
P_{f sys}=\Phi_{\mathrm{m}}[-\widetilde{\beta} ; \widetilde{\widetilde{\rho}}]
```

Simple bounds are given by

```{math}
:label: eqC19a
0 \leq P_{f s y s} \leq \overset{m}{\underset{j=1}{Min}}\left[P\left(F_{j}\right)\right]
```

These are usually too wide for practical applications. An improved upper bound is

```{math}
:label: eqC19b
P_{f sys} \leq \overset{m}{\underset{j, k=1}{Min}}\left[P\left(F_{j} \cap F_{k}\right)\right]
```

The error involved in the first-order evaluation of the intersections, {math}`\mathrm{P}\left[\mathrm{F}_{j} \cap \mathrm{F}_{k}\right]`, is, to a large extent, influenced by the non-linearity of the margins at their respective design points. In order to obtain a better estimate of the intersection probabilities, an improvement on the selection of linearisation points has been suggested.

## Time-Dependent Reliability

### {math}`\underline{\text{General Remarks}}`

Even in considering a relatively simple safety margin for component reliability analysis such as {math}`M=R-S`, where {math}`R` is the resistance at a critical section in a structural member and {math}`S` is the corresponding load effect at the same section, it is generally the case that both {math}`S` and resistance {math}`R` are functions of time. Changes in both mean values and standard deviations could occur for either {math}`R(t)` or {math}`S(t)`. For example, the mean value of {math}`R(t)` may change as a result of deterioration (e.g. corrosion of reinforcement in an RC bridge implies loss of area, hence a reduction in the mean resistance) and its standard deviation may also change (e.g. uncertainty in predicting the effect of corrosion on loss of area may increase as the periods considered become longer). On the other hand, the mean value of {math}`S(t)` may increase over time (e.g. due to higher traffic flow and/or higher individual vehicle weights) and, equally, the estimate of its standard deviation may increase due to lower confidence in predicting the correct mix of traffic for longer periods. A time-dependent reliability problem could thus be schematically represented as in {numref}`figC7`, the diagram implying that, on average, the reliability decreases with time. Although this situation is usual, the converse could also occur in reliability assessment of existing structures, for example through strengthening or favourable change in use.

Thus, the elementary reliability problem described through equations {eq}`eqC3a` and {eq}`eqC3b` may now be formulated as:

```{math}
:label: eqC20a
P_{f}(t)=Prob~\left\lbrace\mathbf{R}(t) \leq \boldsymbol{S}(t)\right\rbrace=Prob~\left\lbrace g(\mathbf{X}(t)) \leq 0 ~00,0 \right\rbrace
```

where {math}`g(\mathbf{X}(t))=\mathrm{M}(t)` is a time-dependent safety margin, and

```{math}
:label: eqC20b
P_{f}(t)=\int_{\mathrm{g}(\mathbf{x}(\mathrm{t})) \leq 0} f_{\mathbf{X}(t)}~(\mathbf{x}(t))~\mathrm{d} \mathbf{x}(t)
```

is the instantaneous failure probability at time {math}`t`, assuming that the structure was safe at time less than {math}`t`.

In time-dependent reliability problems, interest often lies in estimating the probability of failure over a time interval, say from 0 to {math}`t_{\mathrm{L}}`. This could be obtained by integrating {math}`P_{f}(t)` over the interval {math}`\left[0, t_{\mathrm{L}}\right]`, bearing in mind the correlation characteristics in time of the process {math}`\mathbf{X}(t)` or, sometimes more conveniently, the process {math}`\mathbf{R}(t)`, the process {math}`\mathbf{S}(t)`, as well as any cross correlation between {math}`\mathbf{R}(t)` and {math}`\mathbf{S}(t)`. Note that the load effect process {math}`\mathbf{S}(t)` is often composed of additive components, {math}`\mathrm{S}_{1}(t), \mathrm{S}_{2}(\mathrm{t}), \ldots`, for each of which the time fluctuations may have different features (e.g. continuous variation, pulse-type variation, spikes).

Interest may also lie in predicting when {math}`\mathrm{S}(t)` crosses {math}`\mathrm{R}(t)` for the first time, see  {numref}`figC8`, or the probability that such an event would occur within a specified time interval. These considerations give rise to so-called 'crossing' problems, which are treated using stochastic process theory. A key concept for such problems is the rate at which a random process {math}`\mathrm{X}(t)` 'upcrosses' (or crosses with a positive slope) a barrier or level {math}`\xi`, as shown in {numref}`figC9`. This upcrossing rate is a function of the joint probability density function of the process and its derivative, and is given by Rice's formula

```{math}
:label: eqC21
v_{\xi}^{+}=\int_{0}^{\infty} \dot{x} f_{X \dot{X}}(\xi, \dot{x}) d \dot{x}
```

where the rate in general represents an ensemble average at time {math}`t`. For a number of common stochastic processes, useful results have been obtained starting from Equation {eq}`eqC21`. An important simplification can be introduced if individual crossings can be treated as independent events and the occurences may be approximated by a Poisson distribution, which might be a reasonable assumption for certain rare load events.

Another class of problems calling for a time-dependent reliability analysis are those related to damage accumulation, such as fatigue and fracture. This case is depicted in {numref}`figC10` via a fixed threshold (e.g. critical crack size) and a monotonically increasing time-dependent load effect or damage function (e.g. actual crack size at any given time).

It is evident from the above remarks that the best approach for solving a time-dependent reliability problem would depend on a number of considerations, including the time frame of interest, the nature of the load and resistance processes involved, their correlation properties in time, and the confidence required in the probability estimates. All these issues may be important in determining the appropriate idealisations and approximations.

### {math}`\underline{\text{Transformation to Time-Independent Formulations}}`

Although time variations are likely to be present in most structural reliability problems, the methods outlined in Sections [3](../part-01/principles-of-limit-state-design.md) and [4](../part-01/basis-of-uncerainty-modelling.md) have gained wide acceptance, partly due to the fact that, in many cases, it is possible to transform a time dependent failure mode into a corresponding time independent mode. This is especially so in the case of overload failure, where individual time-varying actions, which are essentially random processes, {math}`p(t)`, can be modelled by the distribution of the maximum value within a given reference period T, i.e. {math}`X=\max _{\mathrm{T}}\left\lbrace p(t)\right\rbrace` rather than the point-in-time distribution. For continuous processes, the probability distribution of the maximum value (i.e. the largest extreme) is often approximated by one of the asymptotic extreme value distributions. Hence, for structures subjected to a single time-varying action, a random process model is replaced by a random variable model and the principles and methods given previously may be applied.

The theory of stochastic load combination is used in situations where a structure is subjected to two or more time-varying actions acting simultaneously. When these actions are independent, perhaps the most important observation is that it is highly unlikely that each action will reach its peak lifetime value at the same moment in time. Thus, considering two time-varying load processes {math}`p_{1}(t), p_{2}(t), 0 \leq t \leq \mathrm{T}`, acting simultaneously, for which their combined effect may be expressed as a linear combination {math}`p_{1}(t)+p_{2}(t)`, the random variable of interest is:

```{math}
:label: eqC22a
X=\text{max}_{\mathrm{T}}\left\lbrace p_{1}(t)+p_{2}(t)\right\rbrace
```

If the loads are independent, replacing {math}`X` by {math}`\max _{\mathrm{T}}\left\{p_{1}(t)\right\}+\max _{\mathrm{T}}\left\{p_{2}(t)\right\}` leads to very conservative results. However, the distribution of {math}`X` can be derived in few cases only. One possible way of dealing with this problem, which also leads to a relatively simple deterministic code format, is to replace {math}`X` with the following

```{math}
:label: eqC22b
X' = \text{max}_T \left\lbrace
\begin{array}{l}
\max_T\left\lbrace p_1(t) \right\rbrace + p_2(t) \\ \\ 
p_1(t) + \max_T\left\lbrace p_2(t) \right\rbrace
\end{array}
\right.
```

This rule (Turkstra's rule) suggests that the maximum value of the sum of two independent load processes occurs when one of the processes attains its maximum value. This result may be generalised for several independent time-varying loads. The conditions which render this rule adequate for failure probability estimation are discussed in standard texts. Note that the failure probability associated with the sum of a special type of independent identically distributed processes (so-called FBC process) can be calculated in a more accurate way, as will be outlined below. Other results have been obtained for combinations of a number of other processes, starting from Rice's barrier crossing formula.

The FBC (Ferry Borges-Castanheta) process is generated by a sequence of independent identically distributed random variables, each acting over a given (deterministic) time interval. This is shown in {numref}`figC11` where the total reference period T is made up of {math}`n_{i}` repetitions where {math}`n_{i}=\mathrm{T} / \tau_{i}`. Hence, the FBC process is a rectangular pulse process with changes in amplitude occurring at equal intervals. Because of independence, the maximum value in the reference period {math}`\mathrm{T}` is given by

```{math}
:label: eqC23
\mathrm{F}_{\max _{\mathrm{T}} \mathrm{X}_{\mathrm{i}}}\left(x_{i}\right)=\left[\mathrm{F}_{\mathrm{X}_{\mathrm{i}}}\left(x_{i}\right)\right]^{n_{i}}
```

When a number of FBC processes act in combination and the ratios of their repetition numbers within a given reference period are given by positive integers it is, in principle, possible to obtain the extreme value distribution of the combination through a recursive formula. More importantly, it is possible to deal with the sum of FBC processes by implementing the Rackwitz-Fiessler algorithm in a FORM/SORM analysis.

A deterministic code format, compatible with the above rules, leads to the introduction of combination factors, {math}`\psi_{\mathrm{o}i}`, for each time-varying load {math}`i`. In principle, these factors express ratios between fractiles in the extreme value and point-in-time distributions so that the probability of exceeding the design value arising from a combination of loads is of the same order as the probability of exceeding the design value caused by one load. For time-varying loads, they would depend on distribution parameters, target reliability and FORM/SORM sensitivity factors and on the frequency characteristics (i.e. the base period assumed for stationary events) of loads considered within any particular combination.

### {math}`\underline{\text{Introduction to Crossing Theory}}`

In considering a time-dependent safety margin, i.e. {math}`\mathrm{M}(t)=g(\mathbf{X}(t))`, the problem is to establish the probability that {math}`\mathrm{M}(t)` becomes zero or less in a reference time period, {math}`t_{\mathrm{L}}`. As mentioned previously, this constitutes a so-called 'crossing' problem. The time at which {math}`\mathrm{M}(t)` becomes less than zero for the first time is called the 'time to failure' and is a random variable, see [Fig. 10.13(a)](figC12), or, in a basic variable space, [Fig. 10.13(b)](figC12). The probability that {math}`M(t) \leq 0` occurs during {math}`t_{\mathrm{L}}` is called the 'first-passage' probability. Clearly, it is identical to the probability of failure during time {math}`t_{\mathrm{L}}`.

The determination of the first passage probability requires an understanding of the theory of random processes. Herein, only some basic concepts are introduced in order to see how the methods described above have to be modified in dealing with crossing problems.

The first-passage probability, {math}`P_{f}(t)` during a period {math}`\left[0, t_{\mathrm{L}}\right]` is

```{math}
:label: eqC24a
P_{f}\left(t_{\mathrm{L}}\right)=1-\mathrm{P}\left[N\left(t_{\mathrm{L}}\right)=0 \mid \mathbf{X}(0) \in D\right] P[\mathbf{X}(0) \in D]
```

where {math}`\mathbf{X}(0) \in D` signifies that the process {math}`\mathbf{X}(t)` starts in the safe domain and {math}`N\left(t_{\mathrm{L}}\right)` is the number of outcrossings in the interval {math}`\left[0, t_{\mathrm{L}}\right]`. The second probability term is equivalent to {math}`1-P_{f}(0)`, where {math}`P_{f}(0)` is the probability of failure at {math}`t=0`. Equation {eq}`eqC24a` can be re-written as

```{math}
:label: eqC24b
P_{f}(t_\mathrm{L})=P_{f}(0)+\left(1-P_{f}(0)\right)(1-\mathrm{P}[N(t_\mathrm{L})=0])
```

from which different approximations may be derived depending on the relative magnitude of the terms. A useful bound is

```{math}
:label: eqC25
P_{f}\left(t_{\mathrm{L}}\right) \leq P_{f}(0)+\mathrm{E}\left[N\left(t_{\mathrm{L}}\right)\right]
```

where the first term may be calculated by FORM/SORM and the expected number of outcrossings, {math}`\mathrm{E}\left[N\left(t_{\mathrm{L}}\right)\right]`, is calculated by Rice's formula or one of its generalisations. Alternatively, parallel system concepts can be employed.

## Figures

```{figure} ../part-01/images/Figure-C.1.jpg
:name: figC1

Schematic representation of series and parallel systems
```

```{figure} ../part-01/images/Figure-C.2.jpg
:name: figC2

Idealised load-displacement response of structural elements
```

```{figure} ../part-01/images/Figure-C.3.jpg
:name: figC3

Effect of element correlation and system size on failure probability
(a) series system
(b) parallel system
```

```{figure} ../part-01/images/Figure-C.4.jpg
:name: figC4

Schematic representations
(a) random process
(b) random field
```

```{figure} ../part-01/images/Figure-C.5.jpg
:name: figC5

Limit state surface in basic variable and standard normal space
`
```{figure} ../part-01/images/Figure-C.6(a).jpg
:name: figC6a

Failure region as union of component failure events for series system
```

```{figure} ../part-01/images/Figure-C.6(b).jpg
:name: figC6b

Failure region as intersection of component failure events for parallel system
```

```{figure} ../part-01/images/Figure-C.7.jpg
:name: figC7

General time-dependent reliability problem
```

```{figure} ../part-01/images/Figure-C.8.jpg
:name: figC8

Schematic representation of crossing problems 
(a) slowly varying resistance 
(b) rapidly varying resistance
```

```{figure} ../part-01/images/Figure-C.9.jpg
:name: figC9

Fundamental barrier crossing problem
```

```{figure} ../part-01/images/Figure-C.10.jpg
:name: figC10

Damage accumulation problem
```

```{figure} ../part-01/images/Figure-C.11.jpg
:name: figC11

Realization of an FBC process
```

```{figure} ../part-01/images/Figure-C.12.jpg
:name: figC12

Time-dependent safety margin and schematic representation of vector outcrossing
```

## Bibliography

[C1] Ang A H S and Tang W H, Probability Concepts in Engineering Planning and Design, Vol. I \\& II, John Wiley, 1984.

[C2] Augusti G, Baratta A and Casciati F, Probabilistic Methods in Structural Engineering, Chapman and Hall, 1984.

[C3] Benjamin J R and Cornell C A, Probability, Statistics and Decision for Civil Engineers, McGraw Hill, 1970.

[C4] Bolotin V V, Statistical Methods in Structural Mechanics, Holden-Day, 1969.

[C5] Borges J F and Castanheta M, Structural Safety, Laboratorio Nacional de Engenharia Civil, Lisboa, 1985.

[C6] Ditlevsen O, Uncertainty Modelling, McGraw Hill, 1981.

[C7] Ditlevsen O and Madsen H O, Structural Reliability Methods, J Wiley, 1996.

[C8] Madsen H O, Krenk S and Lind N C, Methods of Structural Safety, Prentice-Hall, 1986.

[C9] Melchers R E, Structural Reliability: Analysis and Prediction, 2nd edition, J Wiley, 1999.

[C10] Thoft-Christensen P and Baker M J, Structural Reliability Theory and its Applications, Springer-Verlag, 1982.

[C11] Thoft-Christensen P and Murotsu Y, Application of Structural Systems Reliability Theory, Springer-Verlag, 1986.

[C12] CEB, First Order Concepts for Design Codes, CEB Bulletin No. 112, 1976.

[C13] CEB, Common Unified Rules for Different Types of Construction and Materials, Vol. 1, CEB Bulletin No. 116, 1976. [C14] Construction Industry Research and Information Association (CIRIA), Rationalisation of Safety and Serviceability Factors in Structural Codes, Report 63, London, 1977.

[C15] International Organization for Standardization (ISO), General Principles on Reliability for Structures, ISO 2394, Third edition.