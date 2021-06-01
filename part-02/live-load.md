# Live Load

## Basic Model

The live loads on floors in buildings are caused by the weight of furniture, equipment, stored objects
and persons. Not included in this type of load are any structural or non-structural elements, partition walls or
extraordinary equipment. The live load is distinguished according the intended user category of the building, i.e.
domestic buildings, hotels, hospitals, office buildings, schools, and stores. At design stage considerations
should also be given to eventual changes of use during the life-time. Areas dedicated to store goods, materials,
etc. must be treated separately. Live loads vary in time and space in a random manner. The spatial variations
are assumed to be homogeneous in a first approximation. With respect to the variation in time, it is divided into
two components, the sustained load and the intermittent load.

The sustained load contains the weight of furniture and heavy equipment. The load magnitude
according to the model represents the time average of the real fluctuating load. Changes usually related to
changes in use and of users in a building. Short term fluctuations are included in the uncertainties of this load
part.

The intermittent load represents all kinds of live loads, which are not covered by the sustained load.
The sources are like gathering of people, crowded rooms during special events, or stacking of furniture during
remodelling. The relative duration of an intermittent loads is fairly small.

## Stochastic Model

The load intensity is represented by a stochastic field $W(x,y)$, whereby the parameters depend on
the user category of the building.

$$
W ( x , y ) = m + V + U ( x, y )
$$

where $m$ is the overall mean load intensity for a particular user category, $V$ is a zero mean normal distributed
variable and $U(x,y)$ is a zero mean random field with a characteristic skewness to the right. The quantities $V$
and U are assumed to be stochastically independent.

The load effects calculated from the model shall describe the load effects caused by the real load, with
sufficient accuracy. For linear elastic systems, where superposition is possible, the load effect $S$ is written as:

$$
S = \int_A W ( x, y ) i( x, y ) dA
$$

where $W(x,y)$ is the load intensity and $i(x,y)$ is the influence function for the load effect over a considered area $A$.

For non-linear structural response a stepwise linearity can be assumed, whereby the proposed relation
for the load effect can be used in each step. The load intensity $W$ is substituted by the step $\Delta W$ and the
influence function $i(x,y)$ must reflect the total load situation, which results in a corresponding step
$\Delta S$ for the load effect. When applying the theory of plasticity, then the influence function is 
proportional to the deflection corresponding to the mechanism.


## Variations in Time
## Load Parameters

