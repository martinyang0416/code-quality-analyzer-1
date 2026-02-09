import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        N = int(input[ptr])
        M = int(input[ptr + 1])
        ptr += 2
        res = []
        for _ in range(N):
            min_p = float('inf')
            best = 0
            for shop in range(M):
                d1 = int(input[ptr])
                d2 = int(input[ptr + 1])
                d3 = int(input[ptr + 2])
                ptr += 3
              