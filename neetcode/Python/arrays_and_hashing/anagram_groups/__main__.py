from .hash_by_sorted import Solution as hash_by_sorted
from test_runner import TestRunner

# https://neetcode.io/problems/anagram-groups

if __name__ == "__main__":
    solutions = [
        hash_by_sorted(),
    ]

    test_cases = [
        {
            'inputs': {'strs': ["act", "pots", "tops", "cat", "stop", "hat"]},
            'expected': [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]},
        {
            'inputs': {'strs': ["x"]},
            'expected': [["x"]]
        },
        {
            'inputs': {'strs': [""]},
            'expected': [[""]]
        },
    ]

    print('Running tests...\n')

    for i, solution in enumerate(solutions):
        print(
            f"Testing solution {i + 1}/{len(solutions)}", '\n')
        TestRunner.run_tests(solution.groupAnagrams, test_cases)
        print('\n')
