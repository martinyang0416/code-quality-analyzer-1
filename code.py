import numpy as np

def main():
    import sys
    N, K, T = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    
    # Compute count array for residues mod N
    count = [0] * N
    for r in range(N):
        if r == 0:
            count[r] = T // N
        else:
            if r > T:
                count[r] = 0
            else:
                count[r] = (T - r) // N + 1
    
    # Compute frequency array for each residue mod N of the initial activ