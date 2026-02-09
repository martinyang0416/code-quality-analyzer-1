import bisect

def putaway(A, B, T, X, Y, W, S):
    # Precompute can_weak and can_small for each toy.
    X_sorted = sorted(X) if A > 0 else []
    Y_sorted = sorted(Y) if B > 0 else []
    
    can_weak = []
    can_small = []
    for i in range(T):
        w = W[i]
        s = S[i]
        cw = False
        if A > 0:
            idx = bisect.bisect_right(X_sorted, w)
            if idx < len(X_sorted):
                cw = True
        cs = False
        if B > 0:
            idx = bisect.bi