"""
Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in the list,
since this is what you'll be asked to do during an interview.

Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

Example

For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
solution(l, k) = [1, 2, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
solution(l, k) = [1, 2, 3, 4, 5, 6, 7].
"""
import unittest


class Solution(unittest.TestCase):

    class LinkedListNode(object):
        def __init__(self, x):
            self.value = x
            self.next = None

    a = LinkedListNode(3)
    a.next = LinkedListNode(1)
    a.next.next = LinkedListNode(2)
    a.next.next.next = LinkedListNode(3)
    a.next.next.next.next = LinkedListNode(4)
    a.next.next.next.next.next = LinkedListNode(5)

    @staticmethod
    def solution(l, k):
        while l and l.value == k:
            l = l.next
        c = l
        while c and c.next:
            if c.next.value == k:
                c.next = c.next.next
            else:
                c = c.next
        return l

    def test_solution(self):
        result = Solution.solution(self.a, 3)
        assert result.value == 1, result.next.value == 2
        assert result.next.next.value == 4, result.next.next.next.value == 5
