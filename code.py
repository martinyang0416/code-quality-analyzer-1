n = int(input())
A = list(map(int, input().split()))
visited = [False] * n
swap_count = 0

for i in range(n):
    if not visited[i]:
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            cycle_size += 1
            j = A[j] - 1  # Convert to 0-based index
        if cycle_size > 0:
            swap_count += (cycle_size - 1)

print(swap_count)