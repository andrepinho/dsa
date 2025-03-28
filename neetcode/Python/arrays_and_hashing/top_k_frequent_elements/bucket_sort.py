from typing import List


class Solution:
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
