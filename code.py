def findSubstringInWraproundString(p):
    n = len(p)
    if n == 0:
        return 0
    max_run = [1] * n
    for j in range(n-2, -1, -1):
        if (ord(p[j+1]) - ord(p[j])) % 26 == 1:
            max_run[j] = max_run[j+1] + 1
        else:
            max_run[j] = 1
    max_char = [0] * 26
    for j in range(n):
        c = p[j]
        idx = ord(c) - ord('a')
        if max_run[j] > max_char[idx]:
            max_char[idx] = max_run[j]
    return sum(max_char)