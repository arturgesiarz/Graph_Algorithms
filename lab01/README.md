# Instructions task: "Tourist guide":

## Contents task: "Tourist guide"

Given an undirected graph G = (V,E), a function c: E -> N giving weights to the edges, and distinguished vertices s and t. We are looking for a path from s to t such that the minimum weight of the edges on this path is as high as possible. Return the lowest edge weight on the found path.

## Solutions:

+ File `ex1.py`
The solution using BFS/DFS browsing will be to go through the graph once to find out what values ​​occurred in specific edges - I will write them in the array O(V^2).The values ​​are natural numbers, i.e. in the pessimistic case when the graph has V vertices and is a dense graph. I will have O(V) paths then consider those that have values ​​greater than or equal to k, where k is the selected number of those. The complexity of the bfs and dfs algorithm is O(E) -> O(V).

+ File `ex2.py`
The consideration consists in finding the maximum spanning tree using the Prima algorithm,
and then finding the minimum value on the straight path from s to t.

## Testing:

+ Folder `graphs-lab1`
This folder contains test graphs saved in DIMACS ascii format, which are intended to check the speed of the algorithm `ex1.py` and `ex2.py`.

+ File `dimacs.py`
This file contains a script that loads graph saved in DIMACS ascii format and then saves them in edge list format.

+ File `testy.py`
This file contains a script that loads test graphs located in the `graphs-lab1` folder, which are saved in the DIMACS ascii. It loads them using a file `dimacs.py`. Once all the tests have been loaded correctly, this file checks `ex1.py` and `ex2.py` to see how many tests from the 'graphs-lab1' folder have passed correctly.







