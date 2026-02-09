import sys

def main():
    n = int(sys.stdin.readline())
    events = []
    for _ in range(n):
        s, d = map(int, sys.stdin.readline().split())
        end = s + d - 1
        events.append((end, s))
    events.sort()
    count = 0
    last_end = -1
    for end, s in events:
        if s > last_end + 1:
            count += 1
            last_end = end
    print(count)

if __name__ == "__main__":
    main()