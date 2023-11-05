#TIME COMPLEXITY: O(V*(V*E^2)) -> O(V^2*E^2)
"""
    Algorithm for finding the smallest number of edges that connect a graph using the flow method.
    To define it well, we will use Wagner's theorem here - it states that if we want to find the minimum number that will separate the path
    between point A and B on the graph, it is equal to the maximum number of non-overlapping paths from A to B -> this can be found by the maximum flow in the graph,
    where the source will be point A and the sink will be point B.

    Once we know how to calculate the minimum number of edges that must be removed from the path from A to B so that there is no longer any possibility
    getting from point A to B. I calculate this from vertex A to every possible one, and I take the minimum from it. This will mean
    the minimum number of edges that need to be removed to obtain a disconnected graph.
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

def bfs(G,parents,s,t):
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
            path_flow=min(path_flow,G[parents[father]][father])
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
        for i in range(len(G[v])):
            u=G[v][i][0]
            cost=G[v][i][1]
            new_graph[v][u]=cost
    return new_graph

def modify_graph(matrix_graph,s,t): #function removes all edges entering the source and removes all edges leaving the sink - this is according to the definition of the sink and the source
    n=len(matrix_graph)
    for i in range(n):
        matrix_graph[i][s]=0
        matrix_graph[t][i]=0

def recovery_graph(orginal_graph,probe_graph,s,t):
    n=len(orginal_graph)
    for i in range(n):
        if orginal_graph[i][s]>0:
            value=deepcopy(orginal_graph[i][s])
            probe_graph[i][s]=value
        if orginal_graph[t][i]>0:
            value=deepcopy(orginal_graph[t][i])
            probe_graph[t][i]=value

def function(graph):
    n=len(graph)
    matrix_graph=convert_graph(graph)
    matrix_graph_copy=[deepcopy(matrix_graph) for _ in range(n)]
    min_flow=float('inf')
    for sink in range(1,n):
        modify_graph(matrix_graph_copy[sink],0,sink)
        flow=max_flow(matrix_graph_copy[sink],0,sink)
        min_flow=min(min_flow,flow)
    return min_flow

testing(function,all_test=True)