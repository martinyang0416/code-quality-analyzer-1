s1 = "What are you doing while sending "  # Length 33
s2 = "? Are you busy? Will you send "     # Length 30
f0 = "What are you doing at the end of the world? Are you busy? Will you save us?"  # Length 75

threshold = 60

def compute_L(n):
    return 143 * (2 ** n) - 68

def get_char(n, k):
    if n < 0 or k < 1:
        return '.'
    
    # Check if within length for small n
    if n <= threshold:
        L_n = compute_L(n)
        if k > L_n:
            return '.'
    
    current_n = n
    c