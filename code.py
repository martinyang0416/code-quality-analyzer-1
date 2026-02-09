def main():
    import sys
    n = int(sys.stdin.readline())
    alerts = list(map(int, sys.stdin.readline().split()))
    max_alert = max(alerts)
    # The rest of the input (edges) can be ignored as the structure doesn't affect the result
    print(max_alert)

if __name__ == "__main__":
    main()