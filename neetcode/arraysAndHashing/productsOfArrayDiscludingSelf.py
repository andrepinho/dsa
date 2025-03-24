from neetcode.testRunner import TestRunner
from typing import List


class Solution:
    # https://neetcode.io/problems/products-of-array-discluding-self

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res


if __name__ == "__main__":
    test_cases = [
        {'inputs': {'nums': [1, 2, 4, 6]}, 'expected': [48, 24, 12, 8]},
        {'inputs': {'nums': [-1, 0, 1, 2, 3]}, 'expected': [0, -6, 0, 0, 0]},
    ]

    TestRunner.run_tests(Solution().productExceptSelf, test_cases)
