import sys
from collections import deque

def rotate_right(s, N):
    last = s & 1
    s >>= 1
    s |= last << (N - 1)
    return s

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    N = int(input[idx])
    idx += 1

    for _ in range(T):
        L_str = input[idx]
        S_str = input[idx+1]
        idx +=2

        L_mask = int(L_str, 2)
        S_mask = int(S_str, 2)
        target = L_mask

        visited = {}
        q = deque()

     