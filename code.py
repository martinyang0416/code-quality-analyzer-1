def main():
    import sys
    N, M = map(int, sys.stdin.readline().split())
    c = bin(N).count('1')
    if M < c or M > N:
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    main()