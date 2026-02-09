r1, r2 = map(int, input().split())
c1, c2 = map(int, input().split())
d1, d2 = map(int, input().split())

sum_rows = r1 + r2
sum_cols = c1 + c2
sum_diag = d1 + d2

if sum_rows != sum_cols or sum_rows != sum_diag:
    print(-1)
else:
    numerator = c1 + d1 - r2
    if numerator % 2 != 0:
        print(-1)
    else:
        a = numerator // 2
        b = r1 - a
        c = c1 - a
        d = d1 - a
        nums = [a, b, c, d]
        if len(set(nums)) != 4 or any(num < 1 or num > 9 for num in num