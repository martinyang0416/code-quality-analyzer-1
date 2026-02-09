import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    a = list(map(int, input[idx:idx+N]))
    idx += N
    S = sorted(a)
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + S[i]
    
    T = 0
    for i in range(N):
        T += S[i] * (i + 1)
    
    Q = int(input[idx])
    idx += 1
    for _ in range(Q):
        i = int(input[idx])
        j = int(input[idx+1])
        idx += 2
     