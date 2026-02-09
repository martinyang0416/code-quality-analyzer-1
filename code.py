import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    grid = []
    for _ in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        grid.append(row)
    
    # Initialize safe matrix
    safe = [[False for _ in range(N)] for _ in range(N)]
    
    for _ in range(M):
        x, y, k = map(int, sys.stdin.readline().split())
        s_i = x - 1  # convert to zero-based indices
        s_j = y - 1
        min_x = max(0, s_i - k)
        max_x = min(N-1,