from .hash_index_by_diff import Solution as hash_index_by_diff
from test_runner import TestRunner

# https://neetcode.io/problems/two-integer-sum

if __name__ == "__main__":
    solutions = [
        hash_index_by_diff(),
    ]

    test_cases = [
        {'inputs': {'nums': [3, 4, 5, 6], 'target': 7}, 'expected': [0, 1]},
        {'inputs': {'nums': [4, 5, 6], 'target': 10}, 'expected': [0, 2]},
        {'inputs': {'nums': [5, 5], 'target': 10}, 'expected': [0, 1]},
    ]

    print('Running tests...\n')

    for i, solution in enumerate(solutions):
        print(
            f"Testing solution {i + 1}/{len(solutions)}", '\n')
        TestRunner.run_tests(solution.twoSum, test_cases)
        print('\n')
