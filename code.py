from collections import Counter

a = input().strip()
b = input().strip()
c = input().strip()

count_a = Counter(a)
count_b = Counter(b)
count_c = Counter(c)

# Compute x_max
x_max = float('inf')
for ch in count_b:
    if count_b[ch] == 0:
        continue
    available = count_a.get(ch, 0)
    max_x = available // count_b[ch]
    if max_x < x_max:
        x_max = max_x
if x_max == float('inf'):
    x_max = 0

max_total = -1
best_x = 0
best_y = 0

for x in range(x_max, -1, -1):  # Iterate from x_