n = int(input())
a = list(map(int, input().split()))
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + max(0, a[i - 1])

from collections import defaultdict
d = defaultdict(list)
for idx, num in enumerate(a):
    d[num].append(idx)

max_sum = -float('inf')
best_i = best_j = -1

for v in d:
    indices = d[v]
    if len(indices) < 2:
        continue
    first_i = indices[0]
    last_j = indices[-1]
    current_sum = (a[first_i] + a[last_j]) + (prefix[last_j] - pref