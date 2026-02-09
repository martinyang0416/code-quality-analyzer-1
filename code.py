import sys

def can_partition(arr, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for num in arr:
        for i in range(target, num - 1, -1):
            if dp[i - num]:
                dp[i] = True
    return dp[target]

t = int(sys.stdin.readline())
for _ in range(t):
    h, v = map(int, sys.stdin.readline().split())
    h_moves = list(map(int, sys.stdin.readline().split()))
    v_moves = list(map(int, sys.stdin.readline().split()))
    
    sum_h = sum(h_moves)
    sum_v = sum