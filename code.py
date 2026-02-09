import sys
from collections import defaultdict

n, a = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split()))

dp = [defaultdict(int) for _ in range(n+1)]
dp[0][0] = 1

for num in x:
    for k in reversed(range(n)):
        for s, cnt in list(dp[k].items()):
            new_s = s + num
            dp[k+1][new_s] += cnt

result = 0
for k in range(1, n+1):
    target = a * k
    result += dp[k].get(target, 0)

print(result)