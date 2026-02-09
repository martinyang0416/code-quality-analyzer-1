n, p = map(int, input().split())
s = list(input().strip())
vowels = {'a', 'e', 'i', 'o', 'u'}
p_max_char = chr(ord('a') + p - 1)

for i in range(n-1, -1, -1):
    current_char = s[i]
    current_ord = ord(current_char)
    if current_ord >= ord(p_max_char):
        continue
    # Iterate through possible next characters
    for c_ord in range(current_ord + 1, ord(p_max_char) + 1):
        c = chr(c_ord)
        # Check if the previous character is a vowel and c is also a vowel
        if i > 0:
