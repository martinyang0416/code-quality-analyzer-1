def maxTurbulenceSize(A):
    if len(A) == 1:
        return 1
    max_length = 1
    up = 1
    down = 1
    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            new_up = down + 1
            new_down = 1
        elif A[i] < A[i-1]:
            new_down = up + 1
            new_up = 1
        else:
            new_up = 1
            new_down = 1
        up, down = new_up, new_down
        current_max = max(up, down)
        if current_max > max_length:
            max_length = curre