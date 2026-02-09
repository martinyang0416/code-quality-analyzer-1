def main():
    import sys
    input = sys.stdin.read().split()
    m = int(input[0])
    n = int(input[1])
    grid = input[2:2+m]
    rows = m
    cols = len(grid[0]) if m > 0 else 0

    # Preprocess blocks
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    block_map = [[None for _ in range(cols)] for _ in range(rows)]
    blocks = []
    for y in range(rows):
        for x in range(cols):
            if not visited[y][x] and grid[y][x] != '0':
                color = grid[