from neetcode.testRunner import TestRunner
from typing import List


class Solution:
    # https://neetcode.io/problems/top-k-elements-in-list

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countByNum = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            countByNum[num] = countByNum.get(num, 0) + 1

        for num, count in countByNum.items():
            freq[count].append(num)

        res = []

        for i in range(
            len(freq) - 1,  # start on the last element of freq
            0,  # stop just before the first
            -1  # counting backwards by 1
        ):
            for num in freq[i]:
                res.append(num)

            if len(res) == k:
                return res


if __name__ == "__main__":
    test_cases = [
        {'inputs': {'nums': [1, 2, 2, 3, 3, 3], 'k': 2}, 'expected': [3, 2]},
        {'inputs': {'nums': [7, 7], 'k': 1}, 'expected': [7]},
        {
            'inputs': {'nums': [99, 1, 99, 100, 99, 100, 99, 1, 1, 1], 'k': 2},
            'expected': [99, 1]
        },
    ]

    TestRunner.run_tests(Solution().topKFrequent, test_cases)
