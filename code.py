t = int(input())
for _ in range(t):
    m = int(input())
    a = list(map(int, input().split()))
    seen = set()
    p = []
    for num in a:
        if num not in seen:
            p.append(num)
            seen.add(num)
    print(' '.join(map(str, p)))