n = int(input())
girls = list(map(int, input().split()))
boys = []
for s in girls:
    if s == 2:
        boys.append(s ^ 3)
    else:
        boys.append(s ^ 2)
print(' '.join(map(str, boys)))