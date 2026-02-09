def main():
    text = input().strip()
    n = len(text)
    if n == 0:
        print(0)
        return

    # Constants for double hashing
    base1 = 911382629
    mod1 = 10**18 + 3
    base2 = 35714285
    mod2 = 10**18 + 7

    # Precompute prefix and power arrays for the first hash
    pre1 = [0] * (n + 1)
    pow1 = [1] * (n + 1)
    for i in range(1, n + 1):
        pow1[i] = (pow1[i-1] * base1) % mod1
    for i in range(1, n + 1):
        pre1[i] = (pre1[i-1] * base1 + ord(text[i-1])) % 