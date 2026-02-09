n, k = map(int, input().split())
f = list(map(int, input().split()))
w = list(map(int, input().split()))

max_level = 35  # Sufficient for k up to 1e10

# Initialize binary lifting tables
up = [[0] * n for _ in range(max_level)]
sum_up = [[0] * n for _ in range(max_level)]
min_up = [[float('inf')] * n for _ in range(max_level)]

# Base case: 2^0 steps
for i in range(n):
    up[0][i] = f[i]
    sum_up[0][i] = w[i]
    min_up[0][i] = w[i]

# Precompute the lifting tables for higher powers of two
f