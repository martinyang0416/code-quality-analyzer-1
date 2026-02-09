import sys
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    N = int(sys.stdin.readline())
    traffic = [0] * (N + 1)
    for i in range(1, N + 1):
        traffic[i] = int(sys.stdin.readline())
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Build parent pointers using BFS
    parent = [0] * (N + 1)
    visited = [False] * (N + 1)
  