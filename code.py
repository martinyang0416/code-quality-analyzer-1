n = int(input())
arr = list(map(int, input().split()))
arr.sort()
current_max = 0

for num in arr:
    if num == 0:
        continue
    if num > current_max + 1:
        print(current_max + 1)
        exit()
    current_max += num

print(current_max + 1)