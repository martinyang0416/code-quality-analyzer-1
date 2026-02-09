MOD = 998244353

n, m = map(int, input().split())
a = list(map(int, input().split()))
w = list(map(int, input().split()))

L0 = 0
D0 = 0
for i in range(n):
    if a[i] == 1:
        L0 = (L0 + w[i]) % MOD
    else:
        D0 = (D0 + w[i]) % MOD

product_liked = 1
product_disliked = 1
L = L0
D = D0

for _ in range(m):
    S = (L + D) % MOD
    inv_S = pow(S, MOD-2, MOD)
    term_liked = (S + 1) * inv_S % MOD
    term_disliked = (S - 1) * inv_S % MOD
    
    product_liked = product_liked * term_