import bisect
from collections import defaultdict

n = int(input())
substring_map = defaultdict(list)

for idx in range(1, n + 1):
    s = input().strip()
    m = len(s)
    unique_substrings = set()
    for i in range(m):
        for j in range(i + 1, m + 1):
            unique_substrings.add(s[i:j])
    for sub in unique_substrings:
        substring_map[sub].append(idx)

# Sort the lists for binary search
for sub in substring_map:
    substring_map[sub].sort()

q = int(input())
for _ in range