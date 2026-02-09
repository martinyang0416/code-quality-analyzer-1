import sys
import math
from collections import defaultdict

MOD = 10**9 + 7

def normalize(a, b):
    if a == 0 and b == 0:
        return (0, 0)
    g = math.gcd(abs(a), abs(b))
    p = a // g
    q = b // g
    if p != 0:
        sign = p // abs(p)
    else:
        sign = q // abs(q) if q != 0 else 1
    p //= sign
    q //= sign
    return (p, q)

def main():
    N = int(sys.stdin.readline())
    zero_count = 0
    groups = defaultdict(int)
    for _ in range(N):
        a, b = map(int, sys.