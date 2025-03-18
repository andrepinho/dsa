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

test_cases = [
    {'i': [1, 2, 3, 3], 'o': True},
    {'i': [1, 2, 3, 1], 'o': True},
    {'i': [1, 2, 3, 4], 'o': False},
    {'i': [10, 0, 1], 'o': False}
]

for case in test_cases:
    actual_output = Solution().hasDuplicate(nums=case['i'])
    expected_output = case['o']

    if actual_output == expected_output:
        print(f"Case {case['i']} passed.")
    else:
        print(f"Case {case['i']} failed. Expected {expected_output} but Got {actual_output}")