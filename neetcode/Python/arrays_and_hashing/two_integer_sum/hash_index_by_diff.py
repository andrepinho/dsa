from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_by_n = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in index_by_n:
                return [index_by_n[diff], i]
            index_by_n[n] = i
