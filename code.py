def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx])
    idx += 1
    m = int(input[idx])
    idx += 1
    grid = []
    for _ in range(n):
        row = list(map(int, input[idx:idx+m]))
        idx += m
        grid.append(row)
    
    row_steps = []
    for i in range(n):
        row = grid[i]
        # Compute ranks for the row
        sorted_row = sorted(row)
        rank = {v: idx+1 for idx, v in enumerate(sorted_row)}
        ranked = [rank[v