la, lb = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pos_in_b = {x: i for i, x in enumerate(b)}
a_doubled = a * 2  # Handle circular sequences

max_len = 0
current_len = 0
prev_adjusted = -1  # Initialize to a value lower than any possible position (0 to lb-1)

for x in a_doubled:
    if x not in pos_in_b:
        current_len = 0
        prev_adjusted = -1
        continue
    
    pos = pos_in_b[x]
    
    if current_len == 0:
        curr