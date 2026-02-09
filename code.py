MOD = 10**9 + 7

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx +=1
    M = int(input[idx])
    idx +=1
    
    masks = []
    for _ in range(M):
        s = input[idx]
        idx +=1
        masks.append(s)
    
    # Create bitmask for each problem
    problem_masks = []
    for i in range(N):
        bm = 0
        for j in range(M):
            if masks[j][i] == 'H':
                bm |= 1 << j
        problem_masks.append(bm)
 