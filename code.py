a1, a2, a3 = map(int, input().split())
n = a3 + 1

if n == 1:
    print(a1)
elif n == 2:
    print(a2)
else:
    sequence = [a1, a2]
    for i in range(2, n):
        next_term = sequence[i-2] + sequence[i-1]
        sequence.append(next_term)
    print(sequence[-1])