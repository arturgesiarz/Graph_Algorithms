#ARTUR GĘSIARZ
#TIME COMPLEXITY:  O(V*E^2) -  exercise1
#TIME COMPLEXITY O(V*E^2 * V^2 * V^2) XD -> O(V^5*E^2) - exercise2
"""
	Ex1:
The task is to implement a function that calculates the maximum flow and compares the time when using BFS and when using DFS.
    Ex2:
However, for the second task, it is necessary to calculate the edge cohesion, this can be done in such a way that
    we will treat each edge as if it had edge equal to 1, and then calculate the number of edge-disjoint paths for each pair of vertices
    and we will choose a pair for which it will be as small as possible and this will be our edge cohesion - but unfortunately the complexity
    There are many such ideas, although they are still polynomial
"""
from testy import testing
from collections import deque
from copy import deepcopy

def dfs(G,parents,s,t):
    n=len(G)
    visited=[False for _ in range(n)]
    visited[s]=True
    def dfs_start(G,parents):
        for v in range(n):
            if not visited[v]:
                dfs_visit(G,parents,v)
    def dfs_visit(G,parents,x):
        nonlocal visited
        visited[x]=True
        for i in range(n):
            if (G[x][i]>0) and (not visited[i]):
                parents[i]=x
                dfs_visit(G,parents,i)
    dfs_start(G,parents)
    return visited[t]

def bfs(G,parents,s,t): #bfs - checks if there is an extension path
    n=len(G)
    visited=[False for _ in range(n)]
    Q=deque()
    visited[s]=True
    Q.append(s)
    while len(Q)>0:
        v=Q.popleft()
        for i in range(n): 
            if  (G[v][i] > 0) and (not visited[i]):
                    Q.append(i)
                    visited[i]=True
                    parents[i]=v
    return visited[t]

def max_flow(G,source,sink): #algorithm that calculates the maximum flow using the bfs/dfs algorithm depending on the setting
    n=len(G)
    parents=[-1 for _ in range(n)]
    max_flow=0
    while bfs(G,parents,source,sink):
        path_flow=float('inf')
        father=sink
        while father!=source: #that's why this condition is because parents[source] will be -1, and we protect ourselves from such a case
            path_flow=min(path_flow,G[parents[father]][father]) #looking for minimum value on my path
            father=parents[father]
        max_flow+=path_flow
        father=sink
        while father!=source:
            G[parents[father]][father]-=path_flow
            G[father][parents[father]]+=path_flow
            father=parents[father]
    return max_flow

def convert_graph(G):
    n=len(G)
    new_graph=[[0 for _ in range(n)] for _ in range(n)]
    for v in range(n):
        for i in range(len(G[v])): #we look through all the edges
            u=G[v][i][0]
            cost=G[v][i][1]
            new_graph[v][u]=cost
    return new_graph

def modify_graph(matrix_graph,s,t): #function removes all edges entering the source and removes all edges leaving the sink - this is according to the definition of the sink and the source
    n=len(matrix_graph)
    for i in range(n):
        matrix_graph[i][s]=0 #because nothing can enter the source
        matrix_graph[t][i]=0 #because nothing can flow out of the mouth

def recovery_graph(orginal_graph,probe_graph,s,t):
    n=len(orginal_graph)
    for i in range(n):
        if orginal_graph[i][s]>0:
            value=deepcopy(orginal_graph[i][s])
            probe_graph[i][s]=value
        if orginal_graph[t][i]>0:
            value=deepcopy(orginal_graph[t][i])
            probe_graph[t][i]=value

def function_ex1(graph,s,t):
    matrix_graph=convert_graph(graph)
    return max_flow(matrix_graph,s,t)

def function_ex2(graph):
    n=len(graph)
    matrix_graph=convert_graph(graph)
    matrix_graph_copy=deepcopy(matrix_graph)
    min_flow=float('inf')
    for s in range(n):
        for t in range(n):
            if s!=t: #we choose the source and sink
                modify_graph(matrix_graph_copy,s,t)
                flow=max_flow(matrix_graph_copy,s,t)
                min_flow=min(min_flow,flow)
            matrix_graph_copy = deepcopy(matrix_graph)
    return min_flow

#To enable more tests, change all_test=True; The exercise value can be set to 1/2 - depending on which exercise we want to include tests in
testing(function_ex1,exercise=1,all_test=True)
