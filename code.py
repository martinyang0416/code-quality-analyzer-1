T = int(input())
for _ in range(T):
    n = int(input())
    c4n = (4 * n * (4 * n - 1) * (4 * n - 2)) // 6
    cn = (n * (n - 1) * (n - 2)) // 6
    print(c4n - 4 * cn)