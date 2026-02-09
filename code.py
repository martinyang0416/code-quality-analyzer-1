import sys
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    n = int(sys.stdin.readline())
    edges = []
    adj = [[] for _ in range(n+1)]
    initial_t = [0] * (n)  # 1-based to n-1
    for i in range(n-1):
        u, v, t = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append((v, i+1))
        adj[v].append((u, i+1))
        initial_t[i+1] = t

    # Root the tree at 1, compute parent and child relationships
    parent = [0