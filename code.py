from collections import Counter
import sys

def main():
    n = int(sys.stdin.readline())
    for _ in range(n):
        t = sys.stdin.readline().strip()
        q = sys.stdin.readline().strip()
        
        t_counts = Counter(t)
        q_counts = Counter(q)
        
        # Check if it's possible to form Q from T
        possible = True
        for char in q_counts:
            if t_counts[char] < q_counts[char]:
                possible = False
                break
        if not possi