Let's now take a look at quantitative variables.

With a set of observations $\mathcal{D} = {x_i}_{1 \le i \le n}$ an observation vector, $x = [x_1, x_2, \dots, x_n]^{\text{T}} \in \mathbb{R}$

**How could be summarise the whole observation $x$ by a single typical "central" value?**

*We will take a look at two datasets : [geo.api.gouv.fr] for the population of ***communes*** *&* ***departments****.* In total, we saw $n = 34875$ observations for communes & $n = 101$ for departments. 

We can have criteria for centrality. The **absolute deviation** at value $u$ is

$$C_1 (u) = \sum_{i=1}^n |x_i - u|$$

We can also use **quadratic deviation**:

$$C_2 : \mathbb{R} \longrightarrow \mathbb{R}; \space\space\space\space\space\space C(u) = \sum_{i=1}^n (x_i - u)^2 = ||x - (\mathbb{1} \times u)||^2$$

Where $\mathbb{1} \times u$ is the $n$ vector of $u$ : $(u, u, \dots, u)$. 

> [!HINT]
> Thoses functions behave quite diferently and depend both of the observations $x$.

We can **minimise** those functions, like the quadratic deviation, to get a mean :

$$\bar{x} = \frac 1n \sum_{i=1}^n x_i$$

We use derivatives to prove it. *But how could we do it with $C_1$?* Proposition: order the data (from min to max) and take the k/k+1th data (where $n = 2k$)

We also can compute the **variation**, the spread arround the central value, 

First, **MAD**

$$ mad(x) = \frac 1n \sum _{i=1}^n |x_i -m | = \frac 1n C_1 (m)$$

(‘MAD’ = mean absolute deviation; not to be confused with the median
absolute deviation median i$^{th}$ $|xi − m|$, sometimes also called MAD)

Then **VARIANCE**:

$$ var(x) = \frac 1n \sum _{i=1}^n (x_i - \bar{x})^2 = \frac 1n C_2 (\bar{x})$$

We also use standard deviation to compute homogeneous data against $x$.

You can also calculate a standardised score call **Standardised variable (z-score)** and computed as follow :

$$z_i = \frac{x_i - \bar{x}}s$$

*This transformation destroys units, but is standard over other datas.*

## Drawing histograms

To draw histogram, we need to define some variables

- a min & a max to draw our interval (and/or bounds)
- define the interval width $δ = (xmax − xmin)/k$;
- define $k + 1$ thresholds $tℓ (0 ≤ ℓ ≤ k) by tℓ = xmin + ℓδ$;
- associate to each interval the number of observations it contains:

$$n_ℓ = | {\{ i : x_i ∈ [t_ℓ−1; t_ℓ]  }\} |$$

*Where || refer to the size, so the cardinal of $n_l$*

We can now compute the proportion of observations less or equal to t (**mass** or **density** function)

$$F_n(t) = \frac{\# {\{i : xi ≤ t}\}}n$$

With ordered data, the probability is simple to compute :

$$F_n (x_{(j)}) = \frac jn$$

*Beacause there are j data behind smaller, and n in total*

## Resume

### Central value (**Espérance**)

- Mean $\bar{x}$ minimises $C_2(u) = \sum(x_i − u)^2$
- Median $m$ minimises $C_1(u) = \sum|x_i − u|$
- Huygens: $\sum(xi − u)^2 = \sum (x_i − \bar{x})^2 + n(u − \bar{x})^2$
- Mean is linear: $\bar{y} = a + b\bar{x}$; median more robust

### Dispersion **Variance**

- $\mathbb{V} = var(x) = \frac 1n C_2(x)$, $mad(x) = \frac 1n C_1(m)$
- Std. dev. = $\sqrt{var}$, homogeneous with $x$
- $var(y) = b^2var(x)$; MAD more robust
- z-score $(x_i − \bar{x})/s$: mean $0$, variance $1$

### Distribution

- Histogram: bin counts $n_\mathcal{l}$; choice of $k$ matters
- ECDF $F_n(t)$; quantile  $q_u = x_{(⌈nu⌉)}$ (conventionsvary)
- IQR = q75% − q25%; outliers
beyond 1.5 IQR
- Box-plot bundles quartiles, whiskers, outliers

###  Robustness

- Median, MAD, IQR resist extreme values
- C2-based (mean, variance) are more sensitive
- Skewed data 2 median, quantiles, log scale
