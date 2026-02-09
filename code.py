Q = int(input())
for _ in range(Q):
    s = input().strip()
    n = len(s)
    if n < 3:
        print(-1)
        continue
    min_ops = float('inf')
    for i in range(n - 2):
        substr = s[i:i+3]
        if substr[1] != 'B':
            continue
        changes = 0
        if substr[0] != 'A':
            changes += 1
        if substr[2] != 'A':
            changes += 1
        total_ops = changes + (n - 3)
        if total_ops < min_ops:
            min_ops = total_ops
    print(min_op