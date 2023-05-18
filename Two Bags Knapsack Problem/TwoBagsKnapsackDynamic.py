def DoubleMVB_DP(items, capacity1, capacity2):
    n = len(items)
    dp = [[0] * (capacity2 + 1) for _ in range(capacity1 + 1)]

    for i in range(1, n + 1):
        weight1, weight2, value = items[i - 1]
        for w1 in range(capacity1, weight1 - 1, -1):
            for w2 in range(capacity2, weight2 - 1, -1):
                dp[w1][w2] = max(dp[w1][w2], dp[w1 - weight1][w2 - weight2] + value)

    return dp[capacity1][capacity2]
