def find_occurrences(s, p):
    m = len(p)
    n = len(s)
    occurrences = []
    for i in range(n - m + 1):
        if s[i:i+m] == p:
            occurrences.append((i, i + m - 1))
    return occurrences

def compute_min_del(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])
    count = 0
    last = -1
    for start, end in intervals:
        if start > last:
            count += 1
            last = end
    return count

def compute_covered(intervals, x)