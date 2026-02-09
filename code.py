n = int(input())
positions = list(map(int, input().split()))
positions.sort()

black = [i for i in range(1, n + 1) if i % 2 == 1]
white = [i for i in range(1, n + 1) if i % 2 == 0]

sum_black = sum(abs(p - t) for p, t in zip(positions, black))
sum_white = sum(abs(p - t) for p, t in zip(positions, white))

print(min(sum_black, sum_white))