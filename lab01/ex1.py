#AUTHOR: ARTUR GĘSIARZ
#TIME COMPLEXITY:  O(V^2)
"""
The solution using BFS/DFS browsing will be to go through the graph
    once to find out what values ​​occurred in specific edges - I will write them in the array O(V^2).
    The values ​​are natural numbers, i.e. in the pessimistic case when the graph has V vertices and is a dense graph.
    I will have O(V) paths then consider those that have values ​​greater than or equal to k, where k is the selected number of those.
    The complexity of the bfs and dfs algorithm is O(E) -> O(V).
"""
from testy import testing
from sys import setrecursionlimit
setrecursionlimit(10000000)

def dfs(G,min_value,start,end):
    n = len(G)
    visited = [False for _ in range(n)]
    def DFS_visit(G,x):
        visited[x]=True
        for i in range(len(G[x])): #I want to search all my neighbors
            neigh=G[x][i][0]
            costs=G[x][i][1]
            if visited[neigh]==False and costs>=min_value: #condition enabling following edges that are greater or equal
                DFS_visit(G,neigh)
    DFS_visit(G,start)
    return visited[end]

def create_tab(graph): #function that creates an array that will store information about specific edges
    n=len(graph)
    tab=[]
    for v in range(n): #O(V^2)
        neighs=len(graph[v])
        for i in range(neighs):
            cost=graph[v][i][1]
            if not cost in tab: tab.append(cost) #O(V)
    tab.sort()
    return tab

def checked_min_value(graph,tab,s,t):
    min_edge=float('-inf')
    for value in tab: #O(V)*O(V) -> O(V^2)
        if dfs(graph,value,s,t): min_edge=max(min_edge,value) #O(V)
    return min_edge

def function(graph,s,t):
    value_tab=create_tab(graph)
    return checked_min_value(graph,value_tab,s,t)

#To enable more tests, change all_test=True
testing(function,all_test=True)
