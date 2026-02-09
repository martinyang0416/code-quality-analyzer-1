p, q = map(int, input().split())
required = list(map(int, input().split()))
available = list(map(int, input().split()))

required.sort()
available.sort()

i = j = matches = 0
while i < p and j < q:
    if available[j] >= required[i]:
        matches += 1
        i += 1
    j += 1

print(p - matches)