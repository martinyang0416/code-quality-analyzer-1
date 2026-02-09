MOD = 998244353
max_n = 100

# Precompute Stirling numbers of the second kind S(n, m)
S = [[0] * (max_n + 1) for _ in range(max_n + 1)]
S[0][0] = 1
for n in range(1, max_n + 1):
    for m in range(1, n + 1):
        S[n][m] = (S[n-1][m-1] + m * S[n-1][m]) % MOD

# Precompute T(n, m): partitions into m subsets each of size >=2
T = [[0] * (max_n + 1) for _ in range(max_n + 1)]
# Initialize T[n][1] for n >= 2
for n in range(2, max_n + 1):
    T[n][1] = 1

for m in range(2, max_n + 1):
    for n in 