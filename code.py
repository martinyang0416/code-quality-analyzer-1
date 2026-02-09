def mask_pii(S):
    if '@' in S:
        parts = S.split('@')
        local_part = parts[0].lower()
        domain_part = parts[1].split('.')
        masked_name = local_part[0] + '*****' + local_part[-1]
        masked_domain = '.'.join([part.lower() for part in domain_part])
        return f"{masked_name}@{masked_domain}"
    else:
        digits = [c for c in S if c.isdigit()]
        n = len(digits)
        local = digits[-10:]
        country = digits[:-10] if n > 10 else []
        masked