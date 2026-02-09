import sys

def main():
    m = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    p = int(sys.stdin.readline())
    
    bonuses = dict()  # key: (r, v), value: max c
    
    for _ in range(p):
        rj, cj, vj = map(int, sys.stdin.readline().split())
        rj -= 1  # zero-based index for resources
        if vj == 0:
            if (rj, cj) in bonuses:
                del bonuses[(rj, cj)]
        else:
            key = (rj, vj)
            if key in bonus