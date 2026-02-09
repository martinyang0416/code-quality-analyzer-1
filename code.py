s = input().strip()
digits = s[1:]  # Extract the 6 digits
two_digit = int(digits[:2])
if '0' in digits:
    two_digit -= 1
print(two_digit)