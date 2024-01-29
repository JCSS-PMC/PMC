# Annex D:Bayesian Interpretation of Probabilities

## Introduction

This JCSS Probabilistic Model Code offers distribution functions and corresponding parameter models for loads and structural properties in order to carry out failure probability calculations for comparison with specified reliability targets. This annex gives guidance on the interpretation of both input and results of those calculations.

For the sake of discussion three possible alternatives of interpretation will be mentioned:

1. the frequentistic interpretation
2. a purely formal interpretation
3. the Bayesian interpretation

They will be discussed in the following section.

## Discussion

The *frequentistic* interpretation is quite straight forward. It means that if one observes for a long period of time, say {math}`T`, a large set of say {math}`N` similar structures, all having a failure rate of {math}`p` [1/year], one expects the number of failures not to deviate too far from {math}`p T N`. The deviation should fall within the rules of combinatory probabilistic calculations. Such an interpretation, however, can only be justified in a stationary world where the amount of statistical or theoretical evidence for the all distribution functions is very large. It should be clear that such a frequentistic interpretation of the failure probabilities is out of the question in the field of structural design. In almost all cases the data is too scarce and often only of a very generic nature. Note, however, that a frequentistic interpretation still can be used in a conditional sense. The statement that, given a set of statistical models for the various variables, a structure has some failure probability, is meaningful and helpful.

The interpretation mentioned above given as second, that is the *formal* approach, gives full credit to the fact that the numbers used in the analysis are based on (common) ideas rather than statistical evidence. The probabilistic design is considered as a strictly formal procedure without any meaning or interpretation. Such a procedure can be believed to be a more rich and consistent design procedure compared to for instance a Partial Factor Method or Allowable Stress method. The basic philosophy is that a probabilistic design procedure, running on the average the same design result as its successful predecessors, is at least as good as or even better than the other methods. So calibration on the average result is the key point and the absolute values of the distributions and the failure probabilities have no meaning at all. An alternative code, prescribing higher standard deviations (resulting in higher failure probabilities) and corresponding higher target probabilities is considered as fully equivalent.

To some extent this formal interpretation has many advantages, but is difficult to maintain. In many cases, it is at least convenient if the various values in the probabilistic calculations have some meaning in the real world. It should be possible, for instance, to consider the distribution functions in this code as the best estimate to describe our lack of knowledge and use them as priors for Bayesian updating procedures in the case of new data. It should also be possible to use the models for decision making in structural design and optimisation procedures for target reliabilities. If this cannot be done the method loses many features of its attraction.

This leads into the direction of a *Bayesian* probability interpretation, where probabilities are considered as the best possible expression of the degree of belief in the occurrence of a certain event. The Bayesian interpretation does not claim that probabilities are direct and unbiased predictors of occurrence frequencies that can be observed in practice. The only claim is that, if the analysis is carried out carefully, the probabilities will be correct if averaged over a large number of decision situations. The requirement to fulfil that claim, of course, is that the purely intuitive part is neither systematically too optimistic nor systematically too pessimistic. The calibration to common practice on the average may be considered as an adequate means to achieve that goal.

The above statement may sound vague and unsatisfactory at first sight. There seems to be an almost unlimited freedom to make unproven assessments based on a very individual intuition only. In this respect, one should keep in mind that:

1) where data is lacking, statistical parameters like means and standard deviations are not taken as deterministic point estimates but as random quantities usually with a wide scatter; in this code the scatter is not the opinion of an individual engineer, but it is based on the judgement of a group of engineers. 

2) where data is available, estimates can (and often should) be improved on the basis of it; the minimum requirement is that intuitive probability models should not be in contradiction with the data.

Within the Bayesian Probability Theory these starting points have been rigorously formalised. As long as no data is available, a so called uninformative or vague prior estimate is chosen. Given observations, the prior can be updated to a so called posterior distribution, using Bayes' Theorem. For details the reader is referred to Part 3.0, [Material Properties](../part-03/general-principles.md), [General Principles](../part-03/general-principles.md), [Annex A](../part-03/annex-A-bayesian-evaluation-procedure-for-the-normal-and-lognormal-distribution–characteristic-values.md). It should be noted that, in the case of sufficient data, this procedure will tend to probability statements that can be interpreted in a purely frequentistic way.

Data may of course become available in blocks: in such a case the posterior distribution resulting from the first block may be used as a prior distribution for the second data block. That is, in fact, precisely what is present in the various chapters of Parts [2](../part-02/general-principles.md) and [3](../part-03/general-principles.md): the distributions given can often be considered as "data based priors" based on data from a generic world wide population. These models can be "updated" if data of a specific site or a specific producer are available.

Practically spoken, lack of statistical data may lead to (1) uncertainties in statistical parameters (mean, standard deviation, etc) and (2) uncertainty in the type of distribution (normal, lognormal, Weibull, etc). It turns out that the latter type of uncertainty needs unrealistic much data to get a substantial reduction, while calculation results may be very sensitive to it. Also, such large data sets fulfilling the stationarity requirement may hardly be available. It is exactly on this point that there is a need to standardise the input. It should be noted that in this code most distribution types have the nature of a "point estimate", neglecting to some extend the distribution uncertainty.

## Conclusion

The conclusion of the foregoing is that distributions and probabilities in this Model Code should be given a Bayesian degree of belief type interpretation. One may use the distributions as a start for updating in the presence of specific structure related data and as a basis for optimisation.

## Some reflections for closure:

(1) The numbers given in this code do not include the effect of gross errors. This is one of the main sources of the deviation between calculated probabilities and failure frequencies in practice.

(2) The justification for a Bayesian probabilistic approach in decision making is that it makes the anyhow inevitable judgement part explicit and minimises the influence of it. The return to so called deterministic procedures because of a lack of statistical data is no realistic alternative.

(3) In the Bayesian procedure the prior, if no explicit data is available, is often referred to as "subjective" or "person dependent". In the case of this code this would not be the right terminology. The priors given are not the result of the ideas and experience of a single individual, but of a large group of experts. This gives the distributions some flavour of objectivity, however, of course, still on an intuitive basis.

(4) The system of given distributions and their use in Bayesian updating and Bayesian decision procedures may be considered as a formal procedure in itself.