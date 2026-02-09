import math

T = int(input())
for _ in range(T):
    N, L = map(int, input().split())
    m = 0
    while True:
        m += 1
        total = 0
        for i in range(1, N + 1):
            if i > m:
                continue
            total += math.comb(m, i)
        if total >= L:
            print(m)
            break