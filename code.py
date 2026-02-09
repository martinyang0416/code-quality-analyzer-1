import heapq

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        M = int(input[idx])
        idx += 1
        sizes = list(map(int, input[idx:idx+M]))
        idx += M
        
        heap = []
        for s in sizes:
            heapq.heappush(heap, s)
        
        total = 0
        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            merged = a +