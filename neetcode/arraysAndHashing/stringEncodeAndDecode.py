from typing import List

from neetcode.testRunner import TestRunner


class Solution:

    def encode(self, strs: List[str]) -> str:
        lens = ''
        for i, s in enumerate(strs):
            lens += str(len(s))

            if i+1 != len(strs):  # only add "," if not last
                lens += ','

        return lens + '#' + ''.join(strs)

    def decode(self, s: str) -> List[str]:
        if len(s) == 1:
            return []

        lensStr = ''

        for n in s:
            if n == '#':
                break
            lensStr += n

        lenStrs = lensStr.split(',')

        lens = list(map(int, lenStrs))

        cleanStr = s[len(lensStr)+1:len(s)]

        res = []
        for wlen in lens:
            res.append(cleanStr[0:wlen])

            cleanStr = cleanStr[wlen:len(cleanStr)]

        return res

    def encode_and_decode(self, strs: List[str]) -> List[str]:
        """Wrapper function that encodes then decodes the input."""
        encoded = self.encode(strs)
        return self.decode(encoded)


if __name__ == "__main__":
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

    TestRunner.run_tests(Solution().encode_and_decode, test_cases)
