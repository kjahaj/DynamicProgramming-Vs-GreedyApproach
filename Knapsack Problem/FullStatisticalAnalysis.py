import random
import matplotlib.pyplot as plt

# Define the MVB problem and the DP and GA algorithms
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

# Generate a large number of random instances of the MVB problem
n_instances = 1000 #Nr of instances for the problem
max_n = 200
max_C = 500
instances = []
for i in range(n_instances):
    n = random.randint(1, max_n)
    C = random.randint(1, max_C)
    items = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(n)]
    instances.append((n, C, items))

# Compute the relative distances for each instance using DP and GA
relative_distances = []
for instance in instances:
    n, C, items = instance
    m = MVB_DP(items, C)
    g = MVB_GA(items, C)
    if m == 0:
        r = 0
    else:
        r = (m - g) / m
    relative_distances.append(r)

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

