# Snow Load

**List of symbols:**

{math}`\mathrm{C}_{\mathrm{e}} \quad=` exposure coefficient

{math}`\mathrm{C}_{\mathrm{r}} \quad=` redistribution (due to wind) coefficient

{math}`\mathrm{C}_{\mathrm{t}} \quad=` deterministic thermal coefficient

{math}`\mathrm{d} \quad=` snow depth

{math}`\mathrm{h} \quad=` altitute of the building site

{math}`\mathrm{h}_{\mathrm{r}} \quad=` reference altitude

{math}`\mathrm{k}=` coefficient for altitude conversion

{math}`\mathrm{r}=` conversion factor of snow load on ground to snow load on roofs

{math}`\mathrm{S}_{\mathrm{r}} \quad=` snow load on the roof

{math}`\mathrm{S}_{\mathrm{g}} \quad=` snow load on ground at the weather station

{math}`\gamma(\mathrm{d})=` average weight density of the snow for depth {math}`\mathrm{d}`

{math}`\eta_{\mathrm{a}} \quad=` shape coefficient

## Basic Model for Snow Load on roofs

The snow load on roofs, {math}`\mathrm{S_{r}}`, is determined by the relation

```{math}
:label: eq-snow-load-1
\mathrm{S}_{\mathrm{r}}=\mathrm{S}_{\mathrm{g}}~\mathrm{r}~\mathrm{k}^{\mathrm{h} / \mathrm{h}_{\mathrm{r}}}
```

where

{math}`\mathrm{S}_{\mathrm{g}}` is the snow load on ground at the weather station

{math}`\mathrm{r}` is a conversion factor of snow load on ground to snow load on roofs (see [16.3.](section-2.12.3)).

{math}`\mathrm{h}` is the altitute of the building site

{math}`\mathrm{h}_{\mathrm{r}}` is a reference altitude {math}`(=300 \mathrm{~m})`

{math}`\mathrm{k}` is a coefficient: {math}`\mathrm{k}=1.25` for coastal regions, {math}`\mathrm{k}=1.5` for inland mountainous regions

The snow load {math}`\mathrm{S}_{\mathrm{r}}` acts vertically and refers to a horizontal projection of the area of the roof. {math}`\mathrm{S}_{\mathrm{g}}` is time dependent but not space dependent within a specified region with similar climatic conditions and with approximately the same altitude.

The characteristics of the ground snow load {math}`\mathrm{S}_{\mathrm{g}}` should be determined on the basis of observations from weather stations. The results of such observations are either water-equivalents of snow or depths of snow. In the first case the values can be used directly to determine the ground snow load. In the second case the data on snow depth must be converted to snow load by the relation

```{math}
:label: eq-snow-load-2
\mathrm{S}_{\mathrm{g}}=\mathrm{d}~\gamma(\mathrm{d})
```

where

d is the snow depth

{math}`\gamma(\mathrm{d})` is the average weight density of the snow

The density {math}`\gamma(\mathrm{d})` follows from:

```{math}
:label: eq-snow-load-3
\gamma(\mathrm{d})=\frac{\lambda \gamma(\infty)}{\mathrm{d}} \ln \left\{1+\frac{\gamma(0)}{\gamma(\infty)}\left[\exp \left(\frac{\mathrm{d}}{\lambda}\right)-1\right]\right\}
```

where

{math}`\gamma(\infty) =5 \mathrm{kN} / \mathrm{m}^{3}, \gamma(0)=1.70 \mathrm{kN} / \mathrm{m}^{3}` and {math}`\mathrm{x}=0.85 \mathrm{~m}`

## Probabilistic Model for {math}`\mathrm{S_g}`

A probability model of the ground snow load {math}`\mathrm{S}_{\mathrm{g}}` is presented by:

- a probability distribution function for the total duration {math}`\mathrm{T}` of the load
- a probability distribution function for the maximum load {math}`\mathrm{S_{gmax}}` within one year.

The distribution function {math}`\mathrm{F}_{\mathrm{sg} \max }`, its mean {math}`\mu` and its coefficient of variation {math}`\mathrm{V}` are denoted as:

for maritime climate : {math}`\mathrm{F}_{\mathrm{s} 1}, \mu_{1}, \mathrm{~V}_{1}`

for continental climate : {math}`\mathrm{F}_{\mathrm{s} 2}, \mu_{2}, \mathrm{~V}_{2}`

The probability distribution functions in these two cases are gamma distributions. The parameters should be based on local observations. As prior distribution a vague prior should be used. In some cases data from "similar stations" can be used as prior with {math}`\mathrm{n}^{\prime}=3` and {math}`\mathrm{v}^{\prime}=2`.

In those cases when the climate is a mixture of maritime and continental climate, a part {math}`\mathrm{p}` of the observations are associated with a continental climate and a part {math}`1-\mathrm{p}` with a maritime climate. The combined probability distribution function {math}`\mathrm{F}` for the mixed climates can then be written as {math}`\mathrm{F}_{\mathrm{s}}=(1-\mathrm{p}) \mathrm{F}_{\mathrm{s} 1}+\mathrm{p} \mathrm{F}_{\mathrm{s} 2}`.

(section-2.12.3)=
## Conversion ground to roof snow load

### General

The conversion factor {math}`\mathrm{r}` is subdivided into a number of factors and terms according to the expression

```{math}
:label: eq-snow-load-6
\mathrm{r}=\eta_{\mathrm{a}}~\mathrm{C_{e}~C_{t}+C_{r}}
```
where

{math}`\eta_{\mathrm{a}}` is a shape coefficient, a random variable according to [16.3.2.](section-2.12.3.2)

{math}`\mathrm{C}_{\mathrm{e}}` is a deterministic exposure coefficient according to [16.3.2.](section-2.12.3.2)

{math}`\mathrm{C}_{\mathrm{t}}` is a deterministic thermal coefficient according to [16.3.3.](section-2.12.3.3)

{math}`\mathrm{C}_{\mathrm{r}}` is a redistribution (due to wind) coefficient, a random variable according to 2.12.3.4. If redistribution is not taken into account {math}`\mathrm{C}_{\mathrm{r}}=0`

(section-2.12.3.2)=
### The exposure coefficient {math}`\mathrm{C_e}` and shape factor {math}`\eta_\mathrm{a}`

The exposure coefficient, {math}`\mathrm{C_{e}}` and the shape factor {math}`\eta_{\mathrm{a}}` are a reduction coefficients taking account of the exposure to wind of a building and the slope of the roof {math}`\alpha` :

```{math}
\begin{array}{|l|l|}
\hline \alpha=0^{\circ} & \mathrm{C}_{\mathrm{e}} \eta_{\mathrm{a}}=0.4+0.6 \exp (-0,1 \mathrm{u}(\mathrm{H})) \\
\hline \alpha=25^{\circ} & \mathrm{C}_{\mathrm{e}} \eta_{\mathrm{a}}=0.7+0.3 \exp (-0,1 \mathrm{u}(\mathrm{H})) \\
\hline \alpha=60^{\circ} & \mathrm{C}_{\mathrm{e}} \eta_{\mathrm{a}}=0 \\
\hline
\end{array}
```

{math}`\mathrm{u}(\mathrm{H})` is the wind speed, averaged over a period of one week, at roof level {math}`\mathrm{H}`.  
For intermediate values of {math}`\alpha` linear interpolation should be used.

(section-2.12.3.3)=
### The thermal coefficient {math}`\mathrm{C_t}`

The thermal coefficient, {math}`\mathrm{C}_{\mathrm{t}}`, accounts for the reduction of snow load on roofs with high thermal transmittance, in particular glass covered roofs. {math}`\mathrm{C}_{\mathrm{t}}` is equal to 1.0 for buildings which are not heated and for buildings where the roofs are highly insulated. A value of 0.8 shall be used for most other cases.


### The redistribution coefficient {math}`\mathrm{C_r}`

The redistribution coefficient, {math}`\mathrm{C}_{\mathrm{r}}`, takes account of the redistribution of the snow on the roof caused by wind but in some cases also by other causes.

For monopitch roofs the redistribution of snow load may be neglected.

For symmetrical duopitch roofs the coefficient {math}`\mathrm{C}_{\mathrm{r}}` is assumed to be constant and equal to {math}`\pm \mathrm{C}_{\mathrm{ro}}` for each half of the roof according to {numref}`fig-snow-load-1`. {math}`\mathrm{C}_{\mathrm{ro}}` has a {math}`\beta`-distribution with {math}`\mu\left(\mathrm{C}_{\mathrm{ro}}\right)` according to {numref}`fig-snow-load-2`; the coefficient of variation of {math}`\mathrm{C}_{\mathrm{r}}` is equal to 1.0. For other types of roofs the numerical values given in ENV 1991-2-3 and ISO 4355 shall be used. These values can be assumed to correspond to the mean value plus one standard deviation.

```{figure} ../part-02/images/Figure-1.jpg
:name: fig-snow-load-1

The redistributed snow load on a duopitch roof
```

```{figure} ../part-02/images/Figure-2.jpg
:name: fig-snow-load-2

{math}`\mathrm{C}_{\mathrm{ro}}` as function of the roof angle
```

**Summary of snow load variables**

```{table} 
| X | designation | distribution | mean | scatter |
| :---: | :---: | :---: | :---: | :---: |
| {math}`\mathrm{S}_{\mathrm{g}}` <br> {math}`\mathrm{d}_{\mathrm{g}}` | snow depth on the grund snowload on the ground | gamma | observation {math}`^{1)}` | observation {math}`^{1)}` |
| {math}`\rho` | climate type parameter | det | observation | observation |
| {math}`\mathrm{k}` | parameter | det | 1.5 / 1.25 {math}`\mathrm{~m}` | - |
| {math}`\mathrm{h}_{\mathrm{r}}` | reference height | det | 300 {math}`\mathrm{~m}` | - |
| {math}`\gamma(0)` | unit weight at {math}`\mathrm{t}=0` | det | 1.7 {math}`\mathrm{kN} / \mathrm{m}^{3}` | - |
| {math}`\gamma(\infty)` | unit weight at {math}`\mathrm{t}=\infty` | det | 5.0 {math}`\mathrm{kN} / \mathrm{m}^{3}` | - |
| {math}`\lambda` | parameter | det | 0.85 {math}`\mathrm{~m}` | - |
| {math}`\mathrm{C}_{\mathrm{e}} \eta_{\mathrm{a}}` | shape coefficient | beta | [16.3.2.](section-2.12.3.2) | {math}`\mathrm{V}=0.15` |
| {math}`\mathrm{C}_{\mathrm{t}}` | insulation parameter | det | 0.8 - 1.0 | - |
| {math}`\mathrm{C}_{\mathrm{ro}}` | redistribution coefficient | beta | {numref}`fig-snow-load-2` | {math}`\mathrm{~V}=1.0` |
```

{math}`{ }^{1)}` Data from similar stations can be used as prior with {math}`\mathrm{n}^{\prime}=3` and {math}`\mathrm{v}^{\prime}=2`.