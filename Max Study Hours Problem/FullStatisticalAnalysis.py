import random
import numpy as np
import matplotlib.pyplot as plt


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

n = 25
H = 50
num_instances = 1000

instances = []

for i in range(num_instances):
    E = [[random.randint(0, 10) for _ in range(H+1)] for _ in range(n)]
    dp_solution = MSM_DP(E)
    greedy_solution = MSM_Greedy(E)
    instances.append((E, dp_solution, greedy_solution))

relative_distances = []

for instance in instances:
    m = instance[1]
    g = instance[2]
    if m == 0:
        r = 0
    else:
        r = (m - g) / m
    relative_distances.append(r)

# Compute statistical values
mean = np.mean(relative_distances)
std = np.std(relative_distances)
median = np.median(relative_distances)
max_rd = np.max(relative_distances)
outliers = np.mean(sorted(relative_distances, reverse=True)[:int(len(relative_distances)*0.05)])

print(f'Mean: {mean}')
print(f'Standard Deviation: {std}')
print(f'Median: {median}')
print(f'Maximum Relative Distance: {max_rd}')
print(f'Mean of Outliers: {outliers}')

# Plot the histogram of relative distances
plt.hist(relative_distances, bins=80)
plt.title('Histogram of Relative Distances')
plt.xlabel('Relative Distance')
plt.ylabel('Frequency')
plt.show()
