# Excentricities

**List of symbols:**

$\begin{array}{ll}\rho(i, j) & = \text { coefficient of correlation for two columns } i \text { and } j \\
e & = \text { average eccentricities } \\
f & = \text { central eccentricity due to curvature } \\
\phi & = \text { out of plumbness } \\
\mu & = \text { mean } \\
\sigma & = \text { standard deviation }\end{array}$

## Introduction

The bearing capacity of slender elements depends to some extend on the difference between the actual and theoretical lining, the so called excentricity. In this section we will present the models for the excentrities of columns in braced and unbraced frameworks.

## Basic model

In the analysis three types of eccentricities can be distinguished (see {numref}`fig-the-three-basic-excentiricties`)

- the average excentricity
- the initial curvature
- the out of plumbness $\phi$

For the braced frame the out of plumpness is only relevant for the bracing system, but not for the column under consideration; for the unbraced frame especially the out of plumpness is usually dominant over the end point eccentricity and the curvature.

```{figure} ../part-03/images/the-three-basic-excentiricties.jpg 
:name: fig-the-three-basic-excentiricties

The three basic excentiricties $e$, $f$ and $\phi$
```

## Probability modelling

*Distribution type, mean and scatter*

The probabilistic model for the three basic parameters are presented in {numref}`table-statistical-properties-for-excentricities-for-steel-and-concrete-columns`. For all three cases it is assumed that the distribution is symmetrical around zero and that small eccentricities are more likely than large ones, although large ones are more dangerous. Note that in special cases nonsymmetrical cross sections may have $\mu(\mathrm{f}) \neq 0$ due to the fabrication process.

In many cases only the absolute values of the excentricities are important. From the table it can be derived that these absolute values are distributed with a truncated normal distribution, the truncation point being the mean of the untruncated distribution. The absolute value has a mean of about 0.80 times the standard deviation of the untruncated distribution; the coefficient of variation is 0.75 .

```{table} Statistical properties for excentricities (for steel and concrete columns)
:name: table-statistical-properties-for-excentricities-for-steel-and-concrete-columns
| $X$ | description | type | $\mu$ | $\sigma$ |
| :--- | :--- | :--- | :--- | :--- |
| e | average excentricity | normal | 0 m | L/1000 |
| $f$ | out of straightness | normal | 0 m | L/1000 |
| $\phi$ | the out of plumbness | normal | 0 m | 0.0015 rad |
```

All eccentricity parameters $e$, $f$ and $\phi$ shall be regarded as independent variables.

*Time and spatial dependency*

In general eccentricities may be treated as being time independent. An exception might be timber where in particular the initial curvature may depend on the moisture content.

For the spatial fluctuation the dependency between various columns in one building is important. In this code the average eccentricity $e$ as well as the out of straightness $f$ will be considered as being uncorrelated for all members. For $\phi$ the following correlation pattern is recommended:

$\rho\left(\phi_{i}, \phi_{j}\right)=0,5$ for two columns on the same floor   
$\rho\left(\phi_{i}, \phi_{j}\right)=0$ for columns on different floors

In this model some possible negative correlation between columns in vertical direction, resulting from (over) corrections for out of plumbness on lower storeys is not considered. This is a conservative assumption.

**Note on applications**

The limit state function for a simple slender column, clamped at the bottom and free at the top, may be presented as:

```{math}
Z=M_{P}-\frac{P_{E}}{P_{E}}-P P \phi h
```

$M_{p}=$ plastic moment

$P=$ vertical load

$P_{E}=$ Euler buckling load

$h=$ height of the column

## References

1. Ellingwood, B., Galambos, Th., MacGregor, J., Cornell, A.: Development of a probability based load criterion for American national standard A58. Building code requirements for minimum design loads in buildings and other structures. NBS special publication 577, June 1980

2. Bjorhovde, R.: A probabilistic approach to maximum column strength. Reliability of Metal Structures, ASCE, Speciality Conference, Pittsburgh, 1972.

3. Geometrical and cross-sectional properties of steel structures. Chapter 2. European Convention for constructional steelwork. Second international colloquium on stability. Introductory report, sept. 1976, pp. 19-46, 58-59.

4. Edlund, B., Leopoldson, U.: Monte Carlo simulation of the load carrying capacity of steel beams. Chalmers university of technology, division of steel and timber structures, publ. S71-3 \\& S71-5, Göteborg, 1973.

5. Alpsten, G.A.: Statistical Investigation of the strength of rolled and welded structural steel shapes. Report 39.4, Swedish institute of steel construction, Stockholm

6. Hardwick, T.R., Milner, R.M.: Dimensional Variations - Frame structures for schools. The architects, Journal information library, 20 September 1967, vol. 146, technical study, AJ SfB Ba4, pp. 745-748.

7. Klingberg, L.: Studies on the dimensional accuracy of a column and beam framework. National Swedish building research summaries, R38:1970.

8. Klingberg, L.: Studies of dimensional accuracy in prefab building with flexible joints. National Swedish building research summaries, R28:1971.

9. Maass, G.: Statistische Untersuchungen von geometrischen Abweichungen an ausgeführten Stahlbetonbauteilen. Teil II: Messergebnisse geometrischer Abweichungen bei Stützen, Wänden, Balken und Decken des Stahlbetonhochbaus. Berichte zur Zuverlässigkeitstheorie der Bauwerke, TU München Sonderforschungsbereich 96, Heft 28/1978.

10. Fiorato, A.E.: Geometric imperfections in concrete structures. National Swedish building research. Document D5: 1973.
