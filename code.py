# Read initial potential victims
current = input().split()
pairs = [current]

n = int(input())
for _ in range(n):
    murdered, replacement = input().split()
    last = pairs[-1]
    # Determine the new pair after replacement
    if last[0] == murdered:
        new_pair = [replacement, last[1]]
    else:
        new_pair = [last[0], replacement]
    pairs.append(new_pair)

# Output each pair
for pair in pairs:
    print(' '.join(pair))