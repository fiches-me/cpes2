---
title: TD1
---

# TD1

```python
class Noeud:
    def __init__(self, noeud_gauche, valeur, noeud_droit):
        self.g = noeud_gauche
        self.v = valeur
        self.d = noeud_droit

    def afficher_ascii(self, prefix="", is_left=True):
        """Génère une vue ASCII propre et visuelle de l'arbre binaire."""
        res = ""

        # 1. Affichage du sous-arbre droit (situé en haut)
        if self.d is not None:
            res += self.d.afficher_ascii(prefix + ("│   " if is_left else "    "), False)

        # 2. Affichage de la racine courante
        res += prefix + ("└── " if is_left else "┌── ") + "\033[93m" + str(self.v) + "\033[0m\n"

        # 3. Affichage du sous-arbre gauche (situé en bas)
        if self.g is not None:
            res += self.g.afficher_ascii(prefix + ("    " if is_left else "│   "), True)

        return res

    def __str__(self):
        return self.afficher_ascii()

    def __repr__(self):
        return self.afficher_ascii()

    def __len__(self):
        if self.g is None and self.d is None:
            return 1
        elif self.g is None:
            return len(self.d) + 1
        elif self.d is None:
            return len(self.g) + 1
        else:
            return len(self.g) + len(self.d) + 1

    def taille(self):
        return len(self)

    def hauteur(self):
        if self.g is None and self.d is None:
            return 1
        if self.g is None:
            return self.d.hauteur() + 1
        elif self.d is None:
            return self.g.hauteur() + 1
        else:
            return max(self.g.hauteur(), self.d.hauteur()) + 1

    def prefixe(self):
        if self.g is None and self.d is None:
            return str(self.v)
        else:
            res = str(self.v) + ", "
            if self.g:
                res += str(self.g.prefixe()) + ", "
            if self.d:
                res += str(self.d.prefixe()) + ", "

            return res[:-2]

    def infixe(self):
        if self.g is None and self.d is None:
            return str(self.v)
        else:
            res = ""
            if self.g:
                res += str(self.g.infixe()) + ", "
            res += str(self.v) + ", "
            if self.d:
                res += str(self.d.infixe()) + ", "

            return res[:-2]

    def suffixe(self):
        if self.g is None and self.d is None:
            return str(self.v)
        else:
            res = ""
            if self.g:
                res += str(self.g.suffixe()) + ", "
            if self.d:
                res += str(self.d.suffixe()) + ", "
            res += str(self.v) + ", "

            return res[:-2]

    def largeur(self):
        if self.g is None and self.d is None:
            return str(self.v)
        else:
            res = ""
            if self.g:
                res += str(self.g.suffixe()) + ", "
            if self.d:
                res += str(self.d.suffixe()) + ", "
            res += str(self.v) + ", "

            return res[:-2]


    def estFeuille(self):
        return (self.g is None) and (self.d is None)


    def egaliter(self, other):
        if self is None and self is not None or self is not None and other is None:
            return False
        if self.v != other.v:
            return False

        if self.estFeuille() and other.estFeuille():
            return True

        else:
            return self.g.egaliter(other.g) and self.d.egaliter(other.d)

```

```python
from Noeud import Noeud

def peigneG(h: int) -> Noeud:
    n = Noeud(None, h, None)
    l = n
    for i in range(h - 1, 0, -1):
        l.g = Noeud(None, i, None)
        l = l.g

    return n

def parfait(h: int) -> Noeud:
    if h < 2:
        return Noeud(None, h, None)
    else:
        return Noeud(parfait(h-1), h, parfait(h-1))

Arbre1 = Noeud(Noeud(None, "B", Noeud(None, "C", None)), "A", Noeud(None, "D", None))

Arbre2 = Noeud(
    Noeud(
        Noeud(None, "D", None),
        "B",
        Noeud(None, "E", None)
    ),
    "A",
    Noeud(
        Noeud(None, "F", None),
        "C",
        Noeud(None, "G", None)
    )
)

Arbre22 = Noeud(
    Noeud(
        Noeud(None, "D", None),
        "B",
        Noeud(None, "E", None)
    ),
    "A",
    Noeud(
        Noeud(None, "F", None),
        "C",
        Noeud(None, "G", None)
    )
)

Arbre3 = Noeud(Noeud(None, 1, None), 2, Noeud(None, 3, None))

print("Taille: ", Arbre1.taille())
print("Hauteur: ", Arbre1.hauteur())
print(Arbre1)
print("----------------")
print(Arbre1.largeur())
print(Arbre1.prefixe())
print(Arbre1.infixe())
print(Arbre1.suffixe())

print("----------------")

print("Taille: ", Arbre2.taille())
print("Hauteur: ", Arbre2.hauteur())
print(Arbre2)
print("----------------")
print(Arbre2.largeur())
print(Arbre2.prefixe())
print(Arbre2.infixe())
print(Arbre2.suffixe())

print("----------------")
print(peigneG(5))
print(parfait(3))

def nbNoeudsPro(A, k):
    if k <= 2:
        res = 0
        if A.g: res += 1
        if A.d: res += 1
        return res
    else:
        return nbNoeudsPro(A.g, k -1) + nbNoeudsPro(A.d, k - 1)

def nbFeuillePro(A, k):
    if k <= 2:
        if A.estFeuille(): return 1
        return 0
    else:
        return nbNoeudsPro(A.g, k -1) + nbNoeudsPro(A.d, k - 1)

print(nbNoeudsPro(Arbre2, 2))
print(nbFeuillePro(Arbre2, 3))
print(Arbre2.egaliter(Arbre22))
print(Arbre2.egaliter(Arbre1))

def minimun(abr: Noeud):
    j = abr
    while j.g:
        j = j.g
    return j.v

def recherche(abr : Noeud, i : int) -> bool:
    if abr.v == i:
        return True
    else:
        if abr.v <= i:
            if abr.g:
                return recherche(abr.g, i)
            return False
        else:
            if abr.d:
                return recherche(abr.d, i)
            return False


def compte(abr : Noeud, i : int) -> int:
    if abr.v == i:
        res = 1
        while abr.g.v == i:
            res += 1
            abr = abr.g
        return res
    else:
        if abr.v <= i:
            if abr.g:
                return compte(abr.g, i)
            return 0
        else:
            if abr.d:
                return compte(abr.d, i)
            return 0

def ajoutNaif(abr : Noeud | None, i : int) -> Noeud | None:
    if abr is None:
        return Noeud(None, i, Noeud)
    while abr.g and abr.d:
        if abr.v <= i:
            abr = abr.g
        else:
            abr = abr.d
    if abr.v <= i:
        abr.g = Noeud(None, i, None)
    else:
        abr.d = Noeud(None, i, None)

def ajoute(abr : Noeud | None, i : int) -> Noeud | None:
    if abr is None:
        return Noeud(None, i, Noeud)
    while abr.g and abr.d:
        if abr.v <= i:
            abr = abr.g
        else:
            abr = abr.d
    if abr.v <= i:
        abr.g = Noeud(None, i, None)
    else:
        abr.d = Noeud(None, i, None)

```
