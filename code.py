def main():
    import sys
    X, Y = map(int, sys.stdin.readline().split())
    max_n = Y
    
    # Compute smallest prime factors (spf) for all numbers up to max_n
    spf = [0] * (max_n + 1)
    for i in range(2, max_n + 1):
        if spf[i] == 0:
            spf[i] = i
            for j in range(i * i, max_n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    
    # Compute the dp array where dp[n] is the maximum depth of the tree rooted at n
    dp = [0] * (max_n +