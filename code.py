import sys
from sys import stdin
from collections import defaultdict

def main():
    sys.setrecursionlimit(1 << 25)
    N, M = map(int, stdin.readline().split())
    w = list(map(int, stdin.readline().split()))
    total_sum = sum(w)
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    disc = [0] * (N + 1)
    low = [0] * (N + 1)
    parent = [0] * (N + 1)
    sum_subtree = [0] * (N