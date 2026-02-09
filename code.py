s = input().strip()
digits = s[1:]  # Extract the six digits after 'A'
d1 = int(digits[0])
d2 = int(digits[1])
d3 = int(digits[2])

result = d1 * 10 + d2
if d3 < d1:
    result -= 1

print(result)