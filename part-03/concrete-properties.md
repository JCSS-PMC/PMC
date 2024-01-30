# Concrete Properties

## 7. List of symbols:

{math}`\mathrm{f}_{\mathrm{co}}=` basic concrete compression strength

{math}`\mathrm{M}_{\mathrm{j}}=` the logarithmic mean at strength job {math}`\mathrm{j}`

{math}`\Sigma_{\mathrm{j}}=` the logarithmic strength standard deviation at job {math}`\mathrm{j}`

{math}`\mathrm{Y}_{1, \mathrm{j}}=` a log-normal variable representing additional variations due to the special placing, curing and hardening conditions of in situ concrete at job {math}`\mathrm{j}`

{math}`\mathrm{U}_{\mathrm{ij}}=` a standard normal variable

{math}`\lambda=` lognormal variable with mean 0.96 and coefficient of variation 0.005 ; generally it suffices to take {math}`\lambda` deterministically

{math}`\alpha(\mathrm{t}, \tau)=` is a deterministic function which takes into account the concrete age at the loading time {math}`\mathrm{t}` and the duration of loading {math}`\tau`

{math}`\phi(\mathrm{t}, \tau)=` is the creep coefficient.

{math}`\beta_{\mathrm{d}}=` total load and depends from the type of the structure

{math}`\mathrm{E}_{\mathrm{c}}=` modulus of elasticity

{math}`\mathrm{f}_{\mathrm{c}}=` in situ strength

{math}`\varepsilon_{\mathrm{e}}=` strain at yielding

{math}`\varepsilon_{\mathrm{u}}=` ultimate strain

## Basic Properties

The reference property of concrete is the compressive strength {math}`\mathrm{f_{c o}}` of standard test specimens (cylinder of 300 mm height and 150 mm diameter) tested according to standard conditions and at a standard age of 28 days (see ISO/DIS 2736 and ISO 3893). Other concrete properties are related to the reference strength of concrete according to:

```{math}
:label: eq-concrete-properties-1
\text{In situ compressive strength:} \quad \mathrm{f}_{\mathrm{c}}=\alpha(\mathrm{t}, \mathrm{\tau}) \mathrm{f}_{\mathrm{co}}^{\lambda} \hspace{10em} \mathrm{[MPa]}
```

```{math}
:label: eq-concrete-properties-2
\text{Tensile strength:} \hspace{6.2em} \mathrm{f}_{\mathrm{ct}}=0.3~\mathrm{f}_{\mathrm{c}}^{2 / 3} \hspace{10.6 em} \mathrm{[MPa]}
```

```{math}
:label: eq-concrete-properties-3
\text{Modulus of elasticity:} \hspace{4.3 em} \mathrm{E}_{c}=10.5~\mathrm{f}_{\mathrm{c}}^{1 / 3}\left(\frac{1}{1+\beta_{d}~\phi(\mathrm{t}, \tau)}\right) \hspace{4.6 em} \mathrm{[GPa]}
```

```{math}
:label: eq-concrete-properties-4
\text{Ultimate compression strain:}  \hspace{1.3 em} \varepsilon_{\mathrm{u}}=6.10^{-3}~\mathrm{f}_{\mathrm{c}}^{-1 / 6}\left(1+\beta_{\mathrm{d}}~\phi(\mathrm{t}, \tau)\right) \hspace{1.7 em} [\mathrm{m} / \mathrm{m}]
```

{math}`\lambda` is a factor taking into account the systematic variation of in situ compressive strength and strength of standard tests (see [24.3](section-3.1.3))

{math}`\alpha(\mathrm{t}, \tau)` is a deterministic function which takes into account the concrete age at the loading time {math}`\mathrm{t}` [days] and the duration of loading {math}`\tau` [days]. The function is given by:

```{math}
:label: eq-concrete-properties-5a
\alpha(\mathrm{t}, \tau)= \alpha_{1}(\tau) \alpha_{2}(\mathrm{t}) 
```

```{math}
:label: eq-concrete-properties-5b
\begin{array}{rcl}
\alpha_{1}(\tau) & = & \alpha_{3}(\infty) + \left[1 - \alpha_{3}(\infty)\right] \exp\left[-\mathrm{a}_{\tau} \tau\right]  \text{with } \alpha_{3}(\infty) \approx 0.8 \text{ and } \mathrm{a}_{\tau} = 0.04 \\ \\
\alpha_{2}(t) & = & \mathrm{a} + \mathrm{b} \ln(\mathrm{t})
\end{array}
```


In most applications {math}`\alpha_{1}(\tau)=0.8` can be used. The coefficients {math}`\mathrm{a}` and {math}`\mathrm{b}` in {math}`\alpha_{2}(t)` depend on the type of cement and the climatical environment; under normal conditions {math}`\mathrm{a}=0.6` and {math}`\mathrm{b}=0.12`.

{math}`\phi(\mathrm{t}, \tau)` is the creep coefficient according to some modern code assumed to be deterministic.

{math}`\beta_{\mathrm{d}}` is the ratio of the permanent load to the total load and depends on the type of the structure; generally {math}`\beta_{\mathrm{d}}` is between 0.6 and 0.8.

## Stress-strain-relationship

For concrete under compression the following simplified stress-strain relationship holds:

```{math}
:label: eq-concrete-properties-6
\sigma=\mathrm{E}_{\mathrm{c}} \varepsilon \qquad  \text { for } \varepsilon<\varepsilon_{\mathrm{e}} 
```

```{math}
:label: eq-concrete-properties-7
\sigma=\mathrm{f}_{\mathrm{c}} \qquad \text { for } \varepsilon_{\mathrm{e}}<\varepsilon<\varepsilon_{\mathrm{u}} 
```

```{math}
:label: eq-concrete-properties-8
\varepsilon_{\mathrm{e}}=\mathrm{f}_{\mathrm{c}} / \mathrm{E}_{\mathrm{c}} 
```

For calculations where the form of the stress-strain relationships is important the following relationship should be used:

```{math}
:label: eq-concrete-properties-9
\sigma=\mathrm{f}_{\mathrm{c}}\left[1-\left[1-\frac{\varepsilon}{\varepsilon_{\mathrm{s}}}\right]^{\mathrm{k}}\right] 
```

```{math}
:label: eq-concrete-properties-10
\varepsilon_{\mathrm{s}}=0.0011~\mathrm{f}_{\mathrm{c}}^{1 / 6} 
```

```{math}
:label: eq-concrete-properties-11
\mathrm{k}=\frac{\mathrm{E}_{\mathrm{c}} \varepsilon_{\mathrm{s}}}{\mathrm{f}_{\mathrm{c}}}
```

The relationship holds for {math}`0<\varepsilon<\varepsilon_{\text {s }}`.

(section-3.1.3)=
## The probabilistic model

The strength of concrete at a particular point {math}`\mathrm{i}` in a given structure {math}`\mathrm{j}` as a function of standard strength {math}`\mathrm{f_{c 0}}` is given as:

```{math}
:label: eq-concrete-properties-12
\mathrm{f}_{\mathrm{c}, \mathrm{ij}}=\alpha(\mathrm{t}, \mathrm{\tau})\left(\mathrm{f}_{\mathrm{co,ij}}\right)^{\lambda} \mathrm{Y}_{1, \mathrm{j}} 
```

```{math}
:label: eq-concrete-properties-13
\mathrm{f}_{\mathrm{co,ij}}=\exp \left(\left(\mathrm{U}_{\mathrm{ij}} \Sigma_{\mathrm{j}}+\mathrm{M}_{\mathrm{j}}\right)\right)
```

in which

{math}`\mathrm{f}_{\mathrm{co}, \mathrm{ij}}=` log-normal variable, independent of {math}`\mathrm{Y}_{1, \mathrm{j}}` with distribution parameters {math}`\mathrm{M}_{\mathrm{j}}$ and {math}`\Sigma_{\mathrm{j}}` 

{math}`\mathrm{M}_{\mathrm{j}}=` the logarithmic mean at job {math}`\mathrm{j}`

{math}`\Sigma_{\mathrm{j}}=` the logarithmic standard deviation at job {math}`\mathrm{j}`

{math}`\mathrm{Y}_{1, \mathrm{j}}=` a log-normal variable representing additional variations due to the special placing, curing and hardening conditions of in situ concrete at job {math}`\mathrm{j}`

{math}`\mathrm{U}_{\mathrm{ij}}=` a standard normal variable representing the variability within one structure

{math}`\lambda=` lognormal variable with mean 0.96 and coefficient of variation 0.005 ; generally it suffices to take {math}`\lambda` deterministically

The variable {math}`\mathrm{Y_{1, j}}` can also be taken as a spatially varying random field whose mean value function takes account of systematic influences in space.

Correspondingly, for the other three basic properties:

```{math}
:label: eq-concrete-properties-14
\mathrm{f}_{\mathrm{ct}, \mathrm{ij}}=0.3~\mathrm{f}_{\mathrm{c}, \mathrm{ij}}^{2 / 3}~\mathrm{Y}_{2, \mathrm{j}} 
```

```{math}
:label: eq-concrete-properties-15
\mathrm{E}_{c, \mathrm{ij}}=10.5~\mathrm{f}_{\mathrm{c}, \mathrm{ij}}^{1 / 3}~\mathrm{Y}_{3, \mathrm{j}}\left(1+\beta_{d}~\phi(t, \tau)\right)^{-1}  
```

```{math}
:label: eq-concrete-properties-16
\varepsilon_{\mathrm{u}, \mathrm{ij}}=6 \cdot 10^{-3}~\mathrm{f}_{\mathrm{c}, \mathrm{ij}}^{-1 / 6}~\mathrm{Y}_{4, \mathrm{j}}\left(1+\beta_{d}~\phi(\mathrm{t}, \tau)\right) 
```

where the variables {math}`\mathrm{Y}_{2, \mathrm{j}}` to {math}`\mathrm{Y}_{4, \mathrm{j}}` mainly reflect variations due to factors not well accounted for by concrete compressive strength (e.g., gravel type and size, chemical composition of cement and other ingredients, climatical conditions).

The variables {math}`\mathrm{U}_{\mathrm{ij}}` and {math}`\mathrm{U}_{\mathrm{kj}}` within one member are correlated by:

```{math}
:label: eq-concrete-properties-17
\rho\left(\mathrm{U}_{\mathrm{ij}}, \mathrm{U}_{\mathrm{kj}}\right)=\rho+(1-\rho) \exp \left\lbrace \frac{\left(\mathrm{r}_{\mathrm{ij}}-\mathrm{r}_{\mathrm{kj}}\right)^{2}}{\mathrm{~d}_{\mathrm{c}}{ }^{2}}\right\rbrace
```

where {math}`\mathrm{d}_{\mathrm{c}}=5 \mathrm{~m}` and {math}`\rho=0.5`. For different jobs {math}`\mathrm{U}_{\mathrm{ij}}` and {math}`\mathrm{U}_{\mathrm{kj}}` are uncorrelated.

## Distributions of {math}`\mathrm{Y_{kj}}`

Unless direct measurements are available, the parameters of the variables {math}`\mathrm{Y}_{\mathrm{k}, \mathrm{j}}` can be taken from {numref}`tbl-concrete-properties-3.1.1`. The variables are distributed according to the log-normal distibution. The variability of the variables {math}`\mathrm{Y}_{\mathrm{k}, \mathrm{j}}` can further be split into a part depending only on the job under consideration and a part representing spatial variability.

If direct measurements are available, the parameters in {numref}`tbl-concrete-properties-3.1.1` are taken as parameters of an equivalent prior sample with size {math}`\mathrm{n}^{\prime}=10` (see [Part 1](../part-01/introduction.md) for the details of updating).

```{table} Data for parameters $\mathrm{Y_{i}}$
:name: tbl-concrete-properties-3.1.1
| Variable | Distribution type | Mean | Coefficient of variation | Related to |
| :--- | :--- | :--- | :--- | :--- |
| {math}`\mathrm{Y}_{1 \mathrm{j}}` | LN | 1.0 | 0.06 | compression |
| {math}`\mathrm{Y}_{2 \mathrm{j}}` | LN | 1.0 | 0.30 | tension |
| {math}`\mathrm{Y}_{3 \mathrm{j}}` | LN | 1.0 | 0.15 | E-modulus |
| {math}`\mathrm{Y}_{4 \mathrm{j}}` | LN | 1.0 | 0.15 | ultimate strain |
```

## Distribution for {math}`\mathbf{f}_{\mathrm{co}}`

The distribution of {math}`\mathrm{x_{i j}}=\ln \left(\mathrm{f_{c o, i j}}\right)` is normal provided that its parameters {math}`\mathrm{M}` and {math}`\Sigma` obtained from an ideal infinite sample. In general it must be assumed that concrete production varies from production unit, site, construction period, etc. and that sample sizes are limited. Therefore, the parameters {math}`\mathrm{M}` and {math}`\Sigma` must also be treated as random variables. Then, {math}`\mathrm{x}_{\mathrm{ij}}` has a student distribution according to:

```{math}
\mathrm{F_{x}(x)}=F_{t_{\nu^{\prime \prime}}}\left[\frac{\ln \left(\mathrm{x} / m^{\prime \prime}\right)}{s^{\prime \prime}}\left(1+\frac{1}{n^{\prime \prime}}\right)^{-0.5}\right]
```

where {math}`\mathrm{F}_{\mathrm{t}} \nu^{\prime \prime}` is the Student distribution for {math}`\nu^{\prime \prime}` degrees of freedom. {math}`\mathrm{f}_{\mathrm{co,ij}}` can be represented as

```{math}
f_{c o, i j}=\exp \left(m^{\prime \prime}+t_{\nu^{\prime \prime}} s^{\prime \prime}\left(1+\frac{1}{n^{\prime \prime}}\right)^{0.5}\right)
```

The values of {math}`\mathrm{m}^{\prime \prime}, \mathrm{n}^{\prime \prime}, \mathrm{s}^{\prime \prime}` and {math}`\nu^{\prime \prime}` depend on the amount of specific information. {numref}`tbl-concrete-properties-3.1.2` gives the values if no specific information is available (prior information).

```{table} Prior parameters for concrete strength distribution $\left(\mathrm{f}_{\mathrm{co}}\right.$ in MPa) [1,2]
:name: tbl-concrete-properties-3.1.2
| Concrete type | Concrete grade | Parameters |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | {math}`\mathrm{m}^{\prime \prime}` | {math}`\mathrm{n}^{\prime \prime}` | {math}`\mathrm{s}^{\prime \prime}` | {math}`\nu^{\prime \prime}` |
| Ready mixed | C15 | 3.40 | 3.0 | 0.14 | 10 |
|  | C25 | 3.65 | 3.0 | 0.12 | 10 |
|  | C35 | 3.85 | 3.0 | 0.09 | 10 |
|  | C45 | 3.98 | 3.0 | 0.07 | 10 |
|  | C55 | - | - | - | - |
| Pre-cast elements | C15 | - | - | - | - |
|  | C25 | 3.80 | 3.0 | 0.09 | 10 |
|  | C35 | 3.95 | 3.0 | 0.08 | 10 |
|  | C45 | 4.08 | 4.0 | 0.07 | 10 |
|  | C55 | 4.15 | 4.0 | 0.05 | 10 |
```

The prior parameters may depend on the geographical area and the technology with which concrete is produced.

If {math}`\mathrm{n}^{\prime \prime} \nu ">10`, a good approximation of the concrete strength distribution is the log-normal distribution with mean {math}`\mathrm{m}^{\prime \prime}` and standard deviation {math}`\mathrm{s}^{\prime \prime}` {math}`\sqrt{\frac{n}{n^{\prime \prime}-1} \frac{\nu^{\prime \prime}}{\nu^{\prime \prime}-2}}`.

**References**

[1] Kersken-Bradley, M., Rackwitz, R., Stochastic Modeling of Material Properties and Quality Control, JCSS Working Document, IABSE-publication, March 1991

[2] Rackwitz, R., Predictive Distribution of Strength under Control, Materials \\& Structures, 16, 94, 1983, pp. 259 - 267