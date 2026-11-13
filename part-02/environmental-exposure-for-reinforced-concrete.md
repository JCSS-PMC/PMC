# Environmental Exposure for Reinforced Concrete

Updated: 11.2026

```{admonition} Authors
:class: note
This chapter was prepared by **Dimitri Val**, **Carmen Andrade** and **Ton Vrouwenvelder**. The JCSS gratefully acknowledges their work.
```

**List of symbols:**

$\begin{array}{ll}b &= \text { CO}_2\text {-binding capacity of concrete}\\
b_{c},\ b_{w} &= \text { exponents of regression}\\
b_{T} &= \text { regression parameter of the temperature function}\\
c &= \text { concrete cover}\\
d_{h} &= \text { horizontal distance from the roadside}\\
d_{v} &= \text { vertical distance above the roadside}\\
k &= \text { a factor reflecting a number of aspects}\\
k_{e} &= \text { environmental function which accounts for the moisture conditions}\\
k_{c} &= \text { execution transfer parameter}\\
k_{t} &= \text { regression parameter}\\
k_{C,binder} &= \text { parameter accounting for the type of binder}\\
k_{C,w/c} &= \text { parameter accounting for the water-cement ratio of the concrete}\\
k_{C,Cl} &= \text { parameter accounting for the chloride concentration of sea water}\\
k_{C,ec} &= \text { parameter accounting for the exposure class}\\
k_{T} &= \text { temperature parameter which can be calculated from Arrhenius equation}\\
m &= \text { age factor}\\
p_{sr} &= \text { parameter representing the probability of driving rain}\\
t_{p} &= \text { propagation period}\\
x_{c}(t) &= \text { depth of the carbonation front (carbonation depth) at time } t\\
C_{CO_2} &= \text { concentration of CO}_2\\
C_{CO_2,s} &= \text { concentration of CO}_2 \text { in the surrounding air}\\
C_{crit} &= \text { critical chloride content to achieve depassivation of the reinforcement}\\
C &= \text { concentration of chloride ions}\\
D &= \text { chloride diffusion coefficient}\\
F_{Cl} &= \text { chloride corrosion rate factor}\\
F_{rust} &= \text { galvanic effect factor}\\
F_{O2} &= \text { oxygen availability factor}\\
F_{RH,T} &= \text { climatic factor}\\
I_{corr} &= \text { instantaneous corrosion current}\\
J_{CO_2} &= \text { flux of CO}_2\\
K_{corr} &= \text { a constant}\\
P_{corr} &= \text { corrosion penetration}\\
R^{-1}_{NAC,0} &= \text { inverse carbonation resistance of concrete in natural conditions}\\
R^{-1}_{ACC,0} &= \text { inverse effective carbonation resistance of concrete}\\
RH_{real} &= \text { relative air humidity}\\
RH_{ref} &= \text { reference relative humidity at test conditions}\\
ToW &= \text { the relative time of wetness}\\
V_{corr} &= \text { corrosion rate}\\
W(t) &= \text { weather function}\\
\alpha &= \text { pitting factor; FORM sensitivity factor}\\
\beta &= \text { reliability index}\\
\Delta x &= \text { depth of the convection zone}\\
\varepsilon_{t} &= \text { error term}\\
\phi &= \text { bar diameter}\\
\rho &= \text { resistivity}\end{array}$

## Introduction

During its life a structure is subject to various environmental influences (e.g., moisture, temperature, chemical substances, biological processes, etc.) which, over time, may cause deterioration of the structure material(s). Deterioration usually influences both resistance and appearance of a structure, which means that safety and serviceability of the structure may be seriously compromised.

In the case of deterioration, the basic formula of the probability of failure within a certain period of time $t_s$ may be written as:

```{math}
:label: eq-env-2.21.1
P_{F}(t_{s}) = \int f_{\mathbf{X}}(\mathbf{x})\, d\mathbf{x}
```

where the integration domain is given by $\min g[\mathbf{X},t] < 0$ for $t$ in $(0,t_s)$.

$\mathbf{X}$ is the vector of the basic random variables, which now includes in addition to mechanical load and resistance parameters also environmental parameters like chloride concentration, diffusion coefficients, humidity etc. The limit state function (LSF) $g(.)$ includes the effects of deterioration on the resistance properties like strength and geometry. In many cases, $P_F$ may be written as:

```{math}
:label: eq-env-2.21.2
P_{F} = P(g_{1}<0) + P(g_{2}<0 \cap g_{1}>0) + \ldots
```

```{math}
:label: eq-env-2.21.3
g_{k} = R_{k} - S_{k}
```

$R_k$ = mechanical resistance at the end of the time period $k$, as a result of deterioration of the initial resistance.

$S_k$ = the maximum mechanical load within the time period $k$.

The classical limit states are still SLS (appearance) and ULS (collapse). However, for convenience, to deal with different aspects of deterioration additional Condition Limit States are introduced, like the onset of corrosion or the initiation of deterioration (defined as a state corresponding to the initiation of *noticeable* deterioration of a structural component as described in ISO 2394 {cite}`ISO2394_2015` and ISO 13823 {cite}`ISO13823_2008`). These condition/deterioration limit states enable to refine/simplify the analysis of a deterioration process by considering various well-defined and controllable deterioration-related states, which are not associated with direct negative consequences. If done so, care should be taken to be on the conservative side, i.e., verify that the considered condition limit states do occur before the classical limit states.

Modelling a deterioration process involves significant uncertainties associated with environmental conditions, material properties, limitations of predictive models, and inadequacy of material testing, detection, and inspection methods. This section of the JCSS Model Code presents the state of the art on the models needed for the reliability analysis of structures subject to a number of relevant deterioration processes.

### Deterioration processes and modelling

A number of models relating the deterioration processes in reinforced concrete elements with time are currently available in the literature, among which the most mature at present are the ones on corrosion of reinforcing steel due to carbonation and chloride penetration. However, it has to be emphasised that these models have not been validated for longer than 30 years and the validation cases are still very scarce. Thus, the models, including values of their input parameters, presented further in this document have to be treated with caution and considered as a first step in developing more accurate ones in the future. The models in this document are mainly in line with the *fib* Model Code 2010 (MC2010) {cite}`fibMC2010`; however, in Annexes some other important models may also be presented for the sake of completeness. The latter may be used in addition to the models in the main part of the document in order to improve the confidence in obtained results. Furthermore, it is worth to note that the *fib* Model Code 2020 (MC2020) is currently under preparation; compared to MC2010 it includes models on corrosion propagation. Further relevant information on MC2020 can be found in Visser {cite}`Visser2018`.

With respect to other deterioration processes in concrete (freeze-thaw, alkali-aggregate reaction, sulphate attack, etc.), their models are not in MC2010 and not planned to be included in MC2020 due to their insufficient maturity and, as a result of that, a lack of general consensus about their accuracy and validity. Currently, the present document also covers only deterioration associated with corrosion of reinforcing steel.

### The main stages of the deterioration process

Under normal conditions concrete protects embedded reinforcing steel against corrosion. These protective properties of concrete are attributed to a passive oxide film which forms on the surface of steel in a highly alkaline environment provided by the concrete pore solution. However, environmental actions such as carbonation or penetration of chloride ions disrupt the protective properties of concrete and may lead, over time, to corrosion of reinforcing steel. The stage of the deterioration process between the first exposure of a RC structure to the environmental actions and the beginning of corrosion is called the initiation period.

After corrosion starts, there is the so-called propagation period. Its effects on a RC structure usually include cracking and potential delamination of the concrete cover, reduction and eventually loss of bond between concrete and corroding reinforcement, and reduction of the cross-sectional area of reinforcing steel. Hence, corrosion affects both load bearing capacity and serviceability of RC structures. The consequences of corrosion for RC structures are summarised in {numref}`fig-consequences-of-corrosion-for-rc-structures` {cite}`CONTECVET2001`.

```{figure} ../part-02/images/consequences-of-corrosion-for-rc-structures.jpg
:name: fig-consequences-of-corrosion-for-rc-structures
:width: 420px

Consequences of corrosion that affect the performance of RC structures and need to be considered in the verification of SLS and ULS {cite}`CONTECVET2001`, {cite}`DuraCrete2000`.
```

The two main stages of the structural deterioration process associated with corrosion of reinforcing steel are schematically shown in {numref}`fig-stages-of-corrosion-induced-deterioration`. It should be noted that, in principle, a structure can deteriorate during the initiation period due to other reasons than corrosion. However, since this deterioration is not caused by the penetration of chloride ions or carbonation it is not shown in {numref}`fig-stages-of-corrosion-induced-deterioration` {cite}`Tuutti1982`.

```{figure} ../part-02/images/stages-of-corrosion-induced-deterioration.png
:name: fig-stages-of-corrosion-induced-deterioration
:width: 520px

Schematic representation of the development of corrosion-induced deterioration in RC structures. Notation: $t_i$ = the time of corrosion onset; $t_{id}$ = the time of the initiation of deterioration, e.g., hairline (less than 0.05 mm wide) cracks on the concrete surface; $t_s$ = the time of SLS failure due to corrosion-induced damage, e.g., corrosion-induced crack width exceeds a serviceability limit; $t_u$ = the time of ULS failure due to corrosion-induced damage.
```

The two main aspects should be taken into account regarding the propagation stage:

* Corrosion morphology, i.e., whether the corrosion is more or less homogeneous or localised (see {numref}`fig-uniform-homogeneous-and-localised-corrosion`), in particular, because the localised corrosion can lead to the stress concentration phenomenon and negatively affect the steel ductility.
* Corrosion rate, i.e., the rate of the loss of the reinforcing steel cross-section over time, which directly controls the rate of structural deterioration during the propagation stage (see {numref}`fig-consequences-of-corrosion-for-rc-structures`).

With respect to the corrosion morphology, the attack can be more or less homogeneous over the surface (or its major part) of a reinforcing bar. In this case, a uniform loss of the cross-sectional area of the bar over its perimeter is very often assumed, which will be further referred to as *uniform corrosion* (see {numref}`fig-uniform-homogeneous-and-localised-corrosion`(a)). However, in general, corrosion initially starts in the part of the reinforcing bar closest to the concrete surface so that the loss of the bar cross-sectional area is not uniform over its perimeter (see {numref}`fig-uniform-homogeneous-and-localised-corrosion`(b)). This will be further referred to as *homogeneous corrosion*. When corrosion concentrates over a small part of the bar surface area it will be referred to a *localised* (or *pitting*) *corrosion* (see {numref}`fig-uniform-homogeneous-and-localised-corrosion`(c)).

```{figure} ../part-02/images/uniform-homogeneous-and-localised-corrosion.png
:name: fig-uniform-homogeneous-and-localised-corrosion
:width: 600px

Uniform, homogeneous and localised corrosion.
```

Regarding to the corrosion rate, it evolves with the climatic/environmental conditions and with the continuous generation of iron oxides, which modifies the steel concrete interface. The accumulation of the oxides around the corroding reinforcing bar reduces the access of oxygen to the bar surface that may slow down the corrosion process. Cracks in the concrete cover formed due the expansive character of the iron oxides may lead to an acceleration of the corrosion (if the structure is in continuous contact with water) or to slowing it down (if the structure is in air contact since the cracked zones dry quicker than non-cracked ones). Accordingly, there are three possibilities – the corrosion rate (A) remains more or less constant over time; (B) decreases; and (C) increases, especially after the formation of corrosion-induced cracks in the concrete cover (see {numref}`fig-possible-trends-of-the-corrosion-rate-over-time`). In general, in the cases (B) and (C) the relationship between the corrosion rate and the time is non-linear but often can be very well represented by bi-linear functions {cite}`AndradeRebolledo2017`.

```{figure} ../part-02/images/possible-trends-of-the-corrosion-rate-over-time.png
:name: fig-possible-trends-of-the-corrosion-rate-over-time
:width: 520px

Possible trends of the corrosion rate over time.
```

A particular case of steel corrosion in concrete is the stress corrosion cracking (SCC), which may develop in prestressed concrete members. The process starts by the nucleation of microcracks on the surface of the prestressing steel that may take a long time. One of these cracks may progress to a certain critical depth, from which the crack growth velocity is very high and the wire breaks in a brittle manner in a relatively short time. The mechanism of nucleation and, mainly, of progression of SCC is still not well understood. The structural failure may be either brittle or not depending on the reinforcing details, because the brittle failure of a prestressing tendon may not produce the brittle failure of the whole element.

### Limit states related to reinforcement corrosion

Typical limit states associated with corrosion of reinforcing steel are {cite}`DuraCrete2000`:

* Condition Limit States (ISO 2394) or Deterioration Limit States (ISO 13823)
  1. Depassivation of reinforcing steel and onset of corrosion.
  2. Initiation of deterioration, e.g., development of a micro crack (< 0.05 mm wide) parallel to the bar on the concrete surface; corrosion penetration exceeds 50 μm (homogeneous corrosion) or 500 μm (pitting corrosion).
* Serviceability Limit State (SLS)
  3. Width of a corrosion-induced crack exceeds its limit value (e.g. 0.3 mm)
* Ultimate Limit State (ULS)
  4. Loss of load bearing capacity

Another limit state, which may be considered, is *loss of bond*. It may be either a condition limit state (local loss of bond) or ULS (when it results in the loss of anchorage by the corroding reinforcing bar).

**Notes**

(1) The target reliability required for each of these limit states in general will be stricter when going from depassivation to the ultimate limit state, roughly climbing from for instance $\beta$ = from 0 to 1 for depassivation to $\beta$ = 4 for the ULS (design working life values).

(2) If condition limit states verification is used to replace the more complex serviceability of ultimate limit state verification, the target reliability should be chosen accordingly.

(3) Limit state functions may be formulated explicitly in the time domain as well as in the domain or (time dependent) physical variables like the crack width or chloride concentration near reinforcing steel. For example, in the case of SLS associated with corrosion-induced concrete cracking, the LSF can be expressed as either $g(\mathbf{X},t) = t_s - t$ or $g(\mathbf{X},t) = a_{lim} - a_{cr}(t)$, where $t_s$ is the time of serviceability failure, $t$ the time period under consideration, $a_{lim}$ the limit crack width, and $a_{cr}(t)$ the corrosion-induced crack width at $t$.

## Corrosion initiation

### Carbonation induced corrosion

Carbonation is produced due to the ingress of the carbon dioxide gas of the air through the concrete pore network. It is a process involving two mechanisms – diffusion of carbon dioxide, CO$_2$, from the atmosphere into concrete and its reaction with the alkaline cement hydration products. The reaction leads to reduction of the alkalinity of the concrete pore solution from pH about 12 to below 9, which destroys the thin passive oxide layer on the surface of steel reinforcement and makes the steel susceptible to corrosion.

In the case of carbonation, the critical value is reached when the depth of the carbonation front is larger than the cover depth. Thus, the LSF for time $t$ may be defined as (MC2010):

```{math}
:label: eq-env-2.21.4a
g(\mathbf{X},t) = c - x_{c}(t)
```

* $c$ is the thickness of the concrete cover,
* $x_c(t)$ is the carbonation depth at the time $t$,
* $t$ is the time period under consideration,
* $\mathbf{X}$ is the set of relevant (random) parameters.

The value of $x_c$ depends on the diffusion process as described in the next section.

Note that using {eq}`eq-env-2.21.4a` the probability of depassivation can be calculated for any point in time. Taking $t = t_d$ (where $t_d$ is the design working life) the probability of failure, i.e., $P[g(\mathbf{X},t_d)<0]$, for this limit state over the design period can be found. Hence, the alternative formulation of the LSF in the time domain is:

```{math}
:label: eq-env-2.21.4b
g(\mathbf{X},t) = t_{i}(\mathbf{X}) - t_{d}
```

where $t_i$ is the time of corrosion initiation due to carbonation, which can be found from {eq}`eq-env-2.21.4a` $g(\mathbf{X},t_i) = 0$.

#### Carbonation ingress model

The diffusion of CO$_2$ into concrete is usually described by Fick's 1$^{st}$ law of diffusion, which for one-dimensional diffusion is expressed as

```{math}
:label: eq-env-2.21.5
J_{CO_{2}} = - D_{CO_{2}}\frac{\partial C_{CO_{2}}}{\partial x}
```

where $J_{CO_2}$ is the flux of CO$_2$, $C_{CO_2}$ the concentration of CO$_2$, and $D_{CO_2}$ the diffusion coefficient of CO$_2$ in concrete. Considering that $J_{CO_2} = (1/A) \times dQ_{CO_2}/dt$, {eq}`eq-env-2.21.5` can be written as

```{math}
:label: eq-env-2.21.6
dQ_{CO_{2}} = A\, D_{CO_{2}}\frac{\Delta C_{CO_{2}}}{x}\, dt
```

where $Q_{CO_2}$ is the mass of diffusing CO$_2$, $A$ the surface area, $\Delta C_{CO_2}$ the difference in the CO$_2$ concentration in the atmosphere and at the carbonation front, and $x$ the distance from the concrete surface to the carbonation front.

CO$_2$ that diffuses into concrete reacts with the alkaline cement hydration products. This reaction is called carbonation as is the responsible of the pH lowering and it may simply be described by the reaction between Ca(OH)$_2$ and CO$_2$ (e.g., Taylor {cite}`Taylor1997`)

```{math}
:label: eq-env-2.21.7
\text{Ca}\left( \text{OH} \right)_{2} + \text{CO}_{2}\overset{H_{2}O}{\rightarrow}\text{CaCO}_{3} + H_{2}O
```

It should be noted that {eq}`eq-env-2.21.7` represents the final result of the reaction between CO$_2$ and Ca(OH)$_2$, which in reality involves a number of intermediate reactions not shown here for the sake of simplicity (alkali hydroxides carbonates first and later it does the hydrated calcium silicate). As a result of the reaction, practically insoluble CaCO$_3$ and water are formed. The reaction of carbonation removes free CO$_2$ from the mass balance that can be described by the following equation

```{math}
:label: eq-env-2.21.8
dQ_{CO_{2}} = b\, A\, dx
```

where $b$ is the CO$_2$-binding capacity of concrete, which depends mainly on the composition of the concrete.

If to assume that the reaction of carbonation, {eq}`eq-env-2.21.7`, occurs instantaneously withdrawing CO$_2$ from the concrete pores and preventing it from diffusing further, the mass balance equation at the carbonation front can then be formulated using {eq}`eq-env-2.21.6` and {eq}`eq-env-2.21.7`

```{math}
:label: eq-env-2.21.9
b\, A\, dx = A\, D_{CO_{2}}\frac{\Delta C_{CO_{2}}}{x}\, dt
```

The solution of this equation for $x_c(0) = 0$ as proposed by Tuutti {cite}`Tuutti1982` and Schiessl {cite}`Schiessl1997` is:

```{math}
:label: eq-env-2.21.10
x_{c}(t) = \sqrt{\frac{2D_{CO_{2}}\Delta C_{CO_{2}}}{b}}\sqrt{t}
```

where $x_c$ is the depth of the carbonation front at time $t$.

In this document, the model presented is the one used in DuraCrete {cite}`DuraCrete2000` and in slightly modified form in LIFECON {cite}`LIFECON2003`, *fib* {cite}`fib2006` and MC2010. According to this model the depth of carbonation in [m] at time $t$ [s] is evaluated as (*fib* {cite}`fib2006`)

```{math}
:label: eq-env-2.21.11
x_{c}\left( t \right) = \sqrt{2k_{e}k_{c}R_{NAC,0}^{- 1}C_{CO_{2},s}}\sqrt{t}\, W\left( t \right)
```

where $k_e$ is the environmental function which accounts for the moisture conditions, $k_c$ the execution transfer parameter, $R^{-1}_{NAC,0}$ the inverse carbonation resistance of concrete determined in natural conditions in [(m$^2$/s)/(kg/m$^3$)], $C_{CO_2,s}$ the concentration of CO$_2$ in the surrounding air in [kg/m$^3$], and $W(t)$ the weather function.

For $k_e$, $k_c$, $R^{-1}_{NAC,0}$ and $W(t)$ the weather function more detailed models exists:

```{math}
:label: eq-env-2.21.12
k_{e} = \left( \frac{1 - RH_{real}^{5}}{1 - RH_{ref}^{5}} \right)^{2.5}
```

```{math}
:label: eq-env-2.21.13
k_{c} = \left( \frac{t_{c}}{7} \right)^{b_{c}}
```

```{math}
:label: eq-env-2.21.14
R_{NAC,0}^{- 1} = \frac{D_{CO_{2}}}{b}
```

The value of $R^{-1}_{NAC,0}$ can be related to the result of accelerated tests using:

```{math}
:label: eq-env-2.21.15
R_{NAC,0}^{- 1} = k_{t}R_{ACC,0}^{- 1} + \varepsilon_{t}
```

Further:

```{math}
:label: eq-env-2.21.16
W\left( t \right) = \left( \frac{t_{0}}{t} \right)^{w}
```

where the weather exponent $w$ which may be expressed as:

```{math}
:label: eq-env-2.21.17
w = \frac{\left( p_{sr}\, ToW \right)^{b_{w}}}{2}
```

In the above equations, $RH_{real}$ is the relative air humidity obtained using data from the nearest weather station, $RH_{ref}$ the reference relative humidity at test conditions, $RH_{ref}$ = 0.65, $t_c$ the period of curing in [days], $b_c$ the exponent of regression, $D_{CO_2}$ the diffusion coefficient of CO$_2$ in concrete, $b$ the CO$_2$-binding capacity of concrete, $R^{-1}_{ACC,0}$ the inverse effective carbonation resistance of concrete determined by laboratory testing, $k_t$ a regression parameter, $\varepsilon_t$ an error term, $ToW$ the relative time of wetness ($ToW$ represents the relative time that there is more rain than 2.5 mm per day), $p_{sr}$ the parameter representing the probability of driving rain, and $b_w$ the exponent of regression.

#### Random variables for carbonation ingress

{numref}`table-env-carbonation-ingress-input-parameters` gives an overview of the various probabilistic models, where $V$ denotes the coefficient of variation.

```{table} Probabilistic models of input parameters for the carbonation ingress model
:name: table-env-carbonation-ingress-input-parameters
| $X$ | designation | unit | mean | scatter | dist. |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $C_{CO_2,s}$ | Equivalent CO$_2$ concentration | kg/m$^3$ | 8·10$^{-4}$ Note (3) | $V$=0.12 | N |
| $R^{-1}_{NAC,0}$ | Inverse resistance against carbonation | (m$^2$/s)/(kg/m$^3$) | Note (4) | Note (4) | N |
| $RH$ | Equivalent $RH$ at concrete surface | - | Note (1) | - | |
| $RH_{ref}$ | Reference value | - | 0.65 | - | |
| $b_c$ | Empirical constant | - | -0.567 | $V$=0.04 | N |
| $p_{sr}$ | Prob. of rain driving wind direction | - | Note (1,2) | - | |
| $k_t$ | Regression coefficient in resistance | - | 1.25 | $V$=0.28 | N |
| $\varepsilon_t$ | Error term in resistance | (m$^2$/s)/(kg/m$^3$) | 10$^{-11}$ | $V$=0.15 | N |
| $ToW$ | Relative time of wetting | - | Note (1) | - | |
| $b_w$ | Coefficient weather function | - | 0.446 | $V$=0.36 | N |
| $t_o$ | Reference time weather function | s <br> (d) <br> (yr) | 2.4·10$^6$ <br> (28) <br> (0.077) | - | |
```

Note (1): The statistics for $RH$, $p_{sr}$ and $ToW$ should be derived from local weather stations. Example values for the Netherlands are: $RH$ = 0.85, $p_{sr}$ = 0.25 and $ToW$ = 0.05.

Note (2): For horizontal elements $p_{sr}$ = 1 and for interior elements $p_{sr}$ = 0.

Note (3): The ambient CO$_2$ concentration increases over time due to climate change and its mean value should be updated to account for this effect.

Note (4): $R^{-1}_{ACC,0}$ in {eq}`eq-env-2.21.15` is determined by the ACC test, which is carried out using concrete specimens at the age of 28 days (7 day curing in tap water at $T$=+20°C and then 21 day storage at $T$=+20°C and $RH$=0.65). As described in DuraCrete {cite}`DuraCrete1999` or *fib* {cite}`fib2006` the specimens are then stored for 28 days in a carbonation chamber at $T$=+20°C, $RH$=0.65, and the CO$_2$ concentration of 2.0 vol.%. Present European Standard specifies a slightly different procedure (BS EN 12390-12:2020). Any local standard may be used, provided that the method is similar to the one described above.

$R^{-1}_{ACC,0}$ can be described by a normal distribution with mean value estimated using the ACC test result as:

```{math}
:label: eq-env-2.21.18
\mu\left(R^{-1}_{ACC,0}\right) = \left( \frac{x_{c}}{\tau} \right)^{2} \qquad \left[\text{(m}^2\text{/s)/(kg/m}^3\text{)}\right]
```

where $x_c$ is the carbonation depth in [m] measured in the ACC test and $\tau$ = 420 (s/kg/m$^3$)$^{0.5}$ the "time constant". If no test data is available, data from {numref}`table-env-mean-values-of-inverse-carbonation-resistance` can be used for orientation purposes (*fib* {cite}`fib2006`).

Since the relative error in determining $x_c$ decreases with an increase in $x_c$ and the mean value of $R^{-1}_{ACC,0}$ is directly proportional to $x_c$, the coefficient of variation of $R^{-1}_{ACC,0}$ depends on its mean value and can be found as:

```{math}
:label: eq-env-2.21.19
V\left(R^{-1}_{ACC,0}\right) = 0.69\left( \mu\left(R^{-1}_{ACC,0}\right) \times 10^{11} \right)^{-0.22}
```

```{table} Mean values of $R^{-1}_{ACC,0}$ [10$^{-11}$ (m$^2$/s)/(kg/m$^3$)] that can be found for different types of cement
:name: table-env-mean-values-of-inverse-carbonation-resistance
| Cement type | w/c$_{eqv}$ $^1$ = 0.35 | 0.40 | 0.45 | 0.50 | 0.55 | 0.60 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CEM I 42.5 R | n.d.$^2$ | 3.1 | 5.2 | 6.8 | 9.8 | 13.4 |
| CEM I 42.5 R + FA (k=0.5) | n.d.$^2$ | 0.3 | 1.9 | 2.4 | 6.5 | 8.3 |
| CEM I 42.5 R + SF (k=2.0) | 3.5 | 5.5 | n.d.$^2$ | n.d.$^2$ | 16.5 | n.d.$^2$ |
| CEM III/B 42.5 | n.d.$^2$ | 8.3 | 16.9 | 26.6 | 44.3 | 80.0 |
```

$^1$ equivalent water-cement ratio, considering fly ash (FA) or silica fume (SF) with the respective efficiency factors (k-values). The considered contents were: FA – 22% of weight of cement (22 wt% cement), SF – 5 wt% cement.

$^2$ n.d. – data on $R^{-1}_{ACC,0}$ for these cement types is not available.

Note (5): The thickness of the concrete cover $c$ can be described by a lognormal distribution with mean equal to its nominal value and standard deviation of: 8 – 10 mm – without particular execution requirements, and 6 mm – with additional execution requirements.

#### Simplified model

The above model {eq}`eq-env-2.21.11` is often written in simplified form in the following way:

```{math}
:label: eq-env-2.21.20
x_{c}(t) = W(t)\, k\, \sqrt{t}
```

where $k$ = a factor reflecting aspects like the execution, basic resistance of the chosen concrete mix (like w/c-ratio, cement type, additions) under reference conditions and the influence of the basic environmental conditions (like mean relative humidity and the CO$_2$ concentration) against ingress of carbonation. $W(t)$ is estimated using {eq}`eq-env-2.21.16`.

This formulation may be convenient when assessing existing structures on the basis of site measurements. $k$ will then be represented by its average value over the life of the structure until the time of the inspection. The standard deviation of $k$ might also be found from the measurements.

### Chloride induced corrosion

The penetration of chloride ions into concrete is a complex process mainly involving two transport mechanisms – ion diffusion and absorption. It depends on many factors including the properties of concrete (i.e., its composition, porosity and microstructure), the degree of concrete pore saturation, and the exposure conditions at the concrete surface sometimes referred to as "microclimate" (i.e., the surface chloride content, temperature, and humidity). A number of these factors are inter-, time-, spatial-, and temperature-dependent. Since only free chloride ions move inwards, their penetration depends on the binding capacity of concrete and on the achieved free chloride concentration itself, which is obviously time dependent as well.

The limit state function (LSF) is expressed as the difference between the critical (or threshold) chloride concentration and the chloride concentration at the rebar surface level at time $t$ of the design working life

```{math}
:label: eq-env-2.21.21
g(\mathbf{X},t) = C_{crit} - C(c,t)
```

where

* $C_{crit}$ is the critical chloride content to achieve depassivation of the reinforcement,
* $C(c,t)$ is the chloride content at the depth $c$ and time $t$,
* $c$ is the concrete cover,
* $t$ is the time period under consideration.

The limit state may also be formulated in the time domain like in {eq}`eq-env-2.21.4b`.

#### Chloride ingress model

The chloride ingress is treated as a pure diffusion process described by Fick's 2$^{nd}$ law of diffusion

```{math}
:label: eq-env-2.21.22
\frac{\partial C}{\partial t} = D\frac{\partial^{2}C}{\partial x^{2}}
```

where $C$ is the total concentration of chloride ions at distance $x$ from the surface after the time $t$ of exposure to chlorides and $D$ the chloride diffusion coefficient. To complete the problem formulation boundary and initial conditions need to be defined

```{math}
:label: eq-env-2.21.23
\begin{aligned}
C\left( \Delta x, t>0 \right) &= C_{s,\Delta x}\left( t \right)\\
C\left( x > \Delta x, t \right) &= C_{i}\left( x \right)
\end{aligned}
```

where $\Delta x$ is the depth of the convection zone (i.e., the surface concrete layer in which chloride penetration is mainly governed by capillary absorption (convection) and Fick's 2$^{nd}$ law is inapplicable), $C_{s,\Delta x}(t)$ the chloride concentration at depth $\Delta x$, and $C_i(x)$ the initial chloride concentration.

Generally, both the chloride diffusion coefficient and the surface chloride concentration may change with time. In the present model the time dependency of $C_s$ is not taken into account. The time-dependence of the chloride diffusion coefficient is described in the form suggested initially by Maage et al. {cite}`Maage1996` and later modified to make it mathematically correct.

```{math}
:label: eq-env-2.21.24
D_{a}\left( t \right) = D_{a,ref}\left( \frac{t_{ref}}{t} \right)^{m}
```

where $D_a$ denotes the achieved (or apparent) diffusion coefficient, $D_{a,ref}$ its value at the reference time $t_{ref}$, and $m$ the age factor. It is important to stress that according to its definition the achieved diffusion coefficient remains constant within a time period $t$ and changes only when the duration of the time period changes. Therefore, $D_a$ does not represent a physical property of concrete at a particular moment in time, but rather characterises an average diffusivity over the time period $t$.

Assuming that the surface chloride concentration remains constant with time and the time-dependence of the diffusion is described by {eq}`eq-env-2.21.24`, the solution of {eq}`eq-env-2.21.22` can be expressed as

```{math}
:label: eq-env-2.21.25
C\left( x,t \right) = C_{i} + \left( C_{s,\Delta x} - C_{i} \right)\operatorname{erfc}\left( \frac{x - \Delta x}{2\sqrt{D_{a}\left( t \right)}} \right)
```

where $D_a(t)$ the apparent diffusion coefficient, which apart from time depends also on temperature (see below) and erfc(.) the error function complement. To find $C(c,t)$ in {eq}`eq-env-2.21.21` take $x = c$ in {eq}`eq-env-2.21.25`.

It should be noted that in accordance with the adopted definition of the diffusion coefficient, {eq}`eq-env-2.21.24`, the solution, {eq}`eq-env-2.21.25`, is valid only at a single point in time, for which $D_a$ is estimated. Strictly from a mathematical point of view, this cannot be correct. However, if we assume that {eq}`eq-env-2.21.24` describes an instantaneous value of the diffusion coefficient, i.e., the diffusion coefficient changes constantly within a time period $t$, then the solution of {eq}`eq-env-2.21.22` will differ from {eq}`eq-env-2.21.25` only by the multiplier $1/(1-m)$ appearing under the square root. This means that $D_{a,ref}$ in {eq}`eq-env-2.21.24` merely replaces a reference value for the instantaneous diffusion coefficient times $1/(1-m)$. $D_{a,ref}$ can be estimated as

```{math}
:label: eq-env-2.21.26
D_{a,ref} = \frac{1}{1 - m} \cdot k_{T} \cdot D_{ref,0}
```

where $D_{ref,0}$ is the reference value determined in a chloride test at a reference short time (28 days for instance). $k_T$ is the temperature parameter which can be calculated from Arrhenius equation

```{math}
:label: eq-env-2.21.27
k_{T} = \exp\left\lbrack b_{T}\left( \frac{1}{T_{ref}} - \frac{1}{T} \right) \right\rbrack
```

where $b_T$ is the regression parameter, $T_{ref}$ the reference temperature (=293 K), and $T$ the ambient temperature.

#### Random variables for chloride ingress model

{numref}`table-env-chloride-ingress-input-parameters` gives an overview of the various probabilistic models.

```{table} Probabilistic models of input parameters for the chloride ingress model
:name: table-env-chloride-ingress-input-parameters
| $X$ | Designation | unit | mean | scatter |
| :--- | :--- | :--- | :--- | :--- |
| $D_{ref}$ | Chloride diffusion coefficient | 10$^{-12}$ (m$^2$/s) | Note (1) | |
| $m$ | Age factor | - | Note (2) | |
| $b_T$ | Regression parameter (in K) | K | 4800 (Note (3)) | $V$=0.146 |
| $\Delta x$ | Depth of absorption zone | mm | 9 (Note (4)) | $V$=0.6 |
| $C_{s,\Delta x}$ | Chloride concentration at depth $\Delta x$ | % | Note (5) | |
| $C_{crit}$ | Threshold chloride concentration | | See section on critical chloride content | |
```

Note (1): The chloride diffusion coefficient $D_{ref,0}$ represents the rate of chloride penetration. As mentioned above a mean value of $D_{ref,0}$ should be determined by a test. If no test data is available, the following data ({numref}`table-env-mean-values-of-chloride-diffusion-coefficient`) can be used for orientation purposes (*fib* {cite}`fib2006`). The table presents data obtained by the Rapid Chloride Migration (RCM) test carried out at 28 days, i.e. $t_{ref}$ = 28 days, and therefore denoted as $D_{RCM,0}$. $D_{RCM,0}$ can be treated as normally distributed random variable with $V$=0.2.

```{table} Mean values of $D_{RCM,0}$ [10$^{-12}$ (m$^2$/s)] for different types of cement
:name: table-env-mean-values-of-chloride-diffusion-coefficient
| Cement type | w/c$_{eqv}$ $^1$ = 0.35 | 0.40 | 0.45 | 0.50 | 0.55 | 0.60 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CEM I 42.5 R | n.d.$^2$ | 8.9 | 10.0 | 15.8 | 19.7 | 25.0 |
| CEM I 42.5 R + FA (k=0.5) | n.d.$^2$ | 5.6 | 6.9 | 9.0 | 10.9 | 14.9 |
| CEM I 42.5 R + SF (k=2.0) | 4.4 | 4.8 | n.d.$^2$ | n.d.$^2$ | 5.3 | n.d.$^2$ |
| CEM III/B 42.5 | n.d.$^2$ | 1.4 | 1.9 | 2.8 | 3.0 | 3.4 |
```

$^1$ equivalent water-cement ratio, considering fly ash (FA) or silica fume (SF) with the respective efficiency factors (k-values). The considered contents were: FA – 22% of weight of cement (22 wt% cement), SF – 5 wt% cement.

$^2$ n.d. – data on $D_{ref,0}$ for these cement types are not available.

Note (2): The age factor $m$ depends on the type of cement and exposure conditions. It can be presented by a Beta distribution on the interval [0, 1]. It can be tested estimated by extending the diffusion test to longer ages of contact with the salt solution (it can be to 6 or 12 months) and then calculating the aging factor from {eq}`eq-env-2.21.24` or {eq}`eq-env-2.21.26`.

Pure Portland cements may present aging factors from very low values near 0.1 to around 0.3 depending on their calcium aluminate content. The concretes with mineral additions exhibit much higher values due to the slower reaction of the additions with the Ca(OH)$_2$. The range of values can be from 0.3 to 0.8.

The mean and COV of $m$ for RC structures in the splash, tidal, and submerge zones can be adopted in accordance with {numref}`table-env-mean-and-cov-of-the-age-factor`. Note that the values of $m$ in {numref}`table-env-mean-and-cov-of-the-age-factor` were derived by fitting {eq}`eq-env-2.21.24`, with $D_{a,ref}$ replaced by $D_{RCM,0}$ obtained from the RCM test, to a number of values of $D_a$ estimated at different points in time. By this reason the multiplier $1/(1-m)$ should be omitted in {eq}`eq-env-2.21.26` when $D_{a,ref}$ is calculated using the values of $D_{RCM,0}$ from {numref}`table-env-mean-values-of-chloride-diffusion-coefficient`.

```{table} Mean and COV of the age factor $m$
:name: table-env-mean-and-cov-of-the-age-factor
| Type of cement | Mean | COV |
| :--- | :--- | :--- |
| Ordinary Portland cement (OPC) <br> CEM I; 0.40≤w/c≤0.60 | 0.30 | 0.40 |
| OPC with fly ash (FA) <br> CEM I + FA; FA≥20wt% cement; 0.40≤w/c$_{eqv}$≤0.62 | 0.60 | 0.25 |
| Blast furnace slag cement (GBFS) <br> CEM III/B; 0.40≤w/c≤0.60 | 0.45 | 0.44 |
```

Note (3): The regression parameter $b_T$ can be described by a normal distribution.

Note (4): In DuraCrete {cite}`DuraCrete1999`, it has been proposed that for the splash zone, $\Delta x$ can be described by a Beta distribution on [0, 50] mm with mean of 9 mm and COV=0.60 for 50 years.

For the submerged zone and the atmospheric zone (spray conditions, e.g., 1.5 m above the road surface), $\Delta x$ can be treated as a deterministic parameter equal to 0.

For the tidal zone, statistical quantification still needs to be conducted.

Note (5): When the source of chlorides is de-icing salt, $C_{s,\Delta x}$ is described in *fib* Bulletin 34 {cite}`fib2006` by a normal distribution with mean given by the following equation

```{math}
:label: eq-env-2.21.28
\mu_{C_{s,\Delta x}} = 0.465 - 0.051\ln\left( d_{h} + 1 \right) - \left\lbrack 0.00065\left( d_{h} + 1 \right)^{- 0.187} \right\rbrack d_{v} \qquad [\text{wt.-\%/concrete}]
```

where $d_h$ is the horizontal distance from the roadside [cm], $d_v$ the height (vertical distance) above the road surface [cm], and COV=0.75. {eq}`eq-env-2.21.28` is based on data from 5–40-year-old concrete structures made of OPC (CEM I) concrete with 0.45≤w/c≤0.60 and located in urban and rural areas of Germany.

When the source of chlorides is sea water, the ambient chloride concentration depends on the chloride concentration of sea water, distance/height from/above the sea (e.g., splash zone, on the coast, etc.) and several other factors (e.g., sheltered or unsheltered surface, dominant wind direction, etc.). Thus, for realistic predictions of the probability of corrosion initiation in such cases the use of local data on $C_{s,\Delta x}$ is highly desirable.

In the absence of such data, the mean value of $C_{s,\Delta x}$ can be estimated as

```{math}
:label: eq-env-2.21.29
\mu_{C_{s,\Delta x}} = C_{s,0}\, k_{C,binder}\, k_{C,w/c}\, k_{C,Cl}\, k_{C,ec}
```

where $C_{s,0}$=2.5% (wt.-%/concrete) is the average chloride concentration at depth $\Delta x$ for OPC (CEM I) concrete in the tidal/splash zone (XS3 exposure class) exposed to sea water with typical chloride concentration (i.e., about 19.4 g/l), $k_{C,binder}$ the parameter accounting for the type of binder, $k_{C,w/c}$ the parameter accounting for the water-cement ratio of the concrete, $k_{C,Cl}$ the parameter accounting for the chloride concentration of sea water and $k_{C,ec}$ the parameter accounting for the exposure class.

The following values of the parameters are suggested:

```{math}
k_{C,binder} = \begin{cases}
1.0 & \text{CEM I 42.5 R}\\
1.2 & \text{CEM I 42.5 R + FA, CEM I 42.5 R + SF}\\
1.05 & \text{CEM III/B 42.5}
\end{cases}
```

```{math}
k_{C,w/c} = 2.5\,(w/c)
```

```{math}
k_{C,Cl} = \begin{cases}
0.76 & \text{sea water chloride concentration = 5 g/l}\\
0.88 & \text{10 g/l}\\
1.0 & \text{20 g/l}\\
1.12 & \text{25 g/l}
\end{cases}
```

```{math}
k_{C,ec} = \begin{cases}
0.4 & \text{exposure class XS1 (airborne salt, no direct contact with sea water)}\\
2.0 & \text{exposure class XS2 (permanently submerged)}\\
1.0 & \text{exposure class XS3 (tidal and splash zones)}
\end{cases}
```

$C_{s,\Delta x}$ can be modelled as a truncated at 0 normal random variable with coefficient of variation (COV) depending on the exposure class: 0.30 for XS1, 0.15 for XS2 and 0.25 for XS3.

*Comments*: most of relevant data are available for OPC concrete with w/c around 0.40 in splash/tidal zone (XS3 environment) and sea water with the typical chloride concentration (i.e., 19.4 g/l). According to these data from various independent sources, the average value of the surface chloride concentration is about 2.5% wt.-%/concrete {cite}`Bamforth1997`, {cite}`McCarter2008`, {cite}`Pack2010`. Based on that the value of $C_{s,0}$ has been assigned.

There is some evidence that the surface chloride concentration is slightly higher for concretes with FA, SF and GGBS (e.g., DuraCrete {cite}`DuraCrete2000R9`, Pack et al. {cite}`Pack2010`). In particular, DuraCrete BE95-1347/R9 {cite}`DuraCrete2000R9` suggests a linear relationship between the surface chloride concentration, $C_{s,\Delta x}$, and the water-cement ratio, w/c: $C_{s,\Delta x} = A(w/c)$ and provides values of $A$ for different concretes in different environments (see Table 8.5 in DuraCrete BE95-1347/R9). However, these values look inconsistent and many of them are not supported by data reported in other publications. Based on data from various publications, including DuraCrete BE95-1347/R9, the above values of $k_{C,binder}$ are tentatively suggested.

$k_{C,w/c}$ and $k_{C,Cl}$ have been adopted from Lindvall {cite}`Lindvall2003`.

The above values of $k_{C,ec}$ are mainly based on data from DuraCrete {cite}`DuraCrete2000` and McCarter et al. {cite}`McCarter2008`.

Available data on the coefficient of variation of $C_{s,\Delta x}$ are very inconsistent. For example, the data presented in DuraCrete BE95-1347/R9 suggests that the COV is below 0.20 for different concretes and different environments. Statistical analysis of the data presented in Pack et al. {cite}`Pack2010` yielded $V$=0.14 for OPC concrete and 0.05 for GGBS concrete (XS3 environment). At the same time, according to the data presented by Polder and de Rooij {cite}`PolderDeRooij2005` for OPC and GGBS concretes in XS3 environments values of the COV can be very high (for several structures between 0.3 and 0.4, and in one case even 0.71). It is expected that for permanently submerged structures environmental conditions (XS2) are more uniform so that the COV should be the lowest among the three exposure classes. The conditions are much more variable in tidal/splash zones (XS3) and even more variable in XS1 environments. Taking all these into account and with the intent not to be over conservative, the above values of the COV are suggested.

### Depassivation limit state

In carbonated concrete, depassivation is identified with the arrival of the carbonation front to the external surface of the bars. The LSF is {eq}`eq-env-2.21.4a`.

In the case of chlorides, the depassivation is associated to a critical chloride concentration at the bar surface. The LSF is {eq}`eq-env-2.21.21`.

#### Critical chloride content

The threshold or critical chloride concentration in concrete, $C_{crit}$, in many standards is given as 0.4% by weight of cement. However, this threshold is not a fixed quantity as it is influenced by several factors. Only a few statistical distributions of $C_{crit}$ are available in the literature. Hausmann {cite}`Hausmann1996` expressed it as a function of the Cl$^-$/OH$^-$ ratio and by that reason it is difficult to use.

In DuraCrete {cite}`DuraCrete2000`, the distribution of $C_{crit}$ obtained by Breit and Schießl {cite}`BreitSchiessl1995` in bridges in the UK was used. The distribution is Beta with a mean of 0.6 (by % cement weight) and a standard deviation of 0.15 ($V$=0.25).

A broader analysis was made by Markeset {cite}`Markeset2009` using data from a field study of bridges in Norway, where cores were drilled from concrete sections of the bridges to determine their chloride contamination and values of the chloride content at the rebar level when corrosion was "incipient". The values of the chloride content in the cores with incipient corrosion were treated as the chloride threshold concentration. Statistical analysis of the results yielded a log-normal distribution with a mean value of 0.77 and COV of 0.25 (by % cement weight).

Results very similar to those of Markeset {cite}`Markeset2009` were obtained by Izquierdo et al. {cite}`Izquierdo2004` using data from a laboratory study made on mortar specimens fabricated with different cement types and submitted to potentiostatic tests, in which chlorides were forced to penetrate into concrete by applying a voltage difference.

For submerged or very wet conditions, the only results were reported by Izquierdo et al. {cite}`Izquierdo2004` by analysing data on chloride thresholds for cathodic potentials higher than -200 mV$_{SCE}$. According to these results, $C_{crit}$ can be described by a log-normal distribution with a mean value of 1.53 and a standard deviation of 0.53 (both by % cement weight).

{numref}`table-env-total-chloride-threshold-values` (from *fib* Bulletin 112 {cite}`fibBulletin112`) shows the comparison of the distribution obtained by Breit and Schießl {cite}`BreitSchiessl1995` with that of Izquierdo et al. {cite}`Izquierdo2004` and Markeset {cite}`Markeset2009`.

```{table} Total chloride threshold values and statistical distributions
:name: table-env-total-chloride-threshold-values
| Literature source | | Statistical distribution | Average value <br> % by cement weight | Coefficient of variation (%) |
| :--- | :--- | :--- | :--- | :--- |
| Breit et al. 1995 | | Beta | 0.6 | 25.00 |
| Markeset 2009 | | Log-normal | 0.77 | 32.46 |
| Izquierdo et al. 2004 | > -200 mV (atmospheric) | normal | 0.7 | 28.57 |
| | < -200 mV (submerged) | Log-normal | 1.53 | 34.64 |
```

#### The thickness of the concrete cover

The thickness of the concrete cover $c$ can be described by a lognormal distribution with mean equal to its nominal value and standard deviation of: 8 – 10 mm – without particular execution requirements, and 6 mm – with additional execution requirements.

## Corrosion propagation

### Corrosion propagation process

As described in the section on the depassivation limit state, after depassivation is confirmed by maintaining a high enough corrosion rate, the corrosion process evolves by the formation of iron oxides, named usually "rust" {cite}`PageTreadaway1982`, {cite}`Tuutti1982`. These oxides are a mixture of several oxy-hydroxides with different degree of hydration and when generated, their particles are growing in the pore solution, which in consequence, when it is more and more concentrated in salts presents a consistency of a dense liquid or even a soft gel is formed {cite}`Andrade1993`. The oxides initially accommodate in the steel/concrete interface to further diffuse through the pore network. At the same time, they produce a pressure in the concrete surrounding the bar due to the volume of the oxides is larger than that of the parent steel, because of the incorporation of oxygen and water to the iron {cite}`Molina1993`. The process develops depending on the availability of water at the rebar surface and is continuously evolving depending also on temperature changes in the environment.

The loss of parent steel by the corrosion process means the decrease in bar mass and geometrically, of the bar diameter {cite}`AndradeGonzalez1978`. This decrease in diameter can be uniform or localized as shown in {numref}`fig-uniform-homogeneous-and-localised-corrosion`. The total diameter loss ($\phi_{ini} - \phi_t$) (initial diameter minus the diameter at time $t$) or "corrosion penetration depth", $P_{corr}$, is then {cite}`Andrade1989`:

```{math}
:label: eq-env-2.21.30
P_{corr} = \phi_{ini} - \phi_{t}
```

The mass loss in a certain time is what is named "corrosion rate", $V_{corr}$, and expressed for engineering applications in µm/year. It can be measured by weighing the bar piece before and after the corrosion period, or by measuring the decrease in diameter with a caliper as shown in {numref}`fig-measurement-of-corrosion-penetration-depth-by-a-caliper`. If the bar is corrugated, the result can be local or has to be averaged by measuring in several sections.

```{figure} ../part-02/images/measurement-of-corrosion-penetration-depth-by-a-caliper.png
:name: fig-measurement-of-corrosion-penetration-depth-by-a-caliper
:width: 600px

Measurement of corrosion penetration depth by a caliper {cite}`AndradeGonzalez1978`.
```

The bar mass loss can be also recorded continuously by the Polarization Resistance or "Linear Polarization" method that is an electrochemical technique. The corrosion current $I_{corr}$ in µA/cm$^2$ is the ratio between a constant (named $B$) whose value is of 26 mV for the concrete reinforcements and the polarization resistance, $R_p$, in kΩ·cm$^2$ {cite}`AndradeGonzalez1978`.

```{math}
:label: eq-env-2.21.31
I_{corr} = 26 / R_{p}
```

This value of $I_{corr}$ is named "instantaneous corrosion current" or simply "corrosion current" and is expressed in µA/cm$^2$. {numref}`fig-recording-of-corrosion-current-with-time` (left) shows the evolution of the instantaneous $I_{corr}$ with time of a specimen where chlorides were added in the mixing water.

```{figure} ../part-02/images/recording-of-corrosion-current-with-time.png
:name: fig-recording-of-corrosion-current-with-time
:width: 600px

Left: The recording of corrosion current with time in a specimen. Right: The integration of the area $I_{corr}$-time gives the total coulombs that through Faraday's law can be converted into mass loss {cite}`AndradeGonzalez1978`.
```

The integration with time of this instantaneous corrosion current ({numref}`fig-recording-of-corrosion-current-with-time`, right) gives the amount of coulombs (Coulomb = current by time) that through Faraday's law enables the calculation of the total mass loss on that period. The equivalence for the steel between the corrosion rate ($V_{corr}$) and the corrosion current ($I_{corr}$) through Faraday's law is given by {eq}`eq-env-2.21.32` {cite}`Andrade1989`:

```{math}
:label: eq-env-2.21.32
V_{corr} = 11.6\, I_{corr}
```

with $V$ in [µm/year] and $I$ in [µA/cm$^2$].

If the plot is made by the integration at each time step, the result is shown in the same {numref}`fig-recording-of-corrosion-current-with-time` (right) where the $P_{corr}$ (mass loss at each age) is depicted in the axis at the right.

#### Corrosion in prestressed members

In prestressed or postensioned members, corrosion can develop and progress by the same (electrochemical) mechanism as the previously described, but in addition to it, the reinforcement may suffer a process which aims into sudden brittle failures: the Stress Corrosion Cracking (SCC) {cite}`Valiente1998`. This is a set of mechanisms that its development requires the simultaneous presence of a susceptible material (such as high yield strength steels), a corrosive media, and a certain level of mechanical tension.

The process starts from a defect at the bar surface, that can be of mechanical origin or caused by localized corrosion {cite}`Elices2012`. Once the initial crack is nucleated, it may progress to a certain critical depth at which, the stress concentration in its crack bottom may induce the crack to progress until the brittle fracture of the steel. Additionally, the acidification caused by the corrosion generates hydrogen ions that are reduced in the cathodic zones to produce hydrogen atoms that may diffuse inside the steel and generate its embrittlement. This hydrogen inside the metal enhances the effect of external tension, and an unexpected and brittle failure of the wires might occur.

This SCC mechanism will not be treated in the present chapter because at present there is no method to anticipate or predict when the brittle ruptures may occur.

#### Time evolution of the corrosion process (electrochemical)

The corrosion rate may not be constant because it depends on the:

a) Porous microstructure of the concrete and its evolution with time

b) Its degree of saturation

c) The temperature

d) Availability of oxygen

e) The amount of oxides (rust) generated by the corrosion which may be a barrier for further progress of the corrosion.

These parameters evolve with the cement hydration and may vary following the environmental conditions. This is what happens when the concrete element is submitted to the action of the atmosphere. An example of evolution of the corrosion current $I_{corr}$ with time is given in {numref}`fig-corrosion-current-and-penetration-of-a-beam-exposed-outdoors-in-madrid` (left) {cite}`GonzalezAndrade1982`. It corresponds to a beam contaminated with chlorides exposed outdoors to the weather variations (Madrid-Spain exposure of continental time with around 450 l/m$^2$ of annual rainfall and around 15 ºC of averaged temperature and 65% of RH) {cite}`Andrade2002`, {cite}`Andrade2012`.

```{figure} ../part-02/images/corrosion-current-and-penetration-of-a-beam-exposed-outdoors-in-madrid.png
:name: fig-corrosion-current-and-penetration-of-a-beam-exposed-outdoors-in-madrid
:width: 640px

Left: Corrosion current values in the case of a beam with 3% of admixed chlorides exposed outdoors in Madrid weather. Right: Corrosion penetration in the case of a beam with 3% of admixed chlorides exposed outdoors in Madrid weather.
```

The starting of the measurements of corrosion was almost 4 years later than the fabrication of the beam, that is, no corrosion measurements were made during this initial period. The evolution from the 4 years indicates dramatic variations of the corrosion current, because of the rain periods and the seasonal changes. The trend however attenuates after around 2 years attributed to: a) the progressive hydration of the cement, or b) the appearance of cracks in the cover that enable longer drying periods in the bar facing the crack and then, with shorter wetness time or c) to the formation of the oxides (rust) that difficult the further progress of the corrosion.

In {numref}`fig-corrosion-current-and-penetration-of-a-beam-exposed-outdoors-in-madrid` (right) is shown the corrosion penetration depth ($P_{corr}$) of the left plot. This plot, as giving the corrosion degree during the time, enables a better appraisal of the phenomenon. It can be identified that the corrosion current is constant but with two stages (slopes of the curve). One first until around 2 years with a slope (corrosion current) of around 2 µA/cm$^2$ and a second period with a mean corrosion rate of around 0.736 µA/cm$^2$.

#### Ranges of instantaneous corrosion rates

In the laboratory and in the real structures, the corrosion rate measured are of similar level when the concrete is carbonated or contains chlorides or is free of any contamination. Thus, when the steel bar is passive or the corrosion is negligible for life of 100 years, the corrosion rate is below 0.1 µA/cm$^2$ and the maximum values measured have been of around 100-200 µA/cm$^2$. In between those values the ranges of corrosion that have ranked are given in {numref}`table-env-ranges-of-corrosion-rate` {cite}`Andrade1989`, {cite}`CONTECVET2001`.

```{table} Ranges of corrosion rate for laboratory and real structures
:name: table-env-ranges-of-corrosion-rate
| Corrosion rate | µA/cm$^2$ | µm/year | Reinforcing bar condition |
| :--- | :--- | :--- | :--- |
| Negligible | < 0.1 | < 1 | Passive state |
| Low | 0.1 – 0.5 | 1 – 5 | Depassivated in concrete with moderate humidity |
| Moderate | 0.5 – 1 | 5 – 10 | Active corrosion in concrete with medium level humidity |
| High | 1 – 10 | 10 – 100 | Corrosion in wet concrete |
| Very high | > 10 | > 100 | Corrosion in wet and cracked concrete |
```

### Corrosion propagation model

A corrosion propagation model is a mathematical expression of the processes described above. Only the corrosion propagation by electrochemical mechanisms will be here addressed, because for the cases suffering stress corrosion cracking still there is not a model.

Tuutti {cite}`Tuutti1982` proposed for reinforcement corrosion a model in two stages: corrosion initiation ({numref}`fig-possible-trends-of-the-corrosion-rate-over-time`) and corrosion propagation. The (mean) corrosion propagation period was expressed by Andrade et al. ({cite}`AndradeGonzalez1978`, {cite}`Andrade1989`, {cite}`Andrade2012`) in the following manner:

```{math}
:label: eq-env-2.21.33
t_{p} = P_{corr} / V_{corr,m}
```

where the propagation period ($t_p$ in years) is equal to the corrosion penetration $P_{corr}$ (or decrease in diameter, $\phi_0 - \phi_t$ in µm) divided by the annual mean corrosion rate ($V_{corr,m}$ in µm/year). This model assumes a constant corrosion rate as indicated by Tuutti {cite}`Tuutti1982`. The model was incorporated into the Contecvet Manual {cite}`CONTECVET2001`, also in the reports of the DuraCrete project {cite}`DuraCrete1998` and in the Annexes of *fib* Bulletin 34 {cite}`fib2006`. Recently it has been detailed in Annex A of the *fib* Bulletin 119 {cite}`fibBulletin119`.

In the case of pitting attack, as the corrosion penetration is locally deeper, a pitting factor $\alpha$ is introduced in the equation resulting:

```{math}
:label: eq-env-2.21.34
t_{p} = P_{corr} / (V_{corr,m}\, \alpha)
```

where $\alpha$ is the pitting factor [-] indicating the maximum pit depth {cite}`Gonzalez1995`. In the case of chlorides, the mean value found in the DuraCrete project {cite}`DuraCrete1998` was around of $\alpha$=10 times.

A modification of this model has been incorporated into the *fib* MC2020 {cite}`fibMC2020` and the Bulletin 112 {cite}`fibBulletin112` because as described before, the corrosion rate may show more than one mean constant corrosion rate. That situation is represented in {numref}`fig-linear-and-bilinear-corrosion-propagation-models`. In the figure the corrosion rate (slope of the graph $P_{corr}$-time) is represented as always constant (line A), or by a change in the slope at a certain time showing an acceleration (line C) that indicates the case when the corrosion rate increases steadily (for example if the cover cracks and the reinforcement falls in direct contact to saline water) or shows an attenuation of the corrosion in time (line B), typical of when cover cracking occurs outdoors in dry atmosphere where the time of wetness is shorter in the cracked zones than where the bar is fully covered by the concrete (more common in carbonated specimens where the oxides additionally may have a semi-protective character).

Considering these "two consecutive periods" of different corrosion rates (bi-linear progress of the corrosion penetration) the expression {eq}`eq-env-2.21.33` of the propagation period can be substituted by the following one:

```{math}
:label: eq-env-2.21.35
t_{p} = t_{p1} + t_{p2} = \frac{P_{corr,1}}{V_{corr,m1}} + \frac{P_{corr,2}}{V_{corr,m2}}
```

* $P_{corr,1}$ penetration of corrosion attack in period 1 (commonly until cover cracking) [µm]
* $P_{corr,2}$ penetration of corrosion attack in period 2 (for example after cover cracking) [µm]
* $V_{corr,m1}$ mean corrosion rate in period 1 [µm/year]
* $V_{corr,m2}$ mean corrosion rate in period 2 [µm/year]

```{figure} ../part-02/images/linear-and-bilinear-corrosion-propagation-models.png
:name: fig-linear-and-bilinear-corrosion-propagation-models
:width: 400px

Linear (line A) and two-step (bi-linear) corrosion propagation models (line B with a lowering of the corrosion rate and line C with an increase of it with time).
```

In {numref}`fig-consequences-of-corrosion-for-rc-structures` it was indicated that the diameter loss should be further associated to the structural consequences that corrosion induces. This verification of the structural SLS and ULS in corroded elements is out of the scope of the present chapter.

### Random variables in the corrosion propagation model

The variables in the corrosion propagation model (expressions {eq}`eq-env-2.21.33` and {eq}`eq-env-2.21.34` or {eq}`eq-env-2.21.35`) are the corrosion rate $V_{corr}$ and the pitting factor $\alpha$.

The values of $V_{corr}$ can be obtained from:

* An expression in function of its constitutive parameters (factors affecting the rate)
* Average values in function of the exposure classes obtained from experience

#### Model of the corrosion rate and its uncertainty

The model proposed in the DuraCrete project {cite}`DuraCrete1998` was of parametric type. At present that model can be updated in the following manner:

```{math}
:label: eq-env-2.21.36
V_{corr} = \frac{K_{corr}}{\rho} \cdot F_{Cl} \cdot F_{rust} \cdot F_{O2} \cdot F_{RH,T}
```

where:

* $V_{corr}$ = corrosion rate [µm/year]
* $K_{corr}$ = a constant [(μm/year)·kΩ·cm]
* $\rho$ = resistivity [kΩ·cm]
* $F_{Cl}$ = chloride corrosion rate factor [-]
* $F_{rust}$ = galvanic effect factor [-]
* $F_{O2}$ = oxygen availability factor [-]
* $F_{RH,T}$ = climatic factor [-]

From these constitutive parameters, the only one that has been enough quantified is the resistivity because it is a relatively easy to be measured, in addition to be the most influencing of all of them. The $F_{Cl}$ is being studied, but not fully formulated yet.

The model is then summarized as:

```{math}
:label: eq-env-2.21.37
V_{corr} = \frac{K_{corr}}{\rho}
```

and

```{math}
V_{pit} = V_{corr} \cdot \alpha
```

* $V_{pit}$ maximum pit penetration [µm]
* $\alpha$ pitting factor $P_{max}/P_{corr}$ [-]

In this model of expression {eq}`eq-env-2.21.37` the variables whose uncertainty is necessary to be calculated are: $V_{corr}$, $K_{\rho}$ and $\alpha$. This characterization was made in the DuraCrete project {cite}`DuraCrete1998` using the values of a database in Geocisa {cite}`Rodriguez1994`.

#### Statistical characterization of $K_{corr}$ and $\alpha$

The results obtained are given in {numref}`table-env-statistical-characterization-of-kcorr-and-alpha`.

```{table} Statistical characterization of the constant $K_{corr}$ and the pitting factor $\alpha$
:name: table-env-statistical-characterization-of-kcorr-and-alpha
| $X$ | designation | unit | mean | CoV (%) | Distribution |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $K_{corr}$ | Constant | (μm/year)·kΩ·cm | 26 | 159 | LN |
| $\alpha$ | Pitting factor | - | 9.28 | 44 | N |
```

#### Statistical characterization of $V_{corr,m}$

The statistical distribution of corrosion rate values obtained from data in real structures {cite}`AndradeIzquierdo2022` of carbonated and chloride contaminated concretes is shown in {numref}`fig-statistical-distributions-of-corrosion-rate-values-in-corroding-structures`. The representation indicates that the statistical distribution of corrosion rate values are similar in carbonated or chloride contaminated concrete resulting in a log-normal distribution whose characteristics are given in {numref}`table-env-statistical-characterization-of-mean-corrosion-rate`.

```{figure} ../part-02/images/statistical-distributions-of-corrosion-rate-values-in-corroding-structures.png
:name: fig-statistical-distributions-of-corrosion-rate-values-in-corroding-structures
:width: 560px

Statistical distributions of corrosion rate values in corroding structures, either carbonated or chloride contaminated {cite}`AndradeIzquierdo2022`.
```

```{table} Statistical characterization of the mean corrosion rate values in real structures (Andrade and Izquierdo 2022)
:name: table-env-statistical-characterization-of-mean-corrosion-rate
| $X$ | designation | unit | mean | CoV (%) | Distribution |
| :--- | :--- | :--- | :--- | :--- | :--- |
| carbonation | $V_{corr,m}$ | µm/year | 6.1 | 177 | LN |
| chlorides | $V_{corr,m}$ | µm/year | 10.3 | 221 | LN |
| All structures | $V_{corr,m}$ | µm/year | 7.3 | 226 | LN |
```

For the interpretation of the representation, it has to be taken into account that:

* The values were collected in the inspections made to assess the condition of the structure without any previous classification. Then, the cases do not represent all the population of structures, but only a part with visual signs of corrosion.
* Measurements were made in each structure on the same or consecutive days, that is, with almost the same external environmental conditions.
* In each structure, the selection of measurement zones was made by choosing only one zone where corrosion is likely not yet produced and several zones where the corrosion was evident. Then, the number of places measured with no corrosion are smaller than those corroding.
* Because the selection in each structure was made to have corroding and non-corroding zones, the values in each structure represent a kind of spatial variation of the corrosion rate not only of the material, but also of different exposure classes (humidity and contamination).

In {numref}`fig-statistical-distributions-of-corrosion-rate-values-in-corroding-structures` it is underlined in vertical with a dashed line the limit of 0.1 µA/cm$^2$ which could be taken as the frontier between active and negligible corrosion. This values for this limit indicate that around 20% of the zones measured in the corroding structures visited have shown negligible corrosion. Also can be deduced that either the mean value and the CoV are higher in the case of structures contaminated by chlorides. The coefficient of variation is high because in the same structure may coexist non-corroding zones and other with high corrosion rates. The probability of finding values of corrosion rates above 10 µA/cm$^2$ is lower than the 0.35% and values above 5 µA/cm$^2$ smaller than the 1.5%.

#### Values of $V_{corr}$ in function of the exposure classes in EN 1992-1-1

A set of values were proposed in the Contecvet Manual {cite}`CONTECVET2001`, for each exposure class indicated in the standard EN 1992-1-1. Very similar values were adopted by the DuraCrete project {cite}`DuraCrete1998` that additionally statistically characterized them. The values also are mentioned in the Annex A of the *fib* Bulletin 119 {cite}`fibBulletin119` and given in the *fib* Bulletin 112 {cite}`fibBulletin112`. They were also the basis for calculating the cover depths of the chapter 6 of EN 1992-1-1 and explained in its Background Document {cite}`AndradeIzquierdo2023`. They are as well in the Annex 12 on Service life calculation of the Spanish Code from 2008.

The values are based in a database {cite}`Rodriguez1993` from laboratory specimens held in chambers with controlled RH and Temperature and, on the other hand, on data recorded on real outdoors structures. These updated values used for the calibration of the cover depths included in the EN 1992-1-1 {cite}`EN1992_1_1_2023` are given in {numref}`table-env-mean-corrosion-rate-values-for-exposure-classes`.

```{table} (Mean) corrosion rate values for the different EN 206 and EN 1992-1-1 exposure classes
:name: table-env-mean-corrosion-rate-values-for-exposure-classes
| Exposure class | | Mean $V_{corr}$ (µm/year) | CoV (%) | Type of distribution |
| :--- | :--- | :--- | :--- | :--- |
| 0 | No risk of corrosion, very dry | 0 | - | Deterministic |
| XC1 | Dry or permanent wet | 1 | 65 | LN |
| XC2 | Wet rarely dry | 4 | 65 | LN |
| XC3 | Moderate humidity | 2 | 65 | LN |
| XC4 | Cyclic wet dry | 5 | 90 | LN |
| XD1 | Moderate humidity | 4 | 60 | LN |
| XD2 | Wet, rarely dry | 30 | 90 | LN |
| XD3 | Cyclic, wet and dry | 30 | 60 | LN |
| XS1 | Airborne salt conditions | 30 | 60 | LN |
| XS2 | Submerged | 10 | 60 | LN |
| XS3 | Tidal, splash and spray zones | 70 | 90 | LN |
```

### Corrosion limit states

The $P_{corr}$ limiting value of a structure can be directly associated to one of the following Corrosion Limit States (see Condition/Deterioration Limit States in the introduction) (ISO 2394 {cite}`ISO2394_1998`, ISO 13823 {cite}`ISO13823_2008`) represented in {numref}`fig-limit-states-associated-to-reinforcement-corrosion`. The need to define corrosion limit states was introduced by the DuraCrete project {cite}`DuraCrete1998`:

1. *Depassivation* of reinforcing steel and onset of corrosion
2. *Initiation of deterioration*, e.g., development of a micro crack (< 0.05 mm wide) parallel to the bar on the concrete surface; corrosion penetration exceeds 50 μm (homogeneous corrosion) or 500 μm (pitting corrosion)
3. *Cracking* when the limit is a crack width
4. *Spalling* when the limit is the detachment of the concrete cover
5. *Bond* loss, when the loss in diameter is related to the loss in bond

```{figure} ../part-02/images/limit-states-associated-to-reinforcement-corrosion.png
:name: fig-limit-states-associated-to-reinforcement-corrosion
:width: 480px

Limit states associated to reinforcement corrosion (adapted from DuraCrete {cite}`DuraCrete1998`).
```

#### Condition (corrosion) limit state, CLS

This is a new limit state implicitly incorporated into the calculation of the cover depths of chapter 6 in the EN 1992-1-1 {cite}`EN1992_1_1_2023` and introduced in MC2020 {cite}`fibMC2020`. It is based in that since the depassivation moment is very difficult to be on site detected, unless monitoring is installed, the CLS considers that the limit state is when a certain corrosion has been produced that is not inducing a crack width higher than 0.1 mm in the cover depth. This propagation time is incorporated into the design service life. It has been associated to a $P_{corr}$ of 50 µm in the case of uniform corrosion (carbonation) and of 500 µm for pitting attack (chlorides) ({numref}`fig-concept-of-condition-corrosion-limit-state`).

```{figure} ../part-02/images/concept-of-condition-corrosion-limit-state.png
:name: fig-concept-of-condition-corrosion-limit-state
:width: 640px

Concept of Condition (Corrosion) Limit State introduced implicitly in EN 1992-1-1 {cite}`EN1992_1_1_2023` and described in MC2020 {cite}`fibMC2020`.
```

Then, assuming a design service life value, the limit state function (LSF) may be formulated in the time domain as:

```{math}
:label: eq-env-2.21.38
g(\mathbf{X}) = t_{SL} - t_{ini} - t_{prop}
```

Then the requirement with respect to this limit state is given by:

```{math}
:label: eq-env-2.21.39
P\{F_{cls}\} = P\{t_{SL} - t_{ini} - t_{prop} < 0\} < P_{target,cls}
```

where:

* $P\{\}$ is probability of reaching depassivation plus a propagation to attain a specified corrosion penetration value
* $t_{SL}$ is design service life [years],
* $t_{ini}$ is initiation period [years],
* $t_{prop}$ is propagation period [years]
* $P_{target,cls}$ is target failure probability for the limit state, depending on the direct or later consequences, including envisaged inspection options

As limit for the start of cracking usually values of $P_{corr}$ of 50 µm in the case of uniform corrosion (carbonation) and of 500 µm for pitting attack (chlorides) are used as stated before.

#### Corrosion induced cracking or spalling limit states

The limit state for corrosion-induced cracking will depend on the $P_{corr}$ associated to each of the limiting value associated to these damages. Generically it can be expressed in terms of the cracking stage. The same format as in {eq}`eq-env-2.21.38` can be used. The difference is that $P_{corr}$ now corresponds to the attainment of a specified undesired crack width or spalling situation.

### Example of calculation of the propagation periods of the corrosion limit state

For the calculation of the design value of the propagation period associated to the Corrosion Limit State ($P_{corr}$ = 50 µm for uniform corrosion or $P_{pit}$ = 500 µm for pitting) we may use the expressions in prEN 1990-2:2026 {cite}`EN1990_2_2026`.

For CoV < 20-25% and N distribution:

```{math}
:label: eq-env-2.21.42
V_{corr,d} = V_{corr,m} \cdot e^{-\alpha\beta \cdot CV}
```

For CoV > 20-25% and LN distribution:

```{math}
:label: eq-env-2.21.43
V_{corr,d} = V_{corr,m} \cdot e^{\left( -\frac{1}{2}\ln\left(1 + CoV_{y}^{2}\right) - \alpha_{y}\,\beta_{y}\sqrt{\ln\left(1 + CoV_{y}^{2}\right)} \right)}
```

where:

* $\alpha$ FORM sensitivity factor for the $V_{corr}$
* $\beta$ the target reliability index
* CoV the coefficient of variation

{numref}`table-env-sensitivity-factors-for-the-corrosion-limit-state` shows the sensitivity factors of {eq}`eq-env-2.21.42` and {eq}`eq-env-2.21.43` calculated for the limit state of Corrosion (CLS) by Izquierdo {cite}`Izquierdo2003`.

```{table} Sensitivity factors for the Corrosion Limit State (Izquierdo 2003)
:name: table-env-sensitivity-factors-for-the-corrosion-limit-state
| Exposures | Sensitivity factor |
| :--- | :--- |
| XC1, XC2, XC3, XC4, XS1, XD1 | -0.7 |
| XS2, XS3, XD2, XD3 | -0.3 |
```

Adopting this last possibility (Tanner et al. {cite}`Tanner2011`, Lara et al. {cite}`Lara2021`) {numref}`table-env-calculated-propagation-periods` shows the results of the propagation periods calculated through expression {eq}`eq-env-2.21.42` and {eq}`eq-env-2.21.43` for variables with CV > 20% as is the case of the corrosion rate. The target value $\beta$ = 1.5 is often used in the case of a not very aggressive environment.

```{table} Calculated propagation periods until $P_{corr}$ = 50 µm or $P_{pit}$ = 500 µm for a $\beta$ = 1.5 assuming the corrosion rates of the previous table (CONTECVET 2001, DuraCrete 1998), using the two expressions above
:name: table-env-calculated-propagation-periods
| Exposure and $P_{corr}$ limit | $\alpha$ | $\beta$ | CV | $V_{corr,m}$ | $t_{p,m}$ | $V_{corr,d}$ {eq}`eq-env-2.21.42` | $t_{p,d}$ {eq}`eq-env-2.21.42` | $V_{corr,d}$ {eq}`eq-env-2.21.43` | $t_{p,d}$ {eq}`eq-env-2.21.43` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| XC1 – 50 µm | -0.7 | 1.5 | 0.65 | 1 | 50.00 | 1.98 | **25** | 1.56 | **32** |
| XC2 – 50 µm | -0.3 | 1.5 | 0.65 | 4 | 12.50 | 5.36 | **9** | 4.38 | **11** |
| XC3 – 50 µm | -0.7 | 1.5 | 0.65 | 2 | 25.00 | 3.96 | **32** | 3.13 | **16** |
| XC4 – 50 µm | -0.7 | 1.5 | 0.9 | 5 | 10.00 | 12.86 | **2** | 8.34 | **6** |
| XS1 – 500 µm | -0.7 | 1.5 | 0.6 | 30 | - | 56.33* | **-** | 46.0* | **1** |
| XS2 – 500 µm | -0.3 | 1.5 | 0.6 | 10 | 5.00 | 13.10* | **4** | 11.0* | **5** |
| XS3 – 500 µm | -0.3 | 1.5 | 0.9 | 70 | - | 104.95* | **-** | 73.6* | **-** |
| XD1 – 500 µm | -0.7 | 1.5 | 0.6 | 4 | 12.50 | 7.51* | **7** | 6.1* | **8** |
| XD2 – 500 µm | -0.3 | 1.5 | 0.9 | 30 | 1.67 | 44.98* | **1** | 31.5* | **2** |
| XD3 – 500 µm | -0.3 | 1.5 | 0.6 | 30 | 1.67 | 39.30* | **1** | 33.0* | **2** |
```

\* these values are multiplied by the pitting factor $\alpha$ = 10

The expression {eq}`eq-env-2.21.43` gives longer $t_{p,d}$ values than expression {eq}`eq-env-2.21.42`. The $t_{p,d}/t_{p,m}$ ratios with expression {eq}`eq-env-2.21.43` result around 1.5-1.6 times, a safety factor of the order of the calculated by Izquierdo {cite}`Izquierdo2003` by means of a full probabilistic calculation, for the cases of carbonated concrete or chloride atmospheric exposures. It seems more reasonable the use of expression {eq}`eq-env-2.21.43` for the corrosion rate variable, because it evolves with variations in log scales with CV's higher than 20%.

Regarding the $t_{p,d}$ values, they result short of being practical in the exposures XS1, XS2, XD2 and XD3 even if $t_{p,m}$ values are used and therefore, in these exposure conditions it seems better to use the limit state of depassivation by selecting a chloride threshold value not too conservative.

{cite:empty}`Breit2001,Rodriguez1997`

**References**

```{bibliography}
:filter: docname in docnames
:style: unsrt
:labelprefix: 23.
```
