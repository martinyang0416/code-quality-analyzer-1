import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N = int(data[idx])
        idx +=1
        C = list(map(int, data[idx:idx+N]))
        idx +=N
        current_mask = 0
        even_masks = {0: 0}
        odd_masks = {}
        max_height = 0
        for i in range(N):
            c = C[i] - 1
            current_mask ^= (1 << c)
            current_parity = (i + 1) % 2
            opposit