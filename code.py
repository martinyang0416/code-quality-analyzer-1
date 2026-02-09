import sys
from collections import deque

def main():
    n, m = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * (n + 1)
    possible = True
    
    for u in range(1, n + 1):
        if color[u] == -1:
            if not adj[u]:
                color[u] = 0
                continue
            queue = deque([u])
      