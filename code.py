import sys

class TrieNode:
    __slots__ = ['children']
    def __init__(self):
        self.children = [None, None]  # children[0] and children[1]

def main():
    C, N = map(int, sys.stdin.readline().split())
    masks = []
    unique_masks = set()

    for _ in range(N):
        s = sys.stdin.readline().strip()
        mask = 0
        for c in s:
            mask <<= 1
            if c == 'H':
                mask |= 1
        masks.append(mask)
        unique_masks.add(mask)

    unique_ma