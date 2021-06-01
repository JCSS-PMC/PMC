# General Principles

## Introduction

The environment in which structural systems function gives rise to internal forces, deformations, material deterioration and other short-term or long-term effects in these systems. The causes of these effects are termed actions. The environment from which the actions originate can be of a natural
character, for example, snow, wind and earthquake. lt can also be associated with human activities such as living in a domestic house, working in a factory, etc.
The following concepts of actions are used in this document.

1. An action is an assembly of concentrated or distributed forces acting on the structure. This kind of action is also denoted by "load".
2. An action is the cause of imposed displacements or thermal effects in the structure. This kind of action is often denoted by "indirect action".
3. An action is an environmental influence which may cause changes with time in the material properties or in the dimensions of a structure.

Action descriptions are in most cases based on suitably simple mathematical models, describing the temporal, spatial and directional properties of the action across the structure. The choice of the level of richness of details is guided by a balance between the quality of the available or obtainable information and a reasonably accurate modelling of the action effect. The choice of the level of realism and accuracy in predicting the relevant action effects is, in time, guided by the sensitivity of the implied design decisions to variations of this level and the economical weight of these decisions.
Thus the same action phenomenon may give rise to several very different action models dependent on the effect and structure under investigation.

## Classifications

Loads can be classified according to a number of characteristics. With respect to the type of the loads, the following subdivision can be made:

- self weight of structures
- occupancy loads in buildings, e.g. loads from persons and equipment
- actions caused by industrial activities, e.g. silo loads
- actions caused by transport: traffic, liquids in pipelines, cranes, impact, etc.
- climatic actions, e.g. snow. wind, outdoor temperature etc.
- hydraulic actions, e.g. water and ground water pressures
- actions from soil or rock, including earth quake

This classification does not cover all possible actions hut most of the common types of actions can be included in one or more classes. Some of the classes belong as a whole either to uncontrollable actions or to controllable actions. Other actions may belong to both e.g. water pressure.

With respect to the variations in time the following classification can be made:

- **permanent** actions, whose variations in time around their mean is small and slow (e.g. self weight, earth pressure) or which monotonically a limiting value (C.g. prestressing, imposed deformation from construction processes, effects from temperature, shrinkage, creep or settlements)
- **variable actions**, whose variations in time are frequent and large (e.g. all actions caused by the use of the structure and by most of the external actions such as wind and snow)
- **exceptional actions**, whose magnitude can be considerable but whose probability of occurrence for a given structure is small related to the anticipated time of use. Frequently the duration is short (e.g. impact loads, explosions, earth and snow avalanches).

As far as the spatial fluctuations are concerned it is useful to distinguish between fixed and free
actions. **Fixed actions** have a given spatial intensity distribution over the structure. They are
completely defined if the intensity is specified in a particular point of the structure (e.g. earth or water
pressure). For **free actions** the spatial intensity distribution is variable (e.g. regular occupancy
loading, involved although they are variable actions.


## Modelling of actions

There are two main aspects of the description of an action: one is the physical aspect, the other is the
statistical aspect. In most cases these aspects can be clearly separated. Then the physical description
gives the types of physical data which characterise the action model, for example, vertical forces
distributed over a given area. The statistical description gives the statistical properties of the
variables, for example, a probability distribution function. In some cases the physical and statistical
aspects are so integrated that they cannot be considered separately.

A complete action model consists in general, of several constituents which describe the magnitude,
the position, the direction, the duration etc. of the action. Sometimes there is an interaction between
the components. There may in certain cases also be an interaction between the action and the
response of the structure.

One can in many cases distinguish between two kinds of variables (constituents) $F_0$ and $W$ describing
an action $F$ (see also part 1, Basis of Design).

$$
F = φ (F_O, W)
$$(eq_action_F)

- $F_O$ is a basic action variable which is directly associated with the event causing the action and
which should be defined so that it is, as far as possible, independent of the structure. For
example, for snow load Fo is the snow load on ground, on a flat horizontal surface
- $W$ is a kind of conversion factor or model parameter appearing in the transformation from the
basic action to the action F which affects the particular structure. W may depend on the form
and size of the structure etc. For the snow load example W is the factor which transforms the
snow load on ground to the snow load on roof and which depends on the roof slope, the type
of roof surface etc.
- $\varphi$ is a suitable function, often a simple product.

The time variability is normally included in $F_O$, whereas $W$ can often be considered as time
independent. A systematic part of the space variability of an action is in most cases included in $W$,
whereas a possible random part may be included in $F_O$ or in $W$. Eq. {eq}`eq_action_F` should be regarded as a
schematic equation. For one action there may be several variables $F_O$ and several variables $W$.

Any action model contains a set of parameters and variables that must be evaluated before the model
can be used. In probabilistic modelling all action variables are in principle assumed to be random
variables or processes while other parameters may be time or spatial co-ordinates, directions etc.
Sometimes parameters may themselves be random variables, for example when the model allows for
statistical uncertainty due to small sample sizes.

An action model often includes two or more variables of different character as is described by eq. {eq}`eq_action_F`
For each variable a suitable model should be chosen so that the complete action model
consists of a number of models for the individual variables.

These models may be described in terms of:

- stochastic processes or random fields
- sequences of random variables
- individual random variables
- deterministic values or functions

The definition of the models for these quantities require probability distributions (see annex 2) and a
description of the correlation patterns.


## Models for fluctuations in time
### Types of models
### Distribution of extremes for single processes
### Distribution of extremes for hierarchical processes
## Models for Spatial variability
### Hierarchical model
### Equivalent uniformly distributed load (EUDL)
## Dependencies between different actions
## Combination of actions

## ANNEX 1 - DEFINITIONS
## ANNEX 2 - DISTRIBUTIONS FUNCTIONS
## ANNEX 3 - MATHEMATICAL COMBINATION TECHNIQUES

