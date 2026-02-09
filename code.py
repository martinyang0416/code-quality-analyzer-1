import sys
from collections import deque

def main():
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))
    adj = [[] for _ in range(n + 1)]  # 1-based indexing
    for i in range(1, n + 1):
        parent = p[i - 1]
        if parent != 0:
            adj[i].append(parent)
            adj[parent].append(i)
    degrees = [len(neighbors) for neighbors in adj]
    q = deque()
    processed = [False] * (n + 1)
    result = []
    for i in range(1, n + 1):
      