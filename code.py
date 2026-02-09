import sys

def main():
    sys.setrecursionlimit(1 << 25)
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix[i] = prefix[i - 1] + a[i - 1]

    for i in range(1, N + 1):
        # Compute S_in: subarrays including i
        sin = [prefix[r] - prefix[l - 1] for l in range(1, i + 1) for r in range(i, N + 1)]
        
        # Compute S_out: subarrays not including i (split into left and ri