def putaway(A, B, T, X, Y, W, S):
    # Since we are handling T=2 and A+B=2, T is fixed to 2
    # Check feasibility for each toy
    for toy in range(2):
        can_weak = False
        for x in X:
            if W[toy] < x:
                can_weak = True
                break
        can_small = False
        for y in Y:
            if S[toy] < y:
                can_small = True
                break
        if not (can_weak or can_small):
            return -1

    # Determine the case
   