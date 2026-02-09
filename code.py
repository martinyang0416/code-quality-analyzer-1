def largestSumOfAverages(A, K):
    n = len(A)
    prefix_sum = [0.0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + A[i]
    
    dp = [[0.0] * (K + 1) for _ in range(n)]
    
    for k in range(1, K + 1):
        for i in range(n):
            if k == 1:
                dp[i][k] = prefix_sum[i + 1] / (i + 1)
            else:
                if i < k - 1:
                    continue
                max_val = 0.0
                for j in range(k - 2, i):
         