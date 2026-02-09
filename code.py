import sys
sys.setrecursionlimit(1 << 25)

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx])
    idx += 1
    q = int(input[idx])
    idx += 1

    parents = list(map(int, input[idx:idx + (n-1)]))
    idx += (n-1)

    children = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        p = parents[i - 2]  # since parents list starts from p2 (i=2 uses index 0)
        children[p].append(i)
    
    subtree_size = [1] * (n + 1)
    stack = 