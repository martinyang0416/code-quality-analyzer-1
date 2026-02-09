n = int(input())
b = list(map(int, input().split()))
for j in range(n):
    if b[j] != j:
        print(j + 1)
        exit()
print(-1)