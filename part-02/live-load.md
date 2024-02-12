# Live Load

**List of symbols:**

$A=$ area $\left[m^{2}\right]$

$d_{p}=$ duration of intermittend load [year]

$i=$ influence function

$m=$ mean load intensity in $\left[kN / m^{2}\right]$

$p=$ intermittent load in $\left[kN / m^{2}\right]$

$q=$ sustained load in $\left[kN / m^{2}\right]$

$S=$ load effect in $\left[kN / m^{2}\right]$

$T=$ reference time in [year]

$V=$ zero mean normal distributed variable in $\left[kN / m^{2}\right]$

$W=$ load intensity in $\left[kN / m^{2}\right]$

$\lambda=$ occurrence rate of sustained load changes in [1/year]

$v=$ occurrence rate of intermittent load changes in [1/year]

## Basic Model

The live loads on floors in buildings are caused by the weight of furniture, equipment, stored objects
and persons. Not included in this type of load are any structural or non-structural elements, partition walls or
extraordinary equipment. The live load is distinguished according to the intended user category of the building, i.e.
domestic buildings, hotels, hospitals, office buildings, schools, and stores. At design stage, considerations
should also be given to eventual changes of use during the life-time. Areas dedicated to store goods, materials,
etc. must be treated separately. Live loads vary in time and space in a random manner. The spatial variations
are assumed to be homogeneous in a first approximation. With respect to the variation in time, it is divided into
two components, the sustained load and the intermittent load.

The sustained load contains the weight of furniture and heavy equipment. The load magnitude
according to the model represents the time average of the real fluctuating load. Changes usually related to
changes in use and of users in a building. Short term fluctuations are included in the uncertainties of this load
part.

The intermittent load represents all kinds of live loads, which are not covered by the sustained load.
The sources are like gathering of people, crowded rooms during special events, or stacking of furniture during
remodelling. The relative duration of an intermittent loads is fairly small.

## Stochastic Model

The load intensity is represented by a stochastic field $W(x,y)$, whereby the parameters depend on
the user category of the building.

```{math}
:label: eq-live-load-1
W ( x , y ) = m + V + U ( x, y )
```

where $m$ is the overall mean load intensity for a particular user category, $V$ is a zero mean normal distributed
variable and $U(x,y)$ is a zero mean random field with a characteristic skewness to the right. The quantities $V$
and $U$ are assumed to be stochastically independent.

The load effects calculated from the model shall describe the load effects caused by the real load, with
sufficient accuracy. For linear elastic systems, where superposition is possible, the load effect $S$ is written as:

```{math}
:label: eq-live-load-2
S = \int_A W ( x, y ) i( x, y ) dA
```

where $W(x,y)$ is the load intensity and $i(x,y)$ is the influence function for the load effect over a considered area $A$.

For non-linear structural response a stepwise linearity can be assumed, whereby the proposed relation
for the load effect can be used in each step. The load intensity $W$ is substituted by the step $\Delta W$ and the
influence function $i(x,y)$ must reflect the total load situation, which results in a corresponding step
$`\Delta S$ for the load effect. When applying the theory of plasticity, then the influence function is 
proportional to the deflection corresponding to the mechanism.

An equivalent uniformly distributed load for the sustained load per unit area is that load having the same load effect as the original load field, i.e.

```{math}
:label: eq-live-load-3
q=\frac{\int_{A} W(x, y) i(x, y) d A}{\int_{A} i(x, y) d A}
```

The statistical parameters of the sustained load are:

```{math}
:label: eq-live-load-4
\begin{aligned}
& E[q]=m \\
& \operatorname{Var}[q]=\sigma_{V}^{2}+\sigma_{U}^{2} \frac{A_{0}}{A} \kappa
\end{aligned}
```

whereby the factor $\kappa$ is given in {numref}`fig-Random-fields-and-corresponding-kappa-values` in Part 2.0. Note that for $A < A_{0}$ one should take $A_{0} / A=1$.

The variable $V$ describes the variability of sustained loads related to areas $A_{1}$ and $A_{2}$, which are assumed to be independent and non overlapping. These areas can be either on the same floor or on different floors. The covariance between the corresponding loads $q_{1}$ and $q_{2}$ is given as:

```{math}
:label: eq-live-load-5
\operatorname{Cov}\left[q_{1}, q_{2}\right]=\sigma_{V}^{2}
```

The stochastic distribution of $V$ is assumed to be normally distributed. The random field $U(x, y)$ has a specific skewness to the right, and in consequence also the load effect $S$ and the sustained load $q$. A Gamma distribution for the sustained load fits best the actual observations, with parameters defined through the relations $E[q]=k / \mu_{U}$ and $\operatorname{Var}[q]=k / \mu_{U}^{2}$.

The load intensity for the intermittent load $p$ is represented by the same stochastic field as the sustained load, whereby the parameters depend on the user category of the building. The intermittent load can generally be considered as concentrated load. But, for design purposes, the same approach as for the sustained load is used. The duration of the intermittent load $d_{p}$ is considered as deterministic.

The equivalent uniformly distributed load for intermittent loads $p$ has the statistical properties as the sustained load and can be evaluated in the same manner. Generally, there is a lack of data for this load. The standard deviation normally gets values in the same magnitude as the mean value, $E[p]=\mu_{p}$. Therefore, the intermittent load is assumed to be exponentially distributed.

## Variations in Time

The time between load changes is assumed to be exponentially distributed, then the number of load changes is Poisson distributed. The probability function for the maximum sustained load is given by:

```{math}
:label: eq-live-load-6
F_{q_{\max }}(x)=\exp \left[-\lambda T\left(1-F_{q}(x)\right)\right]
```

where $F_{q}(x)$ is the probability function of the sustained load, $T$ is the reference time, like the anticipated lifetime of the building, and$\lambda$ is the occurrence rate of sustained load changes. Thus $\lambda T$ is the mean of the number of occupancy changes.

The maximum of the intermittent load is defined to occur as a Poisson process in time with the mean occurrence rate $v$. The average duration of the intermittent load depends on the process, i.e. personnel, emergency or remodeling. 

The maximum load which will occur in a building is a combination of sustained load and intermittent load. Assuming a stochastic independence between both load types, the maximum load during one occupancy is obtained from the convolution integral. The total maximum load during the reference time $T$ is obtained by employing the extreme value theory.

In cases with high share in sustained load the duration statistics becomes of interest, especially for creep and shrinkage problems. Generally, the intermittent load will be of little interest. From the assumed extreme value distribution the statistical quantities of the excursion time $\tau$ over a certain level $x$ can be derived.

```{math}
:label: eq-live-load-7
\begin{aligned}
& E[\tau(x)]=T\left(1-F_{q}(x)\right) \\
& \operatorname{Var}[\tau(x)]=2 T\left(1-F_{q}(x)\right) / \lambda
\end{aligned}
```

## Load Parameterss

A list of parameters in {numref}`table-Parameters-for-live-loads-depending-on-the-user-category` are to be used in the live load model.

```{table} Parameters for live loads depending on the user category
:name: table-Parameters-for-live-loads-depending-on-the-user-category
| Type of use | $A_o$ <br> $[m^2]$ | $m_q$ <br> $[kN/m^2]$ | $\sigma_{v}$ <br> $[kN/m^2]$ | $\sigma_{u}$ <br> $[kN/m^2]$ | $1/\lambda$ <br> $[a]$ | $m_p$ $[kN/m^2]$ | $\sigma_{U}$ <br> $[kN/m^2]$ | $1/\nu$ <br> $[a]$ | $d_P$ <br> $[d]$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  | Sustained <br> Load | Sustained <br> Load | Sustained <br> Load | Sustained <br> Load | Intermittent <br> Load | Intermittent <br> Load | Intermittent <br> Load | Intermittent <br> Load |
| Office | 20 | 0.5 | 0.3 | 0.6 | 5 | 0.2 | 0.4 | 0.3 | 1 - 3 |
| Lobby | 20 | 0.2 | 0.15 | 0.3 | 10 | 0.4 | 0.6 | 1.0 | 1 - 3 |
| Residence | 20 | 0.3 | 0.15 | 0.3 | 7 | 0.3 | 0.4 | 1.0 | 1 - 3 |
| Hotel guest room | 20 | 0.3 | 0.05 | 0.1 | 10 | 0.2 | 0.4 | 0.1 | 1 - 3 |
| Patient room | 20 | 0.4 | 0.3 | 0.6 | 5 - 10 | 0.2 | 0.4 | 1.0 | 1 - 3 |
| Laboratory | 20 | 0.7 | 0.4 | 0.8 | 5 - 10 |  |  |  |  |
| Libraries | 20 | 1.7 | 0.5 | 1.0 | >10 |  |  |  |  |
| School classroom | 100 | 0.6 | 0.15 | 0.4 | >10 | 0.5 | 1.4 | 0.3 | 1 - 5 |
| Merchant/retail: <br> first floor <br> upper floor | <br> 100 <br> 100 | <br> 0.9 <br> 0.9 | <br> 0.6 <br> 0.6 | <br> 1.6 <br> 1.6 | <br> 1 - 5 <br> 1 - 5 | <br> 0.4 <br> 0.4 | <br> 1.1 <br> 1.1 | <br> 1.0 <br> 1.0 | <br> 1 - 14 <br> 1 - 14 |
| Storage | 100 | 3.5 | 2.5 | 6.9 | 0.1 - 1.0 |  |  |  |  |
| Industrial: <br> light <br> heavy | <br> 100 <br> 100 | <br> 1.0 <br> 3.0 | <br> 1.0 <br> 1.5 | <br> 2.8 <br> 4.1 | <br> 5 - 10 <br> 5 - 10 |  |  |  |  |
| Concentration of people | 20 |  |  |  |  | 1.25 | 2.5 | 0.02 | 0.5 |
| Concentration of people | 20 |  |  |  |  | 1.25 | 2.5 | 0.02 | 0.5 |
```

**References**

[1] CIB W81. Actions on Structures - Live Loads in Buildings. Conseil International du Bâtiment pour la Recherche l'Etude et la Documentation (CIB). Report 116, Rotterdam, 1989.

[2] EC 1-Part 2.1: Actions on structures - Densities, self-weight, imposed loads. Eurocode 1 - Basis of Design and Actions on Structures. Comité Européen de Normalisation (CEN). Pre-standard draft, Brussels, 1994.

[3] Rackwitz R: Live Loads in Buildings. Manuscript, unpublished, Munich, 1995.

[4] PMC Part 1: Basis of Design. Probabilistic Model Code - third draft. Joint Committee on Structural Safety (JCSS), 1995.



