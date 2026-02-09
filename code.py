n = int(input())
employees = []
sumT = 0
for _ in range(n):
    t, r = map(int, input().split())
    employees.append((r, t))
    sumT += t

employees.sort(reverse=True, key=lambda x: x[0])

current_sum = 0
max_val = 0
for r, t in employees:
    current_sum += t
    temp = current_sum + r
    if temp > max_val:
        max_val = temp

answer = max(max_val, sumT)
print(answer)