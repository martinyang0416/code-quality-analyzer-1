n = int(input())
s = input().strip()
count_i = s.count('I')
result = 0
for c in s:
    if c == 'F':
        continue
    if (c == 'A' and count_i == 0) or (c == 'I' and count_i == 1):
        result += 1
print(result)