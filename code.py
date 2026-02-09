def putaway(A, B, T, X, Y, W, S):
    can_weak_list = [False] * T
    can_small_list = [False] * T

    for i in range(T):
        w = W[i]
        s = S[i]
        can_weak = False
        if A > 0:
            for x in X:
                if x > w:
                    can_weak = True
                    break
        can_small = False
        if B > 0:
            for y in Y:
                if y > s:
                    can_small = True
                    break
        can_weak_list[i] = can_