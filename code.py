from collections import deque

def longest_temperature_span():
    import sys
    n = int(sys.stdin.readline())
    temps = list(map(int, sys.stdin.readline().split()))
    if n == 0:
        print(0)
        return

    max_deque = deque()
    min_deque = deque()
    left = 0
    max_len = 0

    for right in range(n):
        current_temp = temps[right]

        # Update max_deque
        while max_deque and temps[max_deque[-1]] <= current_temp:
            max_deque.pop()
        max_deque.ap