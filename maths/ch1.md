---
title: Séries Numériques
---

# Séries Numériques

## Introduction

### Définition

La définition d'une série est la suivante.

> [!définition] 
> Soit une suite $(u_n)$. Une **série** de terme général $u_n$, notée $\sum_{n \ge n_0} u_n$ (ou $\sum u_n$ lorsque $n_0 = 0$) est une suite de *sommes partielles* (elles même notés $(S_n)_{n\ge n_0}$) où pour tout entier naturel $n \ge n_0$ on a $S_n = \sum_{k=n_0}^n u_k$.

Malgrès le symbole de somme, les séries ne sont pas des *sommes* mais des *suites* !

On va chercher les natures des séries que nous utiliseons, car une certaine nature peut donner accès à plus de propriété. Étudier la nature d'une suite correspond à trouver sa limite, et on la calcule de la manière suivante :

> [!définition] 
> La **limite** d'une série (appelée **somme de série**) correspond à la limite de la suite $(S_n)$. Si elle est finie, on dit que la série est *convergente*. Sinon, elle est *divergente*

Si la limite existe **et uniquement si elle existe**, on peut alors écrire $\sum_{k_0}^{+\infty} u_k$. On calculera donc les sommes partielles avant les limites complète pour s'assurer de ne pas écrire de contre sens.

### Propriétés

Il existe plusieurs propriétés "de base" sur les séries :

- On ne change pas la nature d'une série (convergente ou divergente) en suprimmant un nombre fini de termes. $\sum_{n \gt n_1>n_0} \sim \sum_{n \gt n_0}$ 
- Si une série de terme général $u_n$ converge, alors $\lim_{x\to\infty} u_n = 0$ (mais pas de réciproques).
- *La contraposée est aussi valable,* si la limite ne vaux pas 0 alors la suite est divergente (mais pas de réciproques).
- Les séries sont linéaires à condition d'êtres réelles (donc convergentes). De plus, si la série $\sum v_n = \sum \lambda u_n$, alors $\sum v_n = \lambda \sum u_n$ et la série de $v_n$ a la même nature que celle de $u_n$.

### Séries à termes positifs

De plus, pour des séries strictement croissante (et inversement avec décroissant) :

- Si une série possède un majorant, alors elle est convergente
     -> on cherche alors un majorant de $u_n$ puis on le somme 
- On également peut comparer les séries et les sommes de séries
- Si $u_n \sim v_n$ alors leurs série sont de même nature.

### Séries Alternés

Il existe d'autres propriétés plus "niches"

- Si $u_n$ est une suite réelle décroissante convergant vers 0, alors la série $\sum (-1)^n u_n$ est convergente.

## Méthode

< en cours de rédaction >
