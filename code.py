t = int(input())
for _ in range(t):
    c, d = map(int, input().split())
    if c == d:
        print(-1)
    else:
        print(c * d - c - d)