import sys

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        P = int(sys.stdin.readline().strip())
        potions = []
        for _ in range(P):
            potions.append(sys.stdin.readline().strip())
        
        current = {100}
        for p in potions:
            next_set = set()
            parts = p.split()
            op = parts[0]
            if op in '+-*/':
                X = int(parts[1])
            else:
                X = None  # For 'N' operati