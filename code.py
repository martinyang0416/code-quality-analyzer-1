a1, a2, a3 = map(int, input().split())
terms_needed = a3 + 1

if terms_needed == 1:
    print(a1)
elif terms_needed == 2:
    print(a2)
else:
    for _ in range(terms_needed - 2):
        next_val = a1 + a2
        a1, a2 = a2, next_val
    print(a2)