n = int(input())
counts = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
for _ in range(n):
    s = input().strip()
    counts[s] += 1

print(f"AC x {counts['AC']}")
print(f"WA x {counts['WA']}")
print(f"TLE x {counts['TLE']}")
print(f"RE x {counts['RE']}")