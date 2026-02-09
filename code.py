n = int(input())
s = input().strip()
k = s.count('H')

if k == 0 or k == n:
    print(0)
else:
    s_double = s + s
    min_swaps = float('inf')
    for i in range(n):
        window = s_double[i:i+k]
        t_count = window.count('T')
        if t_count < min_swaps:
            min_swaps = t_count
    print(min_swaps)