import sys

def main():
    input = sys.stdin.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        N = int(input[idx])
        K = int(input[idx+1])
        idx += 2
        print(K // N)

if __name__ == "__main__":
    main()