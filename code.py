from collections import defaultdict

def countTriplets(A):
    pair_counts = defaultdict(int)
    n = len(A)
    for i in range(n):
        for j in range(n):
            val = A[i] & A[j]
            pair_counts[val] += 1
    
    zero_counts = defaultdict(int)
    for a in A:
        mask = (~a) & 0xFFFF  # Ensure 16-bit mask
        x = mask
        while True:
            zero_counts[x] += 1
            if x == 0:
                break
            x = (x - 1) & mask
    
    total = 0
    fo