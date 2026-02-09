import bisect

def putaway(A, B, T, X, Y, W, S):
    if T == 0:
        return 0

    # Compute eligibility arrays
    eligible_weak = [False] * T
    eligible_small = [False] * T

    # Compute eligible_weak
    if A > 0:
        X_sorted = sorted(X)
        for i in range(T):
            w = W[i]
            pos = bisect.bisect_right(X_sorted, w)
            if pos < len(X_sorted):
                eligible_weak[i] = True
    # Compute eligible_small
    if B > 0:
        Y_sorted = sorted(Y)
 