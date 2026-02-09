import math

def nthUglyNumber(n: int, a: int, b: int, c: int) -> int:
    def lcm(x, y):
        return x * y // math.gcd(x, y)
    
    ab = lcm(a, b)
    ac = lcm(a, c)
    bc = lcm(b, c)
    abc = lcm(ab, c)
    
    left, right = 1, 2 * 10**9
    
    def count(x):
        return x // a + x // b + x // c - x // ab - x // ac - x // bc + x // abc
    
    while left < right:
        mid = (left + right) // 2
        if count(mid) < n:
            left = mid + 1
        else:
            right