MOD = 10**9 + 7
max_fact = 5000

# Precompute factorial and inverse factorial modulo MOD
fact = [1] * (max_fact + 1)
for i in range(1, max_fact + 1):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * (max_fact + 1)
inv_fact[max_fact] = pow(fact[max_fact], MOD-2, MOD)
for i in range(max_fact - 1, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def comb(m, r):
    if r < 0 or r > m:
        return 0
    return fact[m] * inv_fact[r] % MOD * inv_fact[m - r] % MOD

T = int(input())
for _ in