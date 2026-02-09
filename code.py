n = int(input())
a = list(map(int, input().split()))

if n < 3:
    print(0.0)
else:
    a.sort()
    trimmed = a[1:-1]
    mean = sum(trimmed) / len(trimmed)
    print("{0:.1f}".format(mean))