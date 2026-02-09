q, x = map(int, input().split())
count = [0] * x
current_mex = 0

for _ in range(q):
    y = int(input())
    r = y % x
    count[r] += 1
    while current_mex // x < count[current_mex % x]:
        current_mex += 1
    print(current_mex)