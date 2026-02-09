def getPermutation(n, k):
    factorials = [1] * n
    for i in range(1, n):
        factorials[i] = factorials[i-1] * i
    
    k -= 1  # Convert to zero-based index
    numbers = list(map(str, range(1, n+1)))
    result = []
    
    for i in range(n):
        index = k // factorials[n-1 - i]
        result.append(numbers[index])
        numbers.pop(index)
        k %= factorials[n-1 - i]
    
    return ''.join(result)