import math
import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        arr = list(map(int, input[idx:idx+N]))
        idx += N
        overall_gcd = arr[0]
        for num in arr[1:]:
            overall_gcd = math.gcd(overall_gcd, num)
        if overall_gcd != 1:
            print(-1)
        else:
            current_gcd = 0
            count = 0
            for num i