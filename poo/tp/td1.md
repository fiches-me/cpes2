---
title: "TD #1"
order: 1
---

# TD #1

Si besoin je peux faire des textes explicatifs, envoyez moi un message sur le code qui vous pose problème :)

## Degrees 

```java
import java.util.Locale;
import java.util.Scanner;

public class Degres {

    public static void main(String[] args) {
        System.out.print("Donnez une température en Fahrenheit : ");
        Scanner sc = new Scanner(System.in);
        sc.useLocale(Locale.US);
        double i = sc.nextDouble();
        double c = (5.0 / 9.0) * (i - 32);
        System.out.println(
            "Cette température équivaut à " + c + " degrés Celsius"
        );
        sc.close();
    }
}

```

## Heures, Jours, Minutes, Secondes

```java
import java.util.Locale;
import java.util.Scanner;

public class Hjms {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        sc.useLocale(Locale.US);
        System.out.print("Donnez une durée en secondes : ");
        int i = sc.nextInt();
        System.out.println(
            "Cette durée équivaut à " +
                i / 86400 +
                " jour " +
                (i % 86400) / 3600 +
                " heure " +
                (i % 3600) / 60 +
                " minute " +
                (i % 60) +
                " secondes"
        );
        sc.close();
    }
}

```

## Courrone

Oups

## Trois Nombres

```java
import java.util.Locale;
import java.util.Scanner;

// Attention : nom identique au nom de fichier, majuscules comprises
public class TroisNombres {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        sc.useLocale(Locale.US);

        int one = 0, two = 0, three = 0;

        System.out.print("1er Nombre: : ");
        int a = sc.nextInt();

        System.out.print("2em Nombre: : ");
        int b = sc.nextInt();

        System.out.print("3em Nombre: : ");
        int c = sc.nextInt();

        if (a > b) {
            if (a > c) {
                one = a;
                if (b > c) {
                    two = b;
                    three = c;
                } else {
                    two = c;
                    three = b;
                }
            }
        } else {
            if (a > c) {
                one = b;
                if (b > c) {
                    two = a;
                    three = c;
                } else {
                    two = c;
                    three = a;
                }
            }
        }

         System.out.println(one + ", " + two + ", " + three);
         sc.close();
    }
}

```

## Triangle

```java
public class Triangle{

    public static void main(String[] args) {
        if (args[0] != null) {
            int i = Integer.valueOf(args[0]);
            for (int j = 0; j <= i; j++) {
                for (int k = 0; k < j; k++) {
                    System.out.print("*");
                }
                System.out.print("\n");
            }
        }
    }
}

```

## Pyramide

```java
public class Pyramide{

    public static void main(String[] args) {
        if (args[0] != null) {
            int i = Integer.valueOf(args[0]);
            for (int j = 0; j <= i; j++) {
                for (int l = i - j; l > 0; l--) {
                    System.out.print(" ");
                }
                for (int k = 0; k < j; k++) {
                    System.out.print("*");
                }
                for (int k = 1; k < j; k++) {
                    System.out.print("*");
                }
                System.out.print("\n");
            }
        }
    }
}

```

## Fonctions 

```java
public class Fonctions {
    public static void main(String[] args) {
        int[] tab = new int[10];
        afficheTab(tab);
        System.out.println(
            longeurTab(
                tab
            )
        );
        incrementeTab(tab);
        afficheTab(tab);
    }

    public static void afficheTab(int[] tab) {
        System.out.print("[ ");
        for (int i : tab){
            System.out.print(i);
        }
        System.out.print(" ]\n");
    }

    public static int longeurTab(int[] tab) {
        return tab.length;
    }

    public static void incrementeTab(int[] tab) {
        for (int i = 0; i < tab.length; i++){
            tab[i]++;
        }
    }
}

```

## Fibonacci

```java
public class Fibonacci {
    public static void main(String[] args) {
        if (args.length >= 1) {
            int n = Integer.valueOf(args[0]);
            System.out.println("Fibo " + n + ": " + Fibo1(n));
        }
        if (args.length >= 2) {
            int m = Integer.valueOf(args[1]);
            int l = Fibo2(m);
            System.out.println("Fibo("+ l + ") > " + m + " > Fibo(" + (l - 1) + ")");
        }
    }

    public static int Fibo1(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            return Fibo1(n - 1) +  Fibo1(n - 2);
        }
    }

    public static int Fibo2(int n) {
        int m = 0;
        while(Fibo1(m) < n) { m++; }
        return m;
    }
}

```
