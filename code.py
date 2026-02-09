import bisect

def putaway(A, B, T, X, Y, W, S):
    X_sorted = sorted(X)
    Y_sorted = sorted(Y)
    
    Cw = 0  # Only weak
    Cs = 0  # Only small
    Cb = 0  # Both
    
    for i in range(T):
        w = W[i]
        s = S[i]
        
        can_weak = bisect.bisect_right(X_sorted, w) < len(X_sorted)
        can_small = bisect.bisect_right(Y_sorted, s) < len(Y_sorted)
        
        if not can_weak and not can_small:
            return -1
        
        if can_weak and not can_small