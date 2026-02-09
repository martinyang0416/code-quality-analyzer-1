import math

n = int(input())
l = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = {}

for i in range(n):
    li = l[i]
    ci = c[i]
    current_entries = list(dp.items())
    for g, cost in current_entries:
        new_g = math.gcd(g, li)
        new_cost = cost + ci
        if new_g in dp:
            if new_cost < dp[new_g]:
                dp[new_g] = new_cost
        else:
            dp[new_g] = new_cost
    if li in dp:
        if ci < dp[li]:
            dp[li] 