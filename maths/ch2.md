---
title: Matrices & Applications Linéaires
order: 2
---

# Matrices & Applications Linéaires

## Rappels

### $\mathbb{K}$ espaces vectoriels

Les $\mathbb{K}$ espaces vectoriels sont des ensembles de vecteurs, où la dimension $p$ correspond aux nombres de vecteurs qui composent la base de cet espace (notons le $E$).

Une base est une **combinaison linéaire** de vecteurs à la fois **libre** et **génératrice**. *Libre*  signifie que aucun de ses vecteurs ne peut s'exprimer comme une combinaison linéaire des autres (donc **l'ensemble des scalaires $\lambda$ valent 0**). *Génératrice* signifie que aucun de ses vecteurs ne peut s'exprimer comme une combinaison linéaire des autres.

> [!TIPS] Intuition : c'est souvent le nombre d'élément d'un vecteur de cet ensemble.

La **base canonique** est la base la "*plus jolie* d'un certain espace vectoriel. Par exemple, la base canonique de $\mathbb{R}^n$ est $\mathcal{B} = (e_1, e_2, \dots, e_n)$ tel que $e_i = (0, \dots, 0, 1, 0, \dots, 0)$ (avec $1$ en position $i$). 

### Matrices

On note $\mathcal{M}_{\color{red}n, \color{lime}p} (\mathbb{K})$ l'ensemble des matrices à $\color{red}n$ lignes et $\color{lime}p$ colonnes. Son **rang** correspond à **son nombre de pivot**, *ou le nombre de colonnes linéairement indépendantes*.
é
### Applications Linéaires

Une application est dite **linéaire** si $\forall x, y \in E^2, f(x + y) = f(x) + f(y)$. 

> $f(0_e) \ne 0_f \Rightarrow f$ n'est pas une application linéaire

Les applications linéaires peuvent avoir 3 formes particulières
1. Si $E = F$, alors $f$ est un **endomorphisme**
2. Si $F = \mathbb{R}$, alors $f$ est une **forme linéaire**
3. Si $f$ est *bijective*, on dit que $f$ est un **isomorphisme**

## Introduction

Prenons une application **linéaire** de $\mathbb{R}^3$ dans $\mathbb{R}^2$. Il est possible de s'affranchir complètement de la formule qui définit l'application en calculant l'image des 3 éléments de sa base :

1. $f(e_1) = f([1, 0, 0]) = (2, 1) = 2e^\prime_1 + e^\prime_2$
2. $f(e_1) = f([0, 1, 0]) = (1, 0) = e^\prime_1$
3. $f(e_3) = f([0, 0, 1]) = (0, -1) = - e^\prime_2$

*Cela ressemble fort fort à des tableaux...* Et si on le posait dans une matrice ?

$$\mathcal{M}_{\mathcal{B}, \mathcal{B}^\prime}(f) = \begin{pmatrix}2 & 1 & 0\\1 & 0 & 1\end{pmatrix}$$
Cette matrice est **LA matrice de $f$ dans les bases $\mathcal{B}$ et $\mathcal{B}^\prime$.** Ce passage est un **isomorphisme d'espace vectoriel**, c'est donc une action bijective, donc **toute matrice possède une application correspondante.** *Finit les calculs d'applications, on multiplie des matrices pour faire de la magie sur les fonctions !* Et justement, que fait une multiplication de matrices sur leurs applications correspondantes ?

> [!DÉFINITION]
> Soit une application $f$ linéaire de $E$ à $F$ et une application $g$ linéaire de $F$ à $E$. Alors, on a :
> 
> $$\mathcal{M}_{\mathcal{B}, \mathcal{B}^\prime}(g \circ f) = \mathcal{M}_{\mathcal{B}, \mathcal{B}^\prime}(f) \times \mathcal{M}_{\mathcal{B}^\prime, \mathcal{B}^{\prime\prime}}(g)$$

