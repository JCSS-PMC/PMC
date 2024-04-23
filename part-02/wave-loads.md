# Wave loads

**List of symbols:**

$\begin{array}{ll}c &=  \text { phase velocity} ( c=\omega / k) \\
d &=  \text { water depth} \\
d_{c} &=  \text { thickness of protection block layer} \\
f &=  \text { frequency} (=1/T) \\
f_{p} &=  \text { frequency corresponding to} T_{p} \\
g &=  \text { acceleration of gravity} \\
h &=  \text { water depth in front of the structure;} \\
h^{\prime} &=  \text { water depth at the toe of the front wall} (= d+d_{c} )\\
h_{b} &=  \text { water depth at a distance of 5 times the significant wave height}\\
k &=  \text { wave number} ( k=1 / \lambda) \\
u(x, z, t) &=  \text { horizontal particle velocity}\\
\dot{u}(x, z, t) &=  \text { acceleration} \\
u &=  \text { water velocity perpendicular to structural member} \\
\dot{u} &=  \text { water acceleration perpendicular to structural member} \\
u-\dot{x} &=  \text { relative velocity} \\
\dot{x} &=  \text { cylinder velocity} \\
\ddot{x} &=  \text { cylinder acceleration} \\
x, y, z &=  \text { coordinates} \\
A &=  \text { cross section area} \\
A_{\gamma} &=  \text { normalisation factor,} \approx 1-0.287 \ln (\gamma) \\
C_{M} &=  \text { inertia coefficient} \\
C_{D} \cdot &=  \text { drag coefficient} \\
D &=  \text { cylinder diameter} \\
F &=  \text { force per cylinder length in flow and motion direction} \\
H_{s} &=  \text { significant wave height} \\
H &=  \text { incident wave height (from trough to crest) in front of the structure} \\
K &=  \text { non-linearity factor} \\
L &=  \text { wave length;} \\
M_{n} &=  \text { n-th (spectral) moment} \\
S &=  \text { significant wave slope} \\
S(f), S(\omega) &=  \text { spectral density} \\
T &=  \text { wave period.} \\
T_{p} &=  \text { peak period} \\
T_{z} &=  \text { mean wave period} \\
T_{m o 2} &=  \text { average wave period} \\
T_{d} &=  \text { duration of sea state}\\
T(z, \omega) &=  \text { transfer function} \\
V &=  \text { coefficient of variation} \\
\alpha &=  \text { generalised Phillips' constant, scale parameter} \\
\alpha_{1}, \alpha_{2}, \alpha_{3} &=  \text { factors dependent on hydraulic conditions (see {eq}`eq-wave-2-56`)} \\
\alpha_{4} &=  \text { kurtosis} \\
\beta &=  \text { shape parameter} \\
\beta &=  \text { angle of wave incidence} \\
\gamma &=  \text { location parameter} \\
\gamma &=  \text { peakness parameter in spectrum} \\
\delta, \varepsilon &=  \text { spectral width} \\
\phi_{s} &=  \text { mean wave direction} \\
\lambda &=  \text { wave length} \\
\lambda_{1}, \lambda_{2}, \lambda_{3} &=  \text { factors in wave force model} \\
\theta &=  \text { wave direction} \\
\theta_{w} &=  \text { wave model unertainty} \\
\theta &=  \text { angle between the elementary wave and the main wave direction} \\
\theta_{\mathrm{MG}} &=  \text { model uncertainty marine growth} \\
\eta(x, y, t) &=  \text { surface elevation} \\
\nu_{0}^{u} &=  \text { zero-crossing frequency} \\
\tilde{\nu}(z) &=  \text { ensemble averaged up-crossing rate} \\
\rho &=  \text { density of water} \\
\rho_{i j} &=  \text { coefficient of correlation between members} \\
\sigma &=  \text { standard deviation, spectral width parameter} \\ 
\tau &=  \text { short-term duration} \\
\omega &=  \text { angular wave frequency} (=2 \pi f) \\
\omega_{p} &=  \text { angular spectral peak frequency} (= 2 \pi f_{\mathrm{p.}})\\
\vec{\psi} &=  \text { environmental state}\end{array}$


## Introduction

Waves as relating to wave loads on structures are usually described in terms of sea states. A sea state is an approximately stationary condition described by parameters with long-term fluctuations. These parameters include the significant wave height $H_{s}$, the mean wave period $T_{z}$, the peak period $T_{p}$ and the wave direction $\theta$.

The waves in a sea state are usually described by means of the statistics of the surface elevation $eta(x, y, t)$. Wave forces depend on the velocity and acceleration of water particles below the surface. The relation between these variables can be found using wave theories. Among these may be mentioned:

- *Linear wave* theory, by which the wave profile is described as a sine function.
- *Solitary wave* theories for particularly shallow water.
- *Cnoidal wave* theories which cover the waves above as special cases.
- *Stokes wave* theories for particularly high waves
- *Stream-function waves*, which are based on numerical methods and accurately, describe the wave kinematics over a broad range of water depths
- *Solitons*, weakly non-linear dispersive waves
- *Wave packets*, solutions of Non-Linear Schroedinger Equation

The following wave theories are in common use ( $d$ is the water depth and $\lambda$ is the wave length):

- Solitary wave theory for $d / \lambda<0.1$;
- Stokes' $5^{\text {th }}$ order theory for $0.1<d / \lambda<0.3$;
- Linear wave theory for $d / \lambda>0.3$.

For most practical purposes an appropriate order of Dean's Stream Function or Stokes' 5th is applicable for regular wave analysis. For the spectral description of random seas, the linear wave theory is almost always used.

The most important solution of the linear wave equations is the long crested wave. The surface elevation is a sine wave with amplitude $a$ progressing with phase velocity $c=\omega / k$,

```{math}
:label: eq-wave-2-1
\eta(x, t)=a \sin (\omega t-\vec{k} \vec{x})=a \sin (\omega t-k x))
```

if the wave direction is parallel to the $x$-axis. More general wave forms can be generated by superposition of plane waves with different values of $a$ and $\omega$. The dispersion relation between wave number $k=1 / \lambda$ and angular wave frequency $\omega$ reads

```{math}
:label: eq-wave-2-2
\omega^{2}=g k \tanh (k d)
```

Here $g$ is the constant of gravity and $d$ is the water depth. The deep water approximation $\omega^{2}=g k$ is valid for depths exceeding approximately half the wavelength.

The horizontal particle velocity $u(x, z, t)$ and acceleration $\dot{u}(x, z, t)$ follow from:

```{math}
:label: eq-wave-2-3
u(x, z, t)=\omega \frac{\cosh k(z+d)}{\sinh (k d)} \eta(x, t)=\omega T(z, \omega) \eta(x, t)
```

where $T(z, \omega)$ is a transfer function.

For large $\omega$, the dispersion relation degenerates into the deep-water form, and

```{math}
:label: eq-wave-2-4
T(z, \omega) \sim \exp \left(\frac{\omega^{2} z}{g}\right)
```

The limiting average wave steepness for short-term irregular seastates may in absence of other reliable sources be taken as:

```{math}
:label: eq-wave-2-5
S=\frac{2 \pi}{g} \frac{H_{S}}{T_{Z}^{2}}=\left\lbrace
\begin{array}{lll} \frac{1}{15} & \text { for } T_{Z} \geq 12 s & unlimited~fetch \\ \\ \frac{1}{10} & \text { for } T_{Z}<6 s & limited~fetch \end{array}\right.
```
and interpolated linearly between the boundaries.

Stretching of wave theory to the instantaneous sea surface should be performed. When linear wave theory is applied, the extrapolation of the wave kinematics to the free surface is most appropriately carried out by substituting the true elevation, at which the kinematics are required, with one which is at the same proportion of the still water depth as the true elevation is of the instantaneous water depth. This can be expressed as follows

```{math}
:label: eq-wave-2-6
z_{s}=\frac{z-\eta}{1+\frac{\eta}{d}}
```

where:

$z_{s}=$ The modified coordinate to be used in particle velocity formulation

$z=$ The elevation at which the kinematics are required (coordinate measured vertically upward from the still water surface)

$\eta=$ The instantaneous water level (same axis system as z)

$d=$ The still, or undisturbed water depth (positive).

This method ensures that the kinematics at the surface are always evaluated from the linear wave theory expressions as if they were at the still water level {cite}`Wheeler1969`.


## The short-term random wave process

### Wave spectrum and sea state parameters

During a relatively short period, waves can be conceived as a superposition of deterministic wave components with random phase and amplitude. As a result the waves form a stationary Gaussian process. The period for which such a model holds is called a sea state. The process is described by a variance spectrum $S_{\eta \eta}(\omega)$. Before introducing this spectrum in more detail it is convenient to introduce the spectral moments.

### Spectral Moments

The spectral moment $M_{n}$ of general order $n$ is defined as

```{math}
:label: eq-wave-2-7
M_{n}=\int_{0}^{\infty} \omega^{n} S(\omega) d \omega
```

where $\mathrm{n}=-1,0,1,2,\ldots$

Quantities that may be defined in terms of spectral moments are among others:

Significant wave height

```{math}
:label: eq-wave-2-8
H_{m 0}=4 \sqrt{M_{0}}=4 \sigma_{\eta}
```

where $\sigma_{\eta}$ is the standard deviation of $\eta(t)$.

Average wave period

```{math}
:label: eq-wave-2-9
T_{m o 2}=2 \pi\left(\frac{M_{0}}{M_{2}}\right)^{1 / 2}
```

Significant wave slope

```{math}
:label: eq-wave-2-10
S=\frac{2}{\pi g} \frac{M_{2}}{\sqrt{M_{0}}}
```

Spectral width

```{math}
:label: eq-wave-2-11
\delta=\frac{M_{1}}{\sqrt{M_{0} M_{2}}} 
```

```{math}
:label: eq-wave-2-12
\varepsilon=\sqrt{1-\frac{M_{2}^{2}}{M_{0} M_{4}}}
```

If the spectral density is given as a function of the frequency $f, S=S(f)$, the relation is

```{math}
:label: eq-wave-2-13
S(f)=2 \pi S(\omega)
```

Similarly, if the moments of the circular frequency spectrum $S(f)$ are denoted $M_{n}(f)$, the relationship to $M_{n}$ is

```{math}
:label: eq-wave-2-14
M_{n}(f)=\int_{0}^{\infty} f^{n} S(f) d f=(2 \pi)^{-n} M_{n}
```

Note: If the period is not given for a particular sea-state, a tentative estimate

```{math}
:label: eq-wave-2-15
T_{z}=6 H_{s}^{0.3}
```

where $T_{z}$ is in seconds and $H_{s}$ is in metres.

### Single peak spectrum

The most frequently used spectra are the JONSWAP (Hasselman et al., 1973) spectrum and the {cite}`PiersonMoskowitz1964`. Both spectra describe wind sea conditions that are reasonable for the most severe seastates.

The originally proposed PM spectrum is:

```{math}
:label: eq-wave-2-16
S(\omega)=0.0081 g^{2} \omega^{-5} \exp \left(-0.74\left(\frac{\omega}{\omega_{p}}\right)^{-4}\right)
```

where $g$ is the acceleration of gravity, and $\omega_{p}$ is the angular spectral peak frequency.

The {cite}`ISCC1964` version of the PM spectrum is

```{math}
:label: eq-wave-2-17
S(\omega)=\frac{H_{S}^{2}}{4 \pi}\left(\frac{2 \pi}{T_{Z}}\right)^{4} \omega^{-5} \exp \left(-\frac{1}{\pi}\left(\frac{2 \pi}{T_{Z}}\right)^{4} \omega^{-4}\right)
```

The PM spectrum is meant to be applied for fully developed seas. Observations indicate that the empirical spectrum is often more peaked than the PM spectrum. The JONSWAP spectral density function is:

```{math}
:label: eq-wave-2-18
S(\omega)=\alpha g^{2} \omega^{-5} \exp \left(-\frac{5}{4}\left(\frac{\omega}{\omega_{p}}\right)^{-4}\right) \gamma^{\exp \left(-0.5\left(\frac{\omega-\omega_{p}}{\sigma \omega_{p}}\right)^{2}\right)}
```

where

$
\omega =\text { Angular wave frequency, } \omega=2 \pi f 
$

$f =\text { Wave frequency, } f=1 / T$

$T =\text { Wave period. }$

$T_{p} =\text { Peak period }$

$f_{p} =1 / T_{p}$

$\omega_{p} =\text { Angular spectral peak frequency } \omega_{p}=2 \pi f_{p}$

$g =\text { Acceleration of gravity. }$

$\alpha  =\text { Generalised Phillips’ constant, } =(5 / 16)^{*}\left(H_{s}{ }^{2} \omega_{p}{ }^{4} / g^{2}\right)^{*} ~A_{\gamma}$

$A_{\gamma}  =\text { Normalisation factor, } \approx 1-0.287 \ln (\gamma)$

$\sigma  =\text { Spectral width parameter. }  =0.07 \text { if } \omega \leq \omega_{p}$

$\sigma = \text{Spectral width parameter} = \begin{cases} 
0.07 & \text{if } \omega \leq \omega_p \\
0.09 & \text{if } \omega > \omega_p 
\end{cases}$

$\gamma  =\text { Peakness parameter }(\gamma=1.0 \text { for PM })$

If no particular values are given for the peakedness parameter $\gamma$, the following value may be used:

```{math}
:label: eq-wave-2-19
\begin{aligned}
& \gamma=5 \quad \text { for } \quad \frac{T_{p}}{\sqrt{H_{s}}} \leq 3.6 \\
& \gamma=e^{5.75-1.15 T_{p} / \sqrt{H_{s}}} \text { for } 3.6 \leq \frac{T_{p}}{\sqrt{H_{s}}} \leq 5 \\
& \gamma=1 \quad \text { for } \quad 5 \leq \frac{T_{p}}{\sqrt{H_{s}}}
\end{aligned}
```

where $T_{p}$ is in seconds and $H_{s}$ is in metres.

For the JONSWAP spectrum the spectral moments are given approximately as

```{math}
:label: eq-wave-2-20
\begin{aligned}
M_{-1} &= \frac{1}{16} H_{s}^{2} \omega_{p}^{-1} \frac{4.2+\gamma}{5+\gamma} \\
M_{0} &= \frac{1}{16} H_{s}^{2} \\
M_{1} &= \frac{1}{16} H_{s}^{2} \omega_{p} \frac{6.8+\gamma}{5+\gamma} \\
M_{2} &= \frac{1}{16} H_{s}^{2} \omega_{p}^{2} \frac{11+\gamma}{5+\gamma}
\end{aligned}
```

The average zero-crossing wave period $T_{z}$ may be related to the peak period $T_{p}$ by

```{math}
:label: eq-wave-2-21
T_{z}=T_{p}\left(\frac{5+\gamma}{11+\gamma}\right)^{1 / 2}
```

Note: A possible non-conservatism related to the choice of the spectral model is due to the definition of the frequency exponent describing the equilibrium range of the spectrum. The JONSWAP and Pierson-Moskowitz spectra adopt $\omega^{-5}$. Both the theory, as well as recent analysis of spectral data {cite}`Prevosto1996`, show that the tail of the JONSWAP spectrum is indeed closer to $\omega^{-4}$, as has already been noted by {cite}`Battjes1978`. The tail behaviour may be important for structural response. E.g., {cite}`BitnerGregersen1991` show that the $f^{-4}$ assumption may increase the dynamic response of a jacket structure by $25 \%$ as compared to the $f^{-5}$ model.

### Double peak spectrum

Moderate and low sea states in open sea areas, are often composed of both wind sea and swell (e.g. the Western coast of Europe). A two-peak spectrum may be used to account for combined sea states, i.e.

```{math}
:label: eq-wave-2-22
S(\omega)=S_{H F}(\omega)+S_{L F}(\omega)
```

Splitting of the wave spectrum into wind sea and swell have been made by several authors ({cite}`StrekalovMassel1971`; {cite}`OchiHubble1976`; {cite}`GuedesSoaresNolasco1992`)

Ochi and Hubble represent each spectrum component by a three parameter formula of a Gamma type. The parameters should be determined numerically to best fit the observed spectra.

Input parameters to the Torsethaugen spectrum are significant wave height and peak period. A modified JONSWAP spectrum is used for both wind sea and swell peaks, and the spectrum parameters are related to $H_{s}$ and $T_{p}$ according to empirical parameters based on analysis of measured data from the Norwegian and North Sea.

### Directional wave spectrum

Directional short-crested wave spectra $S(\omega, \theta)$ may be expressed in terms of the nondirectional wave spectra,

```{math}
:label: eq-wave-2-23
S(\omega, \theta)=S(\omega) D(\theta, \omega)=S(\omega) D(\theta)
```

where the latter equality represents a simplification often used in practice. Here $D(\theta, \omega) ; D(\theta)$ is a directionality function, and $\theta$ is the angle between the direction of elementary wave trains and the main wave direction of the short crested wave system.

The directionality function fulfils the requirement

```{math}
:label: eq-wave-2-24
\int_{\theta_{\min }}^{\theta_{\max }} D(\theta, \omega) d \theta=1
```

Different forms of directional functions are given in the literature. An early formulation is the cosine-power model

```{math}
:label: eq-wave-2-25
D(\theta, \omega) \propto \cos ^{n}\left(\theta-\theta_{p}\right) \quad \text { where } \quad 2 \leq \mathrm{n} \leq 10
```

Due consideration is to be taken to reflect an accurate correlation between the actual sea-state and the constant, $`n$. The main direction may be set equal to the prevailing wind direction if directional measurements are not available.

A commonly applied cosine-power form is the cos-2s distribution introduced by {cite}`LonguetHiggins1963`

```{math}
:label: eq-wave-2-26
D(\theta)=\frac{1}{2 \pi} \frac{\Gamma(s+1)}{\sqrt{\pi} \Gamma(s+1 / 2)} \cos ^{2 s}\left(\frac{\theta}{2}\right) \quad \text { for } \quad s>0
```

Measurements should indicate which form and parameters should be preferred.

### Crest distribution for Gaussian Sea-State

The statistical distribution of individual wave crests $Z$ in an irregular short-term stationary sea state is in a linear, narrow band approximation the same as the distribution of the envelope of a Gaussian process, i.e. the Rayleigh distribution

```{math}
:label: eq-wave-2-27
F(z)=1-e^{-\frac{1}{2}\left(\frac{z}{\sigma_{\eta}}\right)^{2}}=1-e^{-8\left(\frac{z}{H_{s}}\right)^{2}}
```

where $\sigma_{\eta}=H_{s} / 4$. The extreme value distribution $F_{E}(z)$ of crest in a stationary sea state of duration $\tau$ follows by assuming Poisson upcrossings of level $z$ as

```{math}
:label: eq-wave-2-28
F_{E}(z) \approx \exp \left\lbrace-\frac{\tau}{T_{z}} \exp \left\lbrace-\frac{1}{2}\left(\frac{z}{\sigma_{\eta}}\right)^{2}\right\rbrace \right\rbrace =\exp \left\lbrace -\frac{\tau}{T_{z}} \exp \left\lbrace -8\left(\frac{z}{H_{s}}\right)^{2}\right\rbrace \right\rbrace
```

### Crest distribution for Non-Gaussian Sea-State

The Gaussian model fails to capture asymmetric, non-linear wave aspects caused by dynamic pressures not included in the linear theory, which is essential for shallow water, but can also be important for deep-water applications. A possible classification of statistical procedures for assessment of non-Gaussian processes $\eta(t)$ is

- establish the probability distribution of the elevation process $\eta(t)$ by modification of a simpler distribution, usually the Gaussian distribution
- transform the elevation process $\eta(t)$ into a Gaussian process $U(t)$ and apply properties of the Gaussian process
- establish the exact joint distribution function of the process and the differentiated process
- fit a distribution function to the sample of local peaks.


### Distribution for wave heights

Assuming a Gaussian narrow banded sea surface elevation, the individual wave heights are described by the Rayleigh distribution as shown by {cite}`LonguetHiggins1952`, and {cite}`Cartwright1956`

```{math}
:label: eq-wave-2-29
P(H>h)=\exp \left\lbrace-\left(\frac{h}{2 \sqrt{2} \sigma_{\eta}}\right)^{2}\right\rbrace
```

For not too narrow banded waves this distribution is a good approximation only when the root-mean-square (rms) amplitude is used instead of the sea surface elevation standard deviation, {cite}`LonguetHiggins1980`.

Other studies of the probability distribution of wave heights are made by e.g. {cite}`Massel1989`, {cite}`Battjes1978`, {cite}`Cavanie1976`, {cite}`Arhan1978`. The following
expression for the exceedance probability for high $h$ values is due to {cite}`Tayfun1981`, {cite}`Tayfun1990`

```{math}
:label: eq-wave-2-30
P(H>h)=\left(1+\frac{1-k^{2}}{4 k h^{2}} \sigma_{\eta}^{2}\right)\left(\frac{1+k^{2}}{2 k}\right)^{1 / 2} \exp \left\lbrace -\frac{h^{2}}{4(1+k) \sigma_{\eta}^{2}}\right\rbrace
```

where $k$ is a parameter for the correlation between crest and subsequent trough.

The extreme wave height estimates can be transformed into measures for the crests using e.g. Stokes theory or regression analysis. E.g., {cite}`Skourup1996` analyse data from the Central North Sea (Gorm field) and finds the expected ratio 0.69 between extreme crest height and extreme wave height.

Note that wave heights may be correlated to water levels through the wind speed.

## Long-term wave conditions

### Marginal distribution of significant wave height

Long-term variations of sea states characteristics represent a base for establishing metocean criteria for design of offshore structures and for different operational conditions. The long-term description of waves is usually governed by the variation of significant wave height.

The following analysis strategies are commonly applied:

- Global method, in which all regular data (all 3-hour data) are fitted by an appropriate distribution function, for example a 3-parameter Weibull distribution.
- Peak over threshold method or storm analysis method, in which peaks over specified thresholds are identified and fitted by a set of relevant statistical distributions (Gumbel, Weibull, exponential). Sensitivity analysis with respect to threshold level should be performed.
- Annual extremes, in which annual or seasonal extremes are fitted by relevant extreme value distributions.

In selecting the method there is a tradeoff between the global models using all data and the extreme event models based on a subset of the largest data points. While the global approach utilises more data, it can obscure critical tail behaviour and introduce correlation between observations. In contrast, extreme events may be more nearly independent, but their scarceness increases statistical uncertainty. Effect of uncertainty is discussed in more detail in [Chapter 19.6.](section-2.15.6).

Frequently applied distribution functions for marginal distribution of significant wave height are for global data 2-parameter Weibull, 3-parameter Weibull and a hybrid lognormal plus 2-parameter Weibull distribution. For event models, 3-parameter Weibull, Gumbel and Generalized Pareto (for Peak Over Threshold) are commonly used. Local measurements should give indications which distribution type is to be preferred.

The 3-parameter Weibull distribution for variable $X$ is given as

```{math}
:label: eq-wave-2-31
F(x)=1-\exp \left\lbrace -\left(\frac{x-\gamma}{\alpha}\right)^{\beta}\right\rbrace
```

where $\alpha=$ scale parameter, $\beta=$ shape parameter, $\gamma=$ location parameter.

The Gumbel extreme value distribution is

```{math}
:label: eq-wave-2-32
F(x)=\exp \left[-e^{-\alpha(x-\beta)}\right]
```

where $\beta$ is a location parameter and $\alpha$ is a scale parameter.

The Pareto distribution ( $y=$ threshold excess values) is

```{math}
:label: eq-wave-2-33
F(y)=1-\left(1+c \frac{y}{a}\right)^{-1 / c} ; \quad \begin{array}{cc}0<y<-\frac{a}{c} & c<0 \\ 0<y<\infty & c \geq 0\end{array}
```

Following {cite}`Naess1998`, efficient parameter estimation is obtained by taking $c=0$. This means that the data are exponential distributed

```{math}
:label: eq-wave-2-34
F(y)=1-\exp (-y / a)
```

and that the extreme value distribution is of the Gumbel type.

### Joint distribution of wave height and period

Joint environmental models may often be used to approximate long-term variations of wave characteristics.

The existing joint environmental models are established by fitting distributions to data from the actual area. The Maximum Likelihood Model (MLM), {cite}`PrinceWright1995`, and the Conditional Modelling Approach (CMA), e.g. {cite}`BitnerGregersen1991`, utilize the complete probabilistic information obtained from simultaneous observations of the environmental variables. If the available information about the simultaneously occurring variables is limited to the marginal distributions and the mutual correlation, then the Nataf model can be used {cite}`DerKiureghian1986`.

In the CMA, the joint density function is defined in terms of a marginal distribution and a series of conditional density functions modelled by parametric functions that are fitted to the conditioned data by some estimation procedure.

For a given directional sector the joint model of significant wave height and spectral/zero-crossing wave period is usually approximated by a marginal distribution for significant wave height, typically the 3-parameter Weibull distribution, and the conditional lognormal distribution for spectral/zero-crossing wave period given the significant wave height

```{math}
:label: eq-wave-2-35
f_{T_{m 02} \mid H m 0}(t \mid h)=\frac{1}{\sigma_{T}(h) t \sqrt{2 \pi}} \exp \left\lbrace-\frac{\left(\ln t-\mu_{T}(h)\right)^{2}}{2 \sigma_{T}^{2}(h)}\right\rbrace
```

where a possible parameterisation is

```{math}
:label: eq-wave-2-36
\mu(h)=a_{0}+a_{1} h^{a_{2}}
```

```{math}
:label: eq-wave-2-37
\sigma(h)=b_{0}+b_{1} \exp \left\lbrace b_{2} h\right\rbrace
```

The parameters $a_{1}, a_{2}, a_{3}, b_{1}, b_{2}$ and $b_{3}$ are determined from the data.

## Extreme individual wave height and crest height

The extreme individual crest or wave height can be determined by combining short term and long term statistics. The long-term distribution of waves is obtained by combining the joint long-term distribution of sea state parameters, with the short-term distribution of sea surface elevation. Let the short term, extreme value distribution of crest $Z$ in an environmental state $\vec{\psi}$ for a short-term duration $\tau$ be denoted $F_{Z \mid \vec{\psi}}(z \mid \vec{\psi} ; \tau)$. Conditioning on the environmental state $\vec{\psi}$ may be integrated out, according to the theorem of total probability, to provide the corresponding short term, extreme value distribution for a single, random, environmental state. The extreme value distribution during an operation time $\lambda$ might then be obtained as

```{math}
:label: eq-wave-2-38
F_{E}(z ; \lambda)=\left[\int F_{Z \mid \vec{\Psi}}(z \mid \vec{\psi} ; \tau) f_{\vec{\Psi}}(\vec{\psi}) d \vec{\psi}\right]^{\lambda / \tau}
```

where $f_{\vec{\psi}}(\vec{\psi})$ is the probability density of the sea state parameters (e.g. $h_{s}$ ).

This expression is based on the multiplication rule and an assumption of independence between the crest level in each short-term state. A slightly different formulation is the following expression due to {cite}`Battjes1978`

```{math}
:label: eq-wave-2-39
F_{E}(z ; \lambda)=\left[\int \frac{v(z \mid \vec{\psi})}{\widetilde{v}(z)} F_{Z \mid \vec{\Psi}}(z \mid \vec{\psi}) f_{\vec{\Psi}}(\vec{\psi}) d \vec{\psi}\right]^{\tilde{v}(z) \lambda}
```

where $\tilde{v}(z)$ is the ensemble averaged up-crossing rate

```{math}
:label: eq-wave-2-40
\widetilde{v}(z)=\int v(z \mid \vec{\psi}) f_{\vec{\Psi}}(\vec{\psi}) d \vec{\psi}
```

Here $v(z \mid \vec{\psi})$ is the mean upcrossing rate of the underlying process through the level $z$, and $F_{z \mid \vec{\Psi}}(z \mid \vec{\psi})$ is the distribution of the random cycle amplitudes. Note the difference between the integrands in Eq. {eq}`eq-wave-2-38` and Eq. {eq}`eq-wave-2-39`, where $F_{Z \mid \vec{\psi}}(z \mid \vec{\psi} ; \tau)$ is the short term extreme value distribution, while $F_{z \mid \vec{\Psi}}(z \mid \vec{\psi})$ is the distribution of a random cycle amplitude.

As an alternative, an ensemble-averaged up-crossing approach may be used, in which the distribution function is expressed as {cite}`Naess1984`

```{math}
:label: eq-wave-2-41
F_{E}(z ; \lambda)=\exp \lbrace-\lambda \tilde{v}(z)\rbrace
```

Eqs. {eq}`eq-wave-2-38` to {eq}`eq-wave-2-41` may be applied directly in a Level 3 structural reliability analysis for modelling of the extreme crest. If the purpose is to estimate the 100 -year crest level, this quantity can be determined as the appropriate fractile of $F_{E}(z ; \lambda)$.

In applications not the extreme wave height as such may be important, but rather the maximum load effect in the structure, e.g. the bending moment in a member. In this respect reference is made to {cite}`Ditlevsen2002`.

## Wave load models

### Slender members

If the diameter of structural elements is small compared to a characteristic wavelength, the loads are calculated by the Morison formula

```{math}
:label: eq-wave-2-42
F=\rho A\left[C_{M} \dot{u}+\left(C_{M}-1\right) \ddot{x}\right]+\frac{1}{2} \rho D C_{D}(u-\dot{x})|u-\dot{x}|
```

where

$F =$ force per cylinder length in flow and motion direction   

$A  =\pi D^{2} / 4$, cross section area  

$D=$ cylinder diameter 

$\dot{x}=$   cylinder velocity  

$\ddot{x}=$   cylinder acceleration   

$u=$ water velocity perpendicular to structural member     

$\dot{u}=$ water acceleration perpendicular to structural member

$u-\dot{x}=$ relative velocity 

$C_{M}=$ inertia coefficient 

$C_{D}=$ drag coefficient 

$\rho=$ water mass density

For $u>>\dot{x}$, a useful approximation is

```{math}
:label: eq-wave-2-43
(u-\dot{x})|u-\dot{x}| \approx u|u|-2|u| \dot{x}
```

The second term provides additional damping, and if the coefficient to $\dot{x}$ is replaced by its expectation, the following form is obtained:

```{math}
:label: eq-wave-2-44
(u-\dot{x})|u-\dot{x}| \approx u|u|-\sqrt{8 / \pi} \sigma_{u} \dot{x}
```

where $\sigma_{u}$ represents the standard deviation of $u$ in a random sea.

Another linearisation schemes exist that include the effect of combined wave and current. The scheme should depend on the application (e.g. collapse versus fatigue analysis).

Assume in the following that linear wave theory can be applied and that the wave elevation $\eta(x, t)$ is a stationary Gaussian process. Then the particle velocity $u(t)$ and acceleration $\dot{u}(t)$ are also normal processes The relevant wave components $u(t)$ and $\dot{u}(t)$ then maybe considered as independent, zero-mean normal processes with standard deviations $\sigma_{u}$ and $\sigma_{\dot{u}}$. A measure of the relative importance of drag and inertia, and of the deviation from normal distribution, is

```{math}
:label: eq-wave-2-45
K=\frac{k_{D}}{k_{M}} \frac{\sigma_{u}^{2}}{\sigma_{\dot{u}}^{2}}
```

where $k_{D}=\frac{1}{2} \rho D C_{D}$ and $k_{M}=\rho A C_{M}$. In normalised form, the Morison can be expressed as the non-Gaussian process {cite}`Madsen1986`

```{math}
:label: eq-wave-2-46
Q(t)=\frac{F}{k_{M} \sigma_{\dot{u}}}=K\left(X_{u}(t)+V\right)\left|X_{u}(t)+V\right|+X_{\dot{u}}(t)
```

where $X_{u}(t)=u(t) / \sigma_{u}$ and $X_{\dot{u}}(t)=\dot{u}(t) / \sigma_{\dot{u}}$. The current velocity, inline with the waves, is $V \sigma_{u}$. The natural period of variation of the current is assumed to be so long that its time variation can be ignored for the considered time span, hence $V$ is taken as a fixed variable.

The second order statistics is characterised by the covariance matrix $C_{\vec{X}}$ of the process  
```{math}
\vec{X}(t)^{T}=\left(X_{u}(t), X_{\dot{u}}(t), \dot{X}_{\dot{u}}(t)\right)
```

```{math}
C_{\vec{X}}=\left(\begin{array}{ccc}1 & 0 & -\omega_{0} \\ 0 & 1 & 0 \\ -\omega_{0} & 0 & \omega_{0}^{2} / \alpha^{2}\end{array}\right)
```

where $\omega_{0} \equiv \sigma_{\dot{u}} / \sigma_{u}$ and $\alpha$ is a bandwidth parameter for the velocity process u(t), i.e. $\alpha=-\sigma_{\dot{u}}^{2} \sigma_{u}^{-1} \sigma_{i i}^{-1}$.

The mean $\mu_{q}$ and standard deviations $\sigma_{q}$ and $\sigma_{\dot{q}}$ of the Morison force are given as {cite}`Madsen1986`:

```{math}
:label: eq-wave-2-47
\mu_{q}  =K\left[2 V \phi(V)+\left(1+V^{2}\right)(1-2 \Phi(-V))\right] 
```

```{math}
:label: eq-wave-2-48
\sigma_{q}^{2}  =K^{2}\left(3+6 V^{2}+V^{4}\right)+1-\mu_{q}^{2} 
```

```{math}
:label: eq-wave-2-49
\sigma_{\dot{q}}^{2}  =4 K^{2}\left(1+V^{2}\right) \frac{\sigma_{\dot{u}}^{2}}{\sigma_{u}^{2}}+\frac{\sigma_{\dot{u}}^{2}}{\sigma_{\dot{u}}^{2}} 
```

Let in the following $V=0$. The probability density of the wave force $Q(t)$ is completely determined by the non-linearity factor $K$ and the variance of the force $\sigma_{q}{ }^{2}$. The kurtosis $\alpha_{4}$ gives the shape of the distribution of $Q(t)$ through the relation

```{math}
:label: eq-wave-2-50
\alpha_{4}=3+\frac{78}{\left(3+1 / K^{2}\right)^{2}}
```

For the narrow band approximation $\alpha \rightarrow 1$, the asymptotic result for the upcrossing rate is {cite}`Madsen1986`

```{math}
:label: eq-wave-2-51
v(q) \approx v_{0}^{u}\left\lbrace \begin{array}{cc}\exp \left(-\frac{1}{2} q^{2}\right), & |q|<\frac{1}{2 K} \\ \\ \exp \left[-\frac{1}{2 K}\left(q-\frac{1}{4 K}\right)\right], & |q| \geq \frac{1}{2 K}\end{array}\right.
```

where $v_{0}^{u}$ is the zero-crossing frequency of $u(t)$. In a narrow-band approximation of the force, the distribution of local maxima can be obtained by neglecting the positive minima and negative maxima. This gives the probability density function of local maxima

```{math}
:label: eq-wave-2-52
f_{m}(q) \approx-\frac{1}{v(0)} \frac{d}{d q} v(q)
```

and the asymptotic result

```{math}
:label: eq-wave-2-53
f_{m}(q) \approx\left\lbrace \begin{array}{cc}q \exp \left(-\frac{1}{2} q^{2}\right), & 0<q<\frac{1}{2 K} \\ \\ \frac{1}{2 K} \exp \left[-\frac{1}{2 K}\left(q-\frac{1}{4 K}\right)\right], & q \geq \frac{1}{2 K}\end{array}\right.
```

This density is derived in {cite}`Borgman1965`.

### Vertical walls

The water pressures $p_{1}$ and $p_{3}$ (see {numref}`fig-water-pressures-on-a-vertical-wall-due-to-pulsating-forces`) on a vertical wall due to pulsating forces (impact and breaking excluded) are given by according {cite}`Goda1985`:

```{math}
:label: eq-wave-2-54
\begin{array}{l}
p_{1} = 0.5(1+\cos \beta)\left(\lambda_{1} \alpha_{1} + \lambda_{2} \alpha_{2} \cos^{2} \beta\right) \rho g H \\
p_{3} = \alpha_{3} p_{1}
\end{array}
```

where:

$H: $ incident wave height (from trough to crest) in front of the structure;

$\beta: $  angle of wave incidence with respect to a line perpendicular to the structure;

$\rho:$ density of water;

$g:$ acceleration of gravity;

$\alpha_{1}, \alpha_{2}, \alpha_{3}:$ factors dependent on hydraulic conditions (see {eq}`eq-wave-2-56`)

$\lambda_{1}, \lambda_{2}, \lambda_{3}:$ factors dependent on the structural geometry (usually =1.0)

The pressure at the top $p_{4}$ for a given value of $R_{C}$ can be derived from:

```{math}
:label: eq-wave-2-55
\eta^{*}=0.75(1+\cos \beta) \lambda_{1} H
```

```{figure} ../part-02/images/fig-water-pressures-on-a-vertical-wall-due-to-pulsating-forces.jpg 
:name: fig-water-pressures-on-a-vertical-wall-due-to-pulsating-forces

Vertical wall on toe-structure
```

The $\alpha$-factors are given by:

```{math}
:label: eq-wave-2-56
\begin{array}{l}
\alpha_{1}=0.6+0.5\left(\frac{4 \pi h / L}{\sinh (4 \pi h / L)}\right)^{2} \\ \\
\alpha_{2}=\min \left(\frac{\left(h_{b}-d\right)}{3 h_{b}}\left(\frac{H}{d}\right)^{2}, \frac{2 d}{H}\right) \\ \\
\alpha_{3}=1-\left(\frac{h^{\prime}}{h}\right)\left(1-\frac{1}{\cosh (2 \pi h / L)}\right)
\end{array}
```

where

$L:$ wave length;

$h^{\prime}:$ water depth at the toe of the front wall $=\left(d+d_{c}\right)$

$h:$ water depth in front of the structure;

$h_{b}:$ water depth at a distance of 5 times the significant wave height.

$d:$ water depth at top of protection blocks

$d_{c}:$ thickness of protection block layer

### Volume members

For large-volume structures (i.e., structures for which a characteristic diameter is comparable to the wavelength), the hydrodynamic loads have to be determined by means of diffraction theory. An overview of the existing diffraction methods is given in ISSC (1991,2000). The diffraction theory is based on potential theory and viscous effects are neglected.

Usually, a linear diffraction analysis will have a sufficient accuracy, such that the load process becomes a linear function of the wave process. Non-linear diffraction theory should be used for shallow water structures, for structures situated in arctic areas with the presence of ice, for structures for which slow drift effects are important, and for calculation of springing response of a TLP. Forces in the splash zone are not adequately described by linear waves. This effect may, however, be accounted for by various stretching techniques without adhering to the full non-linear theory.

The second order hydrodynamic load effects may in many cases be important for the design of large volume structures. These effects may be:

- When a linear regular first order wave is interacting with itself and an ocean platform.
- For irregular sea the resulting second order exciting forces contain three components: the mean forces (drift forces), forces varying in time with the difference frequencies of the wave spectrum (often called slow drift forces) and with the sum frequencies of the wave spectrum (high frequency forces).
- The difference frequency forces may in particular be important for design of mooring and dynamic positioning of offshore structures as well as for offshore loading systems.

A variety of perturbation-based frequency and time domain methods are presented in the literature

Superposing $N$ waves with amplitudes $a_{j}$, frequency $\omega_{j}$ and phase $\varepsilon_{j}, j=1, \ldots, N$

```{math}
:label: eq-wave-2-54-a
\eta^{(1)}(t)=\operatorname{Re} \sum_{j=1}^{N} a_{j} e^{i\left(\omega_{j} t+\varepsilon_{j}\right)}
```

the force (to second order) can be expressed as

```{math}
:label: eq-wave-2-55-a
F_{D}(t)=F_{D}{ }^{(1)}(t)+F_{D}{ }^{(2)}(t)
```

where

```{math}
:label: eq-wave-2-56-a
F_{D}^{(1)}(t)=\operatorname{Re} \sum_{j=1}^{N} a_{j} F^{(1)}\left(\omega_{k}\right) e^{i\left(\omega_{j} t+\varepsilon_{j}\right)} 
```

```{math}
:label: eq-wave-2-57
F_{D}{ }^{(2)}(t)=\operatorname{Re} \sum_{k=1}^{N} \sum_{j=1}^{N} a_{j} a_{k}\left[F_{+}^{(2)}\left(\omega_{j}, \omega_{k}\right) e^{i\left(\left(\omega_{j}+\omega_{k}\right) t+\varepsilon_{j}+\varepsilon_{k}\right)}+F_{-}^{(2)}\left(\omega_{j}, \omega_{k}\right) e^{i\left(\left(\omega_{j}-\omega_{k}\right) t+\varepsilon_{j}-\varepsilon_{k}\right)}\right]
```

where $F^{(1)}$ is the linear transfer function (LTF) and $F_{+}^{(2)}, F_{-}^{(2)}$ are sum- and differencefrequency force quadratic transfer functions (QTF). Response transfer functions, $H^{(1)}, H_{+}^{(2)}, H_{-}^{(2)}$, corresponding to the force transfer functions, are found by solving the simultaneous linear equations of structural motions in 6 degrees of freedom.

Response quantities of interest include both extreme values and fatigue damage. In the following a simplified statistics in terms of four statistical moments is given.

The response $x(t)$ is expressed in terms of standard normal processes $u_{i}(t)$ that are independent at fixed $t$ :

```{math}
:label: eq-wave-2-58
x(t)=\sum_{i} c_{i} u_{i}(t)+\sum_{i} \lambda_{i} u_{i}^{2}(t)
```

The coefficients $\lambda_{i}$ are eigen values of the integral equation {cite}`KacSiegert1947`

```{math}
:label: eq-wave-2-59
\int_{-\infty}^{\infty} \Gamma\left(\omega_{1}, \omega_{2}\right) \Phi\left(\omega_{2}\right) d \omega_{2}=\lambda \Phi\left(\omega_{1}\right)
```

in which $\Gamma\left(\omega_{1}, \omega_{2}\right)=H_{+}^{(2)}\left(\omega_{1},-\omega_{2}\right) \sqrt{S\left(\left|\omega_{1}\right|\right) S\left(\left|\omega_{2}\right|\right)} / 2$. The first order coefficient is next determined as

```{math}
:label: eq-wave-2-60
c_{i}=\int_{-\infty}^{\infty} H_{1}(\omega)[S(|\omega|)]^{1 / 2} \Phi_{i}^{*}(\omega) d \omega
```

The moments follow by algebra as

```{math}
:label: eq-wave-2-61
\mu_{x}=\sum_{i} \lambda_{i}
```

```{math}
:label: eq-wave-2-62
\sigma_{x}^{2}=\sum_{i} c_{i}^{2}+2 \lambda_{i}^{2}
```

```{math}
:label: eq-wave-2-63
\alpha_{3 x}=\sum_{i}\left(6 c_{i}^{2} \lambda_{i}+8 \lambda_{i}^{3}\right) / \sigma_{x}^{3}
```

```{math}
:label: eq-wave-2-64
\alpha_{4 x}=3+\sum_{i} 48 \lambda_{i}^{2}\left(c_{i}^{2}+\lambda_{i}^{2}\right) / \sigma_{x}^{4}
```

E.g., by a Hermite transformation, these moments can be used to model the nonGaussian response process {cite}`Winterstein1991`.

The Gaussian model is approached either if the $\lambda_{i}{ }^{\prime} s$ become small relative to the $c_{i}{ }^{\prime} s$, or when the number of significant $\lambda_{i}$ terms grows.

This second order model has been used also for the slow drift problem (see e.g. {cite}`Naess1984`, {cite}`Naess1985`).

### Slamming loads

Slamming loads in platform decks are important design consideration. Because of non-linear diffraction effects there is still no reliable method for assessing the loads.

In simplified 2D cases a generalised Wagner solution seems to describe the water entry loads. The water exit loads are, however, not properly described.

Impact forces associated with a slam induced whipping response can be reasonably predicted by 2D and 3D methods. However, some of the rigorous treatments that are available are CPU time consuming.

For ships with non-vertical hull-sides in high waves, slamming loads are important. The dominating force is the added mass force. A state-of-the-art review of studies on slamming, including theories, numerical methods, elastic responses due to impact loads and stochastic modelling, is given by {cite}`MizoguchiTanizawa1996`.

Ship hull vibrations are often due to propeller cavitation.

(section-2.15.6)=
## Uncertainties

**Models for random variables**

{numref}`table-wave-load--asic-variables-and-probabilistic-models` presents a list of variables that could be considered as uncertain within a probabilistic wave load analysis. For every variable suggestions are presented for the probabilistic modelling. In most cases these suggestions are based on what is presented in the literature by various authors, sometimes on the basis of observations and data, sometimes only for use in example calculations. As a result, the background of the values given may differ substantially from one random variable to another.

In {numref}`table-wave-load--asic-variables-and-probabilistic-models` mean values are often presented as to the nominal value or the locally measured value. The scatter, introduced as a coefficient of $V$, may also depend heavily on local circumstances. The designation of the distribution type, is clarified at the bottom of the table. For variables which are defined per member or per joint, the value of $\rho_{i j}$ indicates the coefficient of correlation between members. For the interpretation of $\rho_{i j}$ it is convenient to have the following relationship:

```{math}
\rho_{i j}=1-\left(V_{\text {int }} / V\right)^{2}{4}
```

$V_{int}=$ member to member variability

$V=$ total uncertainty

As an example, let the member to member variability for the yield stress within one structure be equal to $V_{\text {int }}=0.4$. The total uncertainty is about $V=0.8$. So:

```{math}
\rho_{i j}=1-(0.4 / 0.8)^{2}=0.75
```

In many practical calculations, values close to 0.0 or 1.0 should be rounded off.

In cases where little data is available, statistical parameters suffer seriously from "statistical uncertainty". The most important statistical uncertainty concerns the uncertainty in the mean, which can be translated into an increased coefficient of variation. The coefficients of variation given in the Table should be considered as including this statistical uncertainty.

**Some detailed comments to {numref}`table-wave-load--asic-variables-and-probabilistic-models`**

**Waves**

The most important load parameter is the sea elevation $\eta$, which can be considered as a zero mean piece-wise stationary Gaussion process. The parameters describing the spectra depend on the site location. When elaborating the parameters for a special case, however, it is recommended that one should take into account the statistical uncertainty due to the limited number of data, the effect of measurement errors and the difference in location between the measurement site and the construction site.

```{table} Basic variables and probabilistic models
:name: table-wave-load--asic-variables-and-probabilistic-models
| $\boldsymbol{X}$ | Designation | $\mu$ | $\mathbf{V}$ | Dist type | $\rho_{i j}$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
|  | Measurement $H_{s}$ | nom | 0.10 | - | - |
| $H_{s}$ | Significant wave height | Local | Local | $W/L$ | - |
| $T_{z} \mid H_{s}$ | Mean period for given $H_{s}$ | Local | Local | $L/N$ | - |
| $\phi_{s}$ | Mean wave direction | Local | Local | Local | - |
| $T_{d}$ | Duration of sea state | 3-6 hrs | 1.0 | $E$ | - |
| $H_{\max } \mid H_{s}$ | Max wave in given sea state | Calculation | Local | $G$ | - |
| $\theta_{w}$ | Wave model | Depends | 0.05 - 0.3 | - | - |
| $\theta_{M G}$ | Marine growth model | 1 | 0.2 - 0.5 | $W$ | 0.9 |
| $C_{D}$ | Drag force coefficient | 0.6 - 1.3 | 0.2 - 0.3 | $L$ | 0.9 |
| $C_{M}$ | Inertia force coefficient | 1.6 - 2.5 | 0.10 - 0.15 | $L$ | 0.9 |
| $p_{1}$ | Horizontal pressure on wall | 0.90 | 0.20 | $L$ | - |
|  | Moment due to horizontal <br> pressure on wall | 0.81 | 0.37 | $L$ | - |
| $p_{4}$ | Uplift pressure | 0.77 | 0.20 | $L$ | - |
|  | Moment due to uplift pressure | 0.72 | 0.34 | $L$ | - |
```

$\theta_{X}=$ model uncertainty of $X, \rho_{i j}=$ correlation between members, $N=$ normal, $L=$ lognormal, $E=$ exponential, $W=$ Weibull, $G=$ Gumbel

There is no generally valid one-to-one relationship between the visual wave height and the significant wave height (instrumentally measured), or between the visual wave period and zero-crossing wave period (instrumentally measured). Thus, usually correction factors should be applied to the visual observations, see for example {cite}`BitnerGregersen1990`.

The Global Wave Statistics (GWS) visual observations of wave climate, see {cite}`BritishMaritime1986`, represent the only truly global set of wave data with a sufficiently long observation history to give reliable global climatic statistics. {cite}`BritishMaritime1986` states that it should not be necessary to apply any correction factors, usually used for estimating wave height and wave period from visual observations. However, the accuracy of the data is still questioned in the literature. The GWS data should be used with care, and if possible they should be checked against available instrumental or hindcast data for considered areas. For the North Pacific, the visual wave observations owing to {cite}`Watanabe1992` are probably of higher accuracy than the Global Wave Statistics data. The Global Wave Statistics data were collected from ships whose density of traffic in the North Pacific area was rather low.

The World Meteorological Organisation's accuracy requirements for waves, in terms of $95 \%$ confidence interval limits, are {cite}`WMO1983`: $\pm 20 \%$ for significant wave height and $\pm 1.0 ~s$ for the average wave period. However, the accuracy of the actual wave data may be widely varying and is very much related to the observation mode.

The instrumental accuracy depends on the type of instrument used. A study by {cite}`Hasselman1973` shows that properly calibrated instruments are in general equally accurate. Wave buoys are regarded as being highly accurate instruments, and error in the estimated significant wave height due to imperfections of the wave buoys may be considered as negligible for most sea states, {cite}`SteelEarle1979`, {cite}`Monaldo1988`. During the severe sea conditions, the buoy may be drawn through the crest of wave, causing a smoothing effect in the recorded data. In the presence of a strong surface current, the buoy will most likely underestimate high wave heights. External forces on the buoy (e.g., breaking waves, mooring) may cause violent accelerations, that will lead to overestimation of the waves. These uncertainties are difficult to quantify.

In steep waves, the differences between sea surface oscillations recorded by a fixed (Eulerian) probe or laser, and those obtained by a free-floating (Lagrangian) buoy can be very marked. Reference is made to, Vartdal et al. (1989), {cite}`MarthinsenWinterstein1992`. Thus the wave buoy data should not be used for estimation of wave profiles in steep waves.

Platform mounted wave gages and other wave sensing devices have the advantage that they measure directly sea surface displacement rather than the acceleration as the buoys. For accuracy of the platform data see e.g. {cite}`Cardone1995`.

Several investigations carried out in the last years indicate very promising results that support use of the satellite data. {cite}`Carter1992` demonstrated that over the range of wave heights 1m - 8m satellite altimeter derived significant wave heights were nearly as accurate as the ones obtained from surface buoy measurements. {cite}`Cooper1995` have shown that the satellite data are suitable for analysing ocean areas dominated by large storms or monsoon flows (accuracy: $COV=10 \%$ ).

Modelled wave data are produced operationally by major national meteorological services and are filed by the data centers. The accuracy of these data may vary and depends strongly on the hindcast models applied to generate the data as well as the adopted wind field. To allow hindcast data to be used, the underlying hindcast models must be calibrated with measured data.

As noted above neither measurements nor wave models can be entirely relied upon to provide unbiased and error-free estimates under all conditions. The best way of providing a reliable metocean database is to make use of both measurements and model data, and to quantify uncertainties related to them. Generally, the offshore industry regards the instrumentally measured data always superior to model derived data, and recommends to use them for evaluating the design and operational criteria. Note that for instrumentally recorded wave data sampling variability due to a limited registration time constitutes a significant part of the random errors.

For the JONSWAP and Pierson-Moskowitz spectrum the sampling variability coefficient of variation of the significant wave height and zero-crossing wave period are approximately $4-6 \%$ and $1.5-2.5 \%$ respectively.

An unbiased noise in the measurement system will increase the measured $H_{S}$. This sampling variability leads to extrapolations of extreme wave heights and periods that are biased. A review of data from 17 storms at Forties carried out by {cite}`Earle1982` indicates that the storm-peak significant wave heights determined from a single 17 -minute record every three hours are biased by about $6 \%$, relative to threehour-average values.

**Long-term Description**

The following epistemic uncertainties are related to the long-term description: data uncertainty (instrumental/hindcast/forecast errors, sampling variability due to limited registration time of sea states), statistical uncertainty (due to limited long-term sample, fitting technique applied) and modelling uncertainty (due to choice of the statistical model, the effects of clustering, climatic uncertainty, fitting technique). Experience shows that the long-term wave description is sensitive to almost all types of uncertainties, even though their relative contribution to the response/structure reliability analysis may be different for various applications and various response calculation procedures.

While both data uncertainty and statistical uncertainty is possible to quantify, and in some cases to eliminate, specification of model uncertainty is still difficult, especially as a theoretical basis for the probabilistic/deterministic models involved in the longterm description is most probably out of reach. However, it is possible to identify differences between predictions of different models, which can be used to give an idea of the model uncertainties involved. Lacking information, it is advisable to use information from various models in order to minimise the risk of wrong predictions, as suggested in {cite}`GuedesSoares1989`.

The global approach utilising all data from long series of regular observations introduces correlation among observations (e.g. clustering), and may obscure critical tail behaviour. However, the method is less sensitive to uncertainties in the few largest data points. In the alternative Peak Over Threshold method extreme observations may be nearly independent, but their scarceness increases the statistical uncertainty relative to the global approach. The method is also more sensitive to errors in the few highest data points. There is no general agreement on whether the global approach or the event method should be used. A choice between the methods should depend on the data set at hand as well as the application considered. However, for fatigue calculations for steel or steel welds all data should generally be preferred. Further, for extreme value analysis there are reasons for favouring event models (Winterstein et al., 2001).

Sampling variability of measured wave data (due to registration time = 1024s and 3- hour spacing interval) will lead to a positive bias in long-term period extreme wave heights estimated either directly from measurements or from hindcast data calibrated with measurements, see {cite}`Heideman1994`. Further, as shown by {cite}`Heideman1995` the $H_{s}$ distribution function is clearly negatively biased for storms with shorter duration and greater intervals between samples, and positively biased for storms with greater duration and more frequent samples. The bias in 100 -year Hs for 1-hour spacing and 3-hour spacing is not negligible. Furthermore, as demonstrated by {cite}`Heideman1995`, uncertainty in design criteria increases rapidly as the data record length decreases below that which is required to achieve an acceptable COV of, say, 0.1 . Too short record has to be compensated by adopting more expensive safety margins by a designer. Thus it may be more desirable to have record with some uncertainty in the accuracy of the data than to have a very short data record of perfect accuracy.

Climatic uncertainty appears when the observed data are obtained from a time interval that is not fully representative for the long-term variations of the environmental conditions. This may result in overestimation or underestimation of the design/operational wave. The database needs to cover at least 20 years of preferably 30 years or more in order to account for climatic variability. In regions where the predominating storm type is a hurricane, and the frequency of occurrence of extreme hurricanes at a site is low (such as in the Gulf of Mexico), the uncertainty in the 100year wave height might not reach a "comfortable" level until the data base coverage actually approaches 100 years, see {cite}`Heideman1994`.

In establishing very large data bases of wave data, there is the danger of joining in a sample data from different populations. {cite}`GuedesSoaresNolasco1992` examined the case of single peaked sea states being pooled with combined ones, while {cite}`GuedesSoaresHenriques1996` looked at the seasonal variability of the data and {cite}`GuedesSoaresFerreira1995` studied the yearly variability of the data. The latter showed that the application of strict statistical criteria defining samples and population would not support pooling together data from different years. In fact, an explanation model was developed based on the concept of sampling from random populations.

There is no industry consensus on how to apply directional criteria in design. Usually the length of the data record is too short to provide a proper directional description of waves. Therefore directional criteria exist only for a few discrete, large directional sectors and they use to be biased. As recommended by {cite}`Forristal1995`, directional effects need to be included in the reliability analysis with some care. A recent directional model is published by {cite}`SterndorffSorensen2001`.

Further studies quantifying relative importance of different types of uncertainties for short-term and long-term wave prediction are also called for.

**Wave models**

All uncertainties related to wave models should where possible be quantified and accounted for when specifying design and operational conditions. The numbers depend on type of application and circumstances.

**Wave loads**

The values of the coefficients $C_{M}$ and $C_{D}$ are a source of model uncertainty. For common structural cross sections, typical values of $C_{D}$ are found in the range between 0.6 and 1.3. Similarly, typical values of $C_{M}$ are found in the range between 1.6 to 2.5 .

The drag coefficient $C_{D}$ is a function of Reynolds number. The inertia coefficient $C_{M}$ can in many cases be evaluated theoretically, as the inertia force is essentially the same force as that evaluated by integrating the pressure over the cylinder surface in a velocity potential representation. Different values of the drag coefficient $C_{D}$ and the inertia coefficient $C_{M}$ below and above sea water level should be considered because of marine growth.

In the reliability analysis it is recommended to adopt $C_{M}$ as a lognormally distributed variable with $C O V=0.10$, and $C_{D}$ as a lognormally distributed variable with $C O V=0.20-0.30$, {cite}`HaringSpencer1979`, {cite}`Dean1979`.

The model uncertainties of the Goda formula (last four lines) have been studied by {cite}`VanDerMeer1994`.

**References**

```{bibliography}
:filter: docname in docnames
```

**Additional References**

Arhan, M. and R. Ezraty (1978), "Statistical Relations Between Successive Wave Heights”, Acta Oceanologica, 1, 151-158.

Battjes, J. A. (1978), "Engineering Aspects of Ocean Waves and Currents", Seminar on Safety of Structures under Dynamic Loading, Trondheim, Norway.

Belverova, D. (1994), "Wind Waves”, PhD, Polish Academy of Sciences, Gdansk.

Borgman, L.E. (1979), "Directional Wave Spectra from Wave Sensors", Ocean Wave Climate, Plenum, New York, pp. 269-300

Buoy-altimeter Comparisons”, J. Geophys., pp. 2285-2302

Takahashi, S (1996): Design of vertical breakwaters. Port and Harbour Research Institute



