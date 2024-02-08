# Reliability

## Reliability measures

 A standard reliability measure may be chosen to be the *generalized
 reliability index*. It is defined as:

```{math}
:label: eq7
\beta = - \Phi^{-1}(P_f)
```

 where  
 
$P_f$ is the probability of failure

$\Phi^{-1}(\cdot)$ is the inverse Gaussian distribution

 Another equivalent reliability measure is the probability of the
 complement of the adverse event

```{math}
:label: eq8
P_s = 1 - P_f
```

 The probability $P_f$ should be calculated on the basis of the
 standardized joint distribution type of the basic variables and the
 standardized distributional formalism of dealing with both model
 uncertainty and statistical uncertainty.

 In special situations other than the standardized distribution types
 can be relevant for the reliability evaluation. In such cases the
 distributional assumptions must be tested on a suitable representative
 set of observation data.

 Reliability analysis principles including time-dependent reliability
 problems are described in [Annex C](../part-01/annex-C-Reliability-Analysis-Principles.md).

## Component reliability and system reliability

 **Component reliability** is the reliability of one single structural
 component which has one dominating failure mode.

 **System reliability** is the reliability of a structural system
 composed of a number of components or the reliability of a single
 component which has several failure modes of nearly equal importance.
 The following type of systems can be classified:

-   \-*redundant systems* where the components are "fail safe", i.e.
    local behaviour of one component does not directly result in failure
    of the structure;

-   \-*non-redundant* systems where local failure of one component leads
    rapidly to failure of the structure.

 Probabilistic structural design is primarily concerned with *component
 behaviour*. System behaviour is, however, of concern because it is
 usually the most serious consequence of structural failure. Therefore
 the likelihood of system failure following an initial component
 failure should be assessed. In particular, it is necessary to
 determine the system characteristics in relation to damage tolerance
 or robustness with respect to accidental events. The requirements for
 the reliability of the components of a system should depend upon the
 system characteristics.

 A probabilistic system analysis should therefore be carried out to
 establish:

-   the redundancy (alternate load-carrying paths)

-   the state and complexity of the structure (multiple failure modes).

Furher aspects on system reliability are provided in [Annex C](../part-01/annex-C-Reliability-Analysis-Principles.md).

##  Methods for reliability analysis and calculation

 The numerical value of the reliability measure is obtained by a
 reliability analysis and calculation method (see [Annex C](../part-01/annex-C-Reliability-Analysis-Principles.md)). The
 reliability method used should be capable of producing a sensitivity
 analysis including importance factors for uncertain parameters. The
 choice of the method should be in general justified. The justification
 can be for example based by another relevant computation method or by
 reference to appropriate literature.

 Due to the computational complexity a method giving an approximation
 to the exact result is generally applied. Two fundamental accuracy
 requirements are:

-   Overestimation of the reliability due to use of an approximative
     calculation method shall be within limits generally accepted for
     the specific type of structure.

-   The overestimation of the reliability index should not exceed 5 %
     with respect to the target level.

 The accuracy of the reliability calculation method is linked to the
 sensitivity with respect to structural dimensions and material
 properties in the resulting design.
