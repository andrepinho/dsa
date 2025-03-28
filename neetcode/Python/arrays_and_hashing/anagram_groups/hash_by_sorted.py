from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sBySortedS = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))

            sBySortedS[sortedS].append(s)

        return list(sBySortedS.values())
