from collections import Counter

def flames_result(name1, name2):
    # Process names and calculate remaining letters count
    name1 = name1.upper().replace(' ', '')
    name2 = name2.upper().replace(' ', '')
    
    cnt1 = Counter(name1)
    cnt2 = Counter(name2)
    
    common = cnt1 & cnt2
    cnt1.subtract(common)
    cnt2.subtract(common)
    
    n = sum(cnt1.values()) + sum(cnt2.values())
    
    if n == 0:
        return 'FRIENDS'  # Edge case when all letters are cancelled
    
    