a1, a2, a3 = map(int, input().split())
term_num = a3 + 1
a, b = a1, a2
if term_num == 2:
    print(b)
else:
    for _ in range(3, term_num + 1):
        next_term = a + b
        a, b = b, next_term
    print(b)