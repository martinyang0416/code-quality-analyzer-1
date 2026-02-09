from collections import Counter

def getHint(secret: str, guess: str) -> str:
    bulls = 0
    s_non_bull = []
    g_non_bull = []
    for s, g in zip(secret, guess):
        if s == g:
            bulls += 1
        else:
            s_non_bull.append(s)
            g_non_bull.append(g)
    s_counter = Counter(s_non_bull)
    g_counter = Counter(g_non_bull)
    cows = sum((s_counter & g_counter).values())
    return f"{bulls}A{cows}B"