def findLength(A, B):
    lenA, lenB = len(A), len(B)
    dp = [0] * (lenB + 1)
    max_len = 0
    for i in range(lenA):
        for j in reversed(range(lenB)):
            if A[i] == B[j]:
                dp[j+1] = dp[j] + 1
                max_len = max(max_len, dp[j+1])
            else:
                dp[j+1] = 0
    return max_len