# Snow Load

**List of symbols:**

$C_{e} \quad=$ exposure coefficient

$C_{r} \quad=$ redistribution (due to wind) coefficient

$C_{t} \quad=$ deterministic thermal coefficient

$d \quad=$ snow depth

$h \quad=$ altitute of the building site

$h_{r} \quad=$ reference altitude

$k=$ coefficient for altitude conversion

$r=$ conversion factor of snow load on ground to snow load on roofs

$S_{r} \quad=$ snow load on the roof

$S_{g} \quad=$ snow load on ground at the weather station

$\gamma(d)=$ average weight density of the snow for depth $d$

$\eta_{a} \quad=$ shape coefficient

## Basic Model for Snow Load on roofs

The snow load on roofs, $S_{r}$, is determined by the relation

```{math}
:label: eq-snow-load-1
S_{r}=S_{g}~r~k^{h / h_{r}}
```

where

$S_{g}$ is the snow load on ground at the weather station

$r$ is a conversion factor of snow load on ground to snow load on roofs (see [16.3.](section-2.12.3)).

$h$ is the altitute of the building site

$h_{r}$ is a reference altitude $(=300 ~m)$

$k$ is a coefficient: $k=1.25$ for coastal regions, $k=1.5$ for inland mountainous regions

The snow load $S_{r}$ acts vertically and refers to a horizontal projection of the area of the roof. $S_{g}$ is time dependent but not space dependent within a specified region with similar climatic conditions and with approximately the same altitude.

The characteristics of the ground snow load $S_{g}$ should be determined on the basis of observations from weather stations. The results of such observations are either water-equivalents of snow or depths of snow. In the first case the values can be used directly to determine the ground snow load. In the second case the data on snow depth must be converted to snow load by the relation

```{math}
:label: eq-snow-load-2
S_{g}=d~\gamma(d)
```

where

d is the snow depth

$\gamma(d)$ is the average weight density of the snow

The density $\gamma(d)$ follows from:

```{math}
:label: eq-snow-load-3
\gamma(d)=\frac{\lambda \gamma(\infty)}{d} \ln \left\{1+\frac{\gamma(0)}{\gamma(\infty)}\left[\exp \left(\frac{d}{\lambda}\right)-1\right]\right\}
```

where

$\gamma(\infty) =5 kN / m^{3}, \gamma(0)=1.70 kN / m^{3}$ and $x=0.85 ~m$

## Probabilistic Model for $S_g$

A probability model of the ground snow load $S_{g}$ is presented by:

- a probability distribution function for the total duration $T$ of the load
- a probability distribution function for the maximum load $S_{gmax}$ within one year.

The distribution function $F_{sg \max }$, its mean $\mu$ and its coefficient of variation $V$ are denoted as:

for maritime climate : $F_{s 1}, \mu_{1}, ~V_{1}$

for continental climate : $F_{s 2}, \mu_{2}, ~V_{2}$

The probability distribution functions in these two cases are gamma distributions. The parameters should be based on local observations. As prior distribution a vague prior should be used. In some cases data from "similar stations" can be used as prior with $n^{\prime}=3$ and $v^{\prime}=2$.

In those cases when the climate is a mixture of maritime and continental climate, a part $p$ of the observations are associated with a continental climate and a part $1-p$ with a maritime climate. The combined probability distribution function $F$ for the mixed climates can then be written as $F_{s}=(1-p) F_{s 1}+p F_{s 2}$.

(section-2.12.3)=
## Conversion ground to roof snow load

### General

The conversion factor $r$ is subdivided into a number of factors and terms according to the expression

```{math}
:label: eq-snow-load-6
r=\eta_{a}~C_{e}~C_{t}+C_{r}
```
where

$\eta_{a}$ is a shape coefficient, a random variable according to [16.3.2.](section-2.12.3.2)

$C_{e}$ is a deterministic exposure coefficient according to [16.3.2.](section-2.12.3.2)

$C_{t}$ is a deterministic thermal coefficient according to [16.3.3.](section-2.12.3.3)

$C_{r}$ is a redistribution (due to wind) coefficient, a random variable according to 2.12.3.4. If redistribution is not taken into account $C_{r}=0$

(section-2.12.3.2)=
### The exposure coefficient $C_e$ and shape factor $\eta_a$

The exposure coefficient, $C_{e}$ and the shape factor $\eta_{a}$ are a reduction coefficients taking account of the exposure to wind of a building and the slope of the roof $\alpha$ :

```{math}
\begin{array}{|l|l|}
\hline \alpha=0^{\circ} & C_{e} \eta_{a}=0.4+0.6 \exp (-0,1 u(H)) \\
\hline \alpha=25^{\circ} & C_{e} \eta_{a}=0.7+0.3 \exp (-0,1 u(H)) \\
\hline \alpha=60^{\circ} & C_{e} \eta_{a}=0 \\
\hline
\end{array}
```

$u(H)$ is the wind speed, averaged over a period of one week, at roof level $H$.  
For intermediate values of $\alpha$ linear interpolation should be used.

(section-2.12.3.3)=
### The thermal coefficient $C_t$

The thermal coefficient, $C_{t}$, accounts for the reduction of snow load on roofs with high thermal transmittance, in particular glass covered roofs. $C_{t}$ is equal to 1.0 for buildings which are not heated and for buildings where the roofs are highly insulated. A value of 0.8 shall be used for most other cases.


### The redistribution coefficient $C_r$

The redistribution coefficient, $C_{r}$, takes account of the redistribution of the snow on the roof caused by wind but in some cases also by other causes.

For monopitch roofs the redistribution of snow load may be neglected.

For symmetrical duopitch roofs the coefficient $C_{r}$ is assumed to be constant and equal to $\pm C_{ro}$ for each half of the roof according to {numref}`fig-redistributed-snow-load-on-a-duopitch-roof`. $C_{ro}$ has a $\beta$-distribution with $\mu\left(C_{ro}\right)$ according to {numref}`fig-C_ro-as-a-function-of-roof-angle`; the coefficient of variation of $C_{r}$ is equal to 1.0. For other types of roofs the numerical values given in ENV 1991-2-3 and ISO 4355 shall be used. These values can be assumed to correspond to the mean value plus one standard deviation.

```{figure} ../part-02/images/redistributed-snow-load-on-a-duopitch-roof.jpg 
:name: fig-redistributed-snow-load-on-a-duopitch-roof

The redistributed snow load on a duopitch roof
```

```{figure} ../part-02/images/C_ro-as-a-function-of-roof-angle.jpg 
:name: fig-C_ro-as-a-function-of-roof-angle

$C_{ro}$ as function of the roof angle
```

**Summary of snow load variables**

```{table} 
| X | designation | distribution | mean | scatter |
| :---: | :---: | :---: | :---: | :---: |
| $S_{g}$ <br> $d_{g}$ | snow depth on the grund snowload on the ground | gamma | observation $^{1)}$ | observation $^{1)}$ |
| $\rho$ | climate type parameter | det | observation | observation |
| $k$ | parameter | det | 1.5 / 1.25 $~m$ | - |
| $h_{r}$ | reference height | det | 300 $~m$ | - |
| $\gamma(0)$ | unit weight at $t=0$ | det | 1.7 $kN / m^{3}$ | - |
| $\gamma(\infty)$ | unit weight at $t=\infty$ | det | 5.0 $kN / m^{3}$ | - |
| $\lambda$ | parameter | det | 0.85 $~m$ | - |
| $C_{e} \eta_{a}$ | shape coefficient | beta | [16.3.2.](section-2.12.3.2) | $V=0.15$ |
| $C_{t}$ | insulation parameter | det | 0.8 - 1.0 | - |
| $C_{ro}$ | redistribution coefficient | beta | {numref}`fig-C_ro-as-a-function-of-roof-angle` | $~V=1.0$ |
```

${ }^{1)}$ Data from similar stations can be used as prior with $n^{\prime}=3$ and $v^{\prime}=2$.