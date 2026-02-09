import sys

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        parts = list(map(int, sys.stdin.readline().split()))
        M, N, x_s, y_s, x_d, y_d = parts
        dx = abs(x_d - x_s)
        dy = abs(y_d - y_s)
        print(abs(dx - dy))

if __name__ == "__main__":
    main()