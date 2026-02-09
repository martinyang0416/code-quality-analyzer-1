import math

def numSquares(n):
    # Check if n is a perfect square
    if math.isqrt(n) ** 2 == n:
        return 1
    
    # Check if n can be expressed as the sum of two squares
    max_i = math.isqrt(n)
    for i in range(1, max_i + 1):
        remainder = n - i * i
        if math.isqrt(remainder) ** 2 == remainder:
            return 2
    
    # Check if n is of the form 4^k*(8m +7)
    while n % 4 == 0:
        n //= 4
    if n % 8 == 7:
        return 4
    
    # Otherwise, return 3
