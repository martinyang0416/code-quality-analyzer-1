import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        grid = []
        for i in range(n):
            grid.append(data[idx].strip())
            idx += 1
        
        # Precompute right[i][j]
        right = [[0] * m for _ in range(n)]
        for i in range(n):
            j = 0
            while j < m:
      