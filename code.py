def numDecodings(s: str) -> int:
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # empty string has one way to decode
    
    # Handle first character
    dp[1] = 1 if s[0] != '0' else 0
    
    for i in range(2, n + 1):
        # Check single digit
        current_digit = s[i-1]
        if current_digit != '0':
            dp[i] += dp[i-1]
        
        # Check two digits
        two_digit = int(s[i-2] + s[i-1])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i-2]
    
    r