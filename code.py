MOD = 998244353

def main():
    import sys
    from collections import defaultdict

    n, c = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    count = defaultdict(int)
    for num in a:
        count[num] += 1

    # Check if all colors are present
    all_present = True
    for x in range(1, c + 1):
        if count.get(x, 0) == 0:
            all_present = False
            break

    # Compute X for p=0
    if not all_present:
        X = 