---
title: Intervalles de confiances
order: 2
---

# Intervalles de confiances

## Introduction

L'un des but principal des statistiques est **d'estimer** des paramètres de loi connus mais de paramètres inconnus. 

Dans certain cas, il n'existe pas de calculs certains. On réalisé alors des **intervalles** pour encadrer nos paramètres selon un certain taux d'erreur.

> [!définition] 
> On appelle **intervalle de confiance** $1 - \alpha$ pour un paramètre $\theta$ un interval *aléatoire* $I_n (\theta) = [I^-_n ; I^+_n]$ tel que
> 
> - $I^-_n$ et $I^+_n$ sont des **statistiques** (qui dépendent donc des **données**)
> - Pour le $\theta$ en question, $\mathbb{P} ( \theta \in I_n (\theta)) = 1 - \alpha$

Parfois, il n'est pas possible de définir/calculer de telles intervalles. Il est aussi possible d'utiliser deux autres outils :

1. Les **intervalles par excès** avec $\mathbb{P} ( \theta \in I_n (\theta)) \ge 1 - \alpha$
2. Les **intervalles asymptotiques** avec $\mathbb{P} ( \theta \in I_n (\theta)) \longrightarrow_n 1 - \alpha$

> [!hint] Remarque
> Plus on accord un niveau de confiance élevé, plus l'intervalle sera grande car on accepte moins d'erreur. 

## Intervalles de confiance pour la moyenne

Selon les données connus, on utilisera plusieurs intervalles différentes 

### 1. Variance Connue *ou* **Z-int Conf**

Ces intervalles de confiances se construisent pour des v.a.i.i.d qui suivent **une/des loi normale(s)**.

> [!définition] Proposition
> Soit $(\mathcal{X}_i)_{1 \ge i \ge n}$ des v.a.i.i.d selon $\mathcal{N} (\mu, \sigma^2)$ avec $(\mu, \sigma) \in \mathbb{R} \times \mathbb{R}_*^+$.
> Soit $\alpha \in ]0 ; 1[$. Un **intervalle de confiance pour $\mu$ de niveau $1 - \alpha$** est défini par :
>
> $$I_n = [\bar{\mathcal{X}_n} - q_{1 - \frac\alpha2} \frac{\sigma}{\sqrt n}; \bar{\mathcal{X}_n} +  q_{1 - \frac\alpha2} \frac{\sigma}{\sqrt n}$$
>
> Ou $q_{1 - \frac \alpha 2}$ est le quantile de la loi **normale centrée réduite** tel que
>
> $$\mathbb{P}(\mathcal{Z} > q_{1 - \frac \alpha 2}) = 1 - \frac \alpha 2$$

::: details Exemple

On étudie l'âge de divorce d'une population de 100 individus divorcés une unique fois. On suppose ces individus indépendant et on suppose également qu'il existe $\mu$ et $\sigma ^2$ tel que l'individu $i \in \textlbrackdbl 1 ; 1000 \textrbrackdbl$
:::

::: details Démonstration

On dispose de vaiid selon des $\mathcal{N}(\mu, \sigma^2)$ et on a vu que $\bar{X}_n \sim \mathcal{N}(\mu, \frac{\sigma^2}n)$.

Par renormalisation, $\frac{\sqrt{n}}{\sigma} ( \bar{X_n} - \mu) \sim \mathcal{N}(0, 1)$

...

- Donc $\mathbb{P}(-q_{1 - \frac \alpha 2} \le \frac{\sqrt{n}}{\sigma} ( \bar{X_n} - \mu) \le q_{1 - \frac \alpha 2}) = 1 - \alpha$
- Donc $\mathbb{P}(- \frac{\sigma}{\sqrt{n}} q_{1 - \frac \alpha 2} \le (\bar{X_n} - \mu) \le \frac{\sigma}{\sqrt{n}} q_{1 - \frac \alpha 2}) = 1 - \alpha$
- Donc $\mathbb{P}(- \bar{X_n} \frac{\sigma}{\sqrt{n}} q_{1 - \frac \alpha 2} \le - \mu \le \bar{X_n} \frac{\sigma}{\sqrt{n}} q_{1 - \frac \alpha 2}) = 1 - \alpha$
- Donc $\mathbb{P}(\bar{X_n} - q_{1 - \frac \alpha 2} \frac{\sigma}{\sqrt{n}} \le \mu \le \bar{X_n} +  q_{1 - \frac \alpha 2} \frac{\sigma}{\sqrt{n}}) = 1 - \alpha$

On obtient donc l'intervalle de confiance :

$$\mathbb{P}(\mu \in [\bar{X_n} - q_{1 - \frac \alpha 2} \frac{\sigma}{\sqrt{n}} ;\bar{X_n} +  q_{1 - \frac \alpha 2} \frac{\sigma}{\sqrt{n}}]) = 1 - \alpha$$

:::

### 2. Variance Inconnue

On va utiliser la même formule mais avec une estimation de la variance

> [!définition] Définition : Écart Type Corrigé
> L'écart type corrigé d'une série de réalisation $(X_i)_{1 \le i \le n}$ es
> 
> $$S_n^2 = \frac{1}{n-1} \sum_{i = 1}^n (X_i - \bar{X_n})$$

Il faut maintenant étudier la loi que suit $(\bar{X_n} - \mu ) \frac{\sqrt n}{S_n}$ pour pouvoir appliquer notre preuve précédente.

> [!définition] Loi du **chi-2** 
> Soit $(X_i)_{1 \le i \le n}$ des vaaid selon des $\mathcal{N}(0, 1)$. Alors la loi de $\mathcal{Z} = \sum_{i=1}^n X_i^2$ est appelé loi du $\chi ^2$ à n degrés de libertés et on note $\mathcal{Z} \sim \chi_n^2$.
> 
> Cette loi vérifie $\mathbb{E} = n$ et $\mathbb{V} = 2n$

On admet que, avec $(X_i)_{1 \le i \le n}$ vaaid $\sim \mathcal{N}(\mu, \sigma^2)$, $\color{red}\frac{n - 1}{\sigma ^2} S_n^2 \sim \chi^2_{n - 1}$

> [!définition] Loi de **Student**
> Soient $\mathcal{Z} \sim \mathcal{N}(0, 1)$ et $\mathcal{Z}_n \sim \chi^2_n$. La loi de la variable aléatoire $T_n = \frac{\mathcal{Z}}{\mathcal{Z}_n/n}$
## Intervalles de confiance pour la variance

