def MSM_Greedy(E):
    n, H = len(E), len(E[0])-1
    A = [[0 for _ in range(H+1)] for _ in range(n+1)]
    M = [[0 for _ in range(H+1)] for _ in range(n+1)]
    # ground cases
    for h in range(H+1):
        M[0][h] = 0
    # recurrence cases
    for k in range(1, n+1):
        for h in range(H+1):
            max_e = -1
            max_hprime = 0
            for hprime in range(h+1):
                if E[k-1][hprime] > max_e:
                    max_e = E[k-1][hprime]
                    max_hprime = hprime
            M[k][h] = max_e + M[k-1][h-max_hprime]
            A[k][h] = max_hprime
    return max(max(M, key=lambda row: max(row)))
