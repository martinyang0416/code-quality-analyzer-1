def minMalwareSpread(graph, initial):
    n = len(graph)
    initial_sorted = sorted(initial)
    min_m = float('inf')
    result = -1
    
    for x in initial_sorted:
        # Create modified graph by removing all edges connected to x
        modified = [row.copy() for row in graph]
        for i in range(n):
            modified[x][i] = 0
            modified[i][x] = 0
        modified[x][x] = 1  # Restore self-loop
        
        # New initial list without x
        new_initial = [node fo