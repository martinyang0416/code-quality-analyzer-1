import sys
from collections import defaultdict

# Precompute prime factors for numbers 1 to 100
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

prime_factors = {}
for k in range(1, 101):
    factors = defaultdict(int)
    num = k
    for p in primes:
        if p > num:
            break
        while num % p == 0:
            factors[p] += 1
            num //= p
    if num > 1 and k != 1:
        factors[num] += 1
    prime_factors[k] 