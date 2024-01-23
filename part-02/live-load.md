# Live Load

**List of symbols:**

{math}`A=` area {math}`\left[\mathrm{m}^{2}\right]`

{math}`\mathrm{d}_{\mathrm{p}}=` duration of intermittend load [year]

{math}`\mathrm{i}=` influence function

{math}`\mathrm{m}=` mean load intensity in {math}`\left[\mathrm{kN} / \mathrm{m}^{2}\right]`

{math}`\mathrm{p}=` intermittent load in {math}`\left[\mathrm{kN} / \mathrm{m}^{2}\right]`

{math}`\mathrm{q}=` sustained load in {math}`\left[\mathrm{kN} / \mathrm{m}^{2}\right]`

{math}`\mathrm{S}=` load effect in {math}`\left[\mathrm{kN} / \mathrm{m}^{2}\right]`

{math}`\mathrm{T}=` reference time in [year]

{math}`\mathrm{V}=` zero mean normal distributed variable in {math}`\left[\mathrm{kN} / \mathrm{m}^{2}\right]`

{math}`\mathrm{W}=` load intensity in {math}`\left[\mathrm{kN} / \mathrm{m}^{2}\right]`

{math}`\lambda=` occurrence rate of sustained load changes in [1/year]

{math}`v=` occurrence rate of intermittent load changes in [1/year]

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

The load intensity is represented by a stochastic field {math}`W(x,y)`, whereby the parameters depend on
the user category of the building.

```{math}
:label: eq-live-load-1
W ( x , y ) = m + V + U ( x, y )
```

where {math}`m` is the overall mean load intensity for a particular user category, {math}`V` is a zero mean normal distributed
variable and {math}`U(x,y)` is a zero mean random field with a characteristic skewness to the right. The quantities {math}`V`
and {math}`U` are assumed to be stochastically independent.

The load effects calculated from the model shall describe the load effects caused by the real load, with
sufficient accuracy. For linear elastic systems, where superposition is possible, the load effect {math}`S` is written as:

```{math}
:label: eq-live-load-2
S = \int_A W ( x, y ) i( x, y ) dA
```

where {math}`W(x,y)` is the load intensity and {math}`i(x,y)` is the influence function for the load effect over a considered area {math}`A`.

For non-linear structural response a stepwise linearity can be assumed, whereby the proposed relation
for the load effect can be used in each step. The load intensity {math}`W` is substituted by the step {math}`\Delta W` and the
influence function {math}`i(x,y)` must reflect the total load situation, which results in a corresponding step
{math}`\Delta S` for the load effect. When applying the theory of plasticity, then the influence function is 
proportional to the deflection corresponding to the mechanism.

An equivalent uniformly distributed load for the sustained load per unit area is that load having the same load effect as the original load field, i. e.

```{math}
:label: eq-live-load-3
q=\frac{\int_{A} W(x, y) i(x, y) d A}{\int_{A} i(x, y) d A}
```

The statistical parameters of the sustained load are:

```{math}
:label: eq-live-load-4
\begin{aligned}
& \mathrm{E[q]=m} \\
& \operatorname{Var}[\mathrm{q}]=\sigma_{\mathrm{V}}^{2}+\sigma_{\mathrm{U}}^{2} \frac{\mathrm{A}_{0}}{\mathrm{A}} \kappa
\end{aligned}
```

whereby the factor {math}`\kappa` is given in {numref}`fig2.5.0.1` in Part 2.0. Note that for {math}`\mathrm{A} < \mathrm{A}_{0}` one should take {math}`\mathrm{A}_{0} / \mathrm{A}=1`.

The variable {math}`V` describes the variability of sustained loads related to areas {math}`A_{1}` and {math}`A_{2}`, which are assumed to be independent and non overlapping. These areas can be either on the same floor or on different floors. The covariance between the corresponding loads {math}`\mathrm{q}_{1}` and {math}`\mathrm{q}_{2}` is given as:

```{math}
:label: eq-live-load-5
\operatorname{Cov}\left[q_{1}, q_{2}\right]=\sigma_{V}^{2}
```

The stochastic distribution of {math}`V` is assumed to be normally distributed. The random field {math}`U(x, y)` has a specific skewness to the right, and in consequence also the load effect {math}`S` and the sustained load {math}`q`. A Gamma distribution for the sustained load fits best the actual observations, with parameters defined through the relations {math}`E[q]=k / \mu_{U}` and {math}`\operatorname{Var}[q]=k / \mu_{U}^{2}`.

The load intensity for the intermittent load {math}`p` is represented by the same stochastic field as the sustained load, whereby the parameters depend on the user category of the building. The intermittent load can generally be considered as concentrated load. But, for design purposes, the same approach as for the sustained load is used. The duration of the intermittent load {math}`\mathrm{d}_{p}` is considered as deterministic.

The equivalent uniformly distributed load for intermittent loads {math}`p` has the statistical properties as the sustained load and can be evaluated in the same manner. Generally, there is a lack of data for this load. The standard deviation normally gets values in the same magnitude as the mean value, {math}`\mathrm{E}[p]=\mu_{p}`. Therefore, the intermittent load is assumed to be exponentially distributed.

## Variations in Time

The time between load changes is assumed to be exponentially distributed, then the number of load changes is Poisson distributed. The probability function for the maximum sustained load is given by:

```{math}
:label: eq-live-load-6
F_{q_{\max }}(x)=\exp \left[-\lambda T\left(1-F_{q}(x)\right)\right]
```

where {math}`\mathrm{F}_{q}(x)` is the probability function of the sustained load, {math}`T` is the reference time, like the anticipated lifetime of the building, and {math}`\lambda` is the occurrence rate of sustained load changes. Thus {math}`\lambda T` is the mean of the number of occupancy changes.

The maximum of the intermittent load is defined to occur as a Poisson process in time with the mean occurrence rate {math}`v`. The average duration of the intermittent load depends on the process, i.e. personnel, emergency or remodeling. 

The maximum load which will occur in a building is a combination of sustained load and intermittent load. Assuming a stochastic independence between both load types, the maximum load during one occupancy is obtained from the convolution integral. The total maximum load during the reference time {math}`T` is obtained by employing the extreme value theory.

In cases with high share in sustained load the duration statistics becomes of interest, especially for creep and shrinkage problems. Generally, the intermittent load will be of little interest. From the assumed extreme value distribution the statistical quantities of the excursion time {math}`\tau` over a certain level $x$ can be derived.

```{math}
:label: eq-live-load-7
\begin{aligned}
& E[\tau(x)]=T\left(1-F_{q}(x)\right) \\
& \operatorname{Var}[\tau(x)]=2 T\left(1-F_{q}(x)\right) / \lambda
\end{aligned}
```

## Load Parameterss

A list of parameters in {numref}`tbl2.2.1` are to be used in the live load model.

```{table} Parameters for live loads depending on the user category
:name: tbl2.2.1
| Type of use | {math}`\mathrm{A_o}` <br> {math}`[\mathrm{m^2}]` | {math}`m_q` <br> {math}`[\mathrm{kN/m^2}]` | {math}`\sigma_{\mathrm{v}}` <br> {math}`[\mathrm{kN/m^2}]` | {math}`\sigma_{\mathrm{u}}` <br> {math}`[\mathrm{kN/m^2}]` | {math}`1/\lambda` <br> {math}`\mathrm{[a]}` | {math}`m_p` {math}`[\mathrm{kN/m^2}]` | {math}`\sigma_{\mathrm{U}}` <br> {math}`[\mathrm{kN/m^2}]` | {math}`1/\nu` <br> {math}`\mathrm{[a]}` | {math}`d_P` <br> {math}`\mathrm{[d]}` |
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



