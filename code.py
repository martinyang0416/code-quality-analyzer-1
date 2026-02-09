MOD = 10**9 + 7

def numPermsDISequence(S: str) -> int:
    n = len(S)
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        prefix = [0] * (i + 2)
        for j in range(i + 1):
            prefix[j + 1] = (prefix[j] + dp[i - 1][j]) % MOD
        
        for j in range(i + 1):
            if S[i - 1] == 'D':
                dp[i][j] = (prefix[i] - prefix[j]) % MOD
            else:
                dp[i][j] = prefix[j] % MOD
    
    return s