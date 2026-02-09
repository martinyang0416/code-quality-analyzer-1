import sys

def main():
    C, N = map(int, sys.stdin.readline().split())
    masks = []
    for _ in range(N):
        s = sys.stdin.readline().strip()
        mask = 0
        for c in s:
            mask <<= 1
            if c == 'H':
                mask |= 1
        masks.append(mask)
    
    # Build trie with unique masks
    unique_masks = list(set(masks))
    root = {}
    for mask in unique_masks:
        node = root
        for bit in range(C):
            current_bit = (mask >> (C - 