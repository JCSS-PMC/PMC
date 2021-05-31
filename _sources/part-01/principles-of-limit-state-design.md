# Principles of limit state design

## Limit states and adverse states

 The structural performance of a whole structure or part of it should
 be described with reference to a specified set of limit states which
 separate desired states of the structure from adverse states.

 The limit states are divided into the following two basic categories:

-   the *ultimate limit states*, which concern the maximum load carrying
     capacity as well as the maximum deformability

-   the *serviceability limit states*, which concern the normal use.

 The exceedance of a limit state may be irreversible or reversible. In
 the irreversible case the damage or malfunction associated with the
 limit state being exceeded will remain until the structure has been
 repaired. In the reversible case the damage or malfunction will remain
 only as long as the cause of the limit state being exceeded is
 present. As soon as this cause ceases to act, a transition from the
 adverse state back to the desired state occurs.

 It is further noted here that in some cases a limit between the
 aforementioned limit state types may be defined This can be done by an
 artificial discretization of a the continuous situation between the
 serviceability and the ultimate limit state. By applying such a
 procedure a so- called *partial damage limit state*" can be defined.
 For example in case of earthquake damage of plant structures such
 limit state is associated to the safe shut down of the plant.

 **Ultimate limit states** may correspond to the following adverse
 states:

-   loss of equilibrium of the structure or of a part of the structure,
    considered as a rigid body (eg. overturning)

-   attainment of the maximum resistance capacity of sections, members
     or connections by rupture or excessive deformations

-   rupture of members or connections caused by fatigue or other
     time-dependent effects instability of the structure or part of it

-   sudden change of the assumed structural system to a new system, (eg.
     snap through)

 The exceedance of an ultimate limit state is almost always
 irreversible and the first time that this occurs causes failure.

 **Serviceability limit states** may correspond to the following
 adverse states:

-   local damage (including cracking) which may reduce the durability of
    the structure or affect the efficiency or appearance of structural
    or non-structural elements.

-   observable damage caused by fatigue or other time dependent effects

-   unacceptable deformations which affect the efficient use or
     appearance of structural or non-structural elements or the
     functioning of equipment.

 excessive vibrations which cause discomfort to people or affect
 non-structural

-   elements or the functioning of equipment

 In the cases of permanent local damage or permanent unacceptable
 deformations the exceedance of a serviceability limit state is
 irreversible and the first time that this occurs causes failure.

 In other cases the exceedance of a serviceability limit state may be
 reversible and then failure occurs:

a)  the first time the serviceability limit state is exceeded, if no
    exceedance is considered as acceptable

b)  if exceedance is acceptable but the time when the structure is in
    the undesired state is longer than specified

c)  if exceedance is acceptable but the number of times that the
    serveciability limit state is exceeded is larger than specified

d)  if a combination of the above criteria occur.

 These cases may involve temporary local damage (eg. temporarily wide
 cracks), temporary large deformations and vibrations. Limit values for
 the serviceability limit state should be defined on the basis of
 *utility considerations*.

## Limit State Function

 For each specific limit state the relevant basic variables should be
 identified, i.e. the variables which characterize:

-   actions and environmental influences

-   properties of materials and soils

-   geometrical parameters

 Such variables may be time dependent. Models, which describe the
 behaviour of a structure, should be established for each limit state.
 These models include mechanical models, which describe the structural
 behaviour, as well as other physical or chemical models, which
 describe the effects of environmental influences on the material
 properties. The parameters of such models should in principle be
 treated in the same way as basic variables.

 Serviceability constaints (limit values according to 4.1) should in
 principle be regarded as random and may in many cases be treated in
 the same way as basic variables.

 Where calculation models are available, the limit state can be
 described with aid of a function, g, of the basic variables
 $X(t)=X_1(t),X_2(t)\dots$ so that

```{math}
:label: eq1
g(X(t))= 0
```

 Eq. {eq}`eq1` is called the limit state equation, and

```{math}
:label: eq2
g(X(t))= 0
```

 identifies the adverse state.

 In a component analysis where there is one dominating failure mode the
 limit state condition can normally be described by one equation
 according to eq. {eq}`eq1`. In a system analysis, where more than one
 failure mode may be determining, there are several such equations.

## Design situations

 Actions, environmental influences and structural properties may vary
 with time. Such variations, which occur throughout the lifetime of the
 structure, should be considered by selected design situations, each
 one representing a certain time intervall with associated hazards,
 conditions and relevant structural limit states.

 The design situations may be classified as:

 *Persistent situations*, which refer to conditions of normal use of
 the structure and are generally related to the working life of the
 structure.

 *Transient situations*, which refer to temporary conditions of the
 structure, in terms of its use or its exposure.

 *Accidental situations*, which refer to exceptional conditions of the
 structure or its exposure.
