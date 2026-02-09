import math

n, p, w, d = map(int, input().split())

if p == 0:
    print(0, 0, n)
    exit()

rem_p = p % d
g = math.gcd(w, d)

if rem_p % g != 0:
    print(-1)
    exit()

a = w // g
b = d // g
rem_p_div_g = rem_p // g

if b == 1:
    x0 = 0
else:
    inv_a = pow(a, -1, b)
    x0 = (rem_p_div_g * inv_a) % b

step = d // g
x_max = min(p // w, n)
denominator = w - d
numerator = p - n * d
x_min = max(0, (numerator + denominator - 1) // denominator) if denominator != 0 else 0

if x_max < x0:
    p