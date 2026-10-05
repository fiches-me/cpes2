---
title: 🌀 Héritage
order: 3
---

# 🌀 Héritage

*Que serait nos objets sans héritage ?* Nous allons voir qu'en java, l'héritage est très présent et permet d'économiser beaucoup de fonctions.

## Interfaces

La première manière de faire des fonctions hérités est d'utiliser des **interfaces**. Cela consiste à écrire une liste de fonction (avec paramètres d'entrées et de sorties). Chaque classe qui veux hérité de cette classe principale **doit** implémenter **exactement toutes ces fonctions**. Voici un petit exemple avec des personnages :

```java

public interface Personnage {
	String getName();
	int getAge();
}

public class Guilhem implements Personnage {

	public String getName() {
		return "Guilhem";
	}
	
	public String getAge() {
		return 19;
	}
}

```

> [!NOTE]
> Dans les interfaces, toutes les fonctions spécifiés sont implicitement publiques. Il est possible de créer autant de fonction privés que necessaire
