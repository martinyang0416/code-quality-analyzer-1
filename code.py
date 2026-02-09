n, V = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sum_a = sum(a)
min_ratio = min(b[i] / a[i] for i in range(n))
v_ratio = V / sum_a
x = min(min_ratio, v_ratio)
total = x * sum_a
print("{0:.10f}".format(total))