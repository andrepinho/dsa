from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        lens = ''
        for i, s in enumerate(strs):
            lens += str(len(s))

            if i+1 != len(strs):  # only add "," if not last
                lens += ','

        return lens + '#' + ''.join(strs)

    def decode(self, s: str) -> List[str]:
        if len(s) == 1:
            return []

        lensStr = ''

        for n in s:
            if n == '#':
                break
            lensStr += n

        lenStrs = lensStr.split(',')

        lens = list(map(int, lenStrs))

        cleanStr = s[len(lensStr)+1:len(s)]

        res = []
        for wlen in lens:
            res.append(cleanStr[0:wlen])

            cleanStr = cleanStr[wlen:len(cleanStr)]

        return res

    def encode_and_decode(self, strs: List[str]) -> List[str]:
        """Wrapper function that encodes then decodes the input."""
        encoded = self.encode(strs)
        return self.decode(encoded)
