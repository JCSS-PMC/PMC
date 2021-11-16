# Models for physical behaviour

here are my edits

## General

 Calculation models shall describe the structure and its behaviour up
 to the limit state under consideration, accounting for relevant
 actions and environmental influences. Models should

 generally be regarded as simplifications which take account of
 decisive factors and neglect the less important ones.

 One can often distinguish between:

-   action models

-   structural models which give action effects (internal forces,
    moments etc.)

-   resistance models which give resistances corresponding to the action
    effects, and are based on.

-   material models and geometry models .

 However, in some cases it is not possible or convenient to make this
 distinction, for example, if the instability or loss of equilibrium of
 an entire structural system is studied or if interactions between
 loads and structural response are of interest.

## Action models

 A complete action model should describe several properties of the
 action such as its magnitude, position, direction, duration etc. In
 some cases there is an interaction between the different properties
 and also between these properties and the response of the structure.
 Such interactions should be taken into account.

 The magnitude $F$ of an action may often be described by two different
 types of variables so that

```{math}
:label: eq4
F = \varphi(F_0,W)
```
 where $\varphi$ is an appropriate function and

 $F_0$ is a basic action variable, often with time and space dependent
 variations (random or non-random) and is generally independent of the
 structure

 $W$ is a random or non-random variable or a random field which may
 depend on the structural properties and which transformes $F_0$ to $F$.

 Eq. {eq}`eq4` should be regarded as a symbolic expression where $F_0$ and $W$ may
 represent several variables.

 One example may be snow load where $F_0$ is the time dependent snow load
 on ground and $W$ is the conversion factor for snow load on ground to
 snow load on roof which normally is assumed to to be time independent.

 Further information on action models is provided in part 2. It is
 noted that action models may include material properties (earthquake
 action depends for example on material damping).

## Geometrical models

 A structure can generally be described by a model consisting of
 one-dimensional elements (beams, columns, cables, arches, etc),
 two-dimensional elements (slabs, walls, shells, etc) and
 three-dimensional elements.

 The geometrical quantities which are included in the model generally
 refer to nominal values,

 i.e. the values given in drawings, descriptions etc. Normally, the
 geometrical quantities of a real structure differ from their nominal
 values, i.e. the structure has geometrical imperfections. If the
 structural behaviour is sensitive to such imperfections, these shall
 be inlcuded in the model.

 In many cases the deformation of a structure causes significant
 deviations from nominal values of geometrical quantities. If such
 deformations are of importance for the structural behaviour, they have
 to be considered in the design in principally the same way as
 imperfections. The effects of such deformations are generally denoted
 *geometrically nonlinear* or *second order effects* and should be
 accounted for.

## Material models

 When strength or stiffness is considered the material model normally
 consists of relations between forces or stresses and deformations i.e
 *costitutive relationships*. The parameters of such relations are
 modulus of elasticity, yield limit, ultimate strength etc. which
 generally are considered as random variables, Sometimes they are time
 dependent or space dependent. There is often an correlation between
 the parameters e.g. the modulus of elasticity and the ultimate
 strength of concrete.

 Other material properties, e.g. resistance against material
 deterioration may often be treated in a similar way. However the
 principles are strongly dependent on type of material and the property
 considered.

 Further information related to models of several material types is
 given in part 3.

## Mechanical models

 The following mechanical models may be classified

1.  models describing static response

2.  models decribing dynamic response

3.  models for fatigue

a)  *models describing static response*

 In almost all design calculations some assumptions concerning the
 relation between forces or moments and deformations (or deformation
 rates) are necessary. These assumptions can vary and depend on the
 purpose and type of calculation. The most general relationship
 regarding structural response is considered to be elastic) developing
 into plastic behaviour in certain parts of the structure at high
 action effects. In other parts of the structure intermediate stages
 occur. Such relationships may be used generally. However the use of
 any theory taking into account in-elastic or post-critical behaviour
 may have to take into account repetitions of variable actions that are
 free. Such actions may cause great variations of the action effects,
 repeated yielding and exhaustion of the deformation capacity.

 The theory of elasticity may be regarded as a simplification of a more
 general theory and may generally be used provided that forces and
 moments are limited to those values, for which the behaviour of the
 structure is still considered as elastic. However, the theory of
 elasticity may also be used in other cases if it is applied as a
 conservative approximation.

 Theories in which fully developed plasticity is assumed to occur in
 certain zones of the structure (plastic hinges in beams, yield lines
 in slabs, etc) may also be used, provided that the deformations which
 are needed to ensure plastic behaviour, occur before the ultimate
 limit state is reached. Thus theory of plasticity should be used with
 care to determine the load carrying capacity of a structure, if this
 capacity is limited by:

-   brittle failure

-   failure due to instability

b)  *models for dynamic response*

 In most cases dynamic response of a structure is caused by a rapid
 variation of the magnitude, position or direction of an action
 However, a sudden change of the stiffness or resistance of a
 structural element may also cause dynamic behaviour.

 The models for dynamic response consist in general of:

-   a stiffness model

-   a damping model

-   an inertia model

c)  *models for fatigue*

 Fatigue models are used for the description of fatigue failures caused
 by fluctuating actions. Two types of models are distinguished:

a)  S-N model based on experiments

b)  fracture mechanics model

 It is further noted here, that other types of degradation such as
 chemical attack or fire can modify the parameters entering the
 aforementioned models or the models themselves.

## Model uncertainties

 A calculation model is a physically based or empirical relation
 between relevant variables, which are in general random variables:

```{math}
:label: eq5
Y = f(X_1,X_2,\dots ,X_n)
```

- $Y$ = model output
- $f( )$ = model function
- $X_i$    = basic variables

 The model $f(\dots)$ may be complete and exact, so that, if the values
 of $X_i$ are known in a particular experiment (from measurements), the
 outcome $Y$ can be predicted without error. This, however, is not
 normally the situation. In most cases the model will be incomplete and
 inexact. This may be the result of lack of knowledge, or a deliberate
 simplification of the model, for the convenience of the designer. The
 difference between the model prediction and the real outcome of the
 experiment can be written down as:

```{math}
:label: eq6
Y = f'(X_1\dots X_n,\theta_1\dots\theta_m)
```

 $\theta_i$ are referred to as parameters which contain the model uncertainties
 and are treated as random variables. Their statistical properties can
 in most cases be derived from experiments or observations. The mean of
 these parameters should be determined in such a way that, on average,
 the calculation model correctly predicts the test results.
