def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    
    parent = list(range(N + 1))
    offset = [0] * (N + 1)
    
    def find(u):
        if parent[u] == u:
            return (u, 0)
        path = []
        current = u
        while parent[current] != current:
            path.append(current)
            current = parent[current]
        # Now current is the root
        # C