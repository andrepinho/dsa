from .set_and_ignore_non_starting import Solution as set_and_ignore_non_starting
from test_runner import TestRunner

# https://neetcode.io/problems/longest-consecutive-sequence

if __name__ == "__main__":
    solutions = [
        set_and_ignore_non_starting(),
    ]

    test_cases = [
        {'inputs': {'nums': [1, 2, 3, 5, 4]}, 'expected': 5},
        {'inputs': {'nums': [2, 20, 4, 10, 3, 4, 5]}, 'expected': 4},
        {'inputs': {'nums': []}, 'expected': 0},
        {'inputs': {'nums': [2, 2]}, 'expected': 1},
    ]

    print('Running tests...\n')

    for i, solution in enumerate(solutions):
        print(
            f"Testing solution {i + 1}/{len(solutions)}", '\n')
        TestRunner.run_tests(solution.longestConsecutive, test_cases)
        print('\n')
