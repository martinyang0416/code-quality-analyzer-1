n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(k)]

# Build adjacency list for connectivity (undirected, ignoring duplicates)
adj = [[] for _ in range(n + 1)]
for u, v, c in edges:
    if v not in adj[u]:
        adj[u].append(v)
    if u not in adj[v]:
        adj[v].append(u)

# Find connected components using BFS
visited = [False] * (n + 1)
components = []
for node in range(1, n + 1):
    if not visited[node]:
        queue = [node]
