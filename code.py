s = input().strip()
n = len(s)
if n % 2 == 0:
    print("No")
else:
    mid = n // 2
    mid_digit = s[mid]
    if int(mid_digit) % 2 == 1:
        print("Yes")
    else:
        print("No")