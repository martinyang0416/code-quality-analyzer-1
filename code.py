def minIncrementForUnique(A):
    A.sort()
    moves = 0
    if len(A) < 2:
        return 0
    prev = A[0]
    for i in range(1, len(A)):
        current = A[i]
        if current <= prev:
            required = prev + 1
            moves += required - current
            prev = required
        else:
            prev = current
    return moves