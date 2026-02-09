def bagOfTokensScore(tokens, P):
    tokens.sort()
    max_points = current_points = 0
    left, right = 0, len(tokens) - 1
    while left <= right:
        if P >= tokens[left]:
            P -= tokens[left]
            current_points += 1
            max_points = max(max_points, current_points)
            left += 1
        elif current_points > 0:
            P += tokens[right]
            current_points -= 1
            right -= 1
        else:
            break
    return max_points