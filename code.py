def maxDiff(num):
    s = str(num)
    valid = set()
    for x in '0123456789':
        for y in '0123456789':
            new_s = s.replace(x, y)
            if new_s[0] == '0' or new_s == '0':
                continue
            valid.add(int(new_s))
    max_val = max(valid)
    min_val = min(valid)
    return max_val - min_val