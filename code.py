def superEggDrop(K, N):
    dp = [0] * (K + 1)
    m = 0
    while True:
        m += 1
        for k in range(K, 0, -1):
            dp[k] = dp[k] + dp[k - 1] + 1
            if dp[k] >= N:
                return m