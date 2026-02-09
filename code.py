MOD = 10**9 + 7

def main():
    import sys
    n, k = map(int, sys.stdin.readline().split())
    
    # Precompute combinatorial numbers
    max_n = n
    comb = [[0]*(max_n + 1) for _ in range(max_n + 1)]
    for i in range(max_n + 1):
        comb[i][0] = 1
        for j in range(1, i + 1):
            comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD
    
    result = 0
    for s in range(n+1):
        for t in range(n+1):
            sign = (-1) ** (s + t)
            c_s = comb[n][s]
    