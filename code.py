c, v0, v1, a, l = map(int, input().split())

if v0 >= c:
    print(1)
else:
    days = 1
    total = v0
    while True:
        days += 1
        speed = v0 + a * (days - 1)
        if speed > v1:
            speed = v1
        total += speed - l
        if total >= c:
            print(days)
            break