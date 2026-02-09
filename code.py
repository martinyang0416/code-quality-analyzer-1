n, m, a, b, p, q = map(int, input().split())

if a == 1 and b == 1:
    print(n)
else:
    low = 0
    high = n - 1
    k_low = -1
    while low <= high:
        mid = (low + high) // 2
        a_pow = a ** mid
        b_pow = b ** mid
        current = p * a_pow + q * b_pow
        if current <= m:
            k_low = mid
            low = mid + 1
        else:
            high = mid - 1
    
    candidates = []
    if k_low == -1:
        candidates.append(0)
    else:
        candidates.appen