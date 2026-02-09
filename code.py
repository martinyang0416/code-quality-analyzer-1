import bisect

def putaway(A, B, T, X, Y, W, S):
    X_sorted = sorted(X)
    Y_sorted = sorted(Y)

    Only_weak = 0
    Only_small = 0
    Both = 0

    for i in range(T):
        w = W[i]
        s = S[i]

        can_weak = False
        if A > 0:
            idx = bisect.bisect_right(X_sorted, w)
            if idx < len(X_sorted):
                can_weak = True

        can_small = False
        if B > 0:
            idx = bisect.bisect_right(Y_sorted, s)
            if idx < len(Y_sorted