from src.reader import Instance
from src.solver import branch_and_bound, bfs_bnb
import time
import argparse

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Read an instance from a file.')
    parser.add_argument('--file', type=str, help='The filename of the instance to read.')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output.')
    # bfs or dfs type - default is dfs
    parser.add_argument('--type', type=str, default='dfs', choices=['dfs', 'bfs'], help='Type of search: dfs or bfs.')
    args = parser.parse_args()

    # Create an instance of the Instance class
    instance = Instance(args.file)

    # Get the instance data
    n, m, obj_coeffs, constraints = instance.get_instance()

    # Print the instance data
    if args.verbose:
        print("Instance data:")
        # objective function
        print(f"Max {' + '.join([f'{obj_coeffs[i]}x{i+1}' for i in range(n)])}")
        print("Subject to:")
        for i in range(m):
            a, b = constraints[i]
            print(f"{' + '.join([f'{a[j]}x{j+1}' for j in range(n)])} <= {b}")
        
    # Solve the problem using branch and bound
    start_time = time.time()
    if args.type == 'bsf':
        best_solution, best_obj = bfs_bnb(instance, verbose=args.verbose)
    else:
        best_solution, best_obj = branch_and_bound(instance, verbose=args.verbose)
    end_time = time.time()
    if args.verbose:
        print(f"\n[DEBUG] Time taken: {end_time - start_time:.2f} seconds")
    if best_solution is not None:
        print(f"Best solution: {best_solution}")
        print(f"Objective value: {best_obj}")
    else:
        print("No feasible solution found.")

if __name__ == "__main__":
    main()