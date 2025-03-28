from .bucket_sort import Solution as bucket_sort
from test_runner import TestRunner

# https://neetcode.io/problems/top-k-elements-in-list
if __name__ == "__main__":
    solutions = [
        bucket_sort(),
    ]

    test_cases = [
        {'inputs': {'nums': [1, 2, 2, 3, 3, 3], 'k': 2}, 'expected': [3, 2]},
        {'inputs': {'nums': [7, 7], 'k': 1}, 'expected': [7]},
        {
            'inputs': {'nums': [99, 1, 99, 100, 99, 100, 99, 1, 1, 1], 'k': 2},
            'expected': [99, 1]
        },
    ]

    print('Running tests...\n')

    for i, solution in enumerate(solutions):
        print(
            f"Testing solution {i + 1}/{len(solutions)}", '\n')
        TestRunner.run_tests(solution.topKFrequent, test_cases)
        print('\n')
