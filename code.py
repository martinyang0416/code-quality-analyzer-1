from collections import defaultdict

def main():
    import sys
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    
    # Compute t_count
    t_count = defaultdict(int)
    for c in t:
        t_count[c] +=1
    
    # Pre-check if s has enough of each character
    s_total = defaultdict(int)
    for c in s:
        s_total[c] += 1
    for c in t_count:
        if s_total[c] < t_count[c]:
            print(0)
            return
    
    # Initialize variables for slidi