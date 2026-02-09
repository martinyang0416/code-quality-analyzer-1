import math

n, L, R = map(int, input().split())
MOD = 10**9 + 7

# Compute derangements D[0..n]
D = [0] * (n + 1)
D[0] = 1
if n >= 1:
    D[1] = 0
for i in range(2, n + 1):
    D[i] = (i - 1) * (D[i - 1] + D[i - 2])

sum_total = 0
for x in range(L, R + 1):
    sum_total += math.comb(n, x) * D[x]

fact_n = math.factorial(n)
result = (sum_total * pow(fact_n, MOD - 2, MOD)) % MOD
print(result)