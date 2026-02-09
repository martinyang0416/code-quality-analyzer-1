import sys
from collections import deque

def main():
    n, m = map(int, sys.stdin.readline().split())
    adjacency = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    
    for _ in range(m):
        v, u, w = map(int, sys.stdin.readline().split())
        adjacency[v].append((u, w))
        in_degree[u] += 1
    
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    topo_order = []
    while queue:
        u = queue.pop