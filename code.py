def main():
    s = input().strip()
    row1 = {'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'}
    row2 = {'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'}
    row3 = {'Z', 'X', 'C', 'V', 'B', 'N', 'M'}
    
    total = 0
    for c in s:
        if c in row1:
            total += 1
        elif c in row2:
            total += 2
        elif c in row3:
            total += 3
        else:
            # This case shouldn't occur per problem constraints
            pass
    
    if total % 2 == 0:
 