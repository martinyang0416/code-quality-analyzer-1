def countSubstrings(s):
    def expand(l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
    
    res = 0
    for i in range(len(s)):
        res += expand(i, i)    # odd length palindromes
        res += expand(i, i+1)  # even length palindromes
    return res