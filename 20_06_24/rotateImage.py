"""
Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an
interview.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

solution(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
"""
import unittest


class Solution(unittest.TestCase):

    example = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    @staticmethod
    def solution(a):
        n = len(a)
        for i in range(n):
            for j in range(i, n):
                a[i][j], a[j][i] = a[j][i], a[i][j]
        for i in range(n):
            a[i].reverse()
        return a

    def test_solution(self):
        assert Solution.solution(self.example) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
