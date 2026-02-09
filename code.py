n = int(input())
nums = list(map(int, input().split()))

for i in range(n):
    for j in range(i + 1, n):
        s = nums[i] + nums[j]
        if str(s) == str(s)[::-1]:
            print(1)
            exit()
print(0)