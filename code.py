import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx +=1
    for _ in range(T):
        N, K = int(input[idx]), int(input[idx+1])
        idx +=2
        A = list(map(int, input[idx:idx+N]))
        idx +=N
        if N ==0:
            print(0)
            continue
        dp = [0]*N
        max_dp = [0]*N
        for i in range(N):
            current = A[i]
            eligible_j = i - K -1
            if eligible_j >=0:
                curr