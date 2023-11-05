#AUTHOR: ARTUR GĘSIARZ
#TIME COMPLEXITY: O(ElogV)
"""
    The consideration consists in finding the maximum spanning tree using the Prima algorithm,
    and then finding the minimum value on the straight path from s to t.
"""
from testy import testing
from queue import PriorityQueue
from collections import deque

def bfs(Graph,x):
    n=len(Graph)
    visited=[False for _ in range(n)]
    parents=[(-1,-1) for _ in range(n)]
    q=deque()
    q.append(x)
    visited[x]=True
    while len(q)>0:
        v=q.popleft()
        neighs=len(Graph[v])
        for i in range(neighs):
            neigh=Graph[v][i][0]
            cost=Graph[v][i][1]
            if not visited[neigh]:
                q.append(neigh)
                visited[neigh]=True
                parents[neigh]=(v,cost)
    return parents

def prim(G,root):
    n=len(G)
    keys=[float('-inf') for _ in range(n)]
    parents=[(-1,-1) for _ in range(n)]
    v_in_quene=[True for _ in range(n)]
    keys[root]=0
    q=PriorityQueue()
    q.put((keys[root],root))
    while q.qsize()>0:
        v=q.get()[1]
        v_in_quene[v]=False
        neightbours=len(G[v])
        for neightbour in range(neightbours):
            id_neightbour=G[v][neightbour][0]
            cost_neightbour=G[v][neightbour][1]
            if keys[id_neightbour]<cost_neightbour and v_in_quene[id_neightbour]:
                parents[id_neightbour]=(v,cost_neightbour)
                keys[id_neightbour]=cost_neightbour
                q.put((-keys[id_neightbour],id_neightbour))
    return parents

def create_new_graph(tree_parents):
    n=len(tree_parents)
    G=[[] for _ in range(n)]
    for son in range(n):
        father=tree_parents[son][0]
        cost=tree_parents[son][1]
        if father!=-1: #ojciec istenieje
            G[son].append((father,cost))
            G[father].append((son,cost))
    return G

def find_sol(pre_sol,t):
    father=t
    sol=float('inf')
    while father!=-1:
        if pre_sol[father][1]!=-1:
            sol=min(sol,pre_sol[father][1])
        father=pre_sol[father][0]
    return sol

def function(graph,s,t):
    tree_parents=prim(graph,s)
    new_G=create_new_graph(tree_parents)
    pre_sol=bfs(new_G,s)
    return find_sol(pre_sol,t)

#To enable more tests, change all_test=True
testing(function,all_test=True)
