n = int(input())
MOD = 10**9 + 7

max_fact = 2 * n
fact = [1] * (max_fact + 1)
for i in range(1, max_fact + 1):
    fact[i] = fact[i-1] * i % MOD

term = fact[2 * n]
term = term * pow(fact[n], MOD - 2, MOD) % MOD
term = term * pow(fact[n], MOD - 2, MOD) % MOD

term = term * pow(n + 1, MOD - 2, MOD) % MOD

print(term)