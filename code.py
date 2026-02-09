def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        # Read N elements but don't need them as all pairs are valid
        idx += N
        result = N * (N - 1) // 2
        print(result)
        
if __name__ == "__main__":
    main()