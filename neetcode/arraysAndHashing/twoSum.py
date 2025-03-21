from neetcode.testRunner import TestRunner
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_by_n = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in index_by_n:
                return [index_by_n[diff], i]
            index_by_n[n] = i

test_cases = [
    {'i': [[3,4,5,6], 7], 'o': [0,1]},
    {'i': [[4,5,6], 10], 'o': [0,2]},
    {'i': [[5,5], 10], 'o': [0,1]},
]

if __name__ == "__main__":
    test_cases = [
        {'inputs': {'nums': [3, 4, 5, 6], 'target': 7}, 'expected': [0, 1]},
        {'inputs': {'nums': [4, 5, 6], 'target': 10}, 'expected': [0, 2]},
        {'inputs': {'nums': [5, 5], 'target': 10}, 'expected': [0, 1]},
    ]

    TestRunner.run_tests(Solution().twoSum, test_cases)