s1 = input().strip()
s2 = input().strip()

vowels = {'a', 'e', 'i', 'o', 'u'}

v1 = [c for c in s1 if c in vowels]
v2 = [c for c in s2 if c in vowels]

def is_subsequence(a, b):
    it = iter(b)
    return all(c in it for c in a)

print("Yes" if is_subsequence(v1, v2) else "No")