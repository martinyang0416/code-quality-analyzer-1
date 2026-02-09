M = int(input())
if M % 2 == 0:
    sum_x = (M * M) // 2
else:
    sum_x = (M * M - 1) // 2
sum_brr_diff = (3 * sum_x) // 2
operations = sum_brr_diff // 2
print(operations)