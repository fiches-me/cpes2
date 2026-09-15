---
title: "TD #2"
order: 2
---

# TD #2

## Tableaux Décalés

```java
public class UTab {

    public static void main(String[] args) {
        // A faire
    }

    private int[] tab;
    private int start;

    public UTab(int[] tab, int start, int end) {

        if (tab.length != end - start) {
            throw new ArrayIndexOutOfBoundsException();
        }

        this.tab = tab;
        this.start = start;
        // Pas utilisé
        // this.end = end;
    }

    public int get(int i) {
        if (i > this.tab.length) { throw new ArrayIndexOutOfBoundsException(); }
        return this.tab[i + start];
    }

    public void set(int i , int val) {
        if (i > this.tab.length) { throw new ArrayIndexOutOfBoundsException(); }
        this.tab[i + start] = val;
    }

    public int lenght() {
        return this.tab.length;
    }
}

```

## Fractions

```java
public class Fraction {

    private int num, denum;

    public static void main(String[] args) {
        // A faire
    }

    public Fraction(int num, int denum) {
        // this.var = var
        // équivalent à self.val = val
        if (denum < 0) { throw new ArrayIndexOutOfBoundsException(); }
        int gdc = this.gdc(num, denum);
        this.num = num / gdc;
        this.denum = denum / gdc;
    }

    public String toString() {
        if (this.denum == 1) {return String.valueOf(this.num);}
        return this.num + "/" + this.denum;
    }

    public Fraction add(Fraction f) {
        return new Fraction(this.num * f.denum + f.num * this.denum, this.denum * f.denum);
    }

    public Fraction mul(Fraction f) {
        return new Fraction(this.num * f.num, this.denum * f.denum);
    }

    public boolean equals(Fraction f) {
        return ((this.num == f.num) && (this.denum == f.denum));
    }

    public int compareTo(Fraction f) {
        if (this.num > this.denum) {
            return 1;
        }
        return 0;
        //return -1;
    }

    private int gdc(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }


}


```

## Chronomètre

> A partir de là c'est pas terminé

```java
import java.lang.ProcessBuilder.Redirect.Type;

public class Chronometre {

    private int h, m, s;

    public static void main(String[] args) {
        // A faire
    }

    public Chronometre(int h, int m, int s) {
        this.h = h;
        this.m = m;
        this.s = s;
    }

    public String toString() {
        return this.h + "h " + this.m + "m " + this.s + "s";
    }

    public int toSeconds() {
        return this.h * 3600 + this.m * 60 + this.s;
    }

    public void normalise() {
        int sn = this.s % 60;
        this.m += (this.s - sn) / 60;
        this.s = sn;

        int mn = this.m % 60;
        this.h += (this.m - mn) / 60;
        this.m = mn;
    }

    public boolean equals(Object o) {
        if (o instanceof Chronometre) {
            if (true) {

                return true;
            }
            return false;
        }
        return false;
    }
}

```

## Intervalles

```java

```

## Agenda

```java

```
