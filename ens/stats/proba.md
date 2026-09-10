---
title: Outils et rappels de probabilités
order: 1
---
# Outils et rappels de probabilités

## Convergence de variables aléatoires

*Dans cette partie, nous allons définir trois manières que peut avoir une suite de vraiables aléatoires de converger. On considère donc $(X_n)_{n \in \mathbb{N}}$ une suite de variables aléatoires réelles et $X$ une variable aléatoire réelle, sa potentielle limite.*

> [!DÉFINITION]
> On dit que $(X_n)_{n \in \mathbb{N}}$ converge en probabilité vers $X$ lorsque $$\forall \epsilon > 0, lim_{n \rightarrow \infty } \mathbb{P} (|X_n - X| > \epsilon) = 0$$
> On note alors $$X_n \rightarrow^{\mathbb{P}}_{n\rightarrow \infty} X$$

**Exemple**: soit $(X_n)_{n \in \mathbb{N}}$ une suite de variables aléatoires telle quel $\forall n \in \mathbb{N}^*$, $X_n \sim \mathcal{B}(\frac pn)$ avec $p \in ]0, 1[$. Montrons que $(X_n)_{n \in \mathbb{N}}$ converge vers $0$ en probabilités.

💡 *La propriété doit être vraie pour tout $\epsilon$. On prend donc un epsilon quelquonque*

Soit $\epsilon > 0$ alors $\mathbb{P}(|X_n - 0| > \epsilon) = \mathbb{P} (X_n > \epsilon)$

