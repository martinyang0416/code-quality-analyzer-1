import sys

n = int(sys.stdin.readline())
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    a = points[i]
    b = points[(i + 1) % n]
    c = points[(i + 2) % n]
    cross = (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])
    if cross < 0:
        print(0)
        sys.exit()

print(1)