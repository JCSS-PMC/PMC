# Static Properties Of Prestressing Steel (Prestressed Concrete)

**List of symbols:**

{math}`E_{p}=` modulus of elasticity

{math}`E_{p}{ }^{\prime}=` tangent to the stress-strain curve at the proof stress {math}`\sigma_{p}`

{math}`f_{p}=` tensile strength

{math}`f_{p 0.1}=0.1 \%` proof stress

{math}`f_{p 0.2}=0.2 \%` proof stress

{math}`f_{p p}=` proportional limit

{math}`f_{p y}=` yield stress

{math}`m=` parameter of the second part of the modified Ramberg-Osgood curve

{math}`n=` parameter of the Ramberg-Osgood curve

{math}`n^{\prime}=` parameter of the first part of the modified Ramberg-Osgood curve

{math}`p=` plastic strain at the proof stress {math}`\sigma_{p}`

{math}`P =` prestressing force

{math}`P_{0}=` jacking force

{math}`\Delta P=` prestress losses

{math}`t=` time

{math}`x=` distance from the jacking end

{math}`\varepsilon=` strain

{math}`\varepsilon_{p}=` full strain at the proof stress {math}`\sigma_{p}`

{math}`\varepsilon_{u}=` strain corresponding to the tensile strength

{math}`\sigma=` stress

{math}`\sigma_{p}=` proof stress

## Types of prestressing steel

Three types of steel are used as prestressing tendons in concrete structures:

- cold drawn wires;
- strands - consist of a number of cold drawn wires spun together in helical configuration, most commonly used are 3-wire and 7-wire strands;
- high-strength bars.

More detailed description and requirements to steel products used in prestressing tendons in different countries may be found in appropriate standards (e.g., EN 10138 [1]).

## Stress-strain relationship

A typical stress-strain diagram of prestressing steel in uniaxial tension is shown in {numref}`fig-static-properties-of-prestressing-steel-1`.

```{figure} ../part-03/images/fig-static-properties-of-prestressing-steel-3.04.1.jpg
:name: fig-static-properties-of-prestressing-steel-1

Typical stress-strain diagram of prestressing steel
```

As it can be seen from the diagram, prestressing steels do not have a distinct yield point, so that their yield stress is determined according to a strain criterion. Depending on the standard, yield stress, {math}`f_{p \mathrm{y}}`, can be defined as the stress at the {math}`0.1 \%` offset, {math}`f_{p 0.1}` (which can also referred to as {math}`0.1 \%` proof stress [1]), as the stress at the {math}`0.2 \%` offset, {math}`f_{p 0.2}` (or {math}`0.2 \%` proof stress) [2], or according to ASTM standards [3] as the stress that corresponds to a total strain of {math}`1 \%` for wires and strands and of {math}`0.75 \%` for prestressing bars.

Other important parameters of the stress-strain diagram are:

- the modulus of elasticity, {math}`E_{p}`;
- the proportional limit, {math}`f_{p p}`, which is usually determined as the stress at the {math}`0.01 \%` (or {math}`0.02 \%` ) offset;
- the tensile strength, {math}`f_{p}`, and
- the elongation at maximum load, {math}`\varepsilon_{u}`.

Only probabilistic models of these parameters of the stress-strain diagram are considered in the following.

For calculations where an analytical description of the stress-strain diagram is needed, it can be represented by the Ramberg-Osgood curve [4] defined in terms of three parameters - the initial modulus of elasticity, {math}`E_{p}`, a proof stress, {math}`\sigma_{p}`, and a parameter {math}`n` defining the sharpness of the knee of the stress-strain diagram

```{math}
:label: eq-static-properties-of-prestressing-steel-1
\varepsilon=\frac{\sigma}{E_{p}}+p\left(\frac{\sigma}{\sigma_{p}}\right)^{n}
```

where {math}`p` is the plastic strain corresponding to {math}`\sigma_{p}`. The proof stress is usually chosen as the {math}`0.1 \%` (i.e., {math}`\sigma_{p}=f_{p 0.1}` ) or {math}`0.2 \%` (i.e., {math}`\sigma_{p}=f_{p 0.2}` ) proof stress and the corresponding values of {math}`p` are 0.001 and 0.002 , respectively. The probabilistic models of {math}`E_{p}, f_{p 0.1}` and {math}`f_{p 0.2}` are presented in the following, while the parameter {math}`n` can be determined by requiring that the Ramberg-Osgood curve passes through the ultimate point {math}`\left(\varepsilon_{u}, f_{p}\right)`

```{math}
:label: eq-static-properties-of-prestressing-steel-2
n=\frac{\ln \left\lfloor\left(\varepsilon_{u}-f_{p} / E_{p}\right) / p\right\rfloor}{\ln \left(f_{p} / \sigma_{p}\right)}
```

However, when {math}`n` is determined using Eq. {eq}`eq-static-properties-of-prestressing-steel-2` the Ramberg-Osgood curve may noticeably deviate from measured stress-strain diagrams, especially for stresses between {math}`f_{p p}` and {math}`\sigma_{p}`. A better approximation may be achieved by using a modified Ramberg-Osgood curve consisting of two parts [5]

```{math}
:label: eq-static-properties-of-prestressing-steel-3
\varepsilon=\left\lbrace\begin{array}{cc}
\frac{\sigma}{E_{p}}+p\left(\frac{\sigma}{\sigma_{p}}\right)^{n^{\prime}} & \text { for } \sigma \leq \sigma_{p} \\
\frac{\sigma-\sigma_{p}}{E_{p}^{\prime}}+\varepsilon_{u}\left(\frac{\sigma-\sigma_{p}}{f_{p}-\sigma_{p}}\right)^{m}+\varepsilon_{p} & \text { for } \sigma>\sigma_{p}
\end{array}\right.
```

where {math}`\varepsilon_{p}` and {math}`E_{p}` 'are the strain and tangent to the stress-strain curve at {math}`\sigma_{p}`, and {math}`m` is a parameter which determines the shape of the stress-strain curve in the range {math}`\sigma_{p} \leq \sigma \leq f_{p}`. The parameter {math}`n` 'for the first part is determined based on the {math}`0.01 \%\left(f_{p p}\right)` and {math}`\sigma_{p}` proof stresses that leads to the following formula

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

Variability of the mechanical properties of prestressing steel is presented by the following independent {math}`{ }^{1}` random variables: {math}`f_{p}, E_{p}` and {math}`\varepsilon_{u}`. Statistical parameters of these random variables are given in {numref}`tbl-static-properties-of-prestressing-steel-1`, where {math}`f_{p k}` is the characteristic (nominal) tensile strength of prestressing steel which usually denotes the steel grade.

```{table} Statistical parameters of mechanical properties of prestressing steels
:name: tbl-static-properties-of-prestressing-steel-1
| Variable | Mean | Std. dev. | COV | Distribution <br> type | Reference |
| :--- | :---: | :---: | :---: | :---: | :---: |
| {math}`f_{p}` | 1.04 {math}`f_{p k}` <br> or <br> {math}`f_{p k}` + 66 [MPa] | - <br> <br> 40 MPa | 0.025 <br> <br> - | Normal | [6] <br> <br> [7] |
| {math}`E_p` | 200 GPa – for wires <br> 195 GPa – for strands <br> 200 GPa – for bars | - | 0.02 | Normal | [6] |
| {math}`\varepsilon_u` | 0.05 | 0.0035 | - | Normal | [6] |
```

According to available experimental data [6] there is strong correlation between the tensile strength {math}`f_{p}` and the other stresses that characterise the stress-strain diagram (i.e., {math}`f_{p p}, f_{p y}`, etc.). Thus, these stresses can be expressed via {math}`f_{p}`. The relation between the stresses and {math}`f_{p}` can be obtained from information provided by the steel supplier, or if such information is not available, data given in {numref}`tbl-static-properties-of-prestressing-steel-2` can be used (see [8-9]).

```{table} Relation between the tensile strength and the other stresses characterising prestressing steel
:name: tbl-static-properties-of-prestressing-steel-2
| Steel type | {math}`f_{p p}` | {math}`f_{p 0.1}` | {math}`f_{p 0.2}` | {math}`f_{p \mathrm{y}}` (at 1\% total strain) |
| :--- | :---: | :---: | :---: | :---: |
| Wire | 0.70 {math}`f_{p}` | 0.86 {math}`f_{p}` | 0.90 {math}`f_{p}` | 0.85 {math}`f_{p}` |
| Strand | 0.65 {math}`f_{p}` | 0.85 {math}`f_{p}` | 0.90 {math}`f_{p}` | 0.85 {math}`f_{p}` |
| Bar |  |  |  | 0.85 {math}`f_{p}` |
```

## Bundles of tendons

A bundle is formed of tendons (wires or strands) laid together in parallel. Although prestressing steels do not show distinct yielding relatively flat and long hardening part of the stress-strain diagram allows to assume that the tensile strength of a bundle of tendons equals to the sum of the strengths of the individual tendons in the bundle (i.e., full plasticity model). If there are no data about correlation between the tensile strengths of individual tendons in a bundle, between tendons that are not parts of a same bundle, etc., full correlation between the tensile strengths of individual tendons can be assumed.

## Prestressing force

The effect of prestress on structural concrete is often considered as a prestressing force applied to the concrete. A prestressing force {math}`P(x, t)` at a distance {math}`x` from the active (i.e., jacking) end at a time {math}`t` can be expressed as

```{math}
:label: eq-static-properties-of-prestressing-steel-8
P(x, t)=P_{0}-\Delta P(x, t)
```

where {math}`P_{0}` is the jacking force and {math}`\Delta P(x, t)` losses of prestress. The losses depend on a number of factors such as the type of prestress (i.e., internal or external, pretensioning or post-tensioning, bonded or unbonded), properties of prestressing steel and concrete, environmental conditions, etc. Due to multiplicity of these factors and interrelation existing between some of them an exact analytical determination of {math}`\Delta P(x, t)` is not possible and different design codes provide different empirical models to estimate the losses.

In practice it is usually necessary to consider the values of prestressing force at two times:

- The prestressing force applied to the concrete at the time {math}`t=t_{0}` immediately after transfer

```{math}
:label: eq-static-properties-of-prestressing-steel-9
P\left(x, t_{0}\right)=P_{0}-\Delta P\left(x, t_{0}\right)
```

where {math}`\Delta P\left(x, t_{0}\right)` is the immediate loss which (depending on the type of prestress) includes losses due to elastic shortening of concrete, friction, short-term relaxation of prestressing steel and anchorage slip.

- The effective (or long-term) prestressing force applied to the concrete at the time {math}`t=\infty`, i.e., after losses have stabilised

```{math}
:label: eq-static-properties-of-prestressing-steel-10
P(x, \infty)=P_{0}-\Delta P\left(x, t_{0}\right)-\Delta P(x, \infty)
```

where {math}`\Delta P(x, \infty)` is the time-dependent (or deferred) loss which includes losses due to creep and shrinkage of concrete and long-term relaxation of prestressing steel.

Normally, jacks used for prestressing are regularly calibrated that ensures good control over the jacking force{math}`P_{0}`. Variability of {math}`P_{0}` can be estimated using data from the equipment producer and equipment calibration. Uncertainty associated with the evaluation of the prestressing force will depend on uncertainty of models used to estimate prestress losses and variability of parameters employed in these models. Currently, no sufficient statistical data are available to quantify uncertainties of the prestress losses models and of the parameters associated with the models (e.g., [10]).

For typical situations the mean values of prestress losses can be estimated in accordance with models provided in design codes and in absence of more specific data COVs of given in {numref}`tbl-static-properties-of-prestressing-steel-3` can be used (Note: these COVs are based on data for internal bonded tendons). Prestress losses can be treated as normal random variables. For typical magnitudes of prestress losses the corresponding COVs of prestressing forces have been estimated and their values are also presented in {numref}`tbl-static-properties-of-prestressing-steel-3` (Note: these values are in good agreement with the assessments presented in [11]).

```{table} Coefficients of variation (COVs) of prestress losses and prestressing force
:name: tbl-static-properties-of-prestressing-steel-3
| Parameter | COV | COV |
| :--- | :---: | :---: |
|  | Immediate, {math}`t=t_{0}` | Long-term, {math}`t=\infty` |
| Prestress losses, {math}`\Delta P(x, t)` | 0.3 | 0.3 |
| Prestressing force, {math}`P(x, t)` | 0.04 - 0.06 | 0.06 - 0.09 |
```

For a bundle of tendons prestress losses are considered for the whole bundle, i.e., there is full correlation between prestress losses in different tendons of the bundle. Full correlation can be also assumed between prestress losses in tendons of the same bundle at different distances from the active end, i.e., {math}`\Delta P\left(x_{1}, t\right)` and {math}`\Delta P\left(x_{2}, t\right)` are fully correlated [10].

**References**

[1] EN 10138. Prestressing steels. CEN, Brussels.

[2] AS 1310. Steel wire for tendons in prestressed concrete. Standards Australia.

[3] ASTM A 421. Uncoated stress-relieved steel wire for prestressed concrete. ASTM A 722. Uncoated high-strength steel bar for prestressing concrete. American Society for Testing and Materials, Philadelphia.

[4] Ramberg, W. and Osgood, W.R. Description of stress-strain curves by three parameters. Technical Note 902, NACA, 1943.

[5] Rasmussen, K.J.R. Full stress-strain curves for stainless steel alloys. Research Report R811, Department of Civil Engineering, University of Sydney, 2001.

[6] Mirza, S.A., Kikuchi, D.K. and MacGregor, J.G. Flexural strength reduction factor for bonded prestressed concrete beams. ACI Journal, 77(4), 1980, pp. 237-246.

[7] Report on Prestressing Steels: Types and Properties. FIP Commission on Prestressing Steels and Systems, FIP, Wexham Spring, England, 1976.

[8] EN 1992-1. Eurocode 2: Design of concrete structures. Part 1: General rules and rules for buildings. CEN, Brussels.

[9] CEB-FIP Model Code 1990 (CEB-FIP MC90). Bulletin D'Information No. 213/214, Lausanne, Switzerland.

[10] Mathieu, H. Reliability problems associated with prestress. In: Bulletin D'Information No. 202: Reliability of Concrete Structures. CEB, Lausanne, Switzerland, 1991, pp. 99-163.

[11] Naaman, A.E. and Siriaksorn, A. Reliability of partially prestressed concrete beams at serviceability limit states. PCI Journal, 27(6), 1982, pp. 66-85.

