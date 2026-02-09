import heapq

def main():
    w, h, limit = map(int, input().split())
    grid = []
    for _ in range(h):
        row = input().strip().split()
        grid.append(row)
    
    # Find the start and end positions
    start = None
    end = None
    for j in range(w):
        if grid[0][j] == 'S':
            start = (0, j)
    for j in range(w):
        if grid[-1][j] == 'T':
            end = (h-1, j)
    
    # Create the cost grid
    cost = [[0 for _ in range(w)] for _ in range(h)]
    for 