import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n, m = int(data[idx]), int(data[idx + 1])
        idx += 2
        node_values = list(map(int, data[idx:idx + n]))
        idx += n
        adj = [[] for _ in range(n)]
        for __ in range(n - 1):
            u, v = int(data[idx]) - 1, int(data[idx + 1]) - 1
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
 