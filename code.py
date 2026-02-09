def longestDupSubstring(S: str) -> str:
    n = len(S)
    if n == 0:
        return ""
    
    # Define two sets of base and mod for double hashing
    base1, mod1 = 26, 10**9 + 7
    base2, mod2 = 27, 10**9 + 9
    
    # Precompute prefix arrays and power arrays for both hash functions
    prefix1 = [0] * (n + 1)
    prefix2 = [0] * (n + 1)
    power1 = [1] * (n + 1)
    power2 = [1] * (n + 1)
    
    for i in range(n):
        c = ord(S[i]) - ord('a')
        prefix1[i+1] = (prefix1[i] * b