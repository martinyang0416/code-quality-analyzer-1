MOD = 10**9 + 7

def numMusicPlaylists(N, L, K):
    dp = [[0] * (N + 1) for _ in range(L + 1)]
    dp[0][0] = 1
    for i in range(1, L + 1):
        max_j = min(i, N)
        for j in range(1, max_j + 1):
            # Adding a new song
            dp[i][j] += dp[i-1][j-1] * (N - (j - 1))
            # Adding a repeated song
            dp[i][j] += dp[i-1][j] * max(j - K, 0)
            dp[i][j] %= MOD
    return dp[L][N] % MOD