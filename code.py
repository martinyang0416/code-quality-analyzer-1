import sys
from collections import deque

def main():
    N = int(sys.stdin.readline())
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    K = int(sys.stdin.readline())
    levels = {}
    for _ in range(K):
        u, L = map(int, sys.stdin.readline().split())
        levels[u] = L
    
    # Check edges between pre-assigned nodes
    for u in levels:
        for v in ad