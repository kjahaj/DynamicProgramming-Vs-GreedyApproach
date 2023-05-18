def MVB_GA(items, capacity):
    # Greedy algorithm implementation of the maximum value bag problem
    items = sorted(items, key=lambda x: x[0], reverse=True)
    value = 0
    space = capacity
    for item in items:
        if item[1] <= space:
            value += item[0]
            space -= item[1]
    return value
