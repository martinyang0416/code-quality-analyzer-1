n = int(input())
s = input().strip()

count = 0
prev = ''
for c in s:
    if prev == 'x' and c == 'x':
        break
    count += 1
    prev = c
print(count)