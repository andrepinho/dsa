from .encode_by_lenght import Solution as encode_by_lenght
from test_runner import TestRunner

# https://neetcode.io/problems/string-encode-and-decode
if __name__ == "__main__":
    solutions = [
        encode_by_lenght(),
    ]

    test_cases = [
        {'inputs': {'strs': []}, 'expected': []},  # Empty list

        {'inputs': {'strs': ["", "", ""]}, 'expected': [
            "", "", ""]},  # Multiple empty strings

        {'inputs': {'strs': [""]}, 'expected': [""]},  # Single empty string

        {'inputs': {'strs': ["a,b", "c,d"]}, 'expected': [
            "a,b", "c,d"]},  # Strings with commas

        {'inputs': {'strs': ["hello#world", "test#"]}, 'expected': [
            "hello#world", "test#"]},  # Strings with #

        {'inputs': {'strs': ["a" * 1000, "b" * 5000]},
            'expected': ["a" * 1000, "b" * 5000]},  # Large strings

        {'inputs': {'strs': ["a", "", "abc", ""]}, 'expected': [
            "a", "", "abc", ""]},  # Mixed lengths

        {'inputs': {'strs': ["こんにちは", "世界"]},
            'expected': ["こんにちは", "世界"]},  # Unicode

        {'inputs': {'strs': ["a", "b", "c"]}, 'expected': [
            "a", "b", "c"]},  # Single-char strings

        {'inputs': {'strs': ["abc", "abc", "abc"]}, 'expected': [
            "abc", "abc", "abc"]},  # Repeated strings

    ]

    print('Running tests...\n')

    for i, solution in enumerate(solutions):
        print(
            f"Testing solution {i + 1}/{len(solutions)}", '\n')
        TestRunner.run_tests(solution.encode_and_decode, test_cases)
        print('\n')
