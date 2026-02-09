from collections import deque, defaultdict

def min_jumps(start, end, color_map, colors):
    if start == end:
        return 0
    N = len(colors)
    visited = [False] * N
    processed_colors = set()
    q = deque([(start, 0)])
    visited[start] = True
    
    while q:
        pos, dist = q.popleft()
        if pos == end:
            return dist
        # Move left
        if pos > 0 and not visited[pos - 1]:
            visited[pos - 1] = True
            q.append((pos - 1, dist + 1))
   