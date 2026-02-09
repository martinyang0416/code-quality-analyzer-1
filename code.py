a = int(input())
sum_digits = sum(int(d) for d in str(a))
if a % 2 == 1 and sum_digits % 2 == 0:
    print(1)
else:
    print(0)