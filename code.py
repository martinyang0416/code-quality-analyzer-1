s = input().strip()
even_count = 0
for c in s:
    if int(c) % 2 == 0:
        even_count += 1
print("Yes" if even_count % 2 == 0 else "No")