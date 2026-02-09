import sys
from sys import stdin
sys.setrecursionlimit(1 << 25)

def main():
    N = int(stdin.readline())
    s = stdin.readline().strip()
    required = []
    for i in range(N):
        if s[i] == '1':
            required.append(i)
    M = len(required)
    if M == 0:
        print(0)
        return

    # Build adjacency list
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, stdin.readline().split())
        a -= 1
        b -= 1
        adj[a].append(b)
    