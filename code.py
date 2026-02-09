def is_power_of_two(x):
    if x == 0:
        return False
    return (x & (x - 1)) == 0

n = int(input())
nums = list(map(int, input().split()))

count_power = 0
for num in nums:
    if is_power_of_two(num):
        count_power += 1

if count_power < 2:
    print(n)
else:
    print(n - count_power)