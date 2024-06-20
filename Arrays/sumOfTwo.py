"""
You have two integer arrays, a and b, and an integer target value v. Determine whether there is a pair of numbers,
where one number is taken from a and the other from b, that can be added together to get a sum of v.
Return true if such a pair exists, otherwise return false.

Example

For a = [1, 2, 3], b = [10, 20, 30, 40], and v = 42, the output should be
solution(a, b, v) = true.
"""
import unittest


class Solution(unittest.TestCase):

    example = {
        "a": [1, 2, 3],
        "b": [10, 20, 30, 40],
        "v": 42
    }

    @staticmethod
    def solution(a, b, v):
        hashmap = {}
        for i in range(0, len(a)):
            needed_value = v - a[i]
            hashmap[needed_value] = a[i]
        for i in range(0, len(b)):
            if b[i] in hashmap:
                return True
        return False

    def test_solution(self):
        assert Solution.solution(self.example["a"], self.example["b"], self.example["v"]) is True
