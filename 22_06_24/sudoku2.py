"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column,
each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9
one time.

Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to
the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

Example

For

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
the output should be
solution(grid) = true;

For

grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
the output should be
solution(grid) = false.

The given grid is not correct because there are two 1s in the second column. Each column, each row,
and each 3 × 3 subgrid can only contain the numbers 1 through 9 one time.
"""

import unittest


class Solution(unittest.TestCase):

    example = [
        [".", ".", ".", "1", "4", ".", ".", "2", "."],
        [".", ".", "6", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "1", ".", ".", ".", ".", ".", "."],
        [".", "6", "7", ".", ".", ".", ".", ".", "9"],
        [".", ".", ".", ".", ".", ".", "8", "1", "."],
        [".", "3", ".", ".", ".", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", "7", ".", ".", "."],
        [".", ".", ".", "5", ".", ".", ".", "7", "."],
    ]

    example_2 = [
        [".", ".", "4", ".", ".", ".", "6", "3", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["5", ".", ".", ".", ".", ".", ".", "9", "."],
        [".", ".", ".", "5", "6", ".", ".", ".", "."],
        ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
        [".", ".", ".", "7", ".", ".", ".", ".", "."],
        [".", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]

    example_3 = [
        [".", "4", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "4", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "1", ".", ".", "7", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "3", ".", ".", ".", "6", "."],
        [".", ".", ".", ".", ".", "6", ".", "9", "."],
        [".", ".", ".", ".", "1", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "8", ".", ".", ".", ".", "."],
    ]

    @staticmethod
    def solution(grid):
        for row in grid:
            row_hashset = set()
            for number in row:
                if number == ".":
                    continue
                if number not in row_hashset:
                    row_hashset.add(number)
                else:
                    return False
        hashmap = {}
        for i in range(0, 9):
            for j in range(0, 9):
                if grid[i][j] == ".":
                    continue
                if j not in hashmap:
                    hashmap[j] = set()
                    hashmap[j].add(grid[i][j])
                else:
                    if grid[i][j] not in hashmap[j]:
                        hashmap[j].add(grid[i][j])
                    else:
                        return False
        return True

    def test_solution(self):
        assert self.solution(self.example) is True

    def test_solution_2(self):
        assert self.solution(self.example_2) is False

    def test_solution_3(self):
        assert self.solution(self.example_3) is False
