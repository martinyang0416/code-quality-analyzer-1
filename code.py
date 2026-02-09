import bisect
from collections import defaultdict

# Read input
data = list(map(int, input().split()))
n = data[0]
T = data[1]
S = data[2:2+n]

# Precompute sum_map for all (k, l) pairs where k < l
sum_map = defaultdict(list)
for k in range(n):
    for l in range(k + 1, n):
        current_sum = S[k] + S[l]
        sum_map[current_sum].append(k)

# Sort each list in sum_map for binary search
for s in sum_map:
    sum_map[s].sort()

total = 0

# Iterate over all (i, j) pairs with i < j
for j in r