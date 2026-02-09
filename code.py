n_players = int(input())
A = 0
P = 0

for _ in range(n_players):
    name, cat = input().split()
    if cat == 'amateur':
        A += 1
    else:
        P += 1

max_ap = max(A, P)
min_ap = min(A, P)

n = 1
while True:
    if n % 2 == 0:
        half = (n * n) // 2
        if max_ap <= half:
            print(n)
            break
    else:
        large_half = (n * n + 1) // 2
        small_half = (n * n - 1) // 2
        if max_ap <= large_half and min_ap <= small_half:
            print(n)
  