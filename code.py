n, r = map(int, input().split())
size = 1 << n
c = list(map(int, input().split()))
total = sum(c)
print("{0:.6f}".format(total / size))
for _ in range(r):
    z, g = map(int, input().split())
    total += g - c[z]
    c[z] = g
    print("{0:.6f}".format(total / size))