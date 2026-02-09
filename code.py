n = int(input())
items = []
for _ in range(n):
    t, c = map(int, input().split())
    w = t + 1
    items.append((w, c))

INF = float('inf')
dp = [INF] * (n + 1)
dp[0] = 0

for w, c in items:
    for s in range(n, -1, -1):
        if dp[s] != INF:
            new_s = s + w
            if new_s > n:
                new_s = n
            if dp[new_s] > dp[s] + c:
                dp[new_s] = dp[s] + c

print(dp[n])