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

for case in test_cases:
    actual_output = Solution().twoSum(nums=case['i'][0], target=case['i'][1])
    expected_output = case['o']

    if actual_output == expected_output:
        print(f"Case {case['i']} passed.")
    else:
        print(f"Case {case['i']} failed. Expected {expected_output} but Got {actual_output}")