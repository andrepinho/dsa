from neetcode.testRunner import TestRunner
from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        unique_nums = {}
        for num in nums:
            unique_nums[num] = True

        if len(unique_nums) == len(nums):
            return False
        else:
            return True


if __name__ == "__main__":
    test_cases = [
        {'inputs': {'nums': [1, 2, 3, 3]}, 'expected': True},
        {'inputs': {'nums': [1, 2, 3, 1]}, 'expected': True},
        {'inputs': {'nums': [1, 2, 3, 4]}, 'expected': False},
        {'inputs': {'nums': [10, 0, 1]}, 'expected': False}
    ]

    TestRunner.run_tests(Solution().hasDuplicate, test_cases)
