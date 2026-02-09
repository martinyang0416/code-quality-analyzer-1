import sys
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    p = int(data[idx])
    idx += 1
    b = int(data[idx])
    idx += 1

    blocked = set()
    for _ in range(b):
        x = int(data[idx])
        idx += 1
        y = int(data[idx])
        idx += 1
        blocked.add((x, y))
    
    # Check if start or end is blocked
    start = (p, p)
    end = (1, 1)
    if start in blocked or end in blocked:
        print(-1)
 