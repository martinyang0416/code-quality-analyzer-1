def strongPasswordChecker(s):
    n = len(s)
    missing_types = 3
    if any(c.islower() for c in s):
        missing_types -= 1
    if any(c.isupper() for c in s):
        missing_types -= 1
    if any(c.isdigit() for c in s):
        missing_types -= 1

    # Compute runs of characters
    runs = []
    if n > 0:
        current = s[0]
        count = 1
        for c in s[1:]:
            if c == current:
                count += 1
            else:
                runs.append(count)
        