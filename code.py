import math

n, x = map(int, input().split())
g = math.gcd(n, x)
print(3 * (n - g))