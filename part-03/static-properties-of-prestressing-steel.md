# Static Properties Of Prestressing Steel (Prestressed Concrete)

**List of symbols:**

$\begin{array}{ll}E_{p} &= \text { modulus of elasticity}\\
E_{p}{ }^{\prime} &= \text { tangent to the stress-strain curve at the proof stress} ~\sigma_{p}\\
f_{p} &= \text { tensile strength}\\
f_{p 0.1} &= \text { 0.1 \% proof stress}\\
f_{p 0.2} &= \text { 0.2 \% proof stress}\\
f_{p p} &= \text { proportional limit}\\
f_{p y} &= \text { yield stress}\\
m &= \text { parameter of the second part of the modified Ramberg-Osgood curve}\\
n &= \text { parameter of the Ramberg-Osgood curve}\\
n^{\prime} &= \text { parameter of the first part of the modified Ramberg-Osgood curve}\\
p &= \text { plastic strain at the proof stress} ~\sigma_{p}\\
P  &= \text { prestressing force}\\
P_{0} &= \text { jacking force}\\
\Delta P &= \text { prestress losses}\\
t &= \text { time}\\
x &= \text { distance from the jacking end}\\
\varepsilon &= \text { strain}\\
\varepsilon_{p} &= \text { full strain at the proof stress} ~\sigma_{p}\\
\varepsilon_{u} &= \text { strain corresponding to the tensile strength}\\
\sigma &= \text { stress}\\
\sigma_{p} &= \text { proof stress}\end{array}$

## Types of prestressing steel

Three types of steel are used as prestressing tendons in concrete structures:

- cold drawn wires;
- strands - consist of a number of cold drawn wires spun together in helical configuration, most commonly used are 3-wire and 7-wire strands;
- high-strength bars.

More detailed description and requirements to steel products used in prestressing tendons in different countries may be found in appropriate standards (e.g., EN 10138 {cite}`EN10138`).

## Stress-strain relationship

A typical stress-strain diagram of prestressing steel in uniaxial tension is shown in {numref}`fig-stress-strain-diagram-of-prestressing-steel`.

```{figure} ../part-03/images/stress-strain-diagram-of-prestressing-steel.jpg 
:name: fig-stress-strain-diagram-of-prestressing-steel

Typical stress-strain diagram of prestressing steel
```

As it can be seen from the diagram, prestressing steels do not have a distinct yield point, so that their yield stress is determined according to a strain criterion. Depending on the standard, yield stress, $f_{p y}$, can be defined as the stress at the $0.1 \%$ offset, $f_{p 0.1}$ (which can also referred to as $0.1 \%$ proof stress {cite}`EN10138`), as the stress at the $0.2 \%$ offset, $f_{p 0.2}$ (or $0.2 \%$ proof stress) {cite}`AS1310`, or according to ASTM standards {cite}`ASTMA421_A722` as the stress that corresponds to a total strain of $1 \%$ for wires and strands and of $0.75 \%$ for prestressing bars.

Other important parameters of the stress-strain diagram are:

- the modulus of elasticity, $E_{p}$;
- the proportional limit, $f_{p p}$, which is usually determined as the stress at the $0.01 \%$ (or $0.02 \%$ ) offset;
- the tensile strength, $f_{p}$, and
- the elongation at maximum load, $\varepsilon_{u}$.

Only probabilistic models of these parameters of the stress-strain diagram are considered in the following.

For calculations where an analytical description of the stress-strain diagram is needed, it can be represented by the Ramberg-Osgood curve {cite}`RambergOsgood1943` defined in terms of three parameters - the initial modulus of elasticity, $E_{p}$, a proof stress, $\sigma_{p}$, and a parameter $n$ defining the sharpness of the knee of the stress-strain diagram

```{math}
:label: eq-static-properties-of-prestressing-steel-1
\varepsilon=\frac{\sigma}{E_{p}}+p\left(\frac{\sigma}{\sigma_{p}}\right)^{n}
```

where $p$ is the plastic strain corresponding to $\sigma_{p}$. The proof stress is usually chosen as the $0.1 \%$ (i.e., $\sigma_{p}=f_{p 0.1}$ ) or $0.2 \%$ (i.e., $\sigma_{p}=f_{p 0.2}$ ) proof stress and the corresponding values of $p$ are 0.001 and 0.002 , respectively. The probabilistic models of $E_{p}, f_{p 0.1}$ and $f_{p 0.2}$ are presented in the following, while the parameter $n$ can be determined by requiring that the Ramberg-Osgood curve passes through the ultimate point $\left(\varepsilon_{u}, f_{p}\right)$

```{math}
:label: eq-static-properties-of-prestressing-steel-2
n=\frac{\ln \left\lfloor\left(\varepsilon_{u}-f_{p} / E_{p}\right) / p\right\rfloor}{\ln \left(f_{p} / \sigma_{p}\right)}
```

However, when $n$ is determined using Eq. {eq}`eq-static-properties-of-prestressing-steel-2` the Ramberg-Osgood curve may noticeably deviate from measured stress-strain diagrams, especially for stresses between $f_{p p}$ and $\sigma_{p}$. A better approximation may be achieved by using a modified Ramberg-Osgood curve consisting of two parts {cite}`Rasmussen2001`

```{math}
:label: eq-static-properties-of-prestressing-steel-3
\varepsilon=\left\lbrace\begin{array}{cc}
\frac{\sigma}{E_{p}}+p\left(\frac{\sigma}{\sigma_{p}}\right)^{n^{\prime}} & \text { for } \sigma \leq \sigma_{p} \\
\frac{\sigma-\sigma_{p}}{E_{p}^{\prime}}+\varepsilon_{u}\left(\frac{\sigma-\sigma_{p}}{f_{p}-\sigma_{p}}\right)^{m}+\varepsilon_{p} & \text { for } \sigma>\sigma_{p}
\end{array}\right.
```

where $\varepsilon_{p}$ and $E_{p}$ 'are the strain and tangent to the stress-strain curve at $\sigma_{p}$, and $m$ is a parameter which determines the shape of the stress-strain curve in the range $\sigma_{p} \leq \sigma \leq f_{p}$. The parameter $n$ 'for the first part is determined based on the $0.01 \%\left(f_{p p}\right)$ and $\sigma_{p}$ proof stresses that leads to the following formula

```{math}
:label: eq-static-properties-of-prestressing-steel-4
n^{\prime}=\frac{\ln (p / 0.0001)}{\ln \left(\sigma_{p} / f_{p p}\right)}
```

The parameters of the second part are estimated as

```{math}
:label: eq-static-properties-of-prestressing-steel-5
\varepsilon_{p}=\frac{\sigma_{p}}{E_{p}}+p
```

```{math}
:label: eq-static-properties-of-prestressing-steel-6
E_{p}^{\prime}=\frac{E_{p}}{1+p n^{\prime} E_{p} / \sigma_{p}} 
```

```{math}
:label: eq-static-properties-of-prestressing-steel-7
m=1+3.5 \frac{\sigma_{p}}{f_{p}}
```

## Probabilistic model

Variability of the mechanical properties of prestressing steel is presented by the following independent ${ }^{1}$ random variables: $f_{p}, E_{p}$ and $\varepsilon_{u}$. Statistical parameters of these random variables are given in {numref}`tbl-statistical-parameters-of-mechanical-properties-of-prestressing-steels`, where $f_{p k}$ is the characteristic (nominal) tensile strength of prestressing steel which usually denotes the steel grade.

```{table} Statistical parameters of mechanical properties of prestressing steels
:name: tbl-statistical-parameters-of-mechanical-properties-of-prestressing-steels
| Variable | Mean | Std. dev. | COV | Distribution <br> type | Reference |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $f_{p}$ | 1.04 $f_{p k}$ <br> or <br> $f_{p k}$ + 66 [MPa] | - <br> <br> 40 MPa | 0.025 <br> <br> - | Normal | {cite}`Mirza1980` <br> <br> {cite}`ReportPrestressingSteels1976` |
| $E_p$ | 200 GPa – for wires <br> 195 GPa – for strands <br> 200 GPa – for bars | - | 0.02 | Normal | {cite}`Mirza1980` |
| $\varepsilon_u$ | 0.05 | 0.0035 | - | Normal | {cite}`Mirza1980` |
```

According to available experimental data {cite}`Mirza1980` there is strong correlation between the tensile strength $f_{p}$ and the other stresses that characterise the stress-strain diagram (i.e., $f_{p p}, f_{p y}$, etc.). Thus, these stresses can be expressed via $f_{p}$. The relation between the stresses and $f_{p}$ can be obtained from information provided by the steel supplier, or if such information is not available, data given in {numref}`tbl-relation-between-tensile-strength-and-other-stresses-characterising-prestressing-steel` can be used (see {cite}`EN1992-1`-{cite}`CEB-FIPMC90`).

```{table} Relation between the tensile strength and the other stresses characterising prestressing steel
:name: tbl-relation-between-tensile-strength-and-other-stresses-characterising-prestressing-steel
| Steel type | {math}`f_{p p}` | {math}`f_{p 0.1}` | {math}`f_{p 0.2}` | {math}`f_{p \mathrm{y}}` (at 1\% total strain) |
| :--- | :---: | :---: | :---: | :---: |
| Wire | 0.70 {math}`f_{p}` | 0.86 {math}`f_{p}` | 0.90 {math}`f_{p}` | 0.85 {math}`f_{p}` |
| Strand | 0.65 {math}`f_{p}` | 0.85 {math}`f_{p}` | 0.90 {math}`f_{p}` | 0.85 {math}`f_{p}` |
| Bar |  |  |  | 0.85 {math}`f_{p}` |
```

## Bundles of tendons

A bundle is formed of tendons (wires or strands) laid together in parallel. Although prestressing steels do not show distinct yielding relatively flat and long hardening part of the stress-strain diagram allows to assume that the tensile strength of a bundle of tendons equals to the sum of the strengths of the individual tendons in the bundle (i.e., full plasticity model). If there are no data about correlation between the tensile strengths of individual tendons in a bundle, between tendons that are not parts of a same bundle, etc., full correlation between the tensile strengths of individual tendons can be assumed.

## Prestressing force

The effect of prestress on structural concrete is often considered as a prestressing force applied to the concrete. A prestressing force $P(x, t)$ at a distance $x$ from the active (i.e., jacking) end at a time $t$ can be expressed as

```{math}
:label: eq-static-properties-of-prestressing-steel-8
P(x, t)=P_{0}-\Delta P(x, t)
```

where $P_{0}$ is the jacking force and $\Delta P(x, t)$ losses of prestress. The losses depend on a number of factors such as the type of prestress (i.e., internal or external, pretensioning or post-tensioning, bonded or unbonded), properties of prestressing steel and concrete, environmental conditions, etc. Due to multiplicity of these factors and interrelation existing between some of them an exact analytical determination of $\Delta P(x, t)$ is not possible and different design codes provide different empirical models to estimate the losses.

In practice it is usually necessary to consider the values of prestressing force at two times:

- The prestressing force applied to the concrete at the time $`t=t_{0}$ immediately after transfer

```{math}
:label: eq-static-properties-of-prestressing-steel-9
P\left(x, t_{0}\right)=P_{0}-\Delta P\left(x, t_{0}\right)
```

where $\Delta P\left(x, t_{0}\right)$ is the immediate loss which (depending on the type of prestress) includes losses due to elastic shortening of concrete, friction, short-term relaxation of prestressing steel and anchorage slip.

- The effective (or long-term) prestressing force applied to the concrete at the time $t=\infty$, i.e., after losses have stabilised

```{math}
:label: eq-static-properties-of-prestressing-steel-10
P(x, \infty)=P_{0}-\Delta P\left(x, t_{0}\right)-\Delta P(x, \infty)
```

where $\Delta P(x, \infty)$ is the time-dependent (or deferred) loss which includes losses due to creep and shrinkage of concrete and long-term relaxation of prestressing steel.

Normally, jacks used for prestressing are regularly calibrated that ensures good control over the jacking force$P_{0}$. Variability of $P_{0}$ can be estimated using data from the equipment producer and equipment calibration. Uncertainty associated with the evaluation of the prestressing force will depend on uncertainty of models used to estimate prestress losses and variability of parameters employed in these models. Currently, no sufficient statistical data are available to quantify uncertainties of the prestress losses models and of the parameters associated with the models (e.g., {cite}`Mathieu1991`).

For typical situations the mean values of prestress losses can be estimated in accordance with models provided in design codes and in absence of more specific data COVs of given in {numref}`COVs-of-prestress-losses-and-prestressing-force` can be used (Note: these COVs are based on data for internal bonded tendons). Prestress losses can be treated as normal random variables. For typical magnitudes of prestress losses the corresponding COVs of prestressing forces have been estimated and their values are also presented in {numref}`COVs-of-prestress-losses-and-prestressing-force` (Note: these values are in good agreement with the assessments presented in {cite}`Naaman1982`).

```{table} Coefficients of variation (COVs) of prestress losses and prestressing force
:name: COVs-of-prestress-losses-and-prestressing-force
| Parameter | COV | COV |
| :--- | :---: | :---: |
|  | Immediate, $t=t_{0}$ | Long-term, $t=\infty$ |
| Prestress losses, $\Delta P(x, t)$ | 0.3 | 0.3 |
| Prestressing force, $P(x, t)$ | 0.04 - 0.06 | 0.06 - 0.09 |
```

For a bundle of tendons prestress losses are considered for the whole bundle, i.e., there is full correlation between prestress losses in different tendons of the bundle. Full correlation can be also assumed between prestress losses in tendons of the same bundle at different distances from the active end, i.e., $\Delta P\left(x_{1}, t\right)$ and $\Delta P\left(x_{2}, t\right)$ are fully correlated {cite}`Mathieu1991`.

**References**

```{bibliography}
:filter: docname in docnames
```

