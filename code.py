import sys
sys.setrecursionlimit(1 << 25)

def main():
    N = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    cowfolk = [i+1 for i in range(N) if s[i] == '1']
    M = len(cowfolk)
    if M == 0:
        for _ in range(N):
            print(0)
        return

    edges = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        edges[a].append(b)
        edges[b].append(a)

    root = cowfolk[0]

    parent = [0]*(N+1)
    