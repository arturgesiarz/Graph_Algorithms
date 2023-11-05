# Instructions task: "Maximum flows":

## Contents task 1 of "Maximum flows":

Given a directed graph G = (V,E), a function c: E -> N giving weights to the edges, and distinguished vertices s and t. We need to find the maximum flow in the graph G between s and t, i.e. a function f: E -> N satisfying the conditions flow definition, ensuring the highest throughput.

## Contents task 2 of "Maximum flows":

Given is an undirected graph G = (V,E). The edge coherence of a graph G is the minimum number of edges after which the graph loses coherence when removed. 
For example:
+ tree edge consistency = 1.
+ cycle edge consistency = 2.
+ n-clique edge consistency = n-1.

Develop and implement an algorithm to calculate the edge connectivity of a given graph G, using the Ford-Fulkerson algorithm and the following fact:
(Menger's Theorem) The minimum number of edges that must be removed so that the given vertices s, t are in different connected components is equal to the number of edge-disjoint paths between s and t.

## Solutions:

+ File (task 1)`ex1_ex2.py` -> `function_ex1(graph,s,t)`
The task is to implement a function that calculates the maximum flow and compares the time when using BFS and when using DFS (Edmonds-Karp).

+ File (task 2)`ex1_ex2.py` -> `function_ex2(graph)`
The edge cohesion can be done in such a way that we will treat each edge as if it had edge equal to 1, and then calculate the number of edge-disjoint paths for each pair of vertices and we will choose a pair for which it will be as small as possible and this will be our edge cohesion - but unfortunately the complexity. There are many such ideas, although they are still polynomial.


## Testing:

+ Folder `connectivity` (task 2) and folder `flow` (task 1)
These folders contains test graphs saved in DIMACS ascii format, which are intended to check the speed of the algorithm `ex1_ex2.py` (task 1 and task 2).

+ File `dimacs.py`
This file contains a script that loads graph saved in DIMACS ascii format and then saves them in edge list format.

+ File `testy.py`
This file contains a script that loads test graphs located in the `connectivity` and `flow` folders, which are saved in the DIMACS ascii. It loads them using a file `dimacs.py`. Once all the tests have been loaded correctly, this file checks `ex1_ex2.py` to see how many tests from the `connectivity` and `flow` folders have passed correctly.







