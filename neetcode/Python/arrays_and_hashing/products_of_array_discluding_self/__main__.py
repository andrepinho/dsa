from .prefix_fwd_suffix_bkd import Solution as prefix_fwd_suffix_bkd
from test_runner import TestRunner

# https://neetcode.io/problems/products-of-array-discluding-self
if __name__ == "__main__":
    solutions = [
        prefix_fwd_suffix_bkd(),
    ]

    test_cases = [
        {'inputs': {'nums': [1, 2, 4, 6]}, 'expected': [48, 24, 12, 8]},
        {'inputs': {'nums': [-1, 0, 1, 2, 3]}, 'expected': [0, -6, 0, 0, 0]},
    ]

    print('Running tests...\n')

    for i, solution in enumerate(solutions):
        print(
            f"Testing solution {i + 1}/{len(solutions)}", '\n')
        TestRunner.run_tests(solution.productExceptSelf, test_cases)
        print('\n')
