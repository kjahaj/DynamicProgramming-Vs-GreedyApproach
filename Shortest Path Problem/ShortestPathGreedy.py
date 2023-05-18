def MCP_G(G):
    L = len(G)
    C = len(G[0])
    sum = 0
    i = 0
    j = 0
    
    while i != L-1 or j != C-1:
        if i == L-1:  # Reached the bottom edge, can only move horizontally
            j += 1
        elif j == C-1:  # Reached the right edge, can only move vertically
            i += 1
        else:
            cost_e = G[i][j+1]  # Cost of moving east
            cost_ne = G[i+1][j+1]  # Cost of moving northeast
            cost_n = G[i+1][j]  # Cost of moving north
            
            # Choose the minimum cost movement
            if cost_e <= cost_ne and cost_e <= cost_n:
                j += 1  # Move east
            elif cost_ne <= cost_e and cost_ne <= cost_n:
                i += 1  # Move northeast
                j += 1
            else:
                i += 1  # Move north
        sum += G[i][j]
    return sum
