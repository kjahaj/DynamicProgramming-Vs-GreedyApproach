# Knapsack Problem: Greedy vs Dynamic Programming

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Welcome to the Knapsack Problem repository! This directory focuses on solving the Knapsack Problem using both greedy and dynamic programming algorithms. Additionally, it provides a comprehensive statistical analysis of the algorithms' performance, helping you understand the trade-offs and effectiveness of each approach.

## Table of Contents
- [Introduction](#introduction)
- [Directory Structure](#directory-structure)
- [Getting Started](#getting-started)
- [Greedy Algorithm](#greedy-algorithm)
- [Dynamic Programming](#dynamic-programming)
- [Statistical Analysis](#statistical-analysis)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Knapsack Problem is a classic optimization problem where given a set of items with weights and values, the goal is to determine the most valuable combination of items that can be packed into a knapsack with a weight capacity constraint.

This directory provides implementations of the Knapsack Problem using both greedy and dynamic programming algorithms. By comparing these approaches and analyzing their statistical performance, you can gain insights into their strengths and weaknesses.

## Directory Structure
The directory structure is as follows:

- `greedy_algorithm/`: This directory contains the implementation of the greedy algorithm for the Knapsack Problem. It provides a heuristic-based approach to select items based on their value-to-weight ratio.

- `dynamic_programming/`: This directory contains the implementation of the dynamic programming algorithm for the Knapsack Problem. It uses a tabulation technique to solve the problem optimally.

- `statistical_analysis/`: This directory includes the full program implementations of both the greedy and dynamic programming algorithms, along with the corresponding statistical analysis. It provides metrics such as execution time, memory usage, and solution quality.

## Getting Started
To get started with this project, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/your-repo.git`
2. Navigate to the cloned directory: `cd your-repo/knapsack_problem`
3. Explore the different directories mentioned above to find the implementations and analysis.

## Greedy Algorithm
The `greedy_algorithm/` directory contains an implementation of the greedy algorithm for the Knapsack Problem. This approach selects items based on their value-to-weight ratio, aiming to maximize the total value while considering the weight constraint. Detailed instructions on running the algorithm are available in the `greedy_algorithm/README.md` file.

## Dynamic Programming
The `dynamic_programming/` directory contains an implementation of the dynamic programming algorithm for the Knapsack Problem. This approach solves the problem optimally by building a table that represents the subproblems and their optimal solutions. Detailed instructions on running the algorithm are available in the `dynamic_programming/README.md` file.

## Statistical Analysis
The `statistical_analysis/` directory provides the full program implementations of both the greedy and dynamic programming algorithms for the Knapsack Problem. It also includes a comprehensive statistical analysis comparing the algorithms' performance. The analysis includes metrics such as execution time, memory usage, and solution quality. Refer to the `statistical_analysis/README.md` file for instructions on running the programs and interpreting the results.

## Contributing
Contributions are welcome and encouraged! If you'd like to contribute to this project, please review the [contributing guidelines](contributing.md) for instructions on how to get started. You can contribute by improving the implementations, adding new algorithms, or enhancing the statistical analysis.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

I hope this directory provides you with valuable insights into solving the Knapsack Problem using both greedy and dynamic programming algorithms. By studying the implementations and the statistical analysis, you can make informed decisions on which approach to choose based on the problem requirements and constraints. Happy optimizing!
