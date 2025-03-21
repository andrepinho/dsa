from neetcode.testRunner import TestRunner

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sBySortedS = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))

            sBySortedS[sortedS].append(s)

        return list(sBySortedS.values())


if __name__ == "__main__":
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

    TestRunner.run_tests(Solution().groupAnagrams, test_cases)
