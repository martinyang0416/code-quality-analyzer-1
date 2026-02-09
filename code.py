n, m, k = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

empty = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            empty.append((i, j))

from collections import deque
visited = set()
order = []
q = deque()

start = empty[0]
q.append(start)
visited.add(start)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while q:
    i, j = q.popleft()
    order.append((i, j))
    for di, dj in directions:
        ni, nj = i + di, j + dj
       