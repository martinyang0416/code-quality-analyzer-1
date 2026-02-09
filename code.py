def minCost(n, cuts):
    cuts_sorted = sorted(cuts)
    sorted_cuts = [0] + cuts_sorted + [n]
    m = len(sorted_cuts)
    dp = [[0] * m for _ in range(m)]
    
    for l in range(2, m):
        for i in range(m - l):
            j = i + l
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
            dp[i][j] += sorted_cuts[j] - sorted_cuts[i]
    
    return dp[0][m-1]