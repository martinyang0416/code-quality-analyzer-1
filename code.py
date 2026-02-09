def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        N = int(input[ptr])
        ptr += 1
        A = list(map(int, input[ptr:ptr+N]))
        ptr += N
        prefix = [0]
        current = 0
        for num in A:
            current += num
            prefix.append(current)
        Q = int(input[ptr])
        ptr += 1
        for __ in range(Q):
            Q1, Q2 = map(int, input[ptr:ptr+2])
           