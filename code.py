n, m, k = map(int, input().split())
moves = [tuple(map(int, input().split())) for _ in range(k)]

added = set()
result = 0

for step in range(k):
    i, j = moves[step]
    added.add((i, j))
    
    # Check all four possible squares that could include (i,j)
    
    # Square 1: (i,j) is top-left
    if i + 1 <= n and j + 1 <= m:
        if (i, j + 1) in added and (i + 1, j) in added and (i + 1, j + 1) in added:
            result = step + 1
            break
    
    # Square 2: (i,j) is top-ri