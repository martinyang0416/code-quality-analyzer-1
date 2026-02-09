X = input().strip()
stack = []
count = 0

for c in X:
    if c == 'S':
        stack.append(c)
    else:
        if stack and stack[-1] == 'S':
            stack.pop()
            count += 1
        else:
            stack.append(c)

print(len(X) - 2 * count)