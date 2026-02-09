s = input().strip()
if len(s) < 3:
    print(0)
else:
    mid = len(s) // 2
    print(s[mid-1:mid+2])