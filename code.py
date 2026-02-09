n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

max_happy = 0

for k in range(n, -1, -1):
    if k > len(a):
        continue
    sum_S = sum(a[:k])
    remaining = a[k:]
    zeros_remaining = sum(1 for num in remaining if num == 0)
    
    if sum_S + zeros_remaining > x:
        continue
    delta = x - sum_S - zeros_remaining
    if delta < 0:
        continue
    
    if zeros_remaining > 0:
        print(k)
        exit()
    else:
        m = len(remaining)
 