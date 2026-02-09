def subtract_one(s):
    s_list = list(s)
    i = len(s_list) - 1
    while i >= 0 and s_list[i] == '0':
        s_list[i] = '9'
        i -= 1
    if i < 0:
        return '0'
    s_list[i] = str(int(s_list[i]) - 1)
    new_s = ''.join(s_list).lstrip('0')
    return new_s if new_s else '0'

def compute(s, m):
    if m == 0:
        return 0
    X = list(map(int, s))
    n = len(X)
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dp(pos, mod, prev_digit, last_dir, tight,