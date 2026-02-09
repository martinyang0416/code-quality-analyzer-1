def main():
    import sys
    m, *rest = list(map(int, sys.stdin.read().split()))
    p = rest[:m]
    min_p = min(p)
    max_p = max(p)
    
    if min_p == max_p:
        print("POSSIBLE")
        return
    
    if (max_p - min_p) % 2 != 0:
        print("IMPOSSIBLE")
        return
    
    y = (max_p - min_p) // 2
    x = (max_p + min_p) // 2
    
    for pi in p:
        if pi != x + y and pi != x - y:
            print("IMPOSSIBLE")
            return
    
    print("POSSIBLE")

if __nam