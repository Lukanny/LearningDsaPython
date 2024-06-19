"""
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character
in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
solution(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
solution(s) = '_'.

There are no characters in this string that do not repeat.
"""
import unittest


class Solution(unittest.TestCase):

    example_1 = 'abacabad'

    @staticmethod
    def solution(s):
        hashmap = {}
        for i in range(0, len(s)):
            if not hashmap.get(s[i]):
                hashmap[s[i]] = 1
            else:
                hashmap[s[i]] += 1
        for k, v in hashmap.items():
            if v == 1:
                return k
        return '_'

    def test_solution(self):
        assert Solution.solution(self.example_1) == 'c'
