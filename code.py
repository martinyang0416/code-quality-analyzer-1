import sys
MOD = 10**9 + 7

def main():
    N, M = map(int, sys.stdin.readline().split())
    test_solvers = []
    for _ in range(M):
        s = sys.stdin.readline().strip()
        test_solvers.append(s)
    
    # Compute H bitmask for each problem
    H_bits = []
    for i in range(N):
        h = 0
        for m in range(M):
            if test_solvers[m][i] == 'H':
                h |= 1 << m
        H_bits.append(h)
    
    # Count occurrences of each H
    from collections import defau