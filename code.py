def hasAllCodes(s: str, k: int) -> bool:
    if len(s) < k:
        return False
    required = 1 << k  # 2^k
    seen = set()
    for i in range(len(s) - k + 1):
        substr = s[i:i+k]
        seen.add(substr)
        if len(seen) == required:
            return True
    return len(seen) == required