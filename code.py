import sys

def main():
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    prefix = [0] * (N + 1)
    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + a[i-1]

    for current_i in range(1, N+1):
        i = current_i
        # Compute S: all subarrays that include i
        S = [prefix[e] - prefix[s-1] for s in range(1, i+1) for e in range(i, N+1)]
        # Compute T_left: all subarrays ending before i
        T_left = [prefix[e] - prefix[s-1] fo