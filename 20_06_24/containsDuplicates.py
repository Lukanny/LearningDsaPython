"""
Given an array of integers, write a function that determines whether the array contains any duplicates.
Your function should return true if any element appears at least twice in the array, and it should return false if
every element is distinct.

Example

For a = [1, 2, 3, 1], the output should be
solution(a) = true.

There are two 1s in the given array.

For a = [3, 1], the output should be
solution(a) = false.

The given array contains no duplicates.
"""
import unittest


class Solution(unittest.TestCase):

    example = [1, 2, 3, 1]

    @staticmethod
    def solution(a):
        hashset = set()
        for i in range(0, len(a)):
            if a[i] not in hashset:
                hashset.add(a[i])
            else:
                return True
        return False

    def test_solution(self):
        assert Solution.solution(self.example) is True
