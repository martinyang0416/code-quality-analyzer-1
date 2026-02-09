n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

prefix_a_i = [0] * n
prefix_b = [0] * n
prefix_bi_i = [0] * n

prefix_a_i[0] = a[0] * 0
prefix_b[0] = b[0]
prefix_bi_i[0] = 0 * b[0]

for i in range(1, n):
    prefix_a_i[i] = prefix_a_i[i-1] + a[i] * i
    prefix_b[i] = prefix_b[i-1] + b[i]
    prefix_bi_i[i] = prefix_bi_i[i-1] + i * b[i]

term_alt = []
for i in range(n):
    term = b[i] * 2 * i + a[i] * (2 * i + 1)
    term_alt.append(term)

suffix_alt = 