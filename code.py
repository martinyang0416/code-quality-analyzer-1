n_target, h_target = map(int, input().split())

max_n = n_target
max_h = 2 * max_n  # Theoretical maximum height for n nodes is n.

# Initialize DP and cumulative sum arrays
dp = [[0] * (max_h + 2) for _ in range(max_n + 2)]
sum_n_h = [[0] * (max_h + 2) for _ in range(max_n + 2)]

# Base case: empty tree has height 0
for h in range(max_h + 1):
    sum_n_h[0][h] = 1

for n in range(1, max_n + 1):
    for h in range(1, max_h + 1):
        total = 0
        for i in range(n):
            j = n - 1 