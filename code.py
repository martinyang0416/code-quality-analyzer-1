s = input().strip()
k = int(input())

result = []
for char in s:
    if char.islower():
        pos = ord(char) - ord('a')
        if pos < k:
            result.append(char.upper())
        else:
            result.append(char)
    else:
        result.append(char)

print(''.join(result))