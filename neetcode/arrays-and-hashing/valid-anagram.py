from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count_by_letter = {}
        t_count_by_letter = {}

        for letter in s:
            s_count_by_letter[letter] = s_count_by_letter.get(letter, 0) + 1
            
        for letter in t:
            t_count_by_letter[letter] = t_count_by_letter.get(letter, 0) + 1

        return s_count_by_letter == t_count_by_letter

test_cases = [
    {'i': ["racecar", "carrace"], 'o': True},
    {'i': ["jar", "jam"], 'o': False},
]

for case in test_cases:
    actual_output = Solution().isAnagram(s=case['i'][0], t=case['i'][1])
    expected_output = case['o']

    if actual_output == expected_output:
        print(f"Case {case['i']} passed.")
    else:
        print(f"Case {case['i']} failed. Expected {expected_output} but Got {actual_output}")