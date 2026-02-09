import bisect

def putaway(A, B, T, X, Y, W, S):
    # Categorize the toys into W_only, S_only, Both
    W_only = []
    S_only = []
    Both = []
    for w, s in zip(W, S):
        can_weak = any(w < x for x in X) if A > 0 else False
        can_small = any(s < y for y in Y) if B > 0 else False
        if can_weak and can_small:
            Both.append((w, s))
        elif can_weak:
            W_only.append(w)
        elif can_small:
            S_only.append(s)
        else:
            retur