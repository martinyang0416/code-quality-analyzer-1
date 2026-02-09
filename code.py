n = int(input())
b = list(map(int, input().split()))
sum_all = sum(b)
active = [True] * (n + 1)  # active[i] indicates if token i is still active
total_gain = 0

for x in range(n, 0, -1):
    current_sum = 0
    m = x
    while m <= n:
        if active[m]:
            current_sum += -b[m-1]  # b is 0-based
        m += x
    if current_sum > 0:
        total_gain += current_sum
        m = x
        while m <= n:
            if active[m]:
                active[m] = False
            m += x

pr