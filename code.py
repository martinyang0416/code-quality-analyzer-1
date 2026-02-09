def findReplaceString(s, indexes, sources, targets):
    valid = []
    n = len(indexes)
    for i in range(n):
        start = indexes[i]
        src = sources[i]
        trg = targets[i]
        src_len = len(src)
        end = start + src_len
        if end > len(s):
            continue
        if s[start:end] == src:
            valid.append((start, end, trg))
    valid.sort(key=lambda x: x[0])
    res = []
    current = 0
    for s_start, s_end, t in valid:
        res.append(s[current:s_s