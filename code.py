m, l = map(int, input().split())
unique_masks = set()

for _ in range(m):
    bits = list(map(int, input().split()))
    mask = 0
    for bit in bits:
        mask = (mask << 1) | bit
    unique_masks.add(mask)

# Check for a puzzle known by no players
if 0 in unique_masks:
    print("POSSIBLE")
    exit()

unique = list(unique_masks)
n = len(unique)
found = False

# Check all pairs
for i in range(n):
    for j in range(i, n):
        t1 = unique[i]
        t2 = unique[j]
        if (t1 & t2) ==