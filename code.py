import bisect
import sys

def main():
    sys.setrecursionlimit(1 << 25)
    N, Q = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    special_str = sys.stdin.readline().strip()

    # Parse L and R indices
    L_indices = []
    R_indices = []
    for idx, c in enumerate(s):
        if c == 'L':
            L_indices.append(idx)
        else:
            R_indices.append(idx)

    # Compute ℓ and r arrays (1-based indexing)
    ℓ = [0] * (N + 1)
    r = [0] * (N + 1