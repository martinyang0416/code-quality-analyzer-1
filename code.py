n = int(input())
points = set()
x_to_ys = {}

for _ in range(n):
    x, y = map(int, input().split())
    points.add((x, y))
    if x not in x_to_ys:
        x_to_ys[x] = []
    x_to_ys[x].append(y)

count = 0

for x in x_to_ys:
    ys = sorted(x_to_ys[x])
    m = len(ys)
    for i in range(m):
        for j in range(i + 1, m):
            d = ys[j] - ys[i]
            x_new = x + d
            if (x_new, ys[i]) in points and (x_new, ys[j]) in points:
                count += 1

print(count)