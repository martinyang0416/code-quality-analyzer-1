def maxLength(arr):
    # Preprocess to filter out strings with duplicate characters
    unique = []
    for s in arr:
        if len(set(s)) == len(s):
            unique.append(s)
    
    # Generate masks and lengths
    masks = []
    for s in unique:
        mask = 0
        for c in s:
            mask |= 1 << (ord(c) - ord('a'))
        masks.append( (mask, len(s)) )
    
    # Dynamic programming to find maximum length
    dp = {0: 0}  # mask: max_length
    for mask, length in masks:
  