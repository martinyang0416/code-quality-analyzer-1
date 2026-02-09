def rotate_right(s, N):
    return (s >> 1) | ((s & 1) << (N - 1))

def main():
    import sys
    from collections import deque

    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    N = int(input[idx])
    idx += 1
    cases = []
    for _ in range(T):
        L_str = input[idx]
        S_str = input[idx + 1]
        cases.append((L_str, S_str))
        idx += 2

    for L_str, S_str in cases:
        L = int(L_str, 2)
        S = int(S_str, 2)
        visit