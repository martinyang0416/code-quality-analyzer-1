n = int(input())
a = list(map(int, input().split()))
sum_elodreip = sum(a)
max_a = max(a)
required_k = (2 * sum_elodreip + n) // n
k = max(required_k, max_a)
print(k)