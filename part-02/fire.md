# Fire

**List of symbols:**

$\mathrm{A}_{\mathrm{f}}=$ floor area

$\mathrm{A}_{\mathrm{i}}=$ area of the vertical opening $\mathrm{i}$ in the fire compartment $\left[\mathrm{m}^{2}\right]$

$\mathrm{A}_{\mathrm{t}}=$ total internal surface area

$\mathrm{f}=$ ventilation opening

$\mathrm{H}_{\mathrm{i}}$ = specific combustible energy for material $\mathrm{i}$

$\mathrm{m}_{\mathrm{i}}=$ derating factor between 0 and 1 , describing the degree of combustion

$\mathrm{M}_{\mathrm{ki}}=$ combustible mass present at $\Delta \mathrm{A}$ for material $\mathrm{i}$

$\mathrm{q}_{\mathrm{o}}=$ fire load density per unit floor area

$\mathrm{t}=$ time

$\mathrm{t}_{\mathrm{eq}}=$ equivalent time of fire duration

$\alpha=$ parameter

$\beta_{\mathrm{f}}=$ coefficient (model uncertainty)

$\theta=$ temperature in the compartment

$\theta_{0}=$ temperature at the start of the fire

$\theta_{\mathrm{A}}=$ parameter

## Fire ignition model

The probability of a fire starting in a given building or area is modelled as a Poisson process with constant occurrence rate:

```{math}
:label: eq-fire-2.20.1
\mathrm{P} \left\lbrace \text{ignition in} (\mathrm{t}, \mathrm{t}+\mathrm{dt}) \text{in a compartment} \right\rbrace = \mathrm{v}_{\text {fire }} \mathrm{dt}
```

The occurrence rate {math}`\mathrm{v_{fire}}` can be written as a summation of local values over the floor area:

```{math}
:label: eq-fire-2.20.2
\mathrm{v_{fire}}=\iint_{\mathrm{A}_{\mathrm{f}}} \lambda(\mathrm{x}, \mathrm{y})~ \mathrm{dx~dy}
```

where {math}`\lambda(\mathrm{x}, \mathrm{y})` corresponds to the probability of fire ignition per year per {math}`\mathrm{m}^{2}` for a given occupancy type; {math}`\mathrm{A}_{\mathrm{f}}` is the floor area of the fire compartment. As in most applications {math}`\lambda(\mathrm{x}, \mathrm{y})` can be simplied as a constant, and {eq}`eq-fire-2.20.2` can be simplified to:

```{math}
:label: eq-fire-2.20.3
\mathrm{v_{fire}}=\mathrm{A_{f}} \lambda
```

Values for {math}`\lambda` are presented in {numref}`tbl2.20.1`.

```{table} Example values of annual fire probabilities λ per unit floor area for several types of occupancy
:name: tbl2.20.1
| Type of building | {math}`\lambda` [m{math}`^{-2}` year{math}`^{-1}`] |
| :--- | :--- |
| dwelling/school | 0.5 to 4 * 10{math}`^{-6}` |
| shop/office | 1 to * 10{math}`^{-6}` |
| industrial building | 2 to 10 * 10{math}`^{-6}` |
```

## Flashover occurrence

After ignition there are various ways in which a fire can develop. The fire might extinguish itself after a certain period of time because no other combustible material is present. The fire may be detected very early and be extinguished by hand. An automatic sprinkler system may operate or the fire brigade may arrive in time to prevent flash over. Only in a minority of cases does a fire develop into a fully developed room or compartment fire; sometimes the fire may break through a barrier and start a fire in another compartment. From the structural point of view only these fully developed or post flashover fires (see {numref}`fig-fire-2.1`) may lead to failure. For very large fire compartments having a very large concentration of fire loads, e.g. industrial buildings, a local fire of high intensity also may lead to (localised) structural damage.

The occurrence rate of flashover is given by:

```{math}
:label: eq-fire-2.20.4
\mathrm{v}_{\text {flash over}} = \mathrm{P} \left\lbrace \text{flash over} \mid \text{ignition} \right\rbrace \mathrm{v}_\mathrm{fire}
```

The probability of a flashover once a fire has taken place, can obviously be influenced by the presence of sprinklers and fire brigades. Numerical values for the analysis are presented in {numref}`tbl2.20.2`. 

```{figure} ../part-02/images/Figure-2.1.png
:name: fig-fire-2.1

Schematic presentation of a temperature-time curve
```

* Curve (a) represents the temperature-time curve when a sprinkler system or a timely fire brigade action is successful.
* Curve (b) presents the temperature-time relation for a fully developed fire.
* Curve (c) indicates the limited influence of a fire brigade arriving after flashover has taken place.
* Curve (d) indicates the ISO-standard temperature curve (see section [19.4.2.](section-2.20.4.2)).

```{table} Probability of flashover for given ignition, depending on the type of active protection measures
:name: tbl2.20.2
| Protection method | P {flashover {math}`\mid` ignition} |
| :--- | :--- |
| Public fire brigade | 10{math}`^{-1}` |
| Sprinkler | 10{math}`^{-2}` |
| High standard fire brigade on site, combined with alarm system (industries only) | 10{math}`^{-3}` to 10{math}`^{-2}` |
| Both sprinkler and high standard residential fire brigade | 10{math}`^{-4}` |
```

## Combustible material modelling

The available combustible material can be considered as a random field, which in general might be nonhomogeneous as well as nonstationary. The intensity of the field {math}`\mathrm{q}` at some point in space and time is defined as:

```{math}
:label: eq-fire-2.20.5
\mathrm{q}=\frac{\Sigma \mathrm{m}_{\mathrm{i}}~\mathrm{M}_{\mathrm{ki}}~\mathrm{H}_{\mathrm{i}}}{\mathrm{A}_{\mathrm{f}}}
```

{math}`\mathrm{m}_{\mathrm{i}}=` derating factor between 0 and 1 , describing the degree of combustion

{math}`\mathrm{M}_{\mathrm{ki}}=` combustible mass present at {math}`\mathrm{A}_{\mathrm{f}}` for material {math}`\mathrm{i}`

{math}`\mathrm{H}_{\mathrm{i}}` = specific combustible energy for material {math}`\mathrm{i}`

{math}`\mathrm{A}_{\mathrm{f}}=` considered floor area

In some cases the intensity {math}`\mathrm{q}` may also depend on a vertical ordinate.

The non-dimensional factor {math}`\mu_{\mathrm{i}}` is a function of the fuel type, the geometrical properties of the fuel, and the position of the fuel in the fire compartment, among other things. For some types of fire load components, {math}`\mathrm{m}_{\mathrm{i}}` depends on the time of fire duration and on the gas temperature-time characteristics of the compartment fire. Probabilistic models for {math}`\mathrm{q}` are presented in {numref}`tbl2.20.3`.

```{table} Recommended values for the average fire load intensity q_o
:name: tbl2.20.3
| Type of fire compartment | Mean value <br> {math}`\mu\left(\mathrm{q}_{0}\right)\left[\mathrm{MJm}^{-2}\right]` | Coefficient of variation <br> {math}`\mathrm{V}\left(\mathrm{q}_{0}\right)` |
| :--- | :--- | :--- |
| 1: Dwellings | 500 | 0.20 |
| 2: Offices | 600 | 0.30 |
| 3: Schools | 350 | 0.20 |
| 4: Hospitals | 450 | 0.30 |
| 5: Hotels | 300 | 0.25 |
```

## Temperature-time relationship

### Scientific models

For known characteristics of both the combustible material and the compartment, the post flash over period of the temperature time curve can be calculated from energy and mass balance equations.

Many variables can be introduced as random in the model, for instance:

- the amount and spatial distributions of combustible material;
- the effective energy value;
- the rate of combustion;
- the ventilation characteristics;
- air use and gas production parameters;
- thermal conductivity properties;
- model uncertainties.

In addition, the development of the fire may depend on events like collapse of windows or containments, which may change the ventilation conditions or the available amount of combustible material respectively. 

As a simplification the following assumptions may be used.

1. the combustible material is wood;
2. the wood is spread uniformly over the floor area;
3. the fire compartment is of a standard building material (brick, concrete);
4. the fire is controlled by ventilation and not by the amount of fuel load (this is conservative);

5. the initial temperature is 20{math}`^{\circ} \mathrm{c}`.

In this case the temperature time curve depends on two parameters:

- the floor averaged fire load density {math}`\mathrm{q}_{\mathrm{o}}`;
- the opening factor {math}`\mathrm{f}`.

The opening factor {math}`\mathrm{f}` is defined as:

```{math}
:label: eq-fire-2.20.7
\mathrm{f}=\frac{\mathrm{A}_{\mathrm{v}}}{\mathrm{A}_{\mathrm{t}}} \sqrt{\mathrm{h}} ; \quad \mathrm{with}~\mathrm{h}=\frac{\sum \mathrm{A}_{\mathrm{i}} \mathrm{h}_{\mathrm{i}}}{\mathrm{A}_{\mathrm{v}}} ; \mathrm{A}_{\mathrm{v}}=\sum \mathrm{A}_{\mathrm{i}}
```

where:

{math}`\mathrm{A}_{\mathrm{t}}=` total internal surface area of the fire compartment, i.e. the area of the walls, floor and ceiling, including the openings {math}`\left[\mathrm{m}^{2}\right]`

{math}`\mathrm{A}_{\mathrm{i}}=` area of the vertical opening {math}`\mathrm{i}` in the fire compartment {math}`\left[\mathrm{m}^{2}\right]`

{math}`\mathrm{h}_{\mathrm{i}}` value of the height of opening {math}`\mathrm{i}[\mathrm{m}]`

For a fire compartment which also contains horizontal openings, the opening factor can be calculated from a similar expression. In calculating the opening factor, it is assumed that ordinary window glass is immediately destroyed when fire breaks out.

In many cases it will be possible to indicate a physical maximum {math}`\mathrm{f}_{\max }`. The actual value of {math}`\mathrm{f}` in a fire should be modelled as a random quantity according to:

```{math}
:label: eq-fire-2.20.8
\mathrm{f}=\mathrm{f}_{\max }(1-\zeta)
```

{math}`\zeta=` random parameter (see {numref}`tbl2.20.4`)

To avoid negative values of {math}`\mathrm{f}`, this lognormal distribution should be cut off at {math}`\zeta=1`. In addition one should multiply the resulting temperatures by an overall model uncertainty factor {math}`\theta_{\text {model }}`.

(section-2.20.4.2)=
### Engineering models

In many engineering applications, use is made of equivalent standard temperature-time-relationship according to ISO 834:

```{math}
:label: eq-fire-2.20.9
\theta=\theta_{\mathrm{o}}+\theta_{\mathrm{A}} \log _{10}\{\alpha \mathrm{t}+1\}~\mathrm{for}~0<\mathrm{t}<\mathrm{t}_{\mathrm{eq}}
```

with:

```{math}
:label: eq-fire-2.20.10
\mathrm{t}_{\mathrm{eq}}=\frac{\beta_{\mathrm{f}}~\mathrm{q}_{\mathrm{o}}~\mathrm{A}_{\mathrm{f}}}{\mathrm{A}_{\mathrm{t}} \sqrt{\mathrm{f}}}
```

{math}`\theta=` temperature in the compartment

{math}`\theta_{\mathrm{o}}=` temperature at the start of the fire

{math}`\theta_{\mathrm{A}}=` parameter

{math}`\alpha=` parameter

{math}`\mathrm{t}=` time

{math}`\mathrm{t}_{\mathrm{eq}}=` equivalent time of fire duration

{math}`\beta_{\mathrm{f}}=` coefficient (model uncertainty)

{math}`\mathrm{q}_{\mathrm{o}}=` fire load density per unit floor area

{math}`\mathrm{A}_{\mathrm{f}}=` floor area

{math}`\mathrm{A}_{\mathrm{t}}=` total internal surface area

{math}`\mathrm{f}=` ventilation opening (see {eq}`eq-fire-2.20.7`, {eq}`eq-fire-2.20.8`)

Numerical values and probabilistic models are given in {numref}`tbl2.20.4`.


```{table} Numerical values for random variables
:name: tbl2.20.4
| Variable | Distribution | Mean | Standard deviation |
| :--- | :--- | :--- | :--- |
| {math}`\zeta` | truncated lognormal {math}`^{1)}` | 0.2 | 0.2 |
| {math}`\beta_{\mathrm{f}}` | lognormal | 4.0 sm{math}`^{2.25}`/MJ | 1.0 |
| {math}`\theta_{\mathrm{o}}` | deterministic | 20{math}`^{\circ}`c | - |
| {math}`\theta_{\mathrm{A}}` | deterministic | 345 K | - |
| {math}`\alpha` | deterministic | 0.13 s{math}`^{-1}` | - |
```
{math}`{ }^{1)}` values of {math}`\zeta>1` should be supressed

