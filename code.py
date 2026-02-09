MOD = 10**9 + 7

def compute_ways(start, end, steps, adj, N):
    dp_prev = [0] * (N + 1)
    dp_prev[start] = 1
    for _ in range(steps):
        dp_next = [0] * (N + 1)
        for u in range(1, N + 1):
            if dp_prev[u] == 0:
                continue
            # Stay
            dp_next[u] = (dp_next[u] + dp_prev[u]) % MOD
            # Move to neighbors
            for v in adj[u]:
                dp_next[v] = (dp_next[v] + dp_prev[u]) % MOD
        dp_prev = dp_next
    return dp