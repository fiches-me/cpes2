---
title: Intervalles de confiances
order: 2
---

# Intervalles de confiances

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
>

$$I_n = [\bar{\mathcal{X}_n} - q_{1 - \frac\alpha2} \frac{\sigma}{\sqrt n}; \bar{\mathcal{X}_n} +  q_{1 - \frac\alpha2} \frac{\sigma}{\sqrt n}$$

### 2. Variance Inconnue *ou* **x**

## Intervalles de confiance pour la variance
