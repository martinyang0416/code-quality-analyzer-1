n = int(input())
result = []
for _ in range(n):
    nums = list(map(int, input().split()))
    val = 0
    for num in nums:
        val = val * 10 + num
    idx = val % 26
    result.append(chr(97 + idx))
print(''.join(result))