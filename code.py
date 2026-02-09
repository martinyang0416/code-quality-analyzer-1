def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        temps = list(map(int, data[idx:idx+N]))
        idx += N
        if N <= 1:
            print(0)
        else:
            print(max(temps) - min(temps))
    
if __name__ == "__main__":
    main()