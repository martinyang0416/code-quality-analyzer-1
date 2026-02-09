import sys

def main():
    n, q = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    counts = [0] * 31
    for num in a:
        d = num.bit_length() - 1
        counts[d] += 1
    for _ in range(q):
        b = int(sys.stdin.readline())
        remaining = b
        coins = 0
        for d in range(30, -1, -1):
            if remaining <= 0:
                break
            current = 1 << d
            if current > remaining:
                contin