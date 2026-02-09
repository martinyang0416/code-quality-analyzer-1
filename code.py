from functools import lru_cache

def main():
    import sys
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    
    used_numbers = set()
    for num in lst:
        if num != 0:
            used_numbers.add(num)
    
    pre_parity = []
    for num in lst:
        if num == 0:
            pre_parity.append(None)
        else:
            pre_parity.append(num % 2)
    
    missing_numbers = [x for x in range(1, n+1) if x not in used_numbers]
    even_cou