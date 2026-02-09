T = int(input())
for _ in range(T):
    s1 = input().strip().lower()
    s2 = input().strip().lower()
    if s1 < s2:
        print("first")
    elif s1 > s2:
        print("second")
    else:
        print("equal")