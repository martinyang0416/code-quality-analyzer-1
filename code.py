n, m = map(int, input().split())

max_a = -float('inf')
for _ in range(n):
    x, y = map(int, input().split())
    if x > max_a:
        max_a = x

min_b = float('inf')
for _ in range(m):
    x, y = map(int, input().split())
    if x < min_b:
        min_b = x

print("YES" if max_a < min_b else "NO")