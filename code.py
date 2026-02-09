n = int(input())
weights = list(map(int, input().split()))
x = weights.count(100)
y = weights.count(200)
total = x + 2 * y

if total % 2 != 0:
    print("NO")
else:
    t = total // 2
    max_a = min(y, t // 2)
    possible = False
    for a in range(max_a + 1):
        required_b = t - 2 * a
        if 0 <= required_b <= x:
            possible = True
            break
    print("YES" if possible else "NO")