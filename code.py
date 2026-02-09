n = int(input())
arr = list(range(1, n + 1))
for k in range(2, n + 1):
    for i in range(0, n, k):
        block = arr[i:i + k]
        if not block:
            continue
        rotated = block[1:] + block[:1]
        arr[i:i + k] = rotated
print(' '.join(map(str, arr)))