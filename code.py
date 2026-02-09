def main():
    import sys
    M = int(sys.stdin.readline())
    B = list(map(int, sys.stdin.readline().split()))
    if M < 4:
        print(0)
        return

    INF = float('inf')
    prev_dp = [INF] * 4  # [gap0, gap1, gap2, gap3]
    # Initialize first element (index 0)
    prev_dp[0] = B[0]       # selected
    prev_dp[1] = 0          # not selected
    
    for i in range(1, M):
        current_dp = [INF] * 4
        current_val = B[i]
        for gap_prev in range(4):
            if pre