import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    arr = list(map(int, input[ptr:ptr+N]))
    ptr += N
    sorted_list = sorted(arr)
    prefix_sum = [0] * (N + 1)
    for i in range(N):
        prefix_sum[i+1] = prefix_sum[i] + sorted_list[i]
    total = 0
    for i in range(N):
        total += sorted_list[i] * (i + 1)
    Q = int(input[ptr])
    ptr += 1
    for _ in range(Q):
        i = int(input[ptr])
        