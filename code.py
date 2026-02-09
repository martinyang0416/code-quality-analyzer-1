import sys

MOD = 10**9 + 7

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        n = int(input[idx])
        m = int(input[idx+1])
        idx += 2
        degrees = [0] * (n + 1)  # 1-based indexing
        for __ in range(m):
            u = int(input[idx])
            v = int(input[idx+1])
            idx += 2
            degrees[u] += 1
            degrees[v] += 1
        
        # Compute Q = product of (1 + degre