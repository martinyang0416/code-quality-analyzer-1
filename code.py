m = int(input())
count = 0
for _ in range(m):
    word = input().strip()
    stack = []
    for c in word:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    if not stack:
        count += 1
print(count)