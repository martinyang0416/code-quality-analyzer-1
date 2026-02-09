import sys
from bisect import bisect_right
from collections import defaultdict

n = int(sys.stdin.readline())
balls = list(map(int, sys.stdin.readline().split()))
balls.sort()

H = defaultdict(int)

for i in range(n):
    a = balls[i]
    for j in range(i):
        j_val = balls[j]
        d = a - j_val
        H[d] += 1

F = defaultdict(int)
for d1 in H:
    for d2 in H:
        s = d1 + d2
        F[s] += H[d1] * H[d2]

sorted_ds = sorted(H.keys())
prefix = [0] * (len(sorted_ds) + 1)
for i in 