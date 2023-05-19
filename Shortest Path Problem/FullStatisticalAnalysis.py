import sys
import numpy as np
import matplotlib.pyplot as plt

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
    
    return M[L-1][C-1]

def minCost(M, i, j, L, C):
    infinity = sys.maxsize
    if inGrid(i, j, L, C):
        return M[i][j]
    else:
        return infinity

def inGrid(i, j, L, C):
    return 0 <= i < L and 0 <= j < C


def MCP_G(G):
    L = len(G)
    C = len(G[0])
    total_sum = G[0][0]
    i = 0
    j = 0

    while not (i == L - 1 and j == C - 1):
        if i == L - 1:  # Reached the bottom edge, can only move horizontally
            j += 1
        elif j == C - 1:  # Reached the right edge, can only move vertically
            i += 1
        else:
            cost_e = G[i][j + 1]  # Cost of moving east
            cost_ne = G[i + 1][j + 1]  # Cost of moving northeast
            cost_n = G[i + 1][j]  # Cost of moving north

            # Choose the minimum cost movement
            if cost_e <= cost_ne and cost_e <= cost_n:
                j += 1  # Move east
            elif cost_ne <= cost_e and cost_ne <= cost_n:
                i += 1  # Move northeast
                j += 1
            else:
                i += 1  # Move north

        total_sum += G[i][j]

    return total_sum



# Parameters
num_matrices = 3000  # Number of random matrices
matrix_size = (8, 8)  # Size of each matrix

# Create the list
instances = []

# Fill the list with random matrices
for _ in range(num_matrices):
    matrix = np.random.randint(low=1, high=30, size=matrix_size)
    instances.append(matrix)

relative_distances = []

for z in range(num_matrices):
    r = []
    m = MCP_DP(instances[z])
    g = MCP_G(instances[z])
    if m == 0:
        r = 0
    else:
        r = (g-m) / g
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

plt.hist(relative_distances, bins=60)
plt.title('Histogram of Relative Distances')
plt.xlabel('Relative Distance')
plt.ylabel('Frequency')
plt.show()
