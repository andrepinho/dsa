from .hash_count_and_compare import Solution as hash_count_and_compare
from test_runner import TestRunner

# https://neetcode.io/problems/is-anagram

if __name__ == "__main__":
    solutions = [
        hash_count_and_compare(),
    ]

    test_cases = [
        {'inputs': {'s': "racecar", 't': "carrace"}, 'expected': True},
        {'inputs': {'s': "jar", 't': "jam"}, 'expected': False},
    ]

    print('Running tests...\n')

    for i, solution in enumerate(solutions):
        print(
            f"Testing solution {i + 1}/{len(solutions)}", '\n')
        TestRunner.run_tests(solution.isAnagram, test_cases)
        print('\n')
