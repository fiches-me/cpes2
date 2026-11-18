---
title: Clustering
order: 4
---

# Unsupervised Clustering

Le clusturing non supervisé correspond à des algorithmes de données non étiquetés par des humains trient par eux même leurs données.

*Comment trouver des similitudes ?*

On détermine un nombre de groupe $k$ à déterminer, suffisamment distant des un aux autres. *Combien de partitions créer ?*

## Dénombrement

$\mathcal{P}$ correspond à tout les sous-ensembles finies de E. On sait que $| \mathcal{P}(E)| = 2^n$.

Une partition est un ensemble de sous ensemble. L'ensemble de partitions possible sont égale à *xxx*. Pour nos 96 départements, ça fait déjà $2.6 \times 10 ^{56}$, beauuucoup trop.

**Ici, un groupe est un ensemble de données, aka une patate dans un espace.**

## Algorithme K-means

La moyenne d'une liste d'observation s'écrit avec des barres, 

$$\bar{\mathbf{x}} = [\bar{\mathbf{x}}_1, \dots, \bar{\mathbf{x}}_j, \dots, \bar{\mathbf{x}}_p]^T$$

Si on prend un groupe individuel $C_g \in \{1, \dots, n\}$,  alors la moyenne **centrée** équivaut à replacer n par le cardinal. 

$$\bar{\mathbf{x}}_{gj} = \frac 1 {n_g} \sum_{i \in C_g} \mathbf{x}_{ij}$$

Pour calculer la dispersion entre des groupes, ***externe***, on **calcule la distance** et on *la recentre* :

$$\sum_{g=1}^k\color{blue}n_g\color{orange}|| \bar{\mathbf{x}}_g - \bar{\mathbf{x}}||$$

On peut aussi calculer la dispersion dans un groupe, ***interne*** :

$$\sum^k_ {g=1} \sum_{i \in C_g} ||\mathbf{x}_i - \bar{\mathbf{x}}_g||^2$$

> [!abstract] 
> Dans la pratique, on va essayer de maximiser la dispersion externe et minimiser la dispersion interne (sachant que l'un implique l'autre). *Comme un critère est suffisant, on va utiliser la dispersion interne.*

On va chercher par itérations k moyennes et k centres pour minimiser la dispersion. On note $c_i^{(h)}$ le groupe à lequel appartient $\mathbf{x}_i$ au temps $h$. On peut alors noter nos groupes $C_g^{(h)} = \{ i : c_i ^{(h)} = g \}$.

## Hiérarchie aglomérative 
