def minimal_length(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return len(stack)

T = int(input())
for _ in range(T):
    s = input().strip()
    print(minimal_length(s))