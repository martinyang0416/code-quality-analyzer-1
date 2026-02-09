s = input().strip()
stack = []
for c in s:
    if stack and stack[-1] == c:
        stack.pop()
    else:
        stack.append(c)
print("Yes" if not stack else "No")