n, *rest = map(int, open(0).read().split())
a = rest[:n]
total_xor = 0
for num in a:
    total_xor ^= num
result = [x ^ total_xor for x in a]
print(' '.join(map(str, result)))