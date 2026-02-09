def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    q = int(data[idx])
    idx += 1
    for _ in range(q):
        m, p = int(data[idx]), int(data[idx+1])
        idx +=2
        b = list(map(int, data[idx:idx+m]))
        idx +=m
        
        # Compute good array
        n = m-1
        good = [0] * n
        for i in range(n):
            if b[i] > 3 * b[i+1]:
                good[i] = 1
        
        # Compute prefix sum
        prefix = [0]