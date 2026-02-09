class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        current_num = 0
        sign = 1  # 1 for positive, -1 for negative

        for c in s:
            if c == ' ':
                continue
            if c.isdigit():
                current_num = current_num * 10 + int(c)
            else:
                # Add the current number to the result with the current sign
                result += sign * current_num
                current_num = 0
   