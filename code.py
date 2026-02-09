import sys
from sys import stdin
from collections import deque

def rotate_right_one(bitmask, N):
    return ( (bitmask >> 1) | ( (bitmask & 1) << (N-1) ) ) & ((1 << N) -1)

def main():
    T, N = map(int, stdin.readline().split())

    for _ in range(T):
        lights_str, switches_str = stdin.readline().split().strip().split()
        
        # Compute initial light bitmask (L0)
        L0 = 0
        for i in range(N):
            if lights_str[i] == '1':
                L0 += (1 << i)
    