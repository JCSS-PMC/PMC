# Static Properties of Structural Steel (Rolled Sections)

## Properties Considered

The following properties of structural steel are dealt with herein:

{math}`f_y=` yield strength [MPa]

{math}`f_u=` ultimate tensile strength [MPa]

{math}`E=` modulus of elasticity [MPa]

{math}`\nu=` Poisson's ratio

{math}`\varepsilon_u=` ultimate strain


A probabilistic model is proposed for the random vector {math}`\mathbf{X}=\left(f_{y}, f_{u}, E, \nu, \varepsilon_{u}\right)` to be used for any particular steel grade, which may be defined in terms of nominal values verified by standard mill tests (e.g. following the procedures of EN 10025 for sampling and selection of test pieces and the requirements of EN 10002-1 for testing) or in terms of minimum (hereinafter referred to as code specified) values given in material specifications (e.g. EN 10025: 1990).

Only distinct points or parts of the full stress-strain curve are considered, thus the proposed model can be used in applications where this type of information is compatible with the parameters of the mechanical model used for strength analysis.

In applications where strain-hardening (and in particular the extent of the yield plateau and the initial strain-hardening) are important (e.g. inelastic local buckling) a more detailed model, which describes the full stress-strain behaviour, may be warranted. Several deterministic models exist in the literature which would allow a probabilistic model to be developed. The parameters of the model chosen to describe the full stress-strain curve should be selected in a way that does not invalidate the statistics given below for the key points of the stress-strain diagram.

In certain cases, where an absence of a yield phenomenon is noted, the values given for the yield strength may be used instead for the 0.2% proof strength. However, it should be emphasised that most of the data examined refers to steels exhibiting a yield phenomenon, hence this is only a tentative proposal.

## Probabilistic Models and Range of Applicability

Mean values and coefficients of variation for the above vector are given in {numref}`tbl-static-properties-of-structural-steel-A` whereas the correlation matrix is given in {numref}`tbl-static-properties-of-structural-steel-B`. A multi-variate log-normal distribution is recommended. The values given are valid for static loading.

The values in {numref}`tbl-static-properties-of-structural-steel-A` may be used for steel grades and qualities given in EN 10025: 1990, which have code specified yield strength of up to 380 MPa. Some studies suggest that it is the standard deviation of the yield strength, rather than its coefficient of variation (CoV), that remains constant, whilst others point to the converse. A practice which creates problems with sample homogeneity, and hence with consistency of estimated statistical properties, is downgrading of material, i.e. re-classifying higher grade steel to a lower grade if it fails to meet the code specified values for the higher grade on the basis of quality control tests. This practice produces bi-modal distributions and is clearly seen in some of the histograms reported in the studies referenced below. Higher mean values but also significantly higher CoV's than those given in {numref}`tbl-static-properties-of-structural-steel-A` are to be expected in such cases.

The values given in {numref}`tbl-static-properties-of-structural-steel-A` and {numref}`tbl-static-properties-of-structural-steel-B` should not be used for ultra high strength steels (e.g. with code specified {math}`f_{y}=690 \mathrm{MPa}` ) without verification. In any case, ultra high strength carbon steel (and stainless steel) grades are characterised by a non-linear uniaxial stress-strain response, usually modelled through the Ramberg-Osgood expression. Practically no statistical data have been found for the three parameters describing the Ramberg-Osgood law (initial modulus, {math}`0.2 \%` proof stress and non-linearity index).

The CoV values refer to total steel production and are based primarily on European studies from 1970 onwards. In US and Canada higher CoV's have been used (on average, about 50\% higher). The main references on which these estimates are based are given below.

The estimates for ultimate strain, {math}`\varepsilon_{u}`, are very sensitive to test instrumentation and rate of loading up to the point of failure. Both significantly higher and lower CoV's have, on occasions, been reported.

Within-batch COVs can be taken as one fourth of the values given in {numref}`tbl-static-properties-of-structural-steel-A` but withinbatch variability for the modulus of elasticity, {math}`E`, and Poisson's ratio, {math}`\nu`, may be neglected. Variations along the length of a rolled section are normally small and can be neglected.

If direct measurements are available, the numbers in {numref}`tbl-static-properties-of-structural-steel-A` should be used as prior statistics with a relatively large equivalent sample size (e.g. {math}`n^{\prime} \approx 50` ).

For applications involving seismic loads, a random variable called 'yield ratio', denoted by {math}`r` and defined as the ratio of yield to ultimate strength, is often of interest. The statistical properties of this ratio can be derived from those given in {numref}`tbl-static-properties-of-structural-steel-A` and {numref}`tbl-static-properties-of-structural-steel-B` for the two basic random variables. Given the positive correlation between {math}`f_{y}` and {math}`f_{u}`, it follows that there is also a positive correlation between {math}`r` and {math}`f_{y}`. It can also be shown that the CoV for {math}`r` lies between the CoV's for {math}`f_{y}` and {math}`f_{u}`.

```{table} Mean and COV values
:name: tbl-static-properties-of-structural-steel-A
| Property | Mean Value, E[.] | COV, {math}`\mathrm{v}` |
| :---: | :---: | :---: |
| {math}`f_{y}` | {math}`f_{y s p} \cdot \alpha \exp (-u \cdot v)-C` | 0.07 |
| {math}`f_{u}` | {math}`B. E[f_u ]` | 0.04 |
| {math}`E` | {math}`E_{s p}` | 0.03 |
| {math}`\nu` | {math}`\nu_{s p}` | 0.03 |
| {math}`\varepsilon_{u}` | {math}`\varepsilon_{u s p}` | 0.06 |
```

```{table} Correlation Matrix
:name: tbl-static-properties-of-structural-steel-B
|  | {math}`f_{y}` | {math}`f_{u}` | {math}`E` | {math}`\nu` | {math}`\varepsilon_{u}`
| :---: | :---: | :---: | :---: | :---: | :---: |
| {math}`f_{y}` | 1 | 0.75 | 0 | 0 | -0.45 |
| {math}`f_{u}` |  | 1 | 0 | 0 | -0.60 |
| {math}`E` |  |  | 1 | 0 | 0 |
| {math}`\nu` |  |  |  | 1 | 0 |
| {math}`\varepsilon_{u}` |  |  |  |  | 1 |
```

## Definitions and Remarks

- the suffix ( {math}`_{s p}` ) is used for the code specified or nominal value for the variable considered
- {math}`\alpha` is spatial position factor ( {math}`\alpha=1.05` for webs of hot rolled sections and {math}`\alpha=1` otherwise)
- {math}`u` is a factor related to the fractile of the distribution used in describing the distance between the code specified or nominal value and the mean value; {math}`u` is found to be in the range of -1.5 to -2.0 for steel produced in accordance with the relevant EN standards; if nominal values are used for {math}`f_{y s p}` the value of {math}`u` needs to be appropriately selected.
- {math}`C` is a constant reducing the yield strength as obtained from usual mill tests to the static yield strength; a value of {math}`20 \mathrm{MPa}` is recommended but attention should be given to the rate of loading used in the tensile tests.

- {math}`B=1.5` for structural carbon steel  
{math}`\quad=1.4` for low alloy steel  
{math}`\quad=1.1` for quenched and tempered steel 

**References**

[1] Baker M J, 'Variability in the Strength of Structural Steels - A Study in Material Variability; Part 1: Material Variability', CIRIA Technical Note 44, 1972.

[2] Edlund L, 'Coefficients of Variation for the Yield Strength of Steel', 2nd Colloquium on Stability of Steel Structures, Final Report, Liege, 1977.

[3] Galambos T V and Ravindra M K, 'Properties of Steel for Use in LRFD', J. Str. Div., ASCE, Vol. 104, ST9, 1978.

[4] Kennedy D J L and Baker K A, 'Resistance Factors for Steel Highway Bridges', Can. J. Civ. Eng., Vol. 11, 1984, 324-34.

[5] Yamanouchi H, Kato B and Aoki H, 'Statistical Features of Mechanical Properties of Current Japanese Steels', Document for ECCS TC13: Seismic Design, 1990.

[6] Manzocchi G M E, Chryssanthopoulos M K and Elnashai A S, 'Statistical Analysis of Steel Tensile Test Data and Implications on Seismic Design Criteria', ESEE Report 92-7, Imperial College, 1992.

[7] Agostoni N, Ballio G and Poggi C, 'Statistical Analysis of the Mechanical Properties of Structural Steel', Costruzioni Metalliche, No.2, 1994, pp. 31-39.

