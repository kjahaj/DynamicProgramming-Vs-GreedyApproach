def DoubleMVB_G(items, capacity1, capacity2):
    items_sorted = sorted(items, key=lambda x: x[2] / (x[0] + x[1]), reverse=True)
    total_value = 0
    remaining_capacity1 = capacity1
    remaining_capacity2 = capacity2

    for item in items_sorted:
        weight1, weight2, value = item

        if remaining_capacity1 >= weight1 and remaining_capacity2 >= weight2:
            total_value += value
            remaining_capacity1 -= weight1
            remaining_capacity2 -= weight2

    return total_value
