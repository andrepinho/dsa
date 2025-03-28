from neetcode.testRunner import TestRunner

from typing import List


class Solution:
    # https://neetcode.io/problems/longest-consecutive-sequence

    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSeq = 0

        for n in numSet:
            if (n-1) not in numSet:
                currentSeq = 1

                while (n + currentSeq) in numSet:
                    currentSeq += 1

                longestSeq = max(longestSeq, currentSeq)

        return longestSeq


if __name__ == "__main__":
    test_cases = [
        {'inputs': {'nums': [1, 2, 3, 5, 4]}, 'expected': 5},
        {'inputs': {'nums': [2, 20, 4, 10, 3, 4, 5]}, 'expected': 4},
        {'inputs': {'nums': []}, 'expected': 0},
        {'inputs': {'nums': [2, 2]}, 'expected': 1},
    ]

    TestRunner.run_tests(Solution().longestConsecutive, test_cases)
