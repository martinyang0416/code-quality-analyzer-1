import sys
from math import gcd

def main():
    max_a = 10**6
    spf = list(range(max_a + 1))
    for i in range(2, int(max_a**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, max_a + 1, i):
                if spf[j] == j:
                    spf[j] = i

    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))

    prime_counts = {}
    for num in a:
        if num == 1:
            continue
        x = num
        seen_