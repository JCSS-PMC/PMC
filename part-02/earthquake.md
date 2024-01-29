# Earthquake Load

## General

The two orthogonal horizontal components and the vertical component of the ground motion produced at a site by an earthquake provide the characterisation of the shaking.

The ground motion representation for structural design may be one of the following:

1) Time histories

2) Power spectral density

3) Response spectra.

Any of these representations can be site-dependent.

A site dependent representation of the seismic input must be appropriate for the soil characteristic where the structure is located, as well as for the source mechanism and the geologic path from the source to the site.

The time histories can be recorded or simulated. The power spectral density is the most representative function to describe the frequency content of the ground motion.

The response spectra for a specified ground motion represents the maximum response of the single degree of freedom (SDOF) structure to that motion.

## Probabilistic seismic hazard assessment (PSHA)

### General Methodology for PSHA

Probabilistic seismic hazard assessment (PSHA) is related to the prediction of the strong ground motion likely to occur at a particular site. The general PSHA is based on the following methodology:

1) Identification of the independent sources of seismic activity and determination of the magnitude model (Gutenberg - Richter relationship) from contribution of each sources;

2) Fitting the attenuation relationship on peak ground motion (or structural response) parameter, properly classified according to the soil category;

3) Calculating the peak ground motion (or structural response) parameter at the site with probability of non-exceedance during a specified time period.

### Magnitude model

The usual expression relating earthquake magnitudes with their rates of occurrence is due to Gutenberg \& Richter (1944). This relation is called "magnitude-frequency formula" and states that in a certain region and in a given period of time given an earthquake event:

```{math}
:label: eq-earthquake-2.17.1
\log \mathrm{N(M)}=\mathrm{a-b~M}
```

where {math}`\mathrm{N}(\mathrm{M})` is the mean number of earthquakes per unit volume and per unit time having magnitude greater than {math}`\mathrm{M}` and {math}`\mathrm{a}` and {math}`\mathrm{b}` are zone dependent constants. The parameter {math}`a` depends on the period of observation and on the level of seismicity of the region, and consequently, varies widely from region to region, while {math}`\mathrm{b}` remains within a relatively narrow range (usually {math}`b=1.0`).

It follows that the magnitude {math}`\mathrm{M}` in a region has a truncated exponential distribution, i.e. for {math}`\mathrm{M}_{1} \leq \mathrm{M} \leq \mathrm{M}_{2}` the cumulative probability distribution (conditional upon {math}`\mathrm{M}>\mathrm{M}_{1}` ) is given by:

```{math}
:label: eq-earthquake-2.17.2
F(M)=\frac{1-\exp \left[-\beta\left(M-M_{1}\right)\right]}{1-\exp \left[-\beta\left(M_{2}-M_{1}\right)\right]}
```

in which:

{math}`\beta=b \cdot \ln 10 \approx 2.30` (if {math}`b=1.0`)

{math}`\mathrm{M}_{1}` is the smallest magnitude of engineering interest considered in the model (here {math}`\mathrm{M}_{1}=4.0` ). {math}`\mathrm{M}_{2}` is the largest magnitude event which can be expected in the region (here {math}`\mathrm{M}_{2}=8.0` ). Geophysical theories relate the upper value of the magnitude to the depth of the solid earth crust and some of its properties. Therefore, different (possibly uncertain) upper values may be assigned in different regions. {math}`\mathrm{M}_{2}` can be consequently considered also as a random variable or approximately obtained by the following relationship:

```{math}
:label: eq-earthquake-2.17.3
\mathrm{M}_{2}=\left(1+\mathrm{r}^{-1}\right) \mathrm{Y}_{1}-\mathrm{r}^{-1} \mathrm{Y_{r}}
```

where {math}`r` is the number of considered earthquakes, {math}`\mathrm{Y}_{1}` is the largest value of magnitude till now and {math}`\mathrm{Y}_{\mathrm{r}}` is the r-largest value

### Attenuation laws

There is a strong correlation between what happens at the source and at the site, specifically at the base of the structure. Generally, the intensity of the motion-at-the-site decreases with increasing distance {math}`\Delta` between the site and the source and with decreasing magnitude. This is reflected in so-called attenuation laws which are based primarily on instrumental and other observed data. The general type of an attenuation law can be established from the theory of propagation of the various types of waves in elastic solid media. A rather general formulation of an attenuation law for the horizontal peak ground acceleration {math}`\mathrm{A}` in fraction of {math}`\mathrm{g}` in firm ground is the following:

```{math}
:label: eq-earthquake-2.17.4
A=b_{1} \cdot e^{b_{2}-M} \cdot(\Delta+k)^{-b_{3}} \cdot \varepsilon_{A}
```

where {math}`\Delta, \mathrm{k}` are in {math}`\mathrm{km}, \mathrm{A}` in fraction of {math}`\mathrm{g}, \mathrm{b}_{1}, \mathrm{~b}_{2}, \mathrm{~b}_{3}` and {math}`\mathrm{k}` are constants which are varying in each seismic region. {math}`\varepsilon_{\mathrm{A}}` is a lognormal error term which takes into account the variability of the attenuation law. Relations of the above type present generally rather large dispersions and are not universally accepted. {numref}`tbl-earthquake-1` collects the proposed coefficients of some attenuation laws relevant for the indicated region. Unfortunately, for the most of them no information related to the residual error is given, but {math}`\mu\left(\varepsilon_{\mathrm{A}}\right)=1` and the coefficient of variation {math}`\mathrm{V}\left(\varepsilon_{\mathrm{A}}\right)` can be presumed not to be less than 0.20 .

```{table} Attenuation Laws for the peak ground acceleration A (in fraction of g )
:name: tbl-earthquake-1
| Region | Literature | {math}`\mathrm{b}_{1}` <br> {math}`[\mathrm{g}]` | {math}`\mathrm{b}_{2}` <br> {math}`[-]` | {math}`\mathrm{b}_{3}` <br> {math}`[-]` | {math}`\mathrm{k}` <br> {math}`[\mathrm{km}]` | {math}`\mathrm{V}\left(\varepsilon_{\mathrm{A}}\right)` |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| California <br> USA | Donovan (1973) | 1.1 | 0.51 | 1.32 | 25 | 0.71 |
| California | Mc Guire (1974) | 0.48 | 0.64 | 1.3 | 25 | 0.22 |
| California and <br> Central America | Esteva \& Villaverde (1973) | 5.7 | 0.8 | 2 | 40 | 0.64 |
| California {math}`{ }^{* 1}` | Campbell (1981) | 0.016 | 0.868 | 1.09 | 2.007 | 0.24 |
| Canada | Milne \& Davenport (1969) | 0.04 | 0.99 | 1.39 | 0 | - |
| Canada | Davenport (1972) | 0.279 | 0.8 | 1.64 | 0 | - |
| Japan | Katayama \& Saeki (1978) | 0.02 | 0.7 | 0.8 | 0 | - |
| Taiwan | Mau \& Kao (1978) | 0.38 | 0.876 | 1.836 | 20 | - |
| South Africa | Donovan \& Bornstein <br> (1977) | 0.073 | 0.756 | 1.01 | 25 | - |
| Central Europe | Ahorner \& Rosenhauer <br> (1975) | 1.28 | 0.8 | 2.0 | 13 | - |
| Greece | Makropoulos (1978) | 2.2 | 0.7 | 1.8 | 20 | 0.50 |
| Switzerland {math}`{ }^{* 1}` | Ziegler (1985) | 0.016 | 0.868 | 0.95 | 2.649 | - |
| Italy {math}`{ }^{* 2}` | Sabetta and Pugliese (1987) | 0.014 | 0.363 | 0.5 | 25 | 0.20 |
```
Notes:

*1) In difference to eq. {eq}`eq-earthquake-2.17.4`, the attenuation laws proposed by Campbell (1981) and Ziegler (1985) are defined as:

```{math}
:label: eq-earthquake-2.17.5
A=b_{1} \cdot e^{b_{2}-M} \cdot(R+k)^{-b_{3}} \cdot \varepsilon_{A}
```

where {math}`\mathrm{R}` is the epicentral distance in {math}`\mathrm{km}`.

*2) The attenuation law by Sabetta and Pugliese (1987) is the following:

```{math}
:label: eq-earthquake-2.17.6
A=b_{1} \cdot e^{b_{2}-M} \cdot\left(\Delta^{2}+k\right)^{-b_{3}} \cdot \varepsilon_{A}
```

### Source geometry model

The source may generally be taken as a spatial random variable. The focus is the point where earthquake motion starts to be generated in the event. The focal distance is taken as the distance between focus and site.

If there are well-defined fault-lines it may be assumed that the focus occurs anywhere along the fault-line with equal probability. The focus may be understood as the center of the rupture zone. The focal distance can also be taken as the closest distance between rupture zone and site. The rupture length {math}`l` may be taken as a fraction of the earthquake magnitude according to: {math}`l=\exp \left(c_{1} . M-c_{2}\right)` with {math}`c_{1}` and {math}`c_{2}` coefficients characteristic for the fault (Der Kiureghian \& Ang 1977).

In many geographical regions fault locations and their activity are not known; existing data are so sparse that a division of a seismic region into faults or other active zones would be meaningless and unreliable. In addition one should consider that in regions with very high seismicity earthquakes occur practically everywhere.

The focal distance {math}`\Delta` is a function of the horizontal distance {math}`\mathrm{R}` from focus to site and of the epicentral depth {math}`\mathrm{H}` :

```{math}
:label: eq-earthquake-2.17.7
\Delta=\left(R^{2}+H^{2}\right)^{1 / 2}
```

The distribution of the horizontal distance {math}`\mathrm{R}` from the focus can be calculated under the assumption that focus locations are uniformly distributed over identified regions of homogeneous seismicity (seismotectonic province). For the focal depth a lognormal distribution is considered.

### Overall approach

{math}`\underline{\text{Life time probability distributions}}`

In good approximation, earthquakes occur according to a poisson process with mean occurrence rate {math}`\nu`. Although physical considerations suggest certain dependence between consecutive events. The exceedance probability {math}`\mathrm{P}[\mathrm{A} \geq a]` in a reference period {math}`\mathrm{T}` per unit area can be then estimated by:


```{math}
:label: eq-earthquake-2.17.8
P[\mathrm{~A} \geq a]=1-\exp \left(-\nu \cdot T P^{\prime}[\mathrm{A} \geq a]\right)
```

{math}`\nu=` number of earthquakes with {math}`\mathrm{M}>\mathrm{M}_{1}` per unit of time (occurrence rate)

{math}`\mathrm{T}=` period of time

{math}`\mathrm{P}^{\prime}[\mathrm{A}>\mathrm{a}]=` probability of {math}`\mathrm{A}>\mathrm{a}` given an earthquake with {math}`\mathrm{M}>\mathrm{M}_{1}` in one source area

The statistical uncertainty in the estimate of {math}`\nu` is very important, particularly if the observation records cover only a short period of time or the seismicity is relative small and consequently a Bayesian model to the description of the uncertainties of {math}`\nu` is recommended (see [Appendix A](section-Appendix-A)). The following simplified expression is proposed by Benjamin (1968) for the mean occurrence rate {math}`\nu` derived from Bayes' theorem:

```{math}
:label: eq-earthquake-2.17.9
-\nu \cdot \mathrm{T}=\ln \left(\frac{1}{\left(1+\frac{\mathrm{T}}{\tau}\right)^{\mathrm{n}+1}}\right)
```

where {math}`\mathrm{n}` is the number of earthquakes observed in the passed time {math}`\tau`.

{math}`\underline{\text { Different potential earthquake sources }}`

In general, different potential earthquake sources must be considered simultaneously. If, for example, a site is affected by more than one ring segment then the probability {math}`\mathrm{P}[\mathrm{A} \geq \mathrm{a}]` is obtained by:

```{math}
:label: eq-earthquake-2.17.10
P[A \geq a]=1-\prod_{i=l}^{m}\left(1-P_{i}[A \geq a]\right)
```

where {math}`m` is the number of the earthquake sources and {math}`\mathrm{P}_{\mathrm{i}}[\mathrm{A} \geq \mathrm{a}]` the exceedance probability for each source.

## Ground motions ground histories and associated response

### Peak ground acceleration and peak ground velocity

The earthquake ground motion at a given site can be assumed on a stationary Gaussian process.

Recorded ground motions should be digitised at a time interval of {math}`0.005 \mathrm{~s}`. Afterwards the correction procedure apply zero base-line, instrument correction and filters. The corrected accelerograms are integrated to find velocity and displacement time-histories.

The main characteristics of the ground motion time history are:

1) Peak ground acceleration (PGA) and corresponding peak velocity (PGV) and peak displacement (PGD);

2) Frequency content;

3) Motion duration.

The peak ground acceleration is the amplitude of ground acceleration. The peak ground velocity is the amplitude of ground velocity. Both parameters are very simple measures of severity of the ground shaking.

PGA and PGV recorded at a site during an earthquake are random variables and they should be defined with a specified probability to be exceeded on a certain area during a specified time interval.

### Strong motion duration

The strong motion duration is defined as the time interval between two specified fractions of the total energy of accelerogram:

```{math}
:label: eq-earthquake-2.17.11
E_{\text {tot }}=\int_{0}^{\mathrm{t_d}}[a(t)]^{2} d t
```

The cumulative energy of accelerogram monotonically increases from zero toward the total energy accumulated during the total duration of the motion {math}`\mathrm{t}_{\mathrm{d}}`. The specified fractions can be: {math}`0.05 \div 0.95,0.15 \div 0.85,0.05 \div 0.75,0.10 \div 0.90`, etc.

The strong motion duration represents the time interval over which the motion power is almost constant and near its maximum (the power is the slope of the cumulative energy plot). Hence different strong motion duration definitions can be used for different seismic records.

For simulated accelerograms, the durations of the strong phase of the motion and of the transient motions can be described by linear duration enveloping functions, {math}`\mathrm{I(t)}` multiplying the stationary acceleration:

Rise time {math}`\mathrm{t}_{\mathrm{r}}` {math}`\hspace{10em}` {math}`\mathrm{t} \leq \mathrm{t}_{\mathrm{r}}` {math}`\hspace{10em}` {math}`\mathrm{I}(\mathrm{t})=\mathrm{t} / \mathrm{t}_{\mathrm{r}}`  

Strong motion duration, {math}`\mathrm{t}_{\mathrm{m}}` {math}`\hspace{4.3em}` {math}`\mathrm{t}_{\mathrm{r}}<\mathrm{t}<\mathrm{t}_{\mathrm{r}}+\mathrm{t}_{\mathrm{m}}` {math}`\hspace{5.8em}` {math}`\mathrm{I}(\mathrm{t})=1.0` 

Decay time {math}`\hspace{10.4em}` {math}`\mathrm{t} \geq \mathrm{t}_{\mathrm{r}}-\mathrm{t}_{\mathrm{m}}` {math}`\hspace{7.8em}` {math}`\mathrm{I}(\mathrm{t})=-\mathrm{t} / \mathrm{t}_{\mathrm{r}}+\mathrm{t}_{\mathrm{d}} /\left(\mathrm{t}_{\mathrm{r}}+\mathrm{t}_{\mathrm{m}}\right)` 

The above time intervals depend on the intensity of the ground shaking. For rock conditions and magnitudes of order of {math}`\mathrm{M}=5.5 \div 7.5`, one may assume {math}`\mathrm{t}_{\mathrm{r}}=1-3 \mathrm{~s}, \mathrm{t}_{\mathrm{m}}=5-15 \mathrm{~s}` and {math}`\text{decay time}~4-10 \mathrm{~s}`.

### Frequency content

The frequency content of ground motion is the crucial concept for the understanding of the mechanism of ground motion to damage structures. The maximum values of structure response are when the structure frequency and the major part of the frequency content of ground motion fall in the same frequency band.

The frequency content can be described:

1) Directly, by density of the variance spectrum (PSD), obtained from stochastic modelling of the acceleration process;

2) Indirectly, by the response spectra obtained from numerical integration of the motion equation for the SDOF structure;

The stochastic measures of frequency content are related to the power spectral density function of stationary segment of the ground motion. They are:

1) The dimensionless indicators {math}`\varepsilon` (Cartwright \& Longuet - Higgins) and {math}`\mathrm{q}` (Vanmarcke);

2) The {math}`f_{10} f_{50}` and {math}`f_{90}` fractile frequencies below which {math}`10 \%, 50 \%` and {math}`90 \%` of the total cumulative power of PSD occur and the frequencies {math}`f_{1} f_{2}` and {math}`f_{3}` corresponding to the highest 1, 2, 3 peaks of the PSD.

The {math}`\varepsilon` and frequency bandwidth measures are defined as functions of the spectral moments of the one-side spectral density of the stationary process of ground acceleration, {math}`\mathrm{G}(\varpi)` :

```{math}
:label: eq-earthquake-2.17.12
\begin{array}{ll}
\varepsilon=\left(1-\lambda_{2}^{2} / \lambda_{0}~\lambda_{4}\right)^{1 / 2} & \qquad 0 \leq \varepsilon \leq 1 \\
q=\left(1-\lambda_{1}^{2} / \lambda_{0}~\lambda_{2}\right)^{1 / 2} & \qquad 0 \leq \mathrm{q} \leq 1
\end{array}
```

where the spectral moment of order {math}`\mathrm{i}~(\mathrm{i}=1,2 \ldots\ldots)` is:

```{math}
:label: eq-earthquake-2.17.13
\lambda=\int_{0}^{\varpi} \varpi^{1} G(\varpi) d \varpi
```

Wide frequency band processes have {math}`\varepsilon` values close to 2/3 and smaller than 0.85 .

Narrow frequency band seismic - processes of long predominant period (i.e. superposition of a single harmonic process at a short predominant frequency, {math}`\mathrm{f}_{\mathrm{p}}` and a wide band process) are characterised by {math}`\varepsilon` values greater than 0.95 .

The RMS value of the ground acceleration process is the square root of a 0 -order spectral moment {math}`\lambda_{0}{ }^{1 / 2}` and is very sensitive to the strong motion duration definition.

Cumulative power of the PSD is defined by:

```{math}
:label: eq-earthquake-2.17.14
\operatorname{Cum} \mathrm{G}\left(\varpi_{1}\right)=\int_{0}^{\varpi \text { cut-off }} G(\varpi) d \varpi
```

where the cut-off frequency is the reverse of the double of time internal used in process digitisation.

The duration for computing PSD of the stationary segment of the acceleration process should be selected as {math}`\mathrm{D}=\mathrm{T}_{0,9}-\mathrm{T}_{0,1}`, where {math}`\mathrm{T}_{0,9}` and {math}`\mathrm{T}_{0,1}` are the times at which {math}`90 \%` and {math}`10 \%` of the total cumulative energy of the accelerogram are reached. Alternative duration definitions are: {math}`\mathrm{D}=\mathrm{T}_{0.95}-\mathrm{T}_{0.05}` or {math}`\mathrm{D}=\mathrm{T}_{0.9}-\mathrm{T}_{0.05}`.

For simulating time-histories, a minimum power spectral density compatible with a specified response spectra functions must be recommended.

The deterministic measures of frequency content are related to the structure maximum response to the ground motion. They are the control frequencies and corresponding control periods:

```{math}
:label: eq-earthquake-2.17.15
\mathrm{f}_{\mathrm{C}}=\frac{1}{T_{C}}=\frac{1 S A_{\text {max }}}{2 \pi S V_{\text {max }}}
```

```{math}
:label: eq-earthquake-2.17.16
\mathrm{f}_{\mathrm{D}}=\frac{1}{T_{D}}=\frac{1 S V \text { max }}{2 \pi S D_{\text {max }}}
```

{math}`\mathrm{f}_{\mathrm{C}}` is the border between the maximum acceleration branch and the maximum velocity branch of response spectra and {math}`\mathrm{f}_{\mathrm{D}}` is the border between the maximum velocity branch and maximum displacement branch of response spectra.

SD, SV and SA are respectively the relative displacement, relative velocity and absolute acceleration spectra of the SDOF structure response.

For classifying the frequency content of the accelerogram the most significant measures are:

1) the control frequency {math}`\mathrm{f_{c}}`

2) the indicator {math}`\varepsilon` and

3) the frequency bandwidth {math}`\mathrm{f}_{10}-\mathrm{f}_{50}-\mathrm{f}_{90}`

4) the first peak of PSD {math}`\mathrm{f}_{1}`

The correlation between median frequency $f_{50}$ and the control frequency $f_{C}$ was found very strong but the stability of control frequency is better than that of the median frequency.

### Response spectra

Response spectra from the time history must be completed at sufficient frequency (period) intervals to have a good fit to the solution of spectral ordinates.

Since the PGA and PGV are not sufficiently consistent scaling factors for the spectral values of the both acceleration and velocity, the effective peak acceleration (EPA) and effective peak velocity (EPV) are recommended to be considered as normalizing factors for response spectra.

The EPA is defined as the average of the maximum ordinates of acceleration spectra in the period range of 0.1 to 0.5 seconds, devided by a standard (mean) value of 2.5 (for 5% damping):

```{math}
:label: eq-earthquake-2.17.17
\mathrm{EPA}=\frac{\text { mean of } S A_{0.1+0.5}(\xi=0.05)}{2.5}
```

The EPA is defined as the average of the maximum ordinates of velocity spectra in the period range of 0.8 to 1.2 seconds, divided by the same standard value of 2.5 (for 5% damping).

### Kanai - Tajimi spectrum

A powerful concept of explaining the mechanism of earthquakes is the so-called elasticrebound theory where gradually built-up strains and stresses in the crustal structure of the earth suddenly exceed the strength of material in a fault and so causing a sequence of rapid global and local displacements along a certain length of the fault. It is then assumed that this sequence of displacements form a Gaussian while noise generating two types of body waves (dilatation waves or primary waves and shear waves or secondary waves) but also surface waves. Clearly, the variance of the white noise process should be directly related to the magnitude. P- (primary) waves travel faster than S- (secondly) waves which, at a given site, are followed by the slower surface waves. In the contrary, the frequencies decrease from Pwaves over S- waves to surface waves while acceleration amplitudes appear to be largest for S- waves. During their travel through the various crustal layers the various earthquake waves are modified differently by multiple filterings, reflections, refractions and attenuations so that the dominating frequency of acceleration at the site decreases with increasing focal distance and increasing magnitude. On the other hand, the duration of an earthquake increases with focal distance and magnitude according to the physical model.

Among others Kanai and Tajimi assumed that the earthquake accelerations process at a given site can be taken as the outcome of a simple one-degree-of-freedom oscillator driven by stationary Gaussian while noise in the so-called strong motion phase and damping properties depending on the soil surrounding the site under investigation. In particular, if (one-sided) spectral density has form

```{math}
:label: eq-earthquake-2.17.18
\mathrm{G}_{\mathrm{A}}(\omega)=\frac{G_{o}\left[1+4 \zeta_{g}^{2}\left(\omega / \omega_{g}\right)^{2}\right]}{\left[1-\left(\omega / \omega_{g}\right)^{2}\right]^{2}+4 \zeta_{g}^{2}\left(\omega / \omega_{g}\right)^{2}}
```

in which {math}`\mathrm{G_{o}}` is a scaling factor, {math}`\omega_{g}` the dominating incoming natural frequency and representative {math}`\zeta_{g}` the damping ratio of the surrounding soil and whose variance can be determined to be

```{math}
:label: eq-earthquake-2.17.19
\lambda_{o}=\sigma_{A}^{2}=\int_{0}^{\infty} G_{A}(\varpi) d \varpi=\frac{\pi G_{0} \omega_{g}}{4 \zeta_{g}}\left(1+4 \zeta_{g}^{2}\right)
```

while higher spectral moments may be evaluated from {eq}`eq-earthquake-2.17.11`

The scaling factor is defined as:

```{math}
:label: eq-earthquake-2.17.20
G_{0}=\frac{A^{2} 2 \zeta_{g} \omega_{g}^{3}}{\pi \ln \left(2.8 \frac{\omega_{g} s}{2 \pi}\right)}
```

### Relative Magnitude and Correlation between Excitation Components

Rotational excitations generally can be neglected. Horizontal and vertical accelerations can be assumed independent as well as any two orthogonal horizontal components which is exactly true for the radial and tangential components for shear waves. The intensity parameter for vertical accelerations is roughly equal to the corresponding one for horizontal motions for small epicentral distances (≈ 20 km) and falls off down to 50 to 30% for larger epicentral distances on firm grounds. On soft grounds vertical motions can generally be disregarded. For all translational components the same type of spectral density function can be used.

Given an earthquake ground accelerations are spatially correlated at any point in time. The following form of the auto-correlation function is suggested: {math}`\rho(\mathrm{r})=\exp \left[-\alpha \mathrm{r}^{2}\right]` where {math}`\mathrm{r}` is the distance in {math}`[\mathrm{m}]` between {math}`10^{-6}` (for firm ground) and {math}`10^{-7}` (for soft ground). For {math}`\mathrm{r}<100 \mathrm{~m}` full correlation may be assumed.

**REFERENCES**

Ahorner, L. \& Rosenhauer, W., 1975, Probability Distribution of Earthquake Accelerations with Applications to Sites in the Northern Rhine Area, Central Europe, Journ. Geophys., 41, 581-594.

Benjamin, J.R., 1968, Probabilistic Models for Seismic Force Design, Journ. Struc. Div., ASCE, 94, ST5, 1174-1195.

Campbell, K.W., 1981, Near-Source-Attenuation of Peak Horizontal Acceleration, BSSA, Vol.71, No.6.

Cornell, C.A., 1971, Probabilistic Analysis of Damage to Structures under Seismic Loads, Dynamic Waves in Civil Engineering, Wiley-Interscience (edited by D.A. Howells, I.P. Haigh and C. Taylor), Great Britain.

Der Kiureghian, A. \& Ang, A., 1977, A Fault Rupture Model for Seismic Risk Analysis, Bull. Seis. Soc. Amer., 67, No. 4, 1173-1194.

Der Kiureghian, A., 1981, Seismic Risk Analysis of Structural Systems, Journ. Eng. Mech. Div., ASCE, 107, No. EM6, 1133-1153.

Donovan, N.C., 1973, A Statistical Evaluation of Strong Motion Data Including the February 9, 1971, San Fernando Earthquake, Proc. of $5^{\text {th }}$ WCEE, Rome, Italy, 1252-1261.

Donovan, N.C. \& Bornstein, A.E., 1977, The Problems of Uncertainties in the Use of Seismic Risk Procedures in Use of Probabilities in Earthquake Engineering, ASCE, Spec. Publ., 1-36.

Esteva, L. \& Villaverde, R., 1973, Seismic Risk, Design Spectra and Structural Reliability, Proc. $5^{\text {th }}$ WCEE, Rome, 2586-2597.

Gutenberg, B. \& Richter, C., 1944, Frequencies of Earthquakes in California, Bull. Seism. Soc. Amer., 34, 185-188.

Katayama, T. \& Saeki, M., 1978, Statistical Analysis of Earthquake Acceleration Response Spectra, Proc. of ISCE, No. 275 (in Japanese).

Makropoulos, K., 1978, The Statistics of Large Earthquake Magnitude and an Evaluation of Greek Seismicity, PhD Thesis, University of Edinburgh, Scotland, 1978.

Mau, S.T. \& Kao, C.S., 1978, A Risk Model for Seismic Zoning in Taiwan, Proc. of $2^{\text {nd }}$ Intern. Conf. on Microzonation, Vol. I, San Francisco, 367-378.

McGuire, R.K., 1974, Seismic structural response risk analysis, incorporating peak response regressions on earthquake magnitude and distance. Massachusets Inst. of Technol., Dep. of Civ. Eng., Res. Rpt. R74-51.

Milne, W.G. \& Davenport, A.G., 1969, Distribution of Earthquake Risk in Canada, Bull. Seism. Soc. Amer., 59, No. 2, 754-799.

Sabetta, F. \& Pugliese, A., 1987, Attenuation of peak horizontal acceleration and velocity from Italian strong-motion records. Bull. Seismol. Soc. Amer. 77 (1987) 1491-1523.

Tajimi, H.: A Statistical Method of Determining the Maximum Response of a Building Structure during an Earthquake, Proc. $2^{\text {nd }}$ WCEE, Tokyo,2,pp. 781.797, Science Council of Japan, Japan.

Ziegler, A., 1985, Bemessungsbeben für Stauanlagen im schweizerischen Alpenraum, Abhandlung zur Erlangung des Titels eines Doktors der Technischen Wissenschaften der Eidgenössischen Technischen Hochschule Zürich, Diss. ETH Nr. 7767, Schweiz.

(section-Appendix-A)=
## Appendix A: Bayesian Updating of Earthquake Occurrence Rates and Magnitudes

The seismology in a given region as being characterized by the Poissonian occurrence rate and the distribution of magnitudes generally is known only approximately due to scarcity of data. Statistical uncertainties need to be considered.

Furthermore, a consistent way to incorporate non - statistical geological information usually is desirable. Assuming a Poisson process for earthquake occurrences and a gamma distribution as the (natural conjugate) prior distribution on the probability mass function of the number of future earthquakes in a given time interval {math}`[0, \mathrm{t}]` is {math}`(/ \mathrm{A} 1 /, / \mathrm{A} 2 /)` :

```{math}
:label: eq-earthquake-A.1
\mathrm{p}\left(\mathrm{n} / \mathrm{n}^{\prime \prime}, \mathrm{t}^{\prime \prime}, \mathrm{t}\right)=\frac{T\left(n+n^{\prime \prime}\right)}{n ! T\left(n^{\prime \prime}\right)}\left(\frac{t^{\prime \prime}}{t+t^{\prime \prime}}\right)^{n^{\prime \prime}}\left(\frac{t}{t+t^{\prime \prime}}\right)^{n}
```

with mean

```{math}
:label: eq-earthquake-A.2
E[N(0, T)]=\frac{n^{\prime \prime}}{t^{\prime \prime}} t
```

and where

```{math}
n^{\prime \prime}=n_{o}+\left(\frac{\overline{\nu^{\prime}}}{\sigma_{\nu}^{\prime}}\right)^{2} \qquad t^{\prime \prime}=t_{o}+\frac{\overline{\nu^{\prime}}}{\left(\sigma_{\nu}^{\prime}\right)^{2}}
```

{math}`n_{o}=` number of earthquakes observed in the past period {math}`t_{o}`

{math}`\overline{\nu^{\prime}}, \sigma^{\prime}{ }_{\nu}=` prior geological assessments on mean and standard of {math}`\nu` which become non-informative if formally {math}`\sigma^{\prime}{ }_{\nu} \rightarrow \infty`

The posterior probability density of {math}`\nu` is

```{math}
:label: eq-earthquake-A.3
f^{\prime \prime}\left(\nu \mid n^{\prime \prime}, t^{\prime \prime}\right)=\frac{t^{\prime \prime}\left(t^{\prime \prime} \nu\right)^{n^{\prime \prime}-1}}{\Gamma\left(n^{\prime \prime}\right)} \exp \left[-\nu t^{\prime \prime}\right]
```

whereas the conditional probability mass function of the number of earthquakes is

```{math}
:label: eq-earthquake-A.4
p\left(N(O, t)=n \mid \nu \right)=\frac{(\nu t)^{n}}{n !} \exp [-\nu t]
```

Similarly, if the value of {math}`\beta` in eq. {eq}`eq-earthquake-2.17.1` is subject to statistical uncertainty and geological judgement, the predictive distribution function of earthquake magnitudes is:

```{math}
:label: eq-earthquake-A.5
F\left(m, m^{\prime \prime}, \eta^{\prime \prime}\right)=\frac{1-\left(\frac{m^{\prime \prime}}{m^{\prime \prime}+m-m_{o}}\right)^{\eta^{\prime \prime}}}{1-\left(\frac{m^{\prime \prime}}{m^{\prime \prime}+m_{u}-m_{o}}\right)^{\eta^{\prime \prime}}}$ for $m_{o} \leq m \leq m_{u}
```

with

```{math}
\eta^{\prime}=n_{o}+\left(\frac{\overline{\beta}}{\sigma^{\prime}{ }_{\beta}}\right)^{2}
```

```{math}
m^{\prime \prime}=n_{o}\left(\overline{m}-m_{o}\right)+\frac{\overline{\beta^{\prime}}}{\left(\sigma^{\prime}{ }_{\beta}\right)^{2}}
```

where {math}`n_{o}` the number of earthquakes with magnitude {math}`M \geq m_{o}` and arithmetic mean {math}`\overline{m}` and {math}`\beta^{\prime}`, {math}`\sigma_{\beta}^{\prime}` the prior (geological) assessments on the mean and standard deviation of the magnitude frequency parameter {math}`\beta`. As before the posterior probability density of {math}`\beta` is gamma-distributed with parameters {math}`\eta^{\prime \prime}` and {math}`\mathrm{m}^{\prime \prime}`.

$\underline{\text {References}}$

[A1] Benjamin, J.R., Cornell, C.A., Probability, Statistics and Decision for Civil Engineers, McGraw-Hill, ,New York, 1970.

[A2] Campbell, K.W., Bayesian Analysis of Extreme Earthquake Occurrences, Part I: Probabilistic Hazard Models, BSSA, 72, 1982, 5. pp. 1689-1705.

