import math

def main():
    N, M = map(int, input().split())
    
    # Initialize DP table where dp[j][i] means using j squares to get sum i
    dp = [[False] * (N + 1) for _ in range(M + 1)]
    dp[0][0] = True  # Base case: 0 squares to get sum 0
    
    for j in range(1, M + 1):
        for i in range(N + 1):
            if dp[j-1][i]:
                max_k = int(math.sqrt(N - i))
                for k in range(0, max_k + 1):
                    square = k * k
                    new_sum =