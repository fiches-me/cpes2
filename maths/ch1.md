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

> [!important] 
> Notre but va être de calculer cette limite pour en déduire le comportement de notre série. On va donc beaucoup étudier la suite en elle même, car si la suite stagne, la série va aussi !
> 
> Globalement, il faut que la suite **"stagne" vers 0** pour que la série stagne, car c'est une suite de sommes et non une suite classique :)

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

## Séries de références

### Série **géométrique**

> [!définition] 
> Une série **géométrique** est une série de la forme $\sum q^n$

Par définition, la série est **convergente** si $|q| < 1$ et dans ce cas $$\sum_{n=p}^{+\infty} q^n = \frac{q^p}{1 -q}$$

### Série *géométrique dérivée première*

> [!définition] 
> Une série **géométrique dérivée première** est une série de la forme $\sum nq^{n-1}$ pour $n \ge 1$.

Par définition, la série est **convergente** si $|q| < 1$ et dans ce cas $$\sum_{\color{red}n = 1}^{+\infty} nq^{n - 1} = \frac{\color{red}1}{(1 -q)^{\color{red}2}}$$

### Série *géométrique dérivée deuxième*

> [!définition] 
> Une série **géométrique dérivée première** est une série de la forme $\sum n(n-1)q^{n-2}$ pour $n \ge 2$.

Par définition, la série est **convergente** si $|q| < 1$ et dans ce cas $$\sum_{\color{cyan}n =2}^{+\infty} n(n-1)q^{n -2} = \frac{\color{cyan}2}{(1 -q)^{\color{cyan}3}}$$

### Série **de Reimann**

> [!définition] 
> Une série **de Reimann** est une série de la forme $\sum \frac 1{n^\alpha}$

Par définition, la série est **convergente** si $\alpha < 1$. *Il n'y a pas de formule générale pour calculer la somme de la série.*

### Série **exponetielle**

> [!définition] 
> Une série **exponetielle** est une série de la forme $\sum \frac{x^n}{n!}$

Par définition, la série est **toujours convergente** et on a : $$\sum_{n=0}^{+ \infty}\frac{x^n}{n!} = e^x$$

## Méthode

Notre but est *presque toujours* de calculer la somme des séries et donc de définir leur nature.

**Inversion des fractions avec les séries ?**

## Séries absolument convergentes

> [!définition]
> Une série est **absolument convergente** si $\sum |u_n|$ est convergente.
