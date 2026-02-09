f0 = "What are you doing at the end of the world? Are you busy? Will you save us?"
s1_str = "What are you doing while sending "  # Length 33
s2_str = "? Are you busy? Will you send "    # Length 30
s3_char = '?'

def get_char(n, k):
    if n == 0:
        if k > len(f0):
            return '.'
        else:
            return f0[k-1]
    # Check if L_n <k
    if n < 60:
        L_n = 135 * (2 ** n) - 64
        if k > L_n:
            return '.'
    current_level = n
    current_k = k
    while 