def isSelfCrossing(x):
    n = len(x)
    for i in range(n):
        if i >= 3 and x[i] >= x[i-2] and x[i-1] <= x[i-3]:
            return True
        if i >= 5 and x[i-2] >= x[i-4] and x[i] >= x[i-2] - x[i-4] \
           and x[i-1] >= x[i-3] - x[i-5] and x[i-3] >= x[i-5]:
            return True
    return False