import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

distance = [[-1] * (n + 1) for _ in range(n + 1)]
parent = [[None] * (n + 1) for _ in range(n + 1)]

start_bob = 1
start_alex = n
distance[start_bob][start_alex] = 0
q = deque([(start_bob, start_alex)])

found = False
while q:
    u, v = q.popleft()
    if u == n and