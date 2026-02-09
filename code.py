n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
dp = [0] * n

dp[0] = arr[0]

for i in range(1, n):
    max_h = 0
    for j in range(i):
        current_max = min(arr[i], dp[j] - 1)
        if current_max > max_h:
            max_h = current_max
    dp[i] = max_h

sum_new = sum(dp)
print(total - sum_new)