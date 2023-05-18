def MVB_DP(items, capacity):
    # Dynamic programming implementation of the maximum value bag problem
    n = len(items)
    m = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(capacity + 1):
            if items[i - 1][1] > j:
                m[i][j] = m[i - 1][j]
            else:
                m[i][j] = max(m[i - 1][j], m[i - 1][j - items[i - 1][1]] + items[i - 1][0])
    return m[n][capacity]
