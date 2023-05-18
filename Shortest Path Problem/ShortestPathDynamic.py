def MCP_DP(G):
    L = len(G)
    C = len(G[0])
    M = [[0] * C for _ in range(L)]
    A = [[0] * C for _ in range(L)]
    
    M[0][0] = G[0][0]
    
    for i in range(L):
        for j in range(C):
            if i == 0 and j == 0:
                continue
            
            m_e = minCost(M, i, j-1, L, C)
            m_ne = minCost(M, i-1, j-1, L, C)
            m_n = minCost(M, i-1, j, L, C)
            
            if m_e == min(m_e, m_ne, m_n):
                A[i][j] = 0
            elif m_ne == min(m_ne, m_n):
                A[i][j] = 1
            else:
                A[i][j] = 2
            
            M[i][j] = min(m_e, m_ne, m_n) + G[i][j]
    
    return M[i][j]
