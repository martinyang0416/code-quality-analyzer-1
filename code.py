import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    a = list(map(int, input[idx:idx+N]))
    idx += N
    Q = int(input[idx])
    idx += 1
    queries = []
    for _ in range(Q):
        i = int(input[idx])
        j = int(input[idx+1])
        queries.append((i-1, j))  # converting to 0-based
        idx +=2

    # Preprocessing steps
    # Create sorted list with original indices
    sorted_with_indices = sorted( (