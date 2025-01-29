# Annex B: Durability

## Probabilistic Formulations

Loads as well as material properties may vary in time as stationary or non-stationary
processes. Time may also be present in the limit state function as an explicit parameter. As a result, the failure probability of a structure is also time dependent. The general formulation for the failure probability for a period of time t may be presented as:

```{math}
:label: eqB1
P_{F}(t)=P[\min g(\mathbf{x}(\tau) ; \tau)<0 \text { for } 0<\tau<t]
```

$g(.)$ = limit state function

$\mathbf{x}(\tau)$ = vector of basic variable at time $\tau$

$t$ = period of time under consideration

$\tau$ = time

The failure may be of ULS as well as SLS type. One should keep in mind that also in the case of a non-deteriorating time independent resistance and a stationary loading condition, the failure probability is also time dependent due to the random fluctuations of the load. This, however, is usually not considered as a durability problem.

Given {eq}`eqB1`, the conditional failure rate (also referred to as risk functions) at time t may be found as:

```{math}
:label: eqB2
r(t)=\frac{P(\text { failure in }[t, t+\Delta t] \mid \text { survival up } t)}{\Delta t}=\frac{p_{F}(t)}{1-P_{F}(t)}
```

where,

```{math}
:label: eqB3
p_F(t) = \frac{dP_F(t)}{dt}
```

is the failure time density. For small values of $t$, the failure probability $P_F( t )$ is close to zero, which makes the conditional failure rate and the density almost numerically equal. For durability problems, the conditional failure rate is usually increasing in time. Reliability limits set in [section 7](../part-01/target-reliability.md) may be related to {eq}`eqB2` or {eq}`eqB3` whichever is appropriate.

If failure of a structural element leads automatically to replacement by a similar element, one may alternatively use the renewal density $h$, defined as;

```{math}
:label: eqB4
h(t)=\frac{\sum_{n=1}^{\infty} P(\text { failure of element number } n \text { in }[t, t+\Delta t])}{\Delta t}
```

For small $t$ the result will be equal to {eq}`eqB2` and {eq}`eqB3`. For large $t$ the value of $h$ will asymptotically lead to $1/μ$ and where $μ$ is the mean time to failure, defined as:

```{math}
:label: eqB5
\mu = \int_{0}^{\infty} t\ \ p_{F}(t) dt = \int_{0}^{\infty} (1 - P_{F}(t)) dt
```

The calculation procedure for $P_F(t)$ depends on the nature of the limit state function $g(.)$. If $g(.)$ is a smooth monotonically decreasing function not depending explicitly on random process variables, the minimum value is reached at the end of the period, and we simply have:

```{math}
:label: eqB6
P_{F}(t)=P[g(\mathbf{x} ; t)<0]
```

If $g(.)$ depends on random process variables and, therefore, is not monotonically decreasing, we have a first passage problem. In that case the following upper bound approximation may be useful:

```{math}
:label: eqB7
P_F(t)=P_F(0)+\int_{0}^{t}v^{-}(\tau) d \tau
```

where $P_F(0)$ is the failure at the start and ${v^{-}}$ the outcrossing rate or unconditional failure rate which is given by:

```{math}
:label: eqB8
v^{-}(\tau)=\frac{P[g(\tau)>0 \cap g(\tau+\Delta \tau)<0]}{\Delta \tau}
```

In general, the limit state function $g(.)$ may be quite complex due to a combination of physical, chemical and mechanical processes. Take as an example the deterioration processes due to carbonation and/or chloride ingress of concrete. After some period of time the carbonation or chloride fronts may reach the reinforcement and corrosion may start, resulting eventually in spalling and later even in failure by collapse due to some large mechanical load (see {numref}`fig-Failure-due-to-a-combination-of-physical-and-chemical-processes-and-a-variable-mechanical-load`). Many parameters like the outside climate, the cover of the concrete, the diffusion properties, the corrosion speed and so on may play a role.

```{figure} ../part-01/images/Failure-due-to-a-combination-of-physical-and-chemical-processes-and-a-variable-mechanical-load.jpg
:name: fig-Failure-due-to-a-combination-of-physical-and-chemical-processes-and-a-variable-mechanical-load

Failure due to a combination of physical and chemical processes and a variable mechanical load.
```

## Modelling of deterioration processes

In this Annex we will restrict the discussion to a family of relatively simple damage
accumulation processes that can be described by the following differential equation:

```{math}
:label: eqB9
\frac{dy}{dt}=y^{k}  h(z)
```

where

```{math}
\begin{aligned}
& y(t)=\text { damage indicator } \\
& z(t)=\text { random process of disturbances } \\
& h(.)=\text { positive definite function of } z \\
& k=\text { parameter determining the nature of the process }
\end{aligned}
```

From {eq}`eqB9` we may arrive at:

```{math}
:label: eqB10
\int_{y(0)}^{y(t)} y^{-k} dy=\int_{0}^{t} ~h(z(\tau)) d \tau
```

Defining $\Psi(y)$ as the integral function of $y^{-k}$ and $\chi(t)$ as the right hand side integral of {eq}`eqB10`, this can be written as:

$$
\Psi(y(t))-\Psi(y(0))=\chi(t)
$$

If $z(t)$ is stationary and ergodic, $\chi(t)$ may asymptotically be taken as implying that the damage increases smoothly:

```{math}
:label: eqB11
\chi(t)=t E\lbrace h(z(t))\rbrace
```

Failure will occur if the damage $y(t)$ exceeds some critical value $y_{cr}$, which leads finally to the following expression for the limit state function:

```{math}
:label: eqB12
g(t)=\Psi\left(y_{cr}(t)\right)-\Psi(y(0))-\chi(t)
```


The critical value $y_{c r}$ may be a constant or time dependent. If $y_{c r}$ is a constant we may use {eq}`eqB3`, to find the failure probability. If $y_{cr}$ is time dependent we have a first passage problem.

$\underline{\text {Characteristic examples}}$

1. *Abrasion / corrosion modelling* 

    Abrasion and/or corrosion mechanisms can be modelled by $k$=0 and $h(z)=z$. In that case {eq}`eqB9` reduces to:

    $$
    \frac{dy}{dt}=z(t)
    $$

    For abrasion or corrosion the damage parameter $y$ corresponds to the thickness of the lost material and $z$ represents the abrasion or corrosion rate. In this case $Psi$ is simple equal to y itself. Assuming that $z(t)$ is a stationary and ergodic random process with mean $z$, we may use {eq}`eqB12` and arrive at:

    $$
    g(t)=y_{cr}-y_{o}-\mu_{z} t
    $$

    The value $y_{o}$ may be 0 (or random) and the critical value of $y_{c r}$ may be related to the load and material strength, for instance:

    ```{math}
    y_{cr} = d_{o} - S / f
    ```

    where $d_{o}$ is the original material thickness, $S$ the load per unit length and $f$ the material rupture strenght. It can easily be seen that $y_{cr}$ is constant in time for a constant load $S$ and that $y_{cr}$ is time dependent for a fluctuating load.

2. *Duration of load*

    We consider again the case $n=0$ and $h(z)=z$. Let now, however, $y$ represent the relative reduction of the material strength $R$, that is $R(t)=R_{o}(1-y)$. Let further the disturbance $z$ be proportional to the mechanical load $S$. In other words: the presence of a load will lead to a damage or strength reduction, and more if the load is higher. Such a model can be used to represent duration of load effects. If we define $z=S / S_{o}$, with $S_{o}$ some random material parameter, we arrive at:

    $$
    g(t)=y_{c r}-y_{o}-\mu_{S} ~t / S_{o}
    $$

    Let $y_{o}=0$ and let $y_{cr}$ correspond to $R(t)=R_{o}\left(1-y_{cr}\right)=S(t)$, we arrive finally at:

    $$
    g(t)=\left(1-\mu_{S} ~t / S_{o}\right)-S(t) / R_{o}
    $$

    or equivalently:

    $$
    g(t)=R_{o}\left(1-\mu_{S} ~t / S_{o}\right)-S(t)
    $$

    Again, if $S$ is a constant load we may use {eq}`eqB6`; if not we have a first passage problem. The resulting time dependent strength for a constant load $S$ is presented in {numref}`Time-dependent-strength-for-constant-load`.

    ```{figure} ../part-01/images/Time-dependent-strength-for-constant-load.jpg
    :name: Time-dependent-strength-for-constant-load

    Load duration dependent strength under constant load
    ```

3. *Fatigue Crack Propagation*

    Due to load fluctuations some initial small crack in a structure may grow and weaken the cross section. Finally some large load amplitude may lead to collapse of the structural element (see {numref}`Fatigue-fracture-under-cyclic-loading`). The differential equation for the crack growth a is given by:

    $$
    \frac{da}{dn}=C ~Y(a)\left[\Delta S(n) \sqrt{\pi a}\right]^{m}
    $$

    Where $\Delta S$ represents the stress range, $Y(a)$ represents a geometrical function, $C$ and $m$ are material constants and $n$ is the stress cycle number. Note that in this example the time $t$ has been replaced by the load cycle number $n$ and that $k$ in {eq}`eqB5` corresponds to $m/2$. The functions $\Psi$ and $\chi$ are then given by (assuming $\Delta S$ to be stationary and ergodic):

    ```{math}
    \begin{aligned}
    & \Psi=\frac{2}{2-m} \frac{1}{C Y} \pi^{--m / 2} ~p^{-m / 2} ~a^{1-m / 2} \\
    \\
    & \chi=nE\left\lbrace (\Delta S)^{m_{m}}\right\rbrace
    \end{aligned}
    ```

    And the limit state function is given by:

    $$ g (t) = \Psi(a_{\text{cr}}) - \Psi(a_0) - \chi $$


    where $a_{0}$ is the initial crack length and $a_{cr}$ the critical crack length, which again may be time dependent or time independent. In the fist case {eq}`eqB6` may be used, in the second case we have a first passage problem.

    Alternatively, one may formulate the limit state function in the crack domain:

    $$
    g(t)=a_{cr}-a(n) \quad \quad \text { with } ~a(n) = \left\lbrace {a_o}^{1-m/2} + \frac{2}{2-m} C~Y \pi^{m/2}~nE \left\lbrace \Delta s^m \right\rbrace \right\rbrace
    $$

    or in the time domain:

    $$
    g(t)=N - n \quad \quad \text{with} ~N= \frac{\psi(a_{cr}) -\psi(a_{o})}{E \left\lbrace (\Delta S)^m \right\rbrace}
    $$

    These alternative formulations are fully equivalent to the first one.

    ```{figure} ../part-01/images/Fatigue-fracture-under-cyclic-loading.jpg
    :name: Fatigue-fracture-under-cyclic-loading

    Fatigue fracture under cyclic loading
    ```

## Effect of inspection

In the case of deteriorating processes it may be uneconomic to design a structure in such a way that the reliability is sufficient for a normal design life of 50 years. In those cases a more economical solution can be obtained by the definition of an inspection scheme. In those cases failure will not occur if the inspection reveals some predefined deterioration criterion and the structure is repaired adequately.

The sequence of events can be represented in an event tree as indicated in {numref}`Event-tree-representation-of-an-inspected-component`. Let the first inspection $I_{i}$ be planned at time $t_{i}$. In that case we may have three possibilities.

1) a failure occurs before $t_{i}$ (branche $F$ )
2) the inspection detects a serious defect and repair is necessary (branche $R$)
3) no serious defect is detected and a next inspection at $t=t_{2}$ is planned

If the structure is repaired, one may usually assume that all variables are reset to the initial situation. From every event $R$ then a new event tree of the same type as the one in {numref}`Event-tree-representation-of-an-inspected-component` is started.

For reasons of simplicity we will start by having one inspection only. Using the total probability theorem, the probability of failure for a period $t$ may then formally be written as:

```{math}
:label: eqB13
P_{F}(t)=P\left[F \mid Z_{i}>0\right] ~P(Z_{i}>0) + P\left[F \mid Z_{i}<0\right] ~P(Z_{i}<0)
```

where

$F \quad=$ failure

$Z_{i} \quad=$ inspection result of inspection at time $t_{i}$ (negative values correspond to the detection of damage)

If we assume that in the case of a serious damage revealed at the inspection (that is $Z<0$ ) the structure will be repaired adequately, {eq}`eqB13` may be reduced to (replacing $F$ by $\min _{\tau} g(\tau)<0$, where $g(~)$ is the limit state function and $0<\tau<t$) :

$$
P_{F}(t)=P\left[min_{\tau}~g(\tau)<0 \mid Z_{i}>0\right] P\left(Z_{i}>0\right)
$$

or simply:

$$
P_{F}(t)=P\left[min_{\tau}~g(\tau)<0 ~\cap~ Z_{i}>0\right]
$$

If more inspections in fixed intervals are present we arrive at:

```{math}
:label: eqB14
P_{F}(t)=P\left[min_{\tau}~g(x(\tau) ;\tau)<0~~\cap~~\left\lbrace \cap Z_i (\mathbf{x}(t_i);t_i)\right\rbrace > 0 ~\text{for}~0<\tau<t \right]
```


$\mathrm{t}_{\mathrm{i}}=$ time of inspection; only inspections with $\mathrm{t}_{\mathrm{i}}<\tau$ are relevant

Note: whether or not an inspection is planned, of course, is a matter of economy.

## Example

{numref}`Fatigue-failure-between-time-interval` clarifies formula {eq}`eqB14` for the case of fatigue. As discussed before, the g-function for the situation at the load cycle at time $\tau` is given by:

$$
g=a_{c r}-a(t)
$$

Let the crack $a(\tau)$ be monitored by a yearly inspection. If the measured crack $a_{m}$ is larger that some limit $a_{lim}$ the structure will be adequately repaired. An inspection failure may then be modelled as $Z_{\text {ins }}<0$ with:

```{math}
Z_{\text {ins }}=a_{\lim }-a_{m}\left(t_{i}\right)
```

In present practice $a_{\lim }$ usually corresponds to the detection limit and the probability distribution for $a_{\lim }$ is then equal to the so called POD-curve (probability of detection).

Failure will occur only if the measured value $a_{m}\left(t_{ins}\right)$ is below the limit value $a_{lim}$ at inspection $t_{i}$ but above the $a_{crit}$ before the next inspection. This way failure probability can be reduced by shorter inspection intervals or by more refined or accurate inspection techniques.

Note that an implication of this method is that these Probability of Detection curves (POD curves) and measurement accuracies must be known to the designer in order to decide whether or not a certain structure meets the reliability requirements. Note further that the probability of repair is given by:

$$
\mathrm{P}=\mathrm{P}\left[\mathrm{Z}_{\text {ins }}<0\right]
$$

Repair may be considered like some serviceability limit state. The designer should also make sure that the probability of repair is below some economic limit value.

```{figure} ../part-01/images/Event-tree-representation-of-an-inspected-component.jpg
:name: Event-tree-representation-of-an-inspected-component

Event tree representation of an inspected component: $R=$ Repair or maintenance action; $F=$ Failure, $I_{i}=$ Inspection at time $t_{i}$
```

```{figure} ../part-01/images/Fatigue-failure-between-time-interval.jpg
:name: Fatigue-failure-between-time-interval

Fatigue failure in the interval $t_{i}, t_{i}+\Delta t_{i}$ with $a(\tau)<a_{lim}$ at the beginning of the interval.
```










