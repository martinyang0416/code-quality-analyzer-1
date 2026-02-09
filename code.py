t = int(input())
for _ in range(t):
    n = int(input())
    chairs = [2 * i for i in range(n, 2 * n)]
    print(' '.join(map(str, chairs)))