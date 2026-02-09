def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    for _ in range(N):
        R = int(input[idx])
        C = int(input[idx+1])
        idx += 2
        grid = []
        for _ in range(R):
            grid.append(input[idx])
            idx += 1
        
        dest_counts = [[0]*C for _ in range(R)]
        
        for r in range(R):
            row = grid[r]
            for c in range(C):
                cell = row[c]
       