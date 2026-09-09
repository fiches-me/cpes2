---
title: "ℹ️ SDD: Introduction"
contact: edgar.jaber@polytechnique.edu
---

# ℹ️ SDD: Introduction

## Variables discrètes (qualitatives)

Nous allons mettre l'accent sur la partie **qualitatives** de nos v.a.. Il faut **extraire** l'information pour la rendre **utile**. On voudrait trouver une **distribution** (*ensemble des données*), **tendance centrale** (*niveau moyen*), **dispersion** (*écart*)... Mais dans certain cas, les variables ne sont pas numériques : elle sont... **qualitatives**. Le genre, une couleur en sont des exemples.

Nous allons voir deux types d'analyses : les analyses **univariés** où on observe la distribution d'une seule variable et les analyses **bivariés** où on observe *plusieurs classes* pour voir si **elles sont liés**.

Quelques notations :
- $n$ correspondra au nombre d'observations
- $i$ un indice d'observation $i \in \{1, \dots n\}$
- $x$ une variable d'interet ou classe
- $x_i$ une valeur de $x$ pour l'observation $i$
- $\mathcal{X}$ correspondra à l'ensemble des modalités (liste des classes) $x_i \in \mathcal{X}$. 
- $k$ le nombre de modalités

Ici, les variables indicatrices $\mathbb{1}$ seront notés $u_{\color{red}i\color{blue}a}$. Elle renverra $1$ si $x_{\color{red}i} = \color{blue}a$, $0$ sinon.