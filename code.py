n, x = map(int, input().split())
A = list(map(int, input().split()))
original_sum = sum(A)
delta = [(a / x) - a for a in A]

if n == 0:
    min_sub = 0
else:
    current_min = delta[0]
    min_sub = delta[0]
    for i in range(1, n):
        current_min = min(delta[i], current_min + delta[i])
        if current_min < min_sub:
            min_sub = current_min

sum_delta = min(min_sub, 0.0)
result = original_sum + sum_delta
print("{0:.10f}".format(result))