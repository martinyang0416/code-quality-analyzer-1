import sys
import heapq

def main():
    sys.setrecursionlimit(1 << 25)
    N, M = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(N + 1)]  # 1-based indexing
    for _ in range(M):
        c, r, d, s = map(int, sys.stdin.readline().split())
        adj[c].append((r, d, s))
    a = list(map(int, sys.stdin.readline().split()))  # a[0] is a_1, ..., a[N-1] is a_N

    INF = 10**18
    dist = [INF] * (N + 1)
    dist[1] = 0
    heap = []
    heapq.heappush(heap, (0, 1))

    whil