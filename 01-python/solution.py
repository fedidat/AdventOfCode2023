import unittest
import heapq

def get_input(filename):
    with open(filename, 'r') as file:
        return [[int(x) for x in s.splitlines()] for s in file.read().split('\n\n')]


class Solution(unittest.TestCase):

    def test_star_1(self):
        data = get_input('01-python/input.txt')
        pass

    def test_star_2(self):
        data = get_input('01-python/input.txt')
        pass


if __name__ == '__main__':
    unittest.main()
