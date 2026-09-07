---
title: ℹ️ Introduction
---

# Introduction

Au dela de découvrir un nouveau language, nous découvrons aujourd'hui également la **compilation**. Pour ce premier CM, je vais mettre les équivalents en python de chaque programme pour voir les différences de structures.

## Le premier fichier

Commencons le java ! 

::: code-group

```java
public class hello {
  // On verra ce que signifie "public" et "static" après
  // "void" signifie que la fonction ne renvoie rien.
  public static void main(String[] args) {
    // Une instruction...
    ...
  }
}
```

```python
# Une instruction
```

:::

Quelques différences :
- Le code est par défaut dans une classe. En java, **il faut que le code soit toujours dans une grande classe publique**.
- Les commentaires utilisent `//` à la place de `#`.
- L'indentation **n'est pas obligatoire** mais utiliser des **crochets `{` et `}` sont obligatoires**
- **Toutes les lignes sans crochets finissent par un ;**.
- La fonction `main` **doit** exister pour le moment car elle est celle utilisée quand on execute le fichier  `.class` avec la commande `java`.
- L'ensemble des arguments sont typés. **On ne peux pas définir d'arguments non typés**.

> [!attention] 
> Le fichier qui contient le code doit avoir le **même nom** que la classe principale. Dans l'exemple si dessus, le fichier qui contient ce code **doit** s'appeler `hello.java`

## Execution

Pour executer ce code, il faut **d'abord et obligatoirement le compiler**. On utilise la commande `javac <nom du fichier>.java`. On obtient alors un fichier `hello.class` que l'on peut executer avec `java hello.class`. 

> [!tip] Pour aller plus loin...
> Si on crée un code avec plusieurs fichiers java, on pourra compiler l'ensemble des fichiers java dans un grand fichier `.jar` executable avec `java -jar server.jar`.

## Variables & types

Les variables restent comme en python des valeurs stockés en mémoire. Il existe aussi des types simple et complexes, composés.

> [!TIP] Conseil
> Les types composés comment par des ma

En java, il faut **déclarer les variables avant de les utiliser**. Pour définir une variable, on utilise `<type> <nom> = <valeur>;` ou `<type> <nom>;` pour ne pas lui donner de valeur.

Voici une liste de types par d

::: code-group

```java
// Types "classiques"
int integrer = 2
float reel = 3.323
// ! NOUVEAU ! On peut faire des réels avec deux chiffres après la virgule
double doub = 3.40
boolean test = True
char c = "c"

// Types composés
// ⚠️ En java, les string sont des types composés de plusieurs char.
String text = "Bonjour"

```

```python
# Types "classiques"
integrer = 2
reel = 3.323
doub = 3.4 # Aussi un flottant
test = True
c = "c"
tetx = "Bonjour"
```

:::

> [!ATTENTION]
> On ne confond pas `=` et `==` comme en python

< ajout tableaux >

## Opérateurs

## Structures de contrôle

On peut bien entendu faire des tests booléens, avec des if, elif, else :::: code-group

::: code-group

```java
if (bool) {
  //
} else {
  // le else est facultatif. MAIS les crochets {} soient fermés
}
```

```python
if bool:
  # ...
else:
  # ...
```

:::

Les boucles `for` et `while` existent aussi en java :

::: code-group

```java
int x = 1
int n = 10
String[] listDeClasse = new String["Guilhem", "Marcel"]

while (x < n) {
  x = 2 * x;
}

// Les boucles for sans tableaux sont assez moches
// i ++ indique que i est incrémenté à chaque tour.
for (int i = 0; i < n; i ++) {
  System.out.println(i)
}

// Ou plus simple, avec un tableau
for (String nom : listDeClasse) {
  System.out.println(nom)
}
```

```python
x = 1
n = 10
listDeClasse = ["Guilhem", "Marcel"]

while x < n:
  x = 2 * x
  
for i in range(0, n):
  print(i)
  
for nom in listDeClasse:
  print(nom)
```

## Fonctions

En java, définir une fonction est plus strict : il faut définir l'ensemble de ses arguments, 