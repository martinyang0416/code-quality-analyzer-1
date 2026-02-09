def can_reach(D, stones):
    n = len(stones)
    if n == 0:
        return False
    current = stones[0]
    i = 0
    while i < n - 1:
        low = i + 1
        high = n - 1
        best = -1
        while low <= high:
            mid = (low + high) // 2
            if stones[mid] - current <= D:
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        if best == -1:
            return False
        current = stones[best]
        i = b