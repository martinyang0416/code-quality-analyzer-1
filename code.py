from collections import deque

def numIslands(grid):
    if not grid or len(grid) == 0:
        return 0
    grid = [list(row) for row in grid]
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                queue = deque([(i, j)])
                grid[i][j] = '0'
                while queue:
                    x, y = queue.popleft()
                    for dx, dy