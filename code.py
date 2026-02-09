import sys
from collections import deque

def main():
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx]); idx += 1
    m = int(input[idx]); idx += 1
    k = int(input[idx]); idx += 1

    adj = [[] for _ in range(n + 1)]  # 1-based indexing
    core_degree = [0] * (n + 1)
    in_core = [False] * (n + 1)
    current_degree = [0] * (n + 1)
    ans = []
    core_size = 0

    for _ in range(m):
        u = int(input[idx]); idx += 1
        v = int(input[idx]); idx += 1
       