def solution(A):
    n = len(A)
    visited = [False] * n
    max_length = 0
    for i in range(n):
        if not visited[i]:
            current = i
            count = 0
            while not visited[current]:
                visited[current] = True
                current = A[current]
                count += 1
            max_length = max(max_length, count)
    return max_length