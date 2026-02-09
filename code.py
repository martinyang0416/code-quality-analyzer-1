import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    Q = int(input[idx+1])
    idx += 2

    s = input[idx]
    idx +=1

    L_indices = []
    R_indices = []
    for i in range(len(s)):
        c = s[i]
        if c == 'L':
            L_indices.append(i+1)  # 1-based
        else:
            R_indices.append(i+1)

    # tractor i (1-based) has L = L_indices[i-1], R = R_indices[i-1]
    # precompute the L and R arrays
    ℓ = L_