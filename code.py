import sys
import bisect

def main():
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    # Compute prefix sums
    prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix[i] = prefix[i - 1] + a[i - 1]

    for i in range(N):
        # Current index is i (0-based)
        L_list = prefix[0:i+1]
        R_list = prefix[i+1:N+1]

        # Compute S_group: all R-L for R in R_list, L in L_list
        S_group = [R - L for L in L_list for R in R_li