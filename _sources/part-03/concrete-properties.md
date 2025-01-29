# Concrete Properties

## List of symbols:

$\begin{array}{ll}f_{co} &= \text { basic concrete compression strength}\\
M_{j} &= \text { the logarithmic mean at strength job}~j\\
\Sigma_{j} &= \text { the logarithmic strength standard deviation at job}~j\\
Y_{1, j} &= \text { a log-normal variable representing additional variations due to the special placing, curing and hardening conditions of in situ concrete at job}~j\\
U_{ij} &= \text { a standard normal variable}\\
\lambda &= \text { lognormal variable with mean 0.96 and coefficient of variation 0.005 ; generally it suffices to take}~\lambda \text { deterministically}\\
\alpha(t, \tau) &= \text { is a deterministic function which takes into account the concrete age at the loading time} t \text { and the duration of loading}~\tau\\
\phi(t, \tau) &= \text { is the creep coefficient}\\
\beta_{d} &= \text { total load and depends from the type of the structure}\\
E_{c} &= \text { modulus of elasticity}\\
f_{c} &= \text { in situ strength}\\
\varepsilon_{e} &= \text { strain at yielding}\\
\varepsilon_{u} &= \text { ultimate strain}\end{array}$

## Basic Properties

The reference property of concrete is the compressive strength $f_{c o}$ of standard test specimens (cylinder of 300 mm height and 150 mm diameter) tested according to standard conditions and at a standard age of 28 days (see ISO/DIS 2736 and ISO 3893). Other concrete properties are related to the reference strength of concrete according to:

```{math}
:label: eq-concrete-properties-1
\text{In situ compressive strength:} \quad f_{c}=\alpha(t, \tau) f_{co}^{\lambda} \hspace{10em} \text{[MPa]}
```

```{math}
:label: eq-concrete-properties-2
\text{Tensile strength:} \hspace{6.2em} f_{ct}=0.3~f_{c}^{2 / 3} \hspace{10.6 em} \text{[MPa]}
```

```{math}
:label: eq-concrete-properties-3
\text{Modulus of elasticity:} \hspace{4.3 em} E_{c}=10.5~f_{c}^{1 / 3}\left(\frac{1}{1+\beta_{d}~\phi(t, \tau)}\right) \hspace{2.0 em} \text{[GPa]}
```

```{math}
:label: eq-concrete-properties-4
\text{Ultimate compression strain:}  \hspace{1.3 em} \varepsilon_{u}=6.10^{-3}~f_{c}^{-1 / 6}\left(1+\beta_{d}~\phi(t, \tau)\right) \hspace{1.7 em} \text{[m/m]}
```

$\lambda$ is a factor taking into account the systematic variation of in situ compressive strength and strength of standard tests (see [24.3](section-3.1.3))

$\alpha(t, \tau)$ is a deterministic function which takes into account the concrete age at the loading time $t$ [days] and the duration of loading $\tau$ [days]. The function is given by:

```{math}
:label: eq-concrete-properties-5a
\alpha(t, \tau)= \alpha_{1}(\tau) \alpha_{2}(t) 
```

```{math}
:label: eq-concrete-properties-5b
\begin{array}{rcl}
\alpha_{1}(\tau) & = & \alpha_{3}(\infty) + \left[1 - \alpha_{3}(\infty)\right] \exp\left[-a_{\tau} \tau\right]  \text{with } \alpha_{3}(\infty) \approx 0.8 \text{ and } a_{\tau} = 0.04 \\ \\
\alpha_{2}(t) & = & a + b \ln(t)
\end{array}
```

In most applications $\alpha_{1}(\tau)=0.8$ can be used. The coefficients $a$ and $b$ in $\alpha_{2}(t)$ depend on the type of cement and the climatical environment; under normal conditions $a=0.6$ and $b=0.12$.

$\phi(t, \tau)$ is the creep coefficient according to some modern code assumed to be deterministic.

$\beta_{d}$ is the ratio of the permanent load to the total load and depends on the type of the structure; generally $\beta_{d}$ is between 0.6 and 0.8.

## Stress-strain-relationship

For concrete under compression the following simplified stress-strain relationship holds:

```{math}
:label: eq-concrete-properties-6
\sigma=E_{c} \varepsilon \qquad  \text { for } \varepsilon<\varepsilon_{e} 
```

```{math}
:label: eq-concrete-properties-7
\sigma=f_{c} \qquad \text { for } \varepsilon_{e}<\varepsilon<\varepsilon_{u} 
```

```{math}
:label: eq-concrete-properties-8
\varepsilon_{e}=f_{c} / E_{c} 
```

For calculations where the form of the stress-strain relationships is important the following relationship should be used:

```{math}
:label: eq-concrete-properties-9
\sigma=f_{c}\left[1-\left[1-\frac{\varepsilon}{\varepsilon_{s}}\right]^{k}\right] 
```

```{math}
:label: eq-concrete-properties-10
\varepsilon_{s}=0.0011~f_{c}^{1 / 6} 
```

```{math}
:label: eq-concrete-properties-11
k=\frac{E_{c} \varepsilon_{s}}{f_{c}}
```

The relationship holds for $0<\varepsilon<\varepsilon_{s}$.

(section-3.1.3)=
## The probabilistic model

The strength of concrete at a particular point $i$ in a given structure $j$ as a function of standard strength $f_{c 0}$ is given as:

```{math}
:label: eq-concrete-properties-12
f_{c, ij}=\alpha(t, \tau)\left(f_{co,ij}\right)^{\lambda} Y_{1, j} 
```

```{math}
:label: eq-concrete-properties-13
f_{co,ij}=\exp \left(\left(U_{ij} \Sigma_{j}+M_{j}\right)\right)
```

in which

$f_{co, ij}=$ log-normal variable, independent of $Y_{1, j}$ with distribution parameters $M_{j}$ and $\Sigma_{j}$ 

$M_{j}=$ the logarithmic mean at job $j$

$\Sigma_{j}=$ the logarithmic standard deviation at job $j$

$Y_{1, j}=$ a log-normal variable representing additional variations due to the special placing, curing and hardening conditions of in situ concrete at job $j$

$U_{ij}=$ a standard normal variable representing the variability within one structure

$\lambda=$ lognormal variable with mean 0.96 and coefficient of variation 0.005 ; generally it suffices to take $\lambda$ deterministically

The variable $Y_{1, j}$ can also be taken as a spatially varying random field whose mean value function takes account of systematic influences in space.

Correspondingly, for the other three basic properties:

```{math}
:label: eq-concrete-properties-14
f_{ct, ij}=0.3~f_{c, ij}^{2 / 3}~Y_{2, j} 
```

```{math}
:label: eq-concrete-properties-15
E_{c, ij}=10.5~f_{c, ij}^{1 / 3}~Y_{3, j}\left(1+\beta_{d}~\phi(t, \tau)\right)^{-1}  
```

```{math}
:label: eq-concrete-properties-16
\varepsilon_{u, ij}=6 \cdot 10^{-3}~f_{c, ij}^{-1 / 6}~Y_{4, j}\left(1+\beta_{d}~\phi(t, \tau)\right) 
```

where the variables $Y_{2, j}$ to $Y_{4, j}$ mainly reflect variations due to factors not well accounted for by concrete compressive strength (e.g., gravel type and size, chemical composition of cement and other ingredients, climatical conditions).

The variables $U_{ij}$ and $U_{kj}$ within one member are correlated by:

```{math}
:label: eq-concrete-properties-17
\rho\left(U_{ij}, U_{kj}\right)=\rho+(1-\rho) \exp \left\lbrace \frac{\left(r_{ij}-r_{kj}\right)^{2}}{~d_{c}{ }^{2}}\right\rbrace
```

where $d_{c}=5 ~m$ and $\rho=0.5$. For different jobs $U_{ij}$ and $U_{kj}$ are uncorrelated.

## Distributions of $Y_{kj}$

Unless direct measurements are available, the parameters of the variables $Y_{k, j}$ can be taken from {numref}`table-data-for-parameters-Y_i`. The variables are distributed according to the log-normal distibution. The variability of the variables $Y_{k, j}$ can further be split into a part depending only on the job under consideration and a part representing spatial variability.

If direct measurements are available, the parameters in {numref}`table-data-for-parameters-Y_i` are taken as parameters of an equivalent prior sample with size $n^{\prime}=10$ (see [Part 1](../part-01/introduction.md) for the details of updating).

```{table} Data for parameters $Y_{i}$
:name: table-data-for-parameters-Y_i
| Variable | Distribution type | Mean | Coefficient of variation | Related to |
| :--- | :--- | :--- | :--- | :--- |
| $Y_{1 j}$ | LN | 1.0 | 0.06 | compression |
| $Y_{2 j}$ | LN | 1.0 | 0.30 | tension |
| $Y_{3 j}$ | LN | 1.0 | 0.15 | E-modulus |
| $Y_{4 j}$ | LN | 1.0 | 0.15 | ultimate strain |
```

## Distribution for $\mathbf{f}_{co}$

The distribution of $x_{i j}=\ln \left(f_{c o, i j}\right)$ is normal provided that its parameters $M$ and $\Sigma$ obtained from an ideal infinite sample. In general it must be assumed that concrete production varies from production unit, site, construction period, etc. and that sample sizes are limited. Therefore, the parameters $M$ and $\Sigma$ must also be treated as random variables. Then, $x_{ij}$ has a student distribution according to:

```{math}
F_{x}(x)=F_{t_{v^{\prime \prime}}}\left[\frac{\ln \left(x / m^{\prime \prime}\right)}{s^{\prime \prime}}\left(1+\frac{1}{n^{\prime \prime}}\right)^{-0.5}\right]
```

where $F_{t} v^{\prime \prime}$ is the Student distribution for $v^{\prime \prime}$ degrees of freedom. $f_{co,ij}$ can be represented as

```{math}
f_{c o, i j}=\exp \left(m^{\prime \prime}+t_{v^{\prime \prime}} s^{\prime \prime}\left(1+\frac{1}{n^{\prime \prime}}\right)^{0.5}\right)
```

The values of $m^{\prime \prime}, n^{\prime \prime}, s^{\prime \prime}$ and $v^{\prime \prime}$ depend on the amount of specific information. {numref}`table-Prior-parameters-for-concrete-strength-distribution` {cite}`KerskenBradley1991`, {cite}`Rackwitz1983` gives the values if no specific information is available (prior information).

```{table} Prior parameters for concrete strength distribution $\left(f_{co}\right.$ in MPa) 
:name: table-Prior-parameters-for-concrete-strength-distribution
| Concrete type | Concrete grade | Parameters |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | $m^{\prime \prime}$ | $n^{\prime \prime}$ | $s^{\prime \prime}$ | $v^{\prime \prime}$ |
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

If $n^{\prime \prime} v ">10$, a good approximation of the concrete strength distribution is the log-normal distribution with mean $m^{\prime \prime}$ and standard deviation $s^{\prime \prime}$ $\sqrt{\frac{n}{n^{\prime \prime}-1} \frac{v^{\prime \prime}}{v^{\prime \prime}-2}}$.


**References**

```{bibliography}
:filter: docname in docnames
:style: unsrt
:labelprefix: 24.
```