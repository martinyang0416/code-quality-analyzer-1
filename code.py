MOD = 10**9 + 7

def main():
    import sys
    N = int(sys.stdin.readline())
    if N < 3:
        print(0)
        return
    A = list(map(int, sys.stdin.readline().split()))
    
    prefix = A[0] + A[1]
    sum1 = A[0] * 1
    sum2 = A[1] * 1
    total = (sum1 + sum2) * A[2]
    
    for m in range(3, N):
        previous_prefix = prefix
        new_prefix = previous_prefix + A[m - 1]
        new_sum1 = sum1 + previous_prefix
        new_sum2 = sum2 + A[m - 1] * (m - 1)
        contribution 