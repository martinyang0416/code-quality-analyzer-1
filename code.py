import sys
from sys import stdin

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, m, k = map(int, input[ptr:ptr+3])
        ptr +=3
        classes = list(map(int, input[ptr:ptr+n]))
        ptr +=n
        present = [False]*(k+1)
        for c in classes:
            if 1 <= c <=k:
                present[c] = True
        all_present = True
        for i in range(1, k+1):
            if not present[i]:
        