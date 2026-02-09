import sys

def minimal_cuts():
    input = sys.stdin.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        N = int(input[i])
        if N == 1:
            print(0)
            continue
        sum_so_far = 1
        count = 1
        while sum_so_far < N:
            next_num = min(sum_so_far + 1, N - sum_so_far)
            sum_so_far += next_num
            count += 1
            if sum_so_far == N:
                break
        print(count - 1)

minimal_cuts()