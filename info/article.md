# Article

## L4: More data means less info. Explain this sentence.

While we could think more data means more information, this is not forcibly true. Stats must have a meaning to bring a new information. If they dont, we increase the computing power needed to treat them (even id its price is at an all time low). If we take, as an example, stats from a grocery store : in a small stall, where products are unique, those stats could help the stall's owner can now how to handle his stocks. But for a big supermarket, with all the references, prices, quantities, you can't do anything with thoses numbers, even with all of them. 

## What is Data Mining?

Data mining is the analysis step of the **Knowledge Discovery in Databases (KDD)** process. It uses statistics, machine learning, and pattern recognition to discover non-obvious patterns, correlations, anomalies, and predictive models within large, complex datasets.

## What is a Genetic Algorithm

A Genetic Algorithm is a heuristic search and optimization algorithm inspired by Charles Darwin’s theory of natural evolution. Operating within artificial intelligence, it iteratively tests a population of candidate solutions against a fitness function, applying biological operators like selection, crossover (recombination), and mutation to evolve increasingly optimal solutions over successive generations.

## What does OLTP stand for and what is the connection between OLTP and the article ?

OLTP stands for **On-line transaction processing**. It is use to handle a lot of data and store it in databases, using **short** transactions (SQL queries such as `INSERT`, `UPDATES`, `QUERIES`...)
In the article, OLTP is used to generate this kind of databases. 
In the article, OLTP is used to generate this kind of databases. Data is later extracted and structured as binary trees for analysis.

## What are the two mining techniques mentionned at the beginning of the article ? How are they different ?

The two mining techniques are **Prediction** and **Knowledge Discovery**.

- Prediction focus on existing data to forecast future outcomes from modles (like linear regressions) -> *What will happen next?*
- Knowledge Discovery looks for unknown patterns, relationships or structure within existing data -> *What pattern is hidden inside the data? What data could we create?* 

## What are decision trees?

Decision trees are a way to store data using a tree structure. Each data is bound to another thanks to an edge, and make, at the end, a tree structure with one "big" data being the central point of the tree (also called **root**). Those trees are labeled, both on nodes & edges. A decision is then made depending on multiples factors : this decision is the path that will, according the the factors, be possible and lead to a leaf.
