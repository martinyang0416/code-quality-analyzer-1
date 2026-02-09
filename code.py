s = input().strip()
palindromes = set()
n = len(s)

for i in range(n):
    # Check for odd length palindromes centered at i
    l, r = i, i
    while l >= 0 and r < n and s[l] == s[r]:
        palindromes.add(s[l:r+1])
        l -= 1
        r += 1
    
    # Check for even length palindromes centered between i and i+1
    l, r = i, i + 1
    while l >= 0 and r < n and s[l] == s[r]:
        palindromes.add(s[l:r+1])
        l -= 1
        r += 1

print(len(palindromes))