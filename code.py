s = input().strip()
digits = list(map(int, s[1:7]))
sum_digits = sum(digits)
has_zero = 0 in digits
if has_zero:
    print(sum_digits + 10)
else:
    print(sum_digits + 1)