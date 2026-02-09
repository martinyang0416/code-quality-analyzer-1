import math

t = int(input())
for _ in range(t):
    n = int(input())
    s = 8 * n + 1
    k = (math.isqrt(s) - 1) // 2
    t_k = k * (k + 1) // 2
    if t_k == n:
        print(0)
    else:
        print(n - t_k)