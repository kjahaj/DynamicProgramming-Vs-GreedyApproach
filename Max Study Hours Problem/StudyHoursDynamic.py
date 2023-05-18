def MSM_DP(E):
    n, H = len(E), len(E[0])-1
    M = [[0 for _ in range(H+1)] for _ in range(n+1)]
    A = [[0 for _ in range(H+1)] for _ in range(n+1)]
    # ground cases
    for h in range(H+1):  
        M[0][h] = 0
    # recurrence cases
    for k in range(1, n+1):
        for h in range(H+1):
            # compute m(k,h) = max{ e(k-1,h’) + m(k-1,h-h’)  } over h’, 0 ≤ h’ ≤ h.
            mkh = float('-inf') # - infinity
            akh = -1 # arg mkh (any value would fit)
            for hprime in range(h+1):
                mkh_hprime = E[k-1][hprime] + M[k-1][h-hprime] # e(k-1,h’) + m(k-1,h-h’)
                if mkh_hprime > mkh:
                    mkh = mkh_hprime
                    akh = hprime
            M[k][h] = mkh
            A[k][h] = akh
    return max(max(M, key=lambda row: max(row)))
