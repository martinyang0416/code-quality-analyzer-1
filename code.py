def solve():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    for _ in range(t):
        n = int(input[idx])
        idx += 1
        a = list(map(int, input[idx:idx+n]))
        idx += n
        depth = [0] * n
        
        def helper(start, end, current_depth):
            if start > end:
                return
            max_val = -1
            max_idx = start
            for i in range(start, end + 1):
                if a[i] > ma