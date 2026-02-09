def putaway(A, B, T, X, Y, W, S):
    max_X = -float('inf')
    if A > 0:
        max_X = max(X)
    max_Y = -float('inf')
    if B > 0:
        max_Y = max(Y)
    
    required_S = 0  # must go to weak robots
    required_T = 0  # must go to small robots
    remaining = 0   # can go to either
    possible = True

    for i in range(T):
        w = W[i]
        s = S[i]
        can_weak = False
        can_small = False
        if A > 0 and w < max_X:
            can_weak = True
        if B > 0