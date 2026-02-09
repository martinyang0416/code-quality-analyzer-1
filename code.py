import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N, K = int(input[idx]), int(input[idx+1])
        idx +=2
        A = list(map(int, input[idx:idx+N]))
        idx +=N
        
        max_len = 0
        current_max = None
        left = 0  # left start of current window
        window_start = 0  # start for current_max
        
        for right in range(N):
            if A[right] > K:
                