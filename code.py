def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    for _ in range(T):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        grid = []
        for i in range(n):
            line = data[index]
            index += 1
            grid.append([int(c) for c in line])
        
        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            print(0)
            continu