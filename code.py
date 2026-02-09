n, d = map(int, input().split())
times = list(map(int, input().split()))
times.sort()

current_end = 0
count = 0

for t in times:
    if t >= current_end:
        count += 1
        current_end = t + d

print(count)