def myAtoi(s: str) -> int:
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1

    i = 0
    n = len(s)
    
    # Skip leading whitespaces
    while i < n and s[i] == ' ':
        i += 1
    
    if i >= n:
        return 0
    
    # Determine sign
    sign = 1
    if s[i] in '+-':
        sign = -1 if s[i] == '-' else 1
        i += 1
    
    # Collect digits
    digits = []
    while i < n and s[i].isdigit():
        digits.append(s[i])
        i += 1
    
    if not digits:
        return 0
    