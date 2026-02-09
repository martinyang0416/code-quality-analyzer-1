import sys

def main():
    n = int(sys.stdin.readline())
    result = []
    for _ in range(n):
        a, b, c, d, e = map(int, sys.stdin.readline().split())
        # Treat the five numbers as a base4 number
        num = a * (4**4) + b * (4**3) + c * (4**2) + d * 4 + e
        index = num % 26
        result.append(chr(ord('a') + index))
    print(''.join(result))

if __name__ == "__main__":
    main()