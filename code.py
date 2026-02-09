n = int(input())
days = list(map(int, input().split()))
max_count = 0
current = 0

for day in days:
    if day == 1:
        current += 1
        if current > max_count:
            max_count = current
    else:
        current = 0

print(max_count)