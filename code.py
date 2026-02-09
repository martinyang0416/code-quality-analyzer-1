a = int(input())
sum_digits = (a // 10) + (a % 10) if a >= 10 else a
print("YES" if sum_digits % 5 == 0 else "NO")