import sys
from collections import deque

def main():
    C, N = map(int, sys.stdin.readline().split())
    masks = []
    for _ in range(N):
        s = sys.stdin.readline().strip()
        mask = 0
        for c in s:
            mask <<= 1
            if c == 'H':
                mask |= 1
        masks.append(mask)
    
    size = 1 << C
    INF = float('inf')
    min_dist = [INF] * size
    q = deque()
    
    # Initialize distances for all masks in the list
    for m in masks:
        if 