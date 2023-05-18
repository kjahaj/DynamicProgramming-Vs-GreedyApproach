import random
import matplotlib.pyplot as plt

def generate_items(n, max_weight, max_value):
    items = []
    for _ in range(n):
        weight1 = random.randint(1, max_weight)
        weight2 = random.randint(1, max_weight)
        value = random.randint(1, max_value)
        items.append((weight1, weight2, value))
    return items

def DoubleMVB_DP(items, capacity1, capacity2):
    n = len(items)
    dp = [[0] * (capacity2 + 1) for _ in range(capacity1 + 1)]

    for i in range(1, n + 1):
        weight1, weight2, value = items[i - 1]
        for w1 in range(capacity1, weight1 - 1, -1):
            for w2 in range(capacity2, weight2 - 1, -1):
                dp[w1][w2] = max(dp[w1][w2], dp[w1 - weight1][w2 - weight2] + value)

    return dp[capacity1][capacity2]


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

num_items = 100
max_weight = 10
max_value = 20
capacity1 = 200
capacity2 = 300

instances = []

# Generate a large number of random instances of the MVB problem
n_instances = 30 #Nr of instances for the problem
instances = []
for i in range(n_instances):
    cap1 = random.randint(1, capacity1)
    cap2 = random.randint(1, capacity2)
    items = generate_items(num_items,max_weight,max_value)
    instances.append((cap1,cap2,items))

relative_distances = []
for instance in instances:
    cap1,cap2,items = instance
    m = DoubleMVB_DP(items, cap1, cap2)
    g = DoubleMVB_G(items, cap1, cap2)
    if m == 0:
        r = 0
    else:
        r = (m - g) / m
    relative_distances.append(r)
    print(r)

mean = sum(relative_distances) / len(relative_distances)
std_dev = (sum((x - mean)**2 for x in relative_distances) / len(relative_distances))**0.5 
median = sorted(relative_distances)[len(relative_distances) // 2]
max_rel_distance = max(relative_distances)

# Compute the mean value of the "outliers" (5% highest relative distances)
n_outliers = int(len(relative_distances) * 0.05)
outliers = sorted(relative_distances)[-n_outliers:]
outlier_mean = sum(outliers) / n_outliers

# Print the results
print(f"Mean: {mean:.3f}")
print(f"Standard deviation: {std_dev:.3f}")
print(f"Median: {median:.3f}")
print(f"Maximum relative distance: {max_rel_distance:.3f}")
print(f"Mean value of outliers: {outlier_mean:.3f}")

plt.hist(relative_distances, bins=80)
plt.xlabel('Relative distance')
plt.ylabel('Frequency')
plt.show()
