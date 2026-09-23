---
title: TD2
---

# TD2

```python
from Noeud import Noeud

tas1 = Noeud(Noeud(Noeud(None, 3, None), 2, None), 1, Noeud(Noeud(None, 5, None), 4, Noeud(None, 6, None)))
tas2 = Noeud(Noeud(Noeud(None, 5, None), 4, Noeud(None, 6, None)), 3, Noeud(Noeud(None, 12, None), 9, Noeud(None, 15, None)))

def minTas(n : Noeud) -> int:
    return n.v

def maxTas(n: Noeud) -> int:
    if n.estFeuille():
        return n.v
    if n.g is None:
        return maxTas(n.d)
    if n.d is None:
        return maxTas(n.g)
    g = maxTas(n.g)
    d = maxTas(n.d)

    if g > d:
        return g
    return d

def FUSION(t1 : Noeud, t2: Noeud) -> Noeud:
    if t2 is None:
        return t1
    if t1 is None:
        return t2
    if minTas(t1) <= minTas(t2):
        return Noeud(FUSION(t1.d, t2), t1.v, t1.g)
    else:
        return Noeud(t2.g, t2.v, FUSION(t1, t2.d))

def retireTas(n: Noeud) -> Noeud:
    return FUSION(n.g, n.d)


def ajouteTas(i: int, n: Noeud) -> Noeud:
    if n is None:
        return Noeud(None, i, None)
    if i < minTas(n):
        return Noeud(FUSION(n.g, Noeud(None, n.v, None)), i, n.g)
    else:
        return FUSION(ajouteTas(i, n.g), FUSION(n.d, Noeud(None, n.v, None)))


print(tas1)
print(tas2)

print(minTas(tas1))
print(minTas(tas2))
print(maxTas(tas1))
print(maxTas(tas2))

print(FUSION(tas1, tas2))

print(retireTas(tas1))
print(retireTas(tas2))

print(ajouteTas(93, tas1))
print(ajouteTas(93, tas2))
print(ajouteTas(2, tas1))
print(ajouteTas(7, tas2))
print(ajouteTas(1, tas1))
print(ajouteTas(1, tas2))

```
