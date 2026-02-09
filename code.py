import sys
from sys import stdin
sys.setrecursionlimit(1 << 25)

def find_centroid(n, edges):
    parent = [0]*(n+1)
    size = [1]*(n+1)
    def dfs(u, p):
        size[u] = 1
        for v in edges[u]:
            if v != p:
                dfs(v, u)
                size[u] += size[v]
        parent[u] = p
    dfs(1, -1)
    for u in range(1, n+1):
        max_sub = 0
        for v in edges[u]:
            if v != parent[u]:
                max_sub = max(max_sub, size[v])
        max_sub = max