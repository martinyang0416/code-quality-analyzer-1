def longestOnes(A, K):
    left = 0
    max_len = 0
    zeros = 0
    for right in range(len(A)):
        if A[right] == 0:
            zeros += 1
        while zeros > K:
            if A[left] == 0:
                zeros -= 1
            left += 1
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
    return max_len