---
title: xxx
order: 3
---

# Linear Regression

Before starting, let's put on the table our dataset infos:
- $n = 342$
- $x_i$ will be the flipper length (in mm), $y_i$ the body mass (g)
  → **Can we predict one from the other?** 

*We are switching from descriptive to links!*

**Covariance** between $x$ & $y$ is computed as follows:

$$cov(\boldsymbol{x}, \boldsymbol{y}) = \frac 1n \sum _{i =1} ^n (x_i - \bar{x})(y_i - \bar{y})  \frac 1n \sum _{i =1} ^n x_i y_i - \bar{x} \bar{y}$$
Covariance is:
- positive, negative or zero
- the product of the unit of $x$ and $y$

It's affine. cov(a +bx, c + dy) = bd cov(x, y)
