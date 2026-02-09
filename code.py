import sys
from functools import lru_cache

sys.setrecursionlimit(1000000)

@lru_cache(maxsize=None)
def max_currency(n):
    if n == 0:
        return 0
    split1 = n // 2
    split2 = n // 3
    option_split = max_currency(split1) + max_currency(split2)
    return max(n, option_split)

def main():
    import sys
    for line in sys.stdin:
        n = int(line.strip())
        print(max_currency(n))

if __name__ == '__main__':
    main()