from .loop_check_in_set import Solution as loop_check_in_set
from .hash_set_length import Solution as hash_set_length
from test_runner import TestRunner

# https://neetcode.io/problems/duplicate-integer


if __name__ == "__main__":
    solutions = [
        hash_set_length(),
        loop_check_in_set()
    ]

    test_cases = [
        {'inputs': {'nums': [1, 2, 3, 3]}, 'expected': True},
        {'inputs': {'nums': [1, 2, 3, 1]}, 'expected': True},
        {'inputs': {'nums': [1, 2, 3, 4]}, 'expected': False},
        {'inputs': {'nums': [10, 0, 1]}, 'expected': False}
    ]

    print('Running tests...\n')

    for i, solution in enumerate(solutions):
        print(
            f"Testing solution {i + 1}/{len(solutions)}", '\n')
        TestRunner.run_tests(solution.hasDuplicate, test_cases)
        print('\n')
