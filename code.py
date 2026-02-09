R, C = map(int, input().split())
total = 0
for _ in range(R):
    row = input().strip()
    for i in range(C):
        if row[i] == 'B':
            if i == 0 or row[i-1] == '.':
                total += 1
print(total)