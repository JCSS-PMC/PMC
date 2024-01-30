# Fatigue Models For Metallic Structures

**List of symbols (main text)**

{math}`a \quad` crack depth

{math}`c \quad` half-length of the crack at the surface

{math}`f ()\quad` probability density function, resistance interaction criterion

{math}`g()\quad` limit state function

{math}`m \quad` parameter in the S-N-approach

{math}`m \quad` parameter in the Paris Law

{math}`n \quad` number of actual stress cycles

{math}`t\quad` time

{math}`A\quad` Paris Law parameter

{math}`C\quad` model uncertainty

{math}`B \quad` plate thickness

{math}`D\quad` damage according to Miner's Rule

{math}`E[~] \quad` expectation operator

{math}`K \quad` parameter in the {math}`\mathrm{S}-\mathrm{N}`-model

{math}`K \quad` elastic stress intensity factor in the fracture mechanics model

{math}`K_{\text {mat}}\quad` material fracture toughness

{math}`K_{r} \quad` fracture ratio

{math}`K_{\text {res}} \quad` stress intensity factor for residual stresses

{math}`K_{s} \quad` stress intensity factor for the applied total stress $S$

{math}`L_{r} \quad` plastic collapse ratio

{math}`M_{k} \quad` stress intensity magnification factor accounting for the stress concentration due to the weld geometry

{math}`N \quad` number of stress cycles to failure at a constant amplitude stress range {math}`\Delta S$

{math}`R_{S} \quad` stress ratio (minimum stress divided by maximum)

{math}`R \quad` normalised fracture toughness resistance parameter

{math}`T_{\min } \quad` minimum operating temperature

{math}`T_{0} \quad` temperature variability of {math}`T_{27 \mathrm{~J}}$

{math}`T_{27 J} \quad` temperature corresponding to a {math}`\mathrm{CVN}` of {math}`27 \mathrm{~J}`

{math}`X\quad` random variable vector

{math}`Y \quad` stress intensity correction factor

{math}`\lambda \quad` Weibull shape parameter

{math}`\sigma \quad` Weibull scale parameter

{math}`\varepsilon \quad` statistical error in S-N curve

{math}`\rho \quad` plasticity correction factor

{math}`\eta \quad` parameter in fracture criterion

{math}`\xi \quad` thickness correction exponent

{math}`\sigma\quad` stress, including stress concentrations due to the joint geometry

{math}`\sigma_{\text {net }} \quad` net section stress (function of the crack size)

{math}`\sigma_{\text {res }} \quad` residual stresses

{math}`\sigma_{y} \quad` yield stress

{math}`\Delta \quad` range operator

{math}`\Phi \quad` complete elliptic integral of the second kind

**Subscripts:**

cr {math}`\quad` limiting or critical value

o {math}`\quad` initial value

tr {math}`\quad` transition value

0 {math}`\quad` threshold value

glob {math}`\quad` global stress analysis

scf {math}`\quad` stress concentration factor

sif {math}`\quad` stress intensity factor

{math}`\mathrm{n} \quad` number of cycles

{math}`\mathrm{m} \quad` membrane

b {math}`\quad` bending

ref {math}`\quad` reference value

## Scope

This chapter is concerned with the treatment of fatigue in metallic structures with particular emphasis on welded joints. The document is applicable to structures such as buildings, bridges, offshore structures, masts, cranes etc., in which the fatigue damage is caused by the cyclic action of wind, waves, traffic or mechanical vibrations. Low-cycle fatigue, which may occur for example due to an earthquake, is not treated.

In this document three different approaches to the formulation of the fatigue limit state will be considered, respectively based on:

1) {math}`S-N` lines in combination with Miner's Damage accumulation rule;

2) a fatigue crack growth model;

3) a fatigue crack growth model in combination with fracture resistance.

The models presented to not include the situation following a crack through situation of the wall thickness. The fatigue loading is characterised by the number of stress cycles and the magnitude of stress range for each cycle. A probabilistic description of stress ranges can be developed if the stochastic properties of the stress process over the entire lifetime of the structure are known. For some models the expectation of the {math}`m^{\text {th }}` moment of the arbitrary point in time distribution of the stress is sufficient.

This chapter is based on BS 7910:2005 as far as possible.

## S-N-approach

**Damage model**

An {math}`S - N` curve is a relation between the stress range under constant amplitude loading and the number of stress cycles to failure. The standard {math}`S-N` curve can be expressed in the form of:

```{math}
:label: eq-fatigue-2.1
N \Delta \sigma^{m}=K
```

where {math}`N` is the number of stress cycles to failure at a constant amplitude stress range {math}`\Delta \sigma, K` and {math}`m` are the material parameters. In order to deal with variable amplitude loading in the {math}`S-N` approach, fatigue damage is quantified in terms of Miner's damage summation. According to this rule all stress cycles cause proportional fatigue damage, which is linearly additive. For an ergodic variable stress process, the scatter in the stress history may be neglected and the damage {math}`D_{\mathrm{n}}` due to {math}`n` cycles is given by:

```{math}
:label: eq-fatigue-2.2
D_{n}=E(n)\left[\frac{1}{K} E\left[\Delta \sigma^{m}\right]\right]
```

{math}`E[..]` denotes the expectation operator. Some elaborations are given in [Annex B](annex-B-fatigue). According to this model failure occurs nominally when {math}`D_{\mathrm{n}}` is equal to unity.

In most cases a model with two lines is being used, having parameters {math}`K_{1}, K_{2}, m_{1}` and {math}`m_{2}`. The stress range level {math}`\Delta \sigma_{t r}` at which the two lines intersect (transition point) is defined by:

```{math}
:label: eq-fatigue-2.3
\Delta \sigma_{\mathrm{tr}}=\left\lbrace\frac{K_{2}}{K_{1}}\right\rbrace^{1 /\left(m_{2}-m_{1}\right)}
```

In case of two branches {eq}`eq-fatigue-2.2` is transformed into:

```{math}
:label: eq-fatigue-2.4
D_{n}=E(n)\left[\frac{1}{K_{1}} E\left[\Delta \sigma^{m_{1}}\right]_{\Delta \sigma_{0}}^{\Delta \sigma_{t r}} C_{g l o b}^{m_{1}}~C_{s c f}^{m_{1}}+\frac{1}{K_{2}} E\left[\Delta \sigma^{m_{2}}\right]_{\Delta \sigma_{t r}}^{\infty} C_{g l o b}^{m_{2}}~C_{s c f}^{m_{2}}\right]
```

The expectation operator {math}`E[..]` in this case is defined by:

```{math}
:label: eq-fatigue-2.5
E\left[\Delta \sigma^{m}\right]_{A}^{B}=\int_{A}^{B} s^{m} f_{\Delta \sigma}(s) d s
```

where {math}`f_{\Delta \sigma}(s)` is the probability density function of the stress ranges {math}`\Delta \sigma`. The integration limit {math}`\Delta \sigma_{0}` represents the fatigue limit (if present) and {math}`\Delta \sigma_{\mathrm{tr}}` the transition point defined by {eq}`eq-fatigue-2.3`. Further, in this approach {math}`C_{\text {glob }}` and {math}`C_{s i f}` have been added as the model uncertainties in the global and local stress analysis, respectively.

The effects of weld geometry, residual stresses and through thickness stress variation are implicitly included in the values of {math}`K` and {math}`m`. The effect of factors such as, plate thickness, environment, weld toe grinding and post-weld heat treatment, etc. is accounted through appropriate corrections to the basic {math}`S-N` curve. For instance, a plate thickness correction factor may be given by:

```{math}
:label: eq-fatigue-2.6
a_{c o r}=\left[\frac{B}{B_{r e f}}\right]^{m \xi}
```

where {math}`\xi` is the thickness correction exponent on stress, {math}`B` is the thickness of the plate and {math}`B_{\text {ref }}` is the reference plate thickness.

**Limit state formulation for SN-approach:**

The limit state function may be given by:

```{math}
:label: eq-fatigue-2.7
\mathrm{g}(\boldsymbol{X}, t)=D_{\mathrm{cr}}-D_{\mathrm{n}}
```

where {math}`\boldsymbol{X}` is the vector of random variables, {math}`t` the time, {math}`D_{\text {cr }}` is Miner's Damage sum at failure, which may deviate systematically and randomly from 1.0 and {math}`D_{\mathrm{n}}` is the damage due to {math}`n` cycles.

## Fracture Mechanics Approach

**Crack Growth model**

The fatigue crack growth model is the bi-linear version (see {numref}`fig-fatigue-3.1`) of the model by Paris \& Erdogan (1963):

```{math}
:label: eq-fatigue-3.1
\begin{aligned}
& \frac{d a}{d N}=A_{1}(\Delta K)^{m_{1}} \quad \text { for } \Delta K_{0}<\Delta K \leq \Delta K_{t r} \\ \\
& \frac{d a}{d N}=A_{2}(\Delta K)^{m_{2}} \quad \text { for } \Delta K_{t r}<\Delta K
\end{aligned}
```

where {math}`a` is the crack depth, {math}`d a / d N` is the instantaneous crack propagation rate and {math}`\Delta K` is the stress intensity factor (SIF) range at the crack tip, {math}`\Delta K_{0}` a threshold value below which the crack is assumed to be nonpropagating; {math}`A_{i}` and {math}`m_{i}` are material constants which can be determined from experiments. {math}`\Delta K_{t r}` is the value at the transition point.

```{figure} ../part-03/images/fig-fatigue-3.1.jpg
:name: fig-fatigue-3.1

Schematic representation of typical crack growth rates with linear and bi-linear approximations
```

The stress intensity factor {math}`K` for a given applied (fluctuating) stress {math}`\sigma` is given as:

```{math}
:label: eq-fatigue-3.2
K=\sigma Y \sqrt{\pi a}
```

The stress {math}`\sigma` should be determined from the applied loading in the vicinity of the crack location (but not influenced by the crack or the details of the weld). It does, however, include the stress concentration, resulting from the global geometry of the joint. The stress intensity correction factor {math}`Y` depends on the crack size normalised with respect to other relevant local dimensions (e.g. plate thickness) and the nature of stress distribution. For details on {math}`Y`, see [Annex A](annex-A-fatigue).

The through-thickness distribution of this stress is often assumed to consist of 'membrane' and 'bending' components and is characterised in terms of the ratio of the bending stress to the total stress, called 'degree-of-bending':

```{math}
:label: eq-fatigue-3.3
K=\left(\sigma_{m} Y_{m}+\sigma_{b} Y_{b}\right) \sqrt{\pi a}
```

where the subscripts ' {math}`m` ' and ' {math}`b` ' refer to membrane and bending components respectively.

For welded joints micro-cracks often initiate from surface-breaking defects at the toe of the weld. These microcracks tend to coalesce to form a single, dominant fatigue crack of roughly semi-elliptical shape. Hence, semielliptical cracks in plated structures are of interest in many practical applications ({numref}`fig-fatigue-3.2`). In this case, two crack dimensions, the depth {math}`a` and the half-length at the surface {math}`c`, become relevant both of which are functions of the fatigue loading process.

```{figure} ../part-03/images/fig-fatigue-3.2.jpg
:name: fig-fatigue-3.2

A semi-elliptical crack in a steel plate at/near the weld toe
```

For each principal direction of crack growth a Paris type expression may be formulated,

```{math}
:label: eq-fatigue-3.4
\begin{aligned}
& \frac{d a}{d N}=A\left(\Delta K_{a}\right)^{m} \text { for } \Delta K_{a}>\Delta K_{0} \\
& \frac{d c}{d N}=A\left(\Delta K_{c}\right)^{m} \text { for } \Delta K_{c}>\Delta K_{0}
\end{aligned}
```

where the first expression relates to point {math}`\mathrm{A}` and growth in the depth direction, whereas the second expression relates to point {math}`\mathrm{C}` and growth in the length direction (see figure {numref}`fig-fatigue-3.2`). For each of these points, the stress intensity factor range, {math}`\Delta K_{a}` and {math}`\Delta K_{c}`, is given by

```{math}
:label: eq-fatigue-3.5
\begin{aligned}
& \Delta K_{a}=\Delta \sigma Y_{a} \sqrt{\pi a} \\
& \Delta K_{c}=\Delta \sigma Y_{c} \sqrt{\pi a}
\end{aligned}
```

where {math}`\Delta \sigma` is the applied stress range and {math}`Y_{a}, Y_{c}` are stress intensity correction factors for points {math}`\mathrm{A}` and {math}`\mathrm{C}` respectively.

Once equations {eq}`eq-fatigue-3.5` are substituted into {eq}`eq-fatigue-3.4`, a pair of coupled differential equations is obtained. With the exception of the material parameters ({math}`A` and {math}`m` ) and the applied stress range {math}`\Delta \sigma`, all other terms are a function of the crack size {math}`(a, c)`, which clearly changes during the fatigue loading process.

**Limit state formulations**

Using the fracture mechanics approach, the time dependent limit state function can be formulated as

```{math}
:label: eq-fatigue-3.6
g(\boldsymbol{X}, t)=a_{c r}-a(t)
```

where {math}`\boldsymbol{X}` is the vector of random variables, {math}`a_{c r}` is a limiting crack depth (for example plate thickness) and {math}`a(t)` is the crack depth after a service exposure of time {math}`t`. At {math}`t=0` the crack size has an initial value {math}`a_{0}`. The calculation of the crack size at time {math}`t` is not trivial as the stress is a random process. Assuming for {math}`\Delta \sigma` a sufficiently mixing (ergodic) process we may use the expectation of the stress range to find the expectation of {math}`d a / d N` (conditional upon the stress and fatigue model):

```{math}
:label: eq-fatigue-3.7
\begin{aligned}
E\left(\frac{d a}{d N}\right)= & A_{1} E\left[\Delta \sigma^{m_{1}}\right]_{\Delta \sigma_{0}}^{\Delta \sigma_{t r}}\left(C_{g l o b}~C_{s c f}~C_{s i f}~Y_{a}~\sqrt{\pi a}\right)^{m_{1}}+ \\
& +A_{2} E\left[\Delta \sigma^{m_{2}}\right]_{\Delta \sigma_{t r}}^{\infty}\left(C_{g l o b}~C_{s c f}~C_{s i f}~Y_{a}~\sqrt{\pi a}\right)^{m_{2}}
\end{aligned}
```

where {math}`C` are model uncertainty factors for the various stress calculations (global analysis, stress concentration and stress intensity factor) and:

```{math}
:label: eq-fatigue-3.8
E\left[\Delta \sigma^{m}\right]_{A}^{B}=\int_{A}^{B} s^{m} f_{\Delta \sigma}(s) d s
```

where {math}`f_{\Delta \sigma}(s)` is the probability density function of the stress ranges {math}`\Delta \sigma`.

In general, the above integral is evaluated through an incremental numerical procedure, which involves subdivision of the total time into a number of steps. At each step, following the evaluation of equation {eq}`eq-fatigue-3.8` for the crack depth {math}`a`, the second crack dimension {math}`c` is computed as well, using a similar set of equations. In that case, however, the value {math}`Y_{\mathrm{a}}` is replaced by {math}`Y_{\mathrm{c}}`. As both {math}`a` and {math}`c` are simultaneously present in {math}`Y`, the two differential equations are coupled.

When the fatigue life of a fatigue sensitive detail is required, the critical crack size may for instance be taken as the plate thickness, but also as a critical value {math}`a_{\text {cr }}` determined through the application of a fracture criterion. In that case the maximum crack size, {math}`a_{c r}` that can be sustained by the component will depend on the material's yield strength and fracture toughness {math}`K_{\text {mat }}`. The limit state function with respect to fracture can be formulated as:

```{math}
:label: eq-fatigue-3.9
g(\mathbf{X}, t)=\min _{t} f\left(K_{r}, L_{r}\right)
```

where {math}`\boldsymbol{X}` is the vector of random variables as a function of the time {math}`t, K_{r}` is the fracture ratio, {math}`L_{r}` is a measure of the proximity to plastic collapse and {math}`f()` is an appropriate interaction criterion, as for example (see {numref}`fig-fatigue-3.3`) given in BS 7910 (BSI, 2005) or (see {numref}`fig-fatigue-3.3`) Dijkstra (1991) as:

```{math}
:label: eq-fatigue-3.10
f\left(K_{r}, L_{r}\right)=R-\sqrt{ }\left(K_{r}^{2}+L_{r}^{2}\right)
```

In this approach failure occurs when a stress cycle arrives that causes the reduced load bearing capacity of the cross section to be exceeded. The residual load bearing capacity depends on the actual crack size $a$ and the interaction between the plastic and the brittle fracture failure modes. To evaluate the failure probability on the basis of {eq}`eq-fatigue-3.9` a time variant reliability method like the out-crossing approach is needed.

```{figure} ../part-03/images/fig-fatigue-3.3.jpg
:name: fig-fatigue-3.3

{math}`K_{r}-L_{r}` interaction curves according to BS 7910 (above) and Dijkstra (below)
```

In {eq}`eq-fatigue-3.10` the variable {math}`R` is a normalised resistance parameter (nominally equal to 1.0) and the quantities {math}`K_{r}` and {math}`L_{r}` are defined as follows:

```{math}
:label: eq-fatigue-3.12
K_{r}=\frac{K_{I}}{K_{m a t}}+\rho \text { and } L_{r}=\frac{\sigma_{n e t}}{\sigma_{y}}
```

where

{math}`K_{\text {mat }}\quad`  material toughness measured by stress intensity factor  

{math}`K_{I} \quad`  stress intensity factor: {math}`K_{I}=(Y \sigma) \sqrt{\pi a}` 

{math}`\rho \quad`  plasticity correction factor 

{math}`\sigma_{\text {net }}\quad`  net section stress (function of the crack size) 

{math}`\sigma_{\mathrm{y}} \quad` yield stress

The factor {math}`\rho` may be determined by the following procedure. For {math}`\chi=K_{\mathrm{I}}^{\mathrm{s}}~L_{\mathrm{r}} / K_{\mathrm{I}}^{\mathrm{p}}>4` an interpolating technique need to be applied (see BS 7910, 2005). For {math}`\chi \leq 4` we have:

```{math}
:label: eq-fatigue-3.13
\begin{array}{lll}
\rho=\rho_{1} & \text { for } & L_{\mathrm{r}} \leq 0.8 \\
\rho=4 \rho_{1}\left(1.05-\mathrm{L}_{\mathrm{r}}\right) & \text { for } & 0.8<L_{r}<1.05 \\
\rho=0 & \text { for } & L_{\mathrm{r}} \geq 1.05
\end{array}
```

with

```{math}
:label: eq-fatigue-3.14
\rho_{1}=0.1 \chi^{0.714}-0.007 \chi^{2}+3 * 10^{-5} \chi^{5}
```

The crack size {math}`a` may be determined from the fatigue crack growth models described above. The plasticity correction factor {math}`\rho` reflects the interaction between the applied load (giving rise to the stress intensity factor {math}`K`) and the residual stresses (giving rise to the stress intensity factor {math}`K_{I}^{S}` ). Different residual stress profiles for various cracked geometries and restraint conditions may be assumed but their use implies that {math}`K_{I}^{s}` would need to be evaluated using either finite element techniques or the weight function method. A simplified (and conservative) method would be to approximate the residual stress field via a linear stress field subtended from the surface and crack tip stress values. The corresponding {math}`K_{I}^{s}` can then be obtained by superposition of the tensile and bending solutions for the geometry in question.

Further details of this approximation are given by Tada et al. (2000). If the bending solution is not known, in which case the previously mentioned procedure cannot be applied, the residual stress field may be assumed to be uniform. This approach will, in general, yield very conservative results for deep cracks and less conservative results for shallow cracks.

## Probabilistic models

{numref}`tbl-fatigue-3.1` gives an overview of all random variables and their probabilistic models. There are four blocks: one for the {math}`S-N` parameters, one for the Fracture Mechanics parameters, one for the stress analysis and one for the Weibull stress process approximation. Additional commentary is given below:

***{math}`S- N` curve parameters***

The stochastic model for the parameters in the {math}`S-N`-based approach can be estimated as follows:

Step 1: For the fatigue detail considered, find (as good as possible) the corresponding detail and test data in the EC3 Background Document prEN 1993-1-9. RWTH, Aachen, 2002.

Step 2: Fit test data to a linear {math}`S-N`-model: {math}`\log N=\log C-m \log \Delta \sigma+\varepsilon` where {math}`N` is the number of cycles to failure with stress range {math}`\Delta \sigma, \varepsilon` is normally distributed with expected value 0 and standard deviation {math}`\sigma_{\varepsilon}`. The parameters {math}`\log C, m` and {math}`\sigma_{\varepsilon}` are fitted to the test data using the Maximum Likelihood Method including run-outs (no-failure tests) in the likelihood.

Step 3: The statistical uncertainty related to the parameter fits can be estimated using the Hessian of the Loglikelihhod function, and included in a reliability analysis.

A bilinear {math}`S-N`-model can be fitted in a similar way. Usually {math}`m` can be assumed fixed to 3 or 5 .

***Miner's sum at failure***

Due to the random nature of fatigue damage, Miner's damage sum at failure {math}`\left(D_{c r}\right)` is not necessarily always exactly unity. It should therefore be treated as a random variable expressing the shortcomings of Miner's rule. Wirsching (1984) suggests that {math}`D_{\text {cr }}` be modelled as a lognormal variable with a mean of unity and coefficient of variation of 0.3 .

***Crack growth parameters***

When a simple Paris type crack propagation model is used, a random variable description for {math}`A`, is usually adequate. In this approach, the crack growth parameter {math}`A` in the Paris law, can be used to describe the scatter in crack propagation data. The parameter {math}`A` will in general depend on the applied stress ratio ( {math}`=\sigma_{\min } / \sigma_{\max }` ) and the environmental conditions and is well described by a lognormal model with coefficient of variation typically in the range of 0.3 - 0.4. In the table the option to use a two branch model has been opened. For a one branch model one uses only {math}`m_{2}` and {math}`A_{2}`. When a cut-off to crack growth {math}`\Delta K_{0}` is adopted, {math}`\Delta K_{0}` is lognormally distributed with a mean of {math}`140 \mathrm{Nmm}^{-3 / 2}` and a coefficient of variation {math}`\mathrm{V}=0.4` (Austen, 1983). In the case of freely corroding steels {math}`\Delta K_{0}=0`.

***Initial defect size***

The distribution of defect sizes should be based on defects existing in a structure entering service and includes those defects that are considered acceptable according to quality control standards, as well as those that remain undetected during fabrication. Thus defect occurrence rate, the amount and quality of NDE used, should be taken into account in developing a distribution for weld defect size. From the limited data available, the mean value and standard deviation of weld defect depth {math}`a_{0}` can be estimated to be 0.15 mm and 0.10 mm for "sound" quality welds. Lognormal, exponential and Weibull distributions have been used by researchers to fit weld defect data. Similarly, initial defect aspect ratio, defined as the ratio of initial defect depth to defect semi-length ( {math}`a / c` ) may also be modelled as a lognormal variable with a mean of 0.62 and coefficient of variation of 0.4 , Kountouris and Baker (1989).

***Fatigue crack propagation model***

The fatigue crack propagation model involves a number of parameters, which are subject to uncertainty. It is convenient to express all sources of uncertainty through a single basic variable {math}`C_{\text {sif }}`, which gives the ratio of stress intensity geometry factor obtained by experiment to that computed using the proposed model. The statistics for this variable can be developed by comparison with experimental compliance function curves. The factor {math}`C_{\text {sif }}` can be modelled as a lognormal variable with a mean of unity and coefficient of variation typically in the range of 0.15 - 0.25. Lower variability may be used if the stress intensity factors are computed using finite element models such as line-spring and weight function models.

***Fracture Toughness***

For the fracture toughness {math}`K_{\text {mat }}` a three-parameter Weibull distribution is proposed to describe fracture toughness related to cleavage fracture (Burdekin \& Hamour, 2000; Lukić \& Cremona, 2001; Righiniotis \& Chryssanthopoulos, 2003):

```{math}
:label: eq-fatigue-4.1
F_{K_{\text {mat }}}(k)=1-\exp \left[-\left(\frac{k-K_{0}}{\sigma}\right)^{\lambda}\right]
```

where

{math}`\lambda` is the shape parameter, taken as 4 on the basis of experiments (Wallin, 1984).

{math}`K_{0}` is the threshold parameter, recommended is {math}`20 \mathrm{MPa}~\mathrm{m}{ }^{1 / 2}` (Burdekin \& Hamour, 2000).

{math}`\sigma` is the scale parameter and may be obtained from the following correlation attributed to Wallin (Burdekin \& Hamour, 2000):

```{math}
:label: eq-fatigue-4.2
\sigma=\left\lbrace 11+77\left[\exp \left(\frac{T-T_{27 J}+T_{0}}{52}\right)\right]\right\rbrace \left(\frac{25}{B}\right)^{1 / 4}\left(\mathrm{~K}_{\mathrm{mat}}\right. \text{in} \left.\mathrm{MPa}~\mathrm{m}{ }^{1 / 2}\right)
```

where:

{math}`T \quad` operating temperature {math}`\left({ }^{\circ} \mathrm{C}\right)` (random FBC process: {math}`\mu=10^{\circ} \mathrm{C}, \sigma=8^{\circ} \mathrm{C}, \Delta=10` days)

{math}`T_{27 \mathrm{~J}} \quad` temperature ({math}`\left({ }^{\circ} \mathrm{C}\right.` ) corresponding to a {math}`\mathrm{CVN}` of {math}`27 \mathrm{~J}` (safe value)

{math}`T_{0} \quad` temperature (random variability of {math}`\mathrm{T}_{27 \mathrm{~J}}: \mu=18^{\circ} \mathrm{C}, \sigma=15^{\circ} \mathrm{C}` )

{math}`B \quad` plate thickness in {math}`[\mathrm{mm}]`

$$ \text{Units:}~\mathbf{m m}~\text{and}~\mathbf{N} $$

```{table} Probabilistic models for the random variables
:name: tbl-fatigue-3.1
| Variable |  | Distribution | Mean | {math}`\mathbf{V}` |  |
| :---: | :---: | :---: | :---: | :---: | :---: |
| {math}`C` | Material parameter S-N curve | lognormal | {math}`1.0 \cdot 10^{13}` | 0.58 |  |
| {math}`m` | Slope value |  | 3 | - |  |
| {math}`\log C_{1}` | Material parameter 2 par {math}`\mathrm{S}-\mathrm{N}` curve | normal | Depends |  | {math}`C_{1}` and {math}`C_{2}` fully <br> correlated |
| {math}`\log C_{2}` | Material parameter 2 par {math}`\mathrm{S}-\mathrm{N}` curve | normal | Depends |  | {math}`C_{1}` and {math}`C_{2}` fully <br> correlated |
| {math}`m_{1}` (air) | Slope value {math}`1^{\text {st }}` branch | deterministic | 5 | - |  |
| {math}`m_{2}` (air) | Slope value {math}`2^{\text {nd }}` branch | deterministic | 3 | - |  |
| {math}`D_{c r}` | Miner's sum at failure | lognormal | 1.0 | 0.3 |  |
| {math}`A_{1}` (air) {math}`^{*}` | Paris Law Parameter 1 | lognormal | {math}`4.80 \cdot 10^{-18}` | 1.70 |  |
| {math}`A_{2}` (air) {math}`^{*}` | Paris Law Parameter 2 | lognormal | {math}`5.86 \cdot 10^{-13}` | 0.60 |  |
| {math}`m_{1}` (air) | Slope value {math}`1^{\text {st }}` branch | deterministic | 5.10 | - |  |
| {math}`m_{2}` (air) | Slope value {math}`2^{\text {nd }}` branch | deterministic | 2.88 | - <br> - |  |
| {math}`\Delta K_{0}` ( air ) | Threshold value for {math}`\Delta K` | lognormal | 140 | 0.40 |  |
| {math}`A_{1}` (marine) {math}`^{*}` | Paris Law Parameter 1 | lognormal | {math}`5.37 \cdot 10^{-14}` | 1.10 |  |
| {math}`A_{2}` (marine) {math}`^{*}` | Paris Law Parameter 2 | lognormal | {math}`5.67 \cdot 10^{-7}` | 0.16 |  |
| {math}`m_{1}` (marine) | Slope value {math}`1^{\text {st }}` branch | deterministic | 3.42 | - <br> - |  |
| {math}`m_{2}` (marine) | Slope value {math}`2^{\text {nd }}` branch | deterministic | 1.11 | - |  |
| {math}`\Delta K_{0}` (marine) | Threshold value for {math}`\Delta K` | lognormal | 0.0 | - <br> - |  |
| {math}`a_{0}` | Initial crack depth | lognormal | 0.15 | 0.66 |  |
| {math}`a_{0} / c_{0}` | Initial aspect ratio | lognormal | 0.62 | 0.40 |  |
| {math}`B_{\text {glob }}` | MU global stress model {math}`{ }^{*}` | lognormal | 1.0 | 0.10 |  |
| {math}`B_{\text {scf }}` | MU stress concentration | lognormal | 1.0 | 0.20 |  |
| {math}`B_{\text {sif }}` | MU stress intensity factor (hand) | lognormal | 1.0 | 0.20 |  |
| {math}`B_{\text {sif }}` | MU stress intensity factor (FEM) | lognormal | 1.0 | 0.07 |  |
| {math}`\sigma_{\text {res }}` | Residual stresses | lognormal | 300 | 0.20 |  |
| {math}`R` | Resistance fracture toughness | lognormal | 1.7 | 0.18 |  |
| {math}`K_{\mathrm{mat}}` | Fracture toughness | Weibull | See {eq}`eq-fatigue-4.1` | See {eq}`eq-fatigue-4.1` |  |
```
*stress ratio {math}`\sigma_{\min } / \sigma_{\max } \geq 0.5`  
{math}`{ }^{* *} \mathrm{MU}=` Model Uncertainty

(annex-A-fatigue)=
## Annex A: The stress intensity correction factor {math}`Y`

The stress intensity correction factor {math}`Y` for membrane loading is determined with the procedure of Newman and Raju (1981) and BS 7910:2005. For the stress intensity correction factor in general they propose:

```{math}
Y=M f_{w} M_{m} M_{k}
```

Factor {math}`M_{k}` accounts for the local stress concentration and is provided in [Annex A.2](annex-A.2-fatigue). The other factors are provided in [Annex A.1](annex-A.1-fatigue). The resulting factors Ya and Yc (in height and width directions) are provided in [Annex A.3](annex-A.3-fatigue)

(annex-A.1-fatigue)=
**A1. The factors {math}`M, M_{m}` and {math}`f_{w}`**

The equations and values provided below apply to membrane loading on flat plates with semi-elliptical cracks.

The factor {math}`M` accounts for bulging effects. For flat plates, {math}`M=1`.

The finite-width correction function {math}`f_{w}` is given by:

```{math}
f_{w}=\left[\sec \left(\frac{\pi c}{W} \sqrt{\frac{a}{B}}\right)\right]^{1 / 2} \quad \text { for }(2 c / W) \leq 0.8
```

The stress intensity magnification factor for semi-elliptical cracks loaded in bending is equal to:

```{math}
M_{m}=\left[M_{1}+M_{2}\left(\frac{a}{B}\right)^{2}+M_{3}\left(\frac{a}{B}\right)^{4}\right] g f_{\theta} / \Phi
```

Where:

```{math}
M_{m}=\left[M_{1}+M_{2}\left(\frac{a}{B}\right)^{2}+M_{3}\left(\frac{a}{B}\right)^{4}\right] g f_{\theta} / \Phi
```

$$
\begin{array}{ll}
M_{1}=1.13-0.09(a / c) & \text { for } 0 \leq a / 2 c \leq 0.5 \\ \\
M_{1}=\sqrt{(c / a)}[1+0.04(c / a)] & \text { for } 0.5<a / 2 c \leq 1.0 \\ \\
M_{2}=\frac{0.89}{0.2+(a / c)}-0.54 & \text { for } 0 \leq a / 2 c \leq 0.5 \\ \\
M_{2}=0.2(c / a)^{4} & \text { for } 0.5<a / 2 c \leq 1.0 \\ \\
M_{3}=0.5-\frac{1.0}{0.65+(a / c)}+14[1.0-(a / c)]^{24} & \text { for } a / 2 c \leq 0.5 \\ \\
M_{3}=-0.11(c / a)^{4} & \text { for } 0.5<a / 2 c \leq 1.0 \\ \\
g=1+\left[0.1+0.35(a / B)^{2}\right](1-\sin \theta)^{2} & \text { for } a / 2 c \leq 0.5 \\ \\
g=1+\left[0.1+0.35(c / a)(a / B)^{2}\right](1-\sin \theta)^{2} & \text { for } 0.5<a / 2 c \leq 1.0
\end{array}
$$

The function {math}`f_{\theta}`, an angular function from the embedded elliptical-crack solution, is:

$$
\begin{array}{ll}
f_{\theta}=\left[(\mathrm{a} / \mathrm{c})^{2} \cos ^{2} \theta+\sin ^{2} \theta\right]^{1 / 4} & \text { for } 0 \leq a / 2 c \leq 0.5 \\
f_{\theta}=\left[(\mathrm{c} / \mathrm{a})^{2} \sin ^{2} \theta+\cos ^{2} \theta\right]^{1 / 4} & \text { for } 0.5<a / 2 c \leq 1.0
\end{array}
$$

The complete elliptic integral of the second kind {math}`\Phi` is given by:

$$
\begin{array}{ll}
\Phi=\sqrt{1+1.464\left(\frac{a}{c}\right)^{1.65}} & \text { for } 0 \leq a / 2 c \leq 0.5 \\
\Phi=\sqrt{1+1.464\left(\frac{c}{a}\right)^{1.65}} & \text { for } 0.5<a / 2 c \leq 1.0
\end{array}
$$

The definitions of {math}`a, c` and {math}`\theta` are provided in {numref}`fig-fatigue-A.1`.

```{figure} ../part-03/images/fig-fatigue-A.1.jpg
:name: fig-fatigue-A.1

Semi-elliptical crack geometry near weld toe
```

(annex-A.2-fatigue)=
**A2. The weld geometry factor {math}`M_{k}`**

The weld geometry {math}`M_{k}` has to be incorporated if the crack is affected by a local stress concentration due to welding. The general formula is given by:

```{math}
M_{k}=D(a / B)^{k 1}~(L / B)^{k 2} \qquad M_{k}>1
```

The parameters {math}`D` and {math}`k` depend on the structural and weld geometry as discribed by {math}`a, B` and {math}`L`. For butt welds and X-joints a set of formulas for {math}`M_{\mathrm{ka}}` values was derived by Maddox et al. (1986). These formulas are valid for weld toe angle {math}`\Theta=45^{\circ}` and weld toe radius {math}`\rho=0`. The functions and the range of applicability are given in {numref}`tbl-fatigue-A.2.1`.

```{table} Stress intensity concentration factors $(M_{\mathrm{ka}}$ ) for butt welds and X-joints
:name: tbl-fatigue-A.2.1
| Loading <br> mode | Applicability |  | Stress intensity <br> concentration factor   |
| :---: | :---: | :---: | :---: |
|  | {math}`L / B` | {math}`a / B` | {math}`M_{\mathrm{ka}}=\mathrm{f}_{\mathrm{L}}(a / B, L / B)` |
| axial | {math}`\leq 2` | {math}`\leq 0.05(L / B)^{0.55}` | {math}`0.51(L / B)^{0.27}(a / B)^{-0.31}` |
| axial | {math}`\leq 2` | {math}`>0.05(L / B)^{0.55}` | {math}`0.83(a / B)^{-0.15(L / B)^{0.46}}` |
| axial | {math}`>2` | {math}`\leq 0.073` | {math}`0.615(a / B)^{-0.31}` |
| axial | {math}`>2` | {math}`>0.073` | {math}`0.83(a / B)^{-0.20}` |
| bending | {math}`\leq 1` | {math}`\leq 0.03(L / B)^{0.55}` | {math}`0.45(L / B)^{0.21}(a / B)^{-0.31}` |
| bending | {math}`\leq 1` | {math}`>0.03(L / B)^{0.55}` | {math}`0.68(a / B)^{-0.19(L / B)^{0.21}}` |
| bending | {math}`>1` | {math}`\leq 0.03` | {math}`0.45(a / B)^{-0.31}` |
| bending | {math}`>1` | {math}`>0.03` | {math}`0.68(a / B)^{-0.19}` |
```
{math}`a=` crack depth, {math}`B=` plate thickness and {math}`L=` size of the node, defined acc. to {numref}`fig-fatigue-A.2`.

For {math}`M_{\mathrm{kc}}` we may use the same formulas, however substitute {math}`a=0,15 \mathrm{~mm}` (See BS 7910:2005).

```{figure} ../part-03/images/fig-fatigue-A.2.jpg
:name: fig-fatigue-A.2

Definition of node length L for two weld details
```

(annex-A.3-fatigue)=
**A3. The stress intensity correction factors {math}`Y_{a}` and {math}`Y_{c}`**

For the factor {math}`Y_{a}` it holds that {math}`\theta=\pi / 2`, therefore:

```{math}
g=1 \quad ; \quad f_{\theta}=1 \text { for } 0 \leq a / 2 c \leq 0.5 \text { and } f_{\theta}=\sqrt{(c / a)} \quad\text { for } 0.5<(a / 2 c) \leq 1.0
```

For {math}`Y_{\mathrm{c}}` with {math}`\theta=0` it follows:

```{math}
g=1.1+0.35(a / \mathrm{B})^{2} ; \quad f_{\theta}=\sqrt{a / c} \quad \text { for } 0 \leq a / 2 c \leq 0.5 \quad \text { and } \quad f_{\theta}=1 \quad \text { for } 0.5<(a / 2 c) \leq 1.0
```

Both factors finally become:

```{math}
\begin{array}{ll}
Y_{a}=M_{k a}\left[M_{1}+M_{2}\left(\frac{a}{B}\right)^{2}+M_{3}\left(\frac{a}{B}\right)^{4}\right] f_{w} / \Phi & \text { for } 0 \leq a / 2 c \leq 0.5 \\
Y_{a}=M_{k a}\left[M_{1}+M_{2}\left(\frac{a}{B}\right)^{2}+M_{3}\left(\frac{a}{B}\right)^{4}\right] f_{w} \sqrt{(c / a)} / \Phi & \text { for } 0.5<(a / 2 c) \leq 1.0 \\
Y_{c}=M_{k c}\left[M_{1}+M_{2}\left(\frac{a}{B}\right)^{2}+M_{3}\left(\frac{a}{B}\right)^{4}\right] f_{w}\left\lbrace 1.1+0.35(\mathrm{a} / \mathrm{B})^{2}\right\rbrace \sqrt{(c / a)} / \Phi & \text { for } 0 \leq a / 2 c \leq 0.5 \\
Y_{c}=M_{k c}\left[M_{1}+M_{2}\left(\frac{a}{B}\right)^{2}+M_{3}\left(\frac{a}{B}\right)^{4}\right] f_{w}\left\lbrace 1.1+0.35(\mathrm{a} / \mathrm{B})^{2}\right\rbrace / \Phi & \text { for } 0.5<(a / 2 c) \leq 1.0
\end{array}
```

(annex-B-fatigue)=
## Appendix B: Fatigue Loading evaluation

In the {math}`S-N` approach as well as in the Fracture Mechanics approach the loading term contains the expectation of the {math}`m^{\text {th }}` moment of the (ergodic part) of the stress distribution.

**B1 Narrow band**

**Rayleigh distribution**

If the stress spectrum is Gaussian and narrow-banded it can be shown that the peaks of the stress process, and hence the stress ranges, follow a Rayleigh distribution. For this case the {math}`m^{\text {th }}` moment of the stress range density function can be obtained as:

```{math}
E\left[\Delta S^{m}\right]=(2 \sigma \sqrt{2})^{m} \Gamma\left(\frac{m}{2}+1\right)
```

where {math}`\sigma` is the standard deviation of the stress process and {math}`\Gamma()` is the Gamma function.

In case we have S-N-lines or fracture mechanics models with two branches:

```{math}
\begin{aligned}
& E\left(\Delta S^{m}\right)_{0}^{S o}=(2 \sigma \sqrt{2})^{m 1} \Gamma\left(\frac{m_{1}}{2}+1 ;\left(\frac{S_{0}}{2 \sigma \sqrt{2}}\right)^{2}\right) \\
& E\left(\Delta S^{m}\right)_{S o}^{\infty}=(2 \sigma \sqrt{2})^{m 2} \Gamma_{o}\left(\frac{m_{2}}{2}+1 ;\left(\frac{S_{0}}{2 \sigma \sqrt{2}}\right)^{2}\right)
\end{aligned}
```

**Two parameter Weibull distribution**

Assume that the stress ranges are Weibull distributed with distribution function:

```{math}
F_{\Delta s}(s)=1-\exp \left(-\left(\frac{s}{k}\right)^{\lambda}\right)
```

In that case we have for the stress expectations

```{math}
E\left(\Delta S^{m}\right)=k^{m} \Gamma\left(\frac{m}{\lambda}+1\right)
```

In case we have S-N-lines or fracture mechanics models with two branches:

```{math}
\begin{aligned}
& E\left(\Delta S^{m}\right)_{0}^{S o}=k^{m 1} \Gamma\left(\frac{m_{1}}{\lambda}+1 ;\left(\frac{S_{0}}{k}\right)^{\lambda}\right) \\
& E\left(\Delta S^{m}\right)_{S o}^{\infty}=k^{m 2} \Gamma_{o}\left(\frac{m_{2}}{\lambda}+1 ;\left(\frac{S_{0}}{k}\right)^{\lambda}\right)
\end{aligned}
```

Where {math}`\Gamma(a ; b)` denotes the Incomplete Gamma function and {math}`\Gamma_{0}(a ; b)=\Gamma(a)-\Gamma(a ; b)` the complementary Gamma function

Note that the Rayleigh distribution for the stress ranges corresponds to a Weibull distribution with {math}`\lambda=2` and {math}`\mathrm{k}=2 \sigma \sqrt{ } 2`, where {math}`\sigma` is the standard deviation of the underlying Gaussian stress process.

**B2 Broad banded processes:**

When the stress process is broad-banded, the stress cycles cannot be easily distinguished, and a convention is required for defining stress cycles. Broadly, there are two approaches available for the modelling of stress cycles of a broad-banded stress process:

***Cycle Counting Methods***

The first approach is to simulate the time history of the stress process and use one of the peak, range or rain flow counting schemes to count the stress cycles, see Dowling (1972). The rain flow counting method is seen to give a good correlation with experimental results of fatigue tests under variable amplitude loading.

***Semi-Analytical Probability Distributions***

In the second approach, analytical distributions for stress ranges of a wide banded stress process are derived empirically, like the following 5-parameter mixed Weibull distribution by Zhao and Baker (1990):

```{math}
\begin{aligned}
& f_{Y}(y)=\gamma \frac{b_{w}}{a_{w}}\left(\frac{y}{a_{w}}\right)^{b_{w}-1} \exp \left[-\left(\frac{y}{a_{w}}\right)^{b_{w}}\right]+(1-\gamma) \frac{d_{w}}{c_{w}}\left(\frac{y}{c_{w}}\right)^{d_{w}-1} \exp \left[-\left(\frac{y}{c_{w}}\right)^{d_{w}}\right] \\
& a_{w}=(8-7 \alpha)^{-1 / b} \\
& b_{w}=1.1 \quad \text { for } \quad \alpha \leq 0.9 \\
& b_{w}=1.1+9(\alpha-0.9) \quad \text { for } \quad \alpha>0.9 \\
& c_{w}=\sqrt{2} \\
& d_{w}=2 \\
& \alpha=\frac{m_{2}}{\sqrt{m_{0} m_{4}}} \\
& \gamma=\frac{1-\alpha}{1-\sqrt{2 / \pi} a_{w} \Gamma\left(\frac{1}{b_{w}}+1\right)}
\end{aligned}
```

where {math}`y=\Delta S / 2 \sigma` is the normalised stress range and {math}`\sigma` is the standard deviation or 'root mean squared' (rms) value of the stress process; {math}`m_{0}, m_{2}` and {math}`m_{4}` are the zero, second and fourth moment of the stress process.

For this distribution the {math}`m^{\text {th }}` expected value of stress range {math}`E\left[y^{m}\right]` can be calculated:

```{math}
E\left[y^{m}\right]=\gamma a_{w}^{m}~\Gamma\left(\frac{m+b_{w}}{b_{w}} ; y_{t h}\right)+(1-\gamma) c_{w}^{m}~\Gamma\left(\frac{m+d_{w}}{d_{w}} ; y_{t h}\right) \quad ; \quad y_{t h}=\frac{S_{t h}}{2 \sigma}
```

where {math}`\Gamma(\cdots ; \cdots)` is the incomplete Gamma function. When the expectation is over all stress cycles, this can be replaced by the complete Gamma function in the above expressions. In fracture mechanics {math}`S_{t h}` is defined in terms of the stress range corresponding to {math}`\Delta K_{t h}` via Eq {eq}`eq-fatigue-3.5` and can be seen as a function of the random crack depth {math}`a` and random aspect ratio {math}`a / c`. In the case of an S-N approach, the threshold may refer to some nonpropagating stress or cut off value.

## References

British Standards Institution (2000). BS7910: Guide on methods for assessing the acceptability of flaws in fusion welded structures, London.

Burdekin, F.M., Hamour, W. (2000). "Partial safety factors for SINTAP procedure", Offshore Technology Report, OTO 2000 020, HSE, London.

Dijkstra O.D. et all (1991), A fracture mechanics approach to the assessment of the remaining fatigue life of defective welded joints, IABSE Workshop, Lausanne, April 1990.

Hobbacher, A. (1993). "Stress intensity factors of welded joints", Eng. Fract. Mech., Vol. 46(2).

Lukić, M. and Cremona, C. (2001). "Probabilistic assessment of welded joints versus fatigue and fracture", J. Struct. Engg., ASCE, Vol. 127(2).

Newman, J.C. and Raju, I.S. (1981). "An empirical stress intensity factor equation for the surface crack", Engg. Fract. Mechs., Vol. 15.

Newman, J.C. and Raju, I.S. (1986). "Stress-intensity factor equations for cracks in three-dimensional finite bodies subjected to tension and bending loads", Computational Methods in the Mechanics of Fracture, S.N. Atluri (ed), Elsevier North Holland, New York.

Paris, P.C. and Erdogan, F.A. (1963). "A critical analysis of crack propagation laws", J. Basic Engineering, ASME Transactions, {math}`85 \mathrm{D}(4)`.

Righiniotis, T.D. and Chryssanthopoulos, M.K. (2003). "Probabilistic fatigue analysis under constant amplitude loading", Journal of Constructional Steel Research, Vol. 59(7), 867-886.

Righiniotis, T.D. and Chryssanthopoulos, M.K. (2004). "Fatigue and fracture simulation of welded bridge details through a bi-linear crack growth law", Struct. Safety, Vol. 26.

Shetty, N.K. and Baker, M.J. (1990). "Fatigue reliability of tubular joints in offshore structures: Crack propagation model", Proc. 9th Offshore Mechanics and Arctic Engineering Conf., ASME.

Tada, H., Paris, P.C. and Irwin, G.R. (2000). The stress analysis of cracks handbook, ASME, New York.

Wallin, K. (1984). "The scatter in K KC results", Eng. Fract. Mechs., Vol 19(6).

