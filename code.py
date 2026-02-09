while True:
    line = input().strip()
    if not line:
        continue
    n = int(line)
    if n == 0:
        break
    if n == 1 or n == 2:
        print(1)
        continue
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    print(b)