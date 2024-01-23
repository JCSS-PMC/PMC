# Annex A: The Robust Requirement

## Introduction 

In [clause 3.1](section-3.1) the following robustment requirement has been formulated:

> *“A structure shall not be damaged by events like fire explosions or consequences of human errors, deterioration effects, etc. to an extend disproportionate to the severeness of the triggering event”.* 

This annex is intended to give some further guidance. No attention is being paid to terrorist actions and actions of war. The general idea is that, whatever the design, proper destructive actions can always be succesful.

(section-A2)=
## Structural and nonstructural measures

In order to attain adequate safety in relation with accidental loads one or more of the following strategies may be followed:

1. reduction of the probability that the action occurs or reduction of the action intensity (prevention)

2. reduction of the effect of the action on the structure (protection)

3. making the structure strong enough to withstand the loads

4. limiting the amount of structural damage

5. migitation of the consequences of failure

The strategies 1, 2 and 5 are so called non-structural measures. These measures are considered as being very effective for some specific accidental action.

The strategies 3 and 4 are so called structural measures. In general strategy 3 is extremely expensive in most cases. Strategy 4, on the other hand accepts some members to fail, but requires that the total damage is limited. This means that the structure should have sufficient redundancy and possibilities to mobilise so called alternative load paths.

In the ideal design procedure, the occurrence and effects of an accidental action (impact, explosion, etc.) are simulated for all possible action scenarios. The damage effect of the structural members is calculated and stability of the remaining structure assessed. Next the consequences are estimated in terms of number of casualties and economic losses. Various measures can be compared on the basis of economic criteria.

## Simplified design procedure

The approach sketched in [A2](section-A2) has two disadvantages:

1. it is extremely complicated

2. it does not work for unforseeable hazards

As a result other more global design strategies have been developed, like the classical
requirements on sufficient ductility and tying of elements.

Another approach is that one considers the situation that a structural element (beam, column) has been damaged, by whatever event, to such an extend that its normal load bearing capacity has vanished almost completely. For the remaining part of the structure it then required that for some relatively short period of time (repair period T) the structure can withstand the "normal" loads with some prescribed reliability:

```{math}
:label: eqA1
P(R < S\ in\ T\ |\ one\ element\ removed) < p_{target}
```

The target reliability in {eq}`eqA1` depends on:

- the normal safety target for the building

- the period under consideration (hours, days or months)

- the probability that the element under consideration is removed (by other causes than
already considered in design).

The probability that some element is removed by some cause, not yet considered in design, depends on the sophistication of the design procedure and on the type of structure. For a conventional structure it should, at least in theory, be possible to include all relevant collapse origins in the design. Of course, it will always be possible to think of failure causes not covered by the design, but those will have a remote likelihood and may be disregarded on the basis of decision theoretical arguments. For unconventional structures this certainly will not be the case.

## Recommendation

For *unconventional* structures, as for instance large structures, the probability of having some unspecified failure cause is substantial. If in addition new materials or new design concepts are used, unexpected failure causes become more likely. This would indicate that for unconventional structures the simplified approach should be recommended.

For *conventional* structures there is a choice:

1. one might argue that, as one never succeeds in dealing with all failure causes explicitly in a satisfactory way, it has no use to make refined analyses including system effect, accidental actions and so on; this leads to the use of the simplified procedure.

2. one might also eliminate the use of an explicit robustness requirement {eq}`eqA1` as much as possible by taking into the design as many aspects explicitly as possible.

Stated as such it seems that the second approach is more rational, as it offers the possibility to reduce the risks in the most economical way, e.g. by sprinklers (for fire), barriers (for collision), QA (for errors), relief openings (for explosions), artificial damping (for earth quake), maintenance (for deterioration) and so on.
