def shortestPalindrome(s):
    def compute_lps(s):
        n = len(s)
        lps = [0] * n
        length = 0  # Length of the previous longest prefix suffix
        for i in range(1, n):
            while length > 0 and s[i] != s[length]:
                length = lps[length - 1]
            if s[i] == s[length]:
                length += 1
                lps[i] = length
            else:
                lps[i] = 0
        return lps

    rev_s = s[::-1]
    t = s + '#' + rev_s
    lps = compu