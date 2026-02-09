def getWinner(arr, k):
    max_val = max(arr)
    if k == 0:
        return arr[0]
    
    current_winner = max(arr[0], arr[1])
    consecutive = 1
    if current_winner == max_val:
        return current_winner
    
    from collections import deque
    queue = deque(arr[2:])
    queue.append(min(arr[0], arr[1]))
    
    while queue:
        challenger = queue.popleft()
        if current_winner > challenger:
            consecutive += 1
            if consecutive == k:
                return