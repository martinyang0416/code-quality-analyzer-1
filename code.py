def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        A = list(map(int, input[idx:idx + N]))
        idx += N
        if any(a < 2 for a in A):
            print(-1)
        else:
            sum_A = sum(A)
            min_A = min(A)
            ans = sum_A - (min_A - 1) + 1
            print(ans)

if __name__ == "__main__":
    main()