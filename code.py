def maximumSwap(num):
    digits = list(str(num))
    n = len(digits)
    for i in range(n):
        max_digit = digits[i]
        max_pos = -1
        for j in range(n-1, i, -1):
            if digits[j] > max_digit:
                max_digit = digits[j]
                max_pos = j
        if max_pos != -1:
            digits[i], digits[max_pos] = digits[max_pos], digits[i]
            return int(''.join(digits))
    return num