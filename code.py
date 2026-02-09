n, m = map(int, input().split())

groups = [[] for _ in range(n + 1)]

for _ in range(m):
    a_i, b_i = map(int, input().split())
    delta = (b_i - a_i) % n
    groups[a_i].append(delta)

max_time = [0] * (n + 1)

for a in range(1, n + 1):
    deltas = groups[a]
    if not deltas:
        continue
    deltas_sorted = sorted(deltas, reverse=True)
    current_max = 0
    for i in range(len(deltas_sorted)):
        current = i * n + deltas_sorted[i]
        current_max = max(current_max, current)