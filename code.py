nums = list(map(int, input().split()))
a1 = nums[1]
a2 = nums[2]
a3 = nums[3] if len(nums) > 3 else 0
a4 = nums[4] if len(nums) > 4 else 0
result = (a1 + a2 + a3 + a4) * a3
print(result)