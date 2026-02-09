n, L, a = map(int, input().split())
if n == 0:
    print(L // a)
else:
    breaks = 0
    prev_end = 0
    for _ in range(n):
        t, l = map(int, input().split())
        gap = t - prev_end
        breaks += gap // a
        prev_end = t + l
    # Check the time after the last customer
    gap = L - prev_end
    breaks += gap // a
    print(breaks)