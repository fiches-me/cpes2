---
title: 🥶 Fonctions & Classes
order: 3
---
# 🥶 Fonctions & Classes

Avant de commencer, **pourquoi de la programmation objet ?** Quand on code, on veut souvent des objets *un poil plus compliqués* que des entiers ou des simples chaines de caractères. **On va vouloir rassembler toute ces informations dans un seul objet.** *Et le Java est super pour ça !*

## Fonctions *in-vitro*

>[!IMPORTANT] Le terme *in-vitro* ne provient pas du cours !

Comme vous l'avez sans doute remarqué, les fichiers java contient tous une grande classe publique qui porte le nom du fichier.

Au delà de l'entrée `main`, il est possible de créer d'autres fonctions dans la classe, créant ainsi un objet de fonctions. 

Voici la liste des mots clefs pour définir une fonction :

- `public` ou `private` qui permet de savoir si d'autres fichiers peuvent utiliser cette fonction ou pas. Nos sous fonctions en python correspondent en java aux fonctions privées
- `static` si la fonction est une fonction *in-vitro*. Si c'est une **méthode** d'un objet, il faut le retirer.
- `void` ou un type qui correspond à ce que la fonction va renvoyer. **Elle ne peux rien renvoyer d'autre**
- un nom suivi de parenthèses et d'arguments, là aussi définis avec leurs types, et des crochets

> [!TIP]
> On verra ensuite que les fichiers java doivent être importés et créés dans d'autres fichiers. Par exemple, pour utiliser Fichier1 dans Fichier2, il faudrait faire `Fichier1 util = new Fichier1(params)`
> 
> C'est lourd pour des fonctions simples sur des arguments. *Si chacune de nos fonctions a des arguments différents, il faudrait construire une classe avec tout les arguments de toutes les fonctions...*
> 
> **Rendre les fonctions statiques permet d'éviter cela et utiliser directement `resultat = Fichier1.maSuperFontctionStatique(params)`.**

## Classes

**On ne peut pas parler de POO sans parler de classses !** Tout les objets en java sont des classes, mais pour l'utiliser comme en vraie objet, il faut créer un constructeur

Le constructeur est une méthode/fonction en haut du fichier avec le même nom que le fichier. Elle contient les arguments nécessaire pour la fabriquer et va définir ses **attributs**. En Java, on utilise `this` à la place de `self`. Voici un exemple pour tout remettre dans l'ordre :

```java
// Le fichier s'appelle donc MonObjet.java
public class MonObjet {
	// Chaque argument doit d'abord être initialisé
	private int ObjetCache;
	
	// Le contructeur, toujours avec le même nom
	public MonObjet(int ObjetCache) {
		// On ajoute des attributs
		this.ObjetCache = ObjetCache;
	}
	
	// Pas besois de mettre "self" ou "this" en argument,
	// c'est automatique en Java
	public int rendObjet() {
		// Ne pas oublier "this" ;)
		return this.ObjetCache;
	}
}
```

Maintenant, **que faire si une fonction peut prendre deux arguments différents ?** *Par exemple, une méthode d’égalité sur plusieurs types ?* Il est possible en java de **redéfinir la fonction**, ce qu'on appelle **surcharger la fonction** avec d'autres types et java utilisera l'une ou l'autre selon le type en entrée.

```java
public class MonObjet {
	
	private int ObjetCache;
	
	// Est appelé si on fait MonObjet.estEgal(32)
	public boolean estEgal(int other) {
		return (this.ObjetCache == other);
	}
	
	// Est appelé si on fait MonObjet.estEgal(MonAutreObjet)
	public boolean estEgal(MonObjet other) {
		return (this.ObjetCache == other.rendObjet());
	}
}
```

**On ne peut pas implémenter les opérations classiques, types `+`, `*`, `==`, sur des types fait main. Il faut créer des méthodes pour.** L'égalité sur des types construit correspond à *Es ce que ces deux objets sont les mêmes et donc possèdent la même adresse mémoire* (rappel du [cours 1](index.md), les types construits sont liés par des pointeurs). 

**La convention java est d'appelé la méthode d'égalité `equals()`.**

Cette règle de surcharge permet cependant de faire également plusieurs constructeurs, donc de faciliter la copie :

```java
public class MonObjet {
	private int ObjetCache;
	
	// Constructeur classique
	// On fait donc MonObjet x = new MonObjet(3)
	public MonObjet(int ObjetCache) {
		this.ObjetCache = ObjetCache;
	}
	
	// Constructeur de copie
	// On fait donc MonObjet y = new MonObjet(x)
	public MonObjet(MonObjet other) {
		this.ObjetCache = other.ObjetCache;
	}
}
```

> [!attention] Il n'est pas possible de faire plusieurs fonctions/méthodes `main`.
