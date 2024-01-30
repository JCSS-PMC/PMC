# Static Properties Of Reinforcing Steel

**List of symbols:**

{math}`\begin{array}{ll}\mathrm{f}_{\mathrm{y}} & =\text { basic yield stress } \\ \sigma & =\text { standard deviation }\end{array}`

## Basic Model

Reinforcing steel generally is classified and produced according to grades, for example S300, S400 and S500, the numbers denoting a specified (minimum) yield stress limit. The basic mechanical property is the static yield strength {math}`\mathrm{f_{y}}` defined at strain {math}`0.2 \%`. The stress-strain curve for hot rolled steels can be approximated by a bi-linear relationship up to strains of {math}`1 \%` to {math}`2 \%`. The (initial) modulus of elasticity can be taken as constant {math}`\mathrm{E}_{\mathrm{a}}=205[\mathrm{Gpa}]`. The stress-strain relationship for cold worked steel can also be represented by a bi-linear law but more realistically by a continuous curve for which several convenient analytical forms exist.

## Probabilistic Model

The yield stress, denoted by {math}`\mathrm{X}_{1}`, can be taken as the sum of three independent Gaussian variables

```{math}
:label: eq-static-properties-of-reinforcing-steel-1
X_{1}(d)=X_{11}+X_{12}+X_{13} \hspace{20em} [\mathrm{MPa}]
```

where {math}`\mathrm{X}_{11} \sim \mathrm{N}\left(\mu_{11}(\mathrm{d}), \sigma_{11}\right)` represents the variations in the global mean of different mills, {math}`\mathrm{X}_{12} \sim \mathrm{N}\left(0, \sigma_{12}\right)` the variations in a mill from batch(melt) to bath and {math}`\mathrm{X}_{13} \sim \mathrm{N}\left(0, \sigma_{13}\right)` the variations within a melt. {math}`\mathrm{D}` is the nominal bar diameter in [mm]. For high standard steel production the following values have been found: {math}`\sigma_{11}=19~[\mathrm{MPa}]`, {math}`\sigma_{12}=22~[\mathrm{MPa}]`, {math}`\sigma_{13}=8~[\mathrm{MPa}]` resulting in an overall standard deviation {math}`\sigma_{1}` of about {math}`30~[\mathrm{MPa}]`. The mean {math}`\mu_{11}=\mu_{1}` is under controlled conditions {math}`\mathrm{Sxxx}` {math}`+2 \sigma_{1}`. Strength fluctuations along bars are negligible. The value of {math}`\mu_{1}(\mathrm{~d})` is defined as the overall mean from the entire production given a particular bar diameter.

```{math}
:label: eq-static-properties-of-reinforcing-steel-2
\mu_{1}(d)=\mu_{1}\left(0.87+0.13 \exp [-0.08 d])^{-1}\right. \hspace{14.2em} [\mathrm{MPa}]
```

Statistical parameters of some other relevant properties are given in the following table:

```{table}
| {math}`\text{Quantity}` | {math}`\text{Mean}` | {math}`\sigma` | {math}`\text{C.o.V}` | {math}`\rho_{\mathrm{ij}}` | {math}`\rho_{\mathrm{ij}}` | {math}`\rho_{\mathrm{ij}}` | {math}`\rho_{\mathrm{ij}}` | 
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| {math}`\text{Bar area}` <br> {math}`\left[\mathrm{mm}^{2}\right]` | {math}`\text { Nom. }` <br> {math}`\text { Area }` | - | 0.02 | 1.00 | 0.5 | 0.35 | 0 |
| {math}`\begin{array}{l}\text { Yield } \\ \text { stress } \\ \text { [MPa] }\end{array}` | {math}`\begin{array}{c}\mathrm{S}_{\mathrm{nom}}+ \\ 2 \sigma\end{array}` | 30 | - |  | 1.00 | 0.85 | -0.50 |
| {math}`\begin{array}{l}\text { Ultimate } \\ \text { strength } \\ \text { [MPa] }\end{array}` | - | 40 | - | sym | sym | 1.00 | -0.55 |
| {math}`\begin{array}{l}\delta_{10} \\ {[\%]}\end{array}` | - | - | 0.09 |  |  |  | 1.00 |
```

For these quantities a normal distribution can be adopted.

## Effect of Prior Investigations and Statistical Quality Control

Tests of the lot of reinforcing steel to be used can considerably diminish steel variations, if the lot is known to belong to the production of a specific mill and if it originates from the same batch. Very few direct tests are necessary. Acceptance control for a given lot can be very efficient to eliminate bad quality lots.

## Strength of Bundles of Bars

The yield forces of bundles of bars under static loading is the sum of the yield forces of each contributing bar (full plasticity model). In general, it can be assumed that all reinforcing steel used at a job originates from a single (but unknown) mill. The correlation coefficient between yield forces of individual bars of the same diameter can then be taken as 0.9. The correlation coefficient between yield forces of bars of different diameter and between the yield forces in different cross-sections in different beams in a structure can be taken as 0.4 . Along structural members the correlation is unity within distances of roughly 10m (representative for bar length) and vanishes outside.


