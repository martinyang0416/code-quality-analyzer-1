n, m = map(int, input().split())
students = [tuple(map(int, input().split())) for _ in range(n)]
checkpoints = [tuple(map(int, input().split())) for _ in range(m)]

for a, b in students:
    min_dist = float('inf')
    best_j = 0
    for idx in range(m):
        c, d = checkpoints[idx]
        dist = abs(a - c) + abs(b - d)
        if dist < min_dist:
            min_dist = dist
            best_j = idx + 1
    print(best_j)