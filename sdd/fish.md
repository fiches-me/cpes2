---
title: 🐟 Fish SDD IPP Mi-S1
---

# Fish SDD IPP Mi-S1

# 0. Notations & Conventions

- **Typographie** :
  - **Scalaires** ($x_i, n, k, \ell, \bar{x}, s, a, b$) : Valeurs individuelles, effectifs, moyennes, écarts-types ou indices.
  - **Vecteurs en gras** ($\mathbf{x}, \mathbf{y}, \mathbf{u}_a, \mathbf{v}_b, \mathbf{e}, \mathbf{b}$) : Vecteurs colonnes de dimension $n$ (ou de dimension $p+1$ pour les coefficients), regroupant l'ensemble des observations d'une variable ou d'indicateurs.
  - **Matrices en gras** ($\mathbf{X}$) : Matrice de données de taille $n \times (p+1)$ regroupant les variables explicatives.
  - **Vecteur unité** ($\mathbf{1}$) : Vecteur colonne de dimension $n$ composé uniquement de $1$ ($\mathbf{1} = [1, 1, \dots, 1]^\top$).
- **Variables indicatrices vectorielles** :
  - $\mathbf{u}_a \in \mathbb{R}^n$ : Vecteur dont la composante $u_{ia} = 1$ si $x_i = a$, et $0$ sinon.
  - $\mathbf{v}_b \in \mathbb{R}^n$ : Vecteur dont la composante $v_{ib} = 1$ si $y_i = b$, et $0$ sinon.
  - $\langle \mathbf{u}_a, \mathbf{v}_b \rangle = \mathbf{u}_a^\top \mathbf{v}_b = \sum_{i=1}^n u_{ia} v_{ib} = n_{ab}$ (Effectif conjoint).

## 1. Variables Qualitatives (Discrètes)

Une variable qualitative décrit une qualité ou un attribut non numérique (ex. : couleur des yeux, catégorie socio-professionnelle, classe à bord du Titanic).

- **Variable indicatrice** : Pour une modalité $a \in \mathcal{X}$, on définit la variable indicatrice $u_{ia} = 1$ si $x_i = a$, et $0$ sinon.

- **Effectif d'une modalité ($n_a$)** : C'est le nombre d'observations vérifiant $x_i = a$, calculé par :

    $$n_a = \sum_{i=1}^n u_{ia}$$

    La somme des effectifs de toutes les modalités est égale à l'effectif total :

    $$\sum_{a=1}^k n_a = n$$

- **Fréquence d'une modalité ($f_a$)** : Calculée par la formule $f_a = \frac{n_a}{n}$. La somme des fréquences de toutes les modalités est égale à $1$ :

    $$\sum_{a=1}^k f_a = 1$$

- **Représentation graphique** : On représente la distribution d'une variable qualitative à l'aide de **diagrammes circulaires**.

### Analyse Bivariée (Deux variables qualitatives)

- **Table de contingence (ou fréquences conjointes)** : Croise deux variables $x$ (à $k$ modalités) et $y$ (à $\ell$ modalités). *Nombres d'individus avec a et b.* L'effectif conjoint $n_{ab}$ compte les individus ayant à la fois la modalité $a$ pour $x$ et $b$ pour $y$ :

    $$n_{ab} = \vert{}\{i : x_i = a \text{ et } y_i = b\}\vert{} = \langle \mathbf{u}_a, \mathbf{v}_b \rangle$$

- **Fréquences conjointes** : $f_{ab} = \frac{n_{ab}}{n}$ avec $\sum_{a=1}^k \sum_{b=1}^\ell f_{ab} = 1$.

- **Fréquences marginales** :

    $$f_{a+} = \frac{n_{a+}}{n} = \sum_{b=1}^\ell f_{ab} \quad \text{et} \quad f_{+b} = \frac{n_{+b}}{n} = \sum_{a=1}^k f_{ab}$$

- **Fréquences conditionnelles** : Fréquence de la modalité $b$ de $y$ sachant la modalité $a$ de $x$ :

    $$f_{b\vert{}a} = \frac{n_{ab}}{n_{a+}} \quad (\text{les lignes somment à } 1)$$

- **Paradoxe de Simpson** : Phénomène où une tendance observée au sein de chaque sous-groupe s'inverse lorsque les données sont regroupées, en raison d'un effet de structure (par exemple, une composition asymétrique des groupes).

## 2. Variables Quantitatives Réelles

Une variable quantitative prend des valeurs numériques sur lesquelles des opérations arithmétiques (sommes, moyennes) sont possibles.

### Tableau Synthétique des Indicateurs

|**Indicateur**|**Formule**|**Sens & Propriétés**|
|---|---|---|
|**Moyenne** ($\bar{x}$)|$\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i$|Minimise l'écart quadratique ($\sum_{i=1}^n (x_i - u)^2$). Sensible aux valeurs extrêmes. Opérateur linéaire ($\bar{y} = a + b\bar{x}$).|
|**Médiane** ($m$)|• Impair ($n=2k+1$) : $m = x_{(k+1)}$<br><br>  <br>  <br><br>• Pair ($n=2k$) : $m = \frac{x_{(k)} + x_{(k+1)}}{2}$|Minimise l'écart absolu ($\sum_{i=1}^n \Vert{}x_i - u\Vert{}$). Robuste aux valeurs extrêmes.|
|**Variance** ($\text{var}(\mathbf{x})$)|$\text{var}(\mathbf{x}) = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2 = \frac{1}{n} \sum_{i=1}^n x_i^2 - (\bar{x})^2$|Mesure de dispersion quadratique. Unité au carré (ex. : $\text{m}^2$). Sensible aux valeurs extrêmes. $\text{var}(a + b\mathbf{x}) = b^2 \text{var}(\mathbf{x})$.|
|**Écart type** ($s$)|$s = \sqrt{\text{var}(\mathbf{x})}$|Racine carrée de la variance. Homogène à la variable $x$ (exprimé dans la même unité).|
|**Écart Moyen Absolu** ($\text{mad}(\mathbf{x})$)|$\text{mad}(\mathbf{x}) = \frac{1}{n} \sum_{i=1}^n \Vert{}x_i - m\Vert{}$|Mesure de dispersion absolue basée sur la médiane.|
|**Écart Interquartile** ($\text{IQR}$)|$\text{IQR} = q_{75\%} - q_{25\%} = q_3 - q_1$|Largeur de l'intervalle contenant les 50 % centraux. Robuste. Détecte les valeurs aberrantes (règle de Tukey : hors de $[q_{25\%} - 1.5\text{IQR}, q_{75\%} + 1.5\text{IQR}]$).|
|**Variable centrée réduite** ($z_i$)|$z_i = \frac{x_i - \bar{x}}{s}$|Nombre d'écarts-types séparant $x_i$ de la moyenne. Sans unité, de moyenne $\bar{z}=0$ et de variance $\text{var}(\mathbf{z})=1$.|

### Formule Clé de Huygens

Pour tout réel $u$ :

$$\sum_{i=1}^n (x_i - u)^2 = \sum_{i=1}^n (x_i - \bar{x})^2 + n(u - \bar{x})^2$$

### Visualisation de la Distribution

- **Histogramme** : Découpe l'amplitude en $k$ intervalles de largeur $\delta = \frac{x_{\max} - x_{\min}}{k}$ et compte les effectifs $n_\ell$.

- **Fonction de répartition empirique (ECDF)** :

    $$F_n(t) = \frac{\vert{}\{i : x_i \le t\}\vert{}}{n}$$

    Fonction en escalier allant de $0$ à $1$.

- **Boîte à moustaches (Box-plot)** : Représente synthétiquement les quartiles ($q_{25\%}, m, q_{75\%}$), la moyenne, les moustaches (bornées à $1.5\text{IQR}$) et les points aberrants au-delà.

## 3. Régression Linéaire et Liaison entre Variables

### Liaison entre deux variables quantitatives

- **Covariance** : Mesure la variation simultanée de deux variables $x$ et $y$ :

    $$\text{cov}(\mathbf{x}, \mathbf{y}) = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) = \frac{1}{n} \sum_{i=1}^n x_i y_i - \bar{x}\bar{y}$$

    Propriété affine : $\text{cov}(a + b\mathbf{x}, c + d\mathbf{y}) = bd\,\text{cov}(\mathbf{x}, \mathbf{y})$.

- **Coefficient de corrélation linéaire ($r$ ou $\text{cor}(\mathbf{x}, \mathbf{y})$)** :

    $$\text{cor}(\mathbf{x}, \mathbf{y}) = \frac{\text{cov}(\mathbf{x}, \mathbf{y})}{\sqrt{\text{var}(\mathbf{x})\text{var}(\mathbf{y})}} \in [-1, 1]$$

    Sans unité, il mesure uniquement la force d'une relation linéaire. *(Rappel : corrélation ne signifie pas causalité).*

### Droite de Régression Linéaire Simple

On cherche à expliquer/prédire $y$ par $x$ selon le modèle $y_i \approx a + b x_i$ en minimisant le critère des moindres carrés :

$$C(a, b) = \sum_{i=1}^n (y_i - a - b x_i)^2 = \sum_{i=1}^n e_i^2$$

- **Pente optimale ($\hat{b}$)** :

    $$\hat{b} = \frac{\text{cov}(\mathbf{x}, \mathbf{y})}{\text{var}(\mathbf{x})} = \text{cor}(\mathbf{x}, \mathbf{y}) \frac{s_y}{s_x}$$

- **Ordonnée à l'origine optimale ($\hat{a}$)** :

    $$\hat{a} = \bar{y} - \hat{b}\bar{x} \quad (\text{la droite passe toujours par le point moyen } (\bar{x}, \bar{y}))$$

- **Résidus ($e_i = y_i - \hat{y}_i$)** : De moyenne nulle ($\bar{e} = 0$) et de covariance nulle avec $x$ ($\text{cov}(\mathbf{x}, \mathbf{e}) = 0$).

- **Décomposition de la variance** :

    $$\text{var}(\mathbf{y}) = \text{var}(\hat{\mathbf{y}}) + \text{var}(\mathbf{e})$$

- **Coefficient de détermination ($R^2$)** :

    $$R^2 = 1 - \frac{\text{var}(\mathbf{e})}{\text{var}(\mathbf{y})} = \frac{\text{var}(\hat{\mathbf{y}})}{\text{var}(\mathbf{y})} = \text{cor}(\mathbf{x}, \mathbf{y})^2 \in [0, 1]$$

    Représente la part de variance de $y$ expliquée par le modèle linéaire.

### Régression Linéaire Multiple

Pour expliciter $y$ à partir de $p$ variables $\mathbf{X} = [\mathbf{1}, \mathbf{x}_1, \dots, \mathbf{x}_p]$, le vecteur de coefficients $\mathbf{b}^*$ minimisant $\Vert{}\mathbf{y} - \mathbf{X}\mathbf{b}\Vert{}^2$ est donné par les équations normales :

$$\mathbf{b}^* = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$$
