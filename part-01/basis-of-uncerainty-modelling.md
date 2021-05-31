# Basis of uncerainty modelling

## Basic variables

 The calculation model for each limit state considered should contain a
 specified set of basic variables, i.e. physical quantities which
 characterize actions and environmental influences, material and soil
 properties and geometrical quantities. The model should also contain
 model parameters which characterize the model itself and which are
 treated as basic variables (compare 4.2). Finally there are also
 parameters which describe the requirements (e.g. serviceability
 constraints) and which may be treated as basic variables. The basic
 variables (in

 the wide sence given above) are assumed to carry the entire input
 information to the calculation model.

 The basic variables may be random variables (indlucing the special
 case deterministic variables) or stochastic processes or random
 fields. Each basic variable is defined by a number of parameters such
 as mean, standard deviation, parameters determining the correlation
 structure etc.

## Types of uncertainty

 Uncertainties from *all essential sources* must be evaluated and
 integrated in a basic variable model. Types of uncertainty to be taken
 into account are:

-   intrinsic physical or mechanical uncertainty

-   statistical uncertainty, when the design decisions are based on a
    small sample of observations or when there are other similar
    conditions

-   model uncertainties (see 5.6).

 Within given classes of structural design problems the types of
 probability distributions of the basic variables should be
 standardized. These standardizations are defined in the parts 2 and 3
 of the probabilistic model code.

## Definition of populations

 The random quantities within a reliability analysis should always be
 related to a meaningfull and consistent set of populations. The
 description of the random quantities should correspond to this set and
 the resulting failure probability is only valid for the same set.

 The basis for the definition of a population is in most cases the
 physical background of the variable. Factors which may define the
 population are:

-   the nature and origin of a random quantity

-   the spatial conditions (e.g. the geographical region considered)

-   the temporal conditions (e.g. the intended time of use of the
     structure considered)

 The choice of a population is to some extent a free choice of the
 designer. It may depend on the objective of the analysis, the amount
 and nature of the available data and the amount of work that can be
 afforded.

 In connection with theoretical treatment of data and with the
 evaluation of observations it is often convenient to divide the
 largest population into sub-populations which in turn are further
 divided in smaller sub-populations etc. Then it is possible to study
 and distinguish variability within a population and variability
 between different populations.

 In an analysis for a specific structure it may be efficient to define
 a population as small as possible as far as use, shape and location of
 the structure are concerned (microzonation). When the results are used
 for design in a national or international code, it may be necessary or
 convenient to put the sub-populations together to the large population
 again in order not to get too complicated rules (randomizing). This
 means that the variability within the population is increased.

## Hierarchy of uncertainty models

 This section contains a convenient and recommended mathematical
 description in general terms of a hierarchical model which can be used
 for different kinds of actions and materials. The details of this
 model have to be stated more precisely for each specific variable. The
 model is associated with a hierarchical set of subpopulations.

 The hierarchical model assumes that a random quantity $\vec{X}$ can be written
 as a function of several variables, each one representing a specific
 type of variability:


```{math}
:label: eq3
X_{ijk} = f(Y_i,Y_{ij},Y_{ijk})
```

 The $Y$ represent various origins, time scales of fluctuation or spatial
 scales of fluctuation.

 For instance $Y_i$ may represent the building to building variation,
 $Y_{ij}$ the floor to floor variation in building $i$ and $Y_{ijk}$ the point
 to point variation on floor $j$ in building $i$.

 In a similar way, $Y_i$ may represent the constant in time variability,
 $Y_{ij}$ a slowly fluctuating time process and $Y_{ijk}$ a fast fluctuating
 time process.
