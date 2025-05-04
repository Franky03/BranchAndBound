**Branch and Bound Solver**

This repository contains a Python implementation of a Branch and Bound solver for solving 0-1 Integer Linear Programming (ILP) problems, with options to use Depth-First Search (DFS) or Breadth-First Search (BFS) strategies.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Command-Line Arguments](#command-line-arguments)
5. [Instance File Format](#instance-file-format)
6. [Examples](#examples)

---

## Prerequisites
- Standard libraries: `argparse`, `time`
- Local modules:
  - `Instance` class for reading input files and holding problem data
  - `branch_and_bound` function for DFS-based search
  - `bfs_bnb` function for BFS-based search

## Installation
1. Clone this repository:
```bash
git clone https://github.com/Franky03/BranchAndBound
cd BranchAndBound
```
2. (Optional) Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

## Usage
Run the solver via the main script. At minimum, provide an instance file:
```bash
python main.py --file path/to/instance.txt
``` 

Additional flags allow you to customize the search strategy and verbosity.

## Command-Line Arguments

| Argument    | Type   | Default | Description                                                                 |
|-------------|--------|---------|-----------------------------------------------------------------------------|
| `--file`    | `str`  | —       | Path to the input instance file (required)                                  |
| `--verbose` | `flag` | `False` | Enable detailed logging and debug output                                    |
| `--type`    | `str`  | `dfs`   | Search strategy: `dfs` for Depth‑First (default), or `bfs` for Breadth‑First |

## Instance File Format

The input file should define an ILP of the form:

```text
# Number of variables n and constraints m
n m

# Objective function coefficients (space-separated)
c1 c2 c3 ... cn

# Constraint matrix and RHS values
# Each of the next m lines: a1 a2 ... an b
# representing a1*x1 + a2*x2 + ... + an*xn <= b

a11 a12 ... a1n b1
...
am1 am2 ... amn bm
```

## Examples

1. **Default DFS search**:

```bash
  python main.py --file instances/01
```

2. **BFS search with verbose output**:
```bash
  python main.py --file instances/01 --type bfs --verbose
```

**Expected output** (with --verbose):
```text
Instance data:
Max 2.0x1 + 10.0x2 + 8.0x3 + 7.0x4 + 10.0x5 + 10.0x6 + 6.0x7
Subject to:
5.0x1 + 7.0x2 + 8.0x3 + 1.0x4 + 7.0x5 + 5.0x6 + 6.0x7 <= 20.0
1.0x1 + 6.0x2 + 4.0x3 + 9.0x4 + 10.0x5 + 6.0x6 + 10.0x7 <= 30.0
4.0x1 + 4.0x2 + 4.0x3 + 1.0x4 + 5.0x5 + 5.0x6 + 10.0x7 <= 40.0
3.0x1 + 10.0x2 + 8.0x3 + 1.0x4 + 3.0x5 + 3.0x6 + 8.0x7 <= 30.0
10.0x1 + 8.0x2 + 9.0x3 + 9.0x4 + 7.0x5 + 6.0x6 + 10.0x7 <= 20.0
6.0x1 + 6.0x2 + 3.0x3 + 6.0x4 + 3.0x5 + 7.0x6 + 2.0x7 <= 80.0
7.0x1 + 10.0x2 + 7.0x3 + 8.0x4 + 7.0x5 + 8.0x6 + 7.0x7 <= 100.0
9.0x1 + 8.0x2 + 1.0x3 + 1.0x4 + 8.0x5 + 10.0x6 + 2.0x7 <= 90.0
1.0x1 + 5.0x2 + 3.0x3 + 10.0x4 + 2.0x5 + 4.0x6 + 9.0x7 <= 70.0
9.0x1 + 6.0x2 + 1.0x3 + 4.0x4 + 7.0x5 + 5.0x6 + 10.0x7 <= 60.0
5.0x1 + 7.0x2 + 4.0x3 + 4.0x4 + 3.0x5 + 4.0x6 + 10.0x7 <= 40.0

[DEBUG] Time taken: 0.19 seconds
Best solution: [0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0]
Objective value: 20.0
```