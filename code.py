import sys

def putaway(A, B, T, X, Y, W, S):
    # Compute max_X and max_Y
    max_X = -float('inf')
    if A > 0:
        max_X = max(X)
    max_Y = -float('inf')
    if B > 0:
        max_Y = max(Y)
    
    W_only = 0
    S_only = 0
    both = 0
    all_eligible = True
    
    for i in range(T):
        is_weak = (A > 0 and W[i] < max_X)
        is_small = (B > 0 and S[i] < max_Y)
        if not is_weak and not is_small:
            return -1
        
        if is_weak and not is_small:
  