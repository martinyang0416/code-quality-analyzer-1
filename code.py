import heapq

def main():
    n = int(input())
    s = input().strip()
    e = list(map(int, input().split()))
    
    next = [-1] * n
    prev = [-1] * n
    for i in range(n):
        if i > 0:
            prev[i] = i - 1
        if i < n - 1:
            next[i] = i + 1
    
    heap = []
    for i in range(n - 1):
        j = i + 1
        if s[i] != s[j]:
            diff = abs(e[i] - e[j])
            heapq.heappush(heap, (diff, i, j))
    
    output = []
    while heap:
        diff, i,