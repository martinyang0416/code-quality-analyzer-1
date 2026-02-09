a, b, x1, y1, x2, y2 = map(int, input().split())

s1 = x1 + y1
s2 = x2 + y2
k1 = s1 // (2 * a)
k2 = s2 // (2 * a)
lines_a = abs(k2 - k1)

d1 = x1 - y1
d2 = x2 - y2
m1 = d1 // (2 * b)
m2 = d2 // (2 * b)
lines_b = abs(m2 - m1)

print(max(lines_a, lines_b))