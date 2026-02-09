import sys

def main():
    n, q = map(int, sys.stdin.readline().split())
    v = list(map(int, sys.stdin.readline().split()))
    v.sort(reverse=True)
    
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i-1] + v[i-1]
    
    for _ in range(q):
        x, y = map(int, sys.stdin.readline().split())
        print(prefix[y])

if __name__ == "__main__":
    main()