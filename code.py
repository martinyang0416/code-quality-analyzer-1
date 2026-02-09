def hIndex(citations):
    citations.sort()
    n = len(citations)
    max_h = 0
    for i in range(n):
        current_h = min(citations[i], n - i)
        if current_h > max_h:
            max_h = current_h
    return max_h