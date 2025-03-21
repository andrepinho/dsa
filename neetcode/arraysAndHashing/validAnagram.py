from neetcode.testRunner import TestRunner

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

if __name__ == "__main__":
    test_cases = [
        {'inputs': {'s': "racecar", 't': "carrace"}, 'expected': True},
        {'inputs': {'s': "jar", 't': "jam"}, 'expected': False},
    ]

    TestRunner.run_tests(Solution().isAnagram, test_cases)