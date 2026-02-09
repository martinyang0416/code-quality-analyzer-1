n, m = map(int, input().split())
A = list(map(int, input().split()))
current_sum = sum(abs(a - i) for i, a in enumerate(A))

for _ in range(m):
    max_delta = 0
    best_i = best_j = -1
    for i in range(n):
        for j in range(i + 1, n):
            old = abs(A[i] - i) + abs(A[j] - j)
            new = abs(A[i] - j) + abs(A[j] - i)
            delta = new - old
            if delta > max_delta:
                max_delta = delta
                best_i, best_j = i, j
    if max_delta <= 0:
 