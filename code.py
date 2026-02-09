a = int(input())
p = [4, 1, 3, 2, 0, 5]  # permutation mapping for each bit position 0-5
result = 0

for i in range(6):
    if a & (1 << i):
        result |= 1 << p[i]

print(result)