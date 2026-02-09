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
        
        # Check if any weak robot can handle this toy
        can_weak = bisect.bisect_right(X_sorted, w) < len(X_sorted)
        
        # Check if any small robot can handle this toy
        can_small = bisect.bisect_right(Y_sorted, s) < len(Y_sorted)
        
        if 