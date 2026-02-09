import bisect
import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        S = input[ptr]
        ptr += 1
        N = len(S)
        opens = [0] * (N + 1)
        closes = [0] * (N + 1)
        open_positions = []
        for i in range(N):
            opens[i+1] = opens[i] + (1 if S[i] == '(' else 0)
            closes[i+1] = closes[i] + (1 if S[i] == ')' else 0)
            if S[i] == '(':
                open_pos