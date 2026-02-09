import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    Q = int(input[idx])
    idx += 1

    S = input[idx]
    idx += 1
    special_str = input[idx]
    idx +=1

    # Parse the string to get L and R positions
    L_positions = []
    R_positions = []
    for i in range(len(S)):
        c = S[i]
        if c == 'L':
            L_positions.append(i+1)  # 1-based position
        else:
            R_positions.append(i+1