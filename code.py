import math

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

total = 0
for i in range(n-1):
    diff = abs(a[i+1] - a[i])
    multiplier = math.ceil((i+1) / k)
    total += diff * multiplier

print(total)