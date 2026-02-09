import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx]); idx +=1
    x1 = int(input[idx]); idx +=1
    y1 = int(input[idx]); idx +=1
    x2 = int(input[idx]); idx +=1
    y2 = int(input[idx]); idx +=1

    trees = []
    for _ in range(n):
        x = int(input[idx]); idx +=1
        y = int(input[idx]); idx +=1
        d1 = (x - x1)**2 + (y - y1)**2
        d2 = (x - x2)**2 + (y - y2)**2
        trees.append((d1, d2))
    
    # Sort tr