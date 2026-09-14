---
title: 🔣 Science des Données
contact: edgar.jaber@polytechnique.edu
---

# 🔣 Science des Données : Introduction

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

On associe à la modalité $a$  de la variable $x$ le vecteur $u_a$ de dimension $n$ :

$$u_a = [ u_{1a}, u_{2a}, u_{3a}, \dots, u_{na}]$$

L'effectif $n_a$ de la modalités $a$ est $$n_a = |\{i : x_i = a \}| = \sum_{i=1}^n u_{ia}$$

*La fréquence marginale est le pourcentage de l'effectif de la modalité par rapport à l'effectif total.*

Nous allons essayer de prouver la proposition $\sum_{a = 1}^k u_{ia} = n$:

$$\sum_{a = 1}^k u_{ia} = \sum_{a = 1}^k \sum_{i=1}^n u_{ia} = \sum_{i=1}^n\sum_{a = 1}^k u_{ia} = \sum_{i=1}^n1 = n$$

> [!tip] Idée ¶
> $\sum_{a = 1}^k u_{ia}$ vaut $1$ car $u_{ia}$ ne peux avoir qu'une classe en même temps.

### Deux variables

> [!note] Rappel :  Produits scalaires
>
> $$\langle \bar{1}, \bar{u_a} \rangle = \sum_{n=1}^n 1 \times u_{ia} = \sum_{i = 1}^n u_{ia} = n_a$$

L'effectif conjoint ou croisé d'une classe $n_{ab}$ est le produit scalaire suivant :

$$n_{ab} = \langle u_a, v_b \rangle$$$$\sum_{a=1}^k\sum_{b=1}^l n_{ab} = n$$

*En gros, on somme le nombre de personnes avec classe 1 ET classe 2. Somme d'une intersection.*

### Fréquence marginales et conditionnelles

#### Fréquences marginales

$n_{a+}$ est l'effectif marginal de la modalité $a$ de $x$ : $\sum_{b=1}^l n_{ab}$. Cela correspond à l'ensemble de personnes en classe a (de n). Globalement, $n_{a+} = n_a$. *Idem pour la fréquence marginale.*

#### Fréquence relative

< ... >

### Plus de deux variables

On ajoute le genre : `x = Class`, `y = Survived`, `z = Sex`. 

On bloque la troisième variable pour obtenir des stats.
