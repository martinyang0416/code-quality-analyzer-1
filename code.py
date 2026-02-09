import sys
from collections import defaultdict

def main():
    sys.setrecursionlimit(1 << 25)
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    adj = [[] for _ in range(n + 1)]  # 1-based indexing
    for idx in range(1, m + 1):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append((v, idx))
        adj[v].append((u, idx))

    # Tarjan's algorithm to find bridges iteratively
    disc = [-1] * (n + 1)
    low = [-1] * (n + 1)