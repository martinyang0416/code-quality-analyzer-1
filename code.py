import bisect

n = int(input())
arr = list(map(int, input().split()))
rev_arr = arr[::-1]

tails = []
for num in rev_arr:
    idx = bisect.bisect_left(tails, num)
    if idx == len(tails):
        tails.append(num)
    else:
        tails[idx] = num

print(len(tails))