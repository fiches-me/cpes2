---
title: Informatique - Rappels
tags:
  - revisions
  - définitions
---

# Informatique - Rappels

## Programmation orientée objet

Cette année, nous allons étudier de nouveaux objets : Nœuds, Arrêtes, Graphes... Il est donc important de comprendre nos objet déjà existant et comment nous les avons construit. 

En python, il existe quelques types natifs que nous utilisons souvent : les `int` (entiers), `float` (réels), `bool` (booléens), `list`, (tableau)...

Nous avons également implémenté nos propres types, via les classes python.

Pour définir un object, on utilise le mot clef `class` suivit du nom de la classe.
On définit ensuite un constructeur, une fonction qui s'execute quand on crée une *instance* de notre classe (une variable de type de notre classe) qui contient les données importantes. Cette fonction, en python, doit **toujours** se nommer `__init__(self, args...)`. 

## Classes Importantes

### Pile 

La première classe étudiée est la **Pile**. Elle possède une structure **LIFO**, *Last In, First Out*, qui signifie donc qu'un élément inséré dans une pile sera en haut de la pile et donc renvoyé en premier. [Voir le cours](https://cpes.fiches.funa.dev/info/ch13)

Voici un exemple d'implémentation d'une pile à partir d'une `list` python.

```python
class Pile:
  def __init__(self):
    self.t = []
    
  def __repr__(self):
    res = "[ "
    for i in self.t:
      res += str(i)
      res += ", "
    res = res[:-2]
    res += " )"
    return res
    
  def empiler(self, i):
    self.t.append(i)
    
  def depiler(self):
    if not self.estVide():
      return self.t.pop()
    raise ValueError("La pile est vide")
    
  def dessus(self):
    return self.t[-1]
    
  def taille(self):
    return len(self.t)
    
  def estVide(self):
    return self.t == []
```

### File 

La structure de donnée des Files est très similaire à celle des Piles. Elle suit une structure **FIFO**, pour *First In, First Out*, qui signifie donc que la première valeur inséré dans la file sera la première renvoyé si on défile la pile.

On peut créer la classe file à partir d'une `list` python. Mais pour entertainer à utiliser les piles, on peut également utiliser deux piles.

```python
from pile import Pile

class File:
  def __init__(self):
    """Constructeur de la classe"""
    self.entree = Pile()
    self.sortie = Pile()
    
  def __repr__(self):
    res = "] "
    for i in self.t:
      res += str(i)
      res += ", "
    res = res[:-2]
    res += " ["
    return res
  
  def __retoure__(self):
    """
    En python, on considère que les fonctions entourés de "__"
    ne sont pas "publiques" et doivent rester interne à notre classe.
    Ici, la fonction est uniquement utilisé pour ne pas répéter du code.
    """
    if self.sortie.estVide():
      while not self.entree.estVide():
        self.sortie.empiler(self.entree.depiler())
    
  def enfiler(self, i):
    self.entre.empiler(i)
    
  def defiler(self):
    if self.sortie.estVide(): self.__retourne__()
    return self.sortie.depiler()
    
  def dessus(self):
    if self.sortie.estVide(): self.__retourne__()
    if not self.sortie.estVide():
      return self.sortie.dessus()
    raise ValueError("La pile est vide")
    
  def taille(self):
    return self.entree.taille() + self.sortie.taille()
```

### Listes Chaînées

...

```python
class Cellule:
  def __init__(self, valeur, suivant):
    self.v = valeur
    self.s = suivant
```

Une liste chainée `1 -> 2 -> 3` s'écrirait de la manière suivante :

```python
l = Cellule(1, Cellule(2, Cellule(3, None)))
```

## Trie

Une autre partie importante de la manipulation d'object en informatique consiste à faire des **tries**. On souhaite souvent trier nos données en ordre croissant pour appliquer d'autres algorithmes de façon plus efficace ensuite.

Il existe, à notre connaissance, deux grandes façon de trier un tableau :

### Tri par sélection (Piles)

```python
from pile import Pile

def tri_selection_pile(tab : list[Pile]):
  for i in range( len(tab) - 1):
    min = float("inf")
    pi = None
    for j in range ( i, len(tab) - 1)
      if tab[j].taille < min:
        min = tab[j].taille
        pi = tab[j]
    le = tab[i]
    tab[i] = pi
  return tab
```

### Tri par insertion (Files)

```python
from file import File

def trie_insertion_file(tab : list[Pile]):
  for i in range( 1, len(tab)):
    pi = tab[i]
    k = i - 1
    while pi.taille > tab[k].taille:
      tab[k + 1] = tab[k]
      k -= 1
    tab[k + 1] = pi
  return tab
      
```

> [!INFO] Information
> Il est aussi possible d'utiliser des files sur le trie par sélection ou des piles sur le trie par insertion. Ce ne sont que des exemples. 
