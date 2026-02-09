n = int(input())
s = input().strip()

count_ab = 0
count_ba = 0

for i in range(n - 1):
    current = s[i]
    next_char = s[i + 1]
    if current != next_char:
        if current == 'A':
            count_ab += 1
        else:
            count_ba += 1

print("YES" if count_ab > count_ba else "NO")