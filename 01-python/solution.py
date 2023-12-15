import unittest


def get_input(filename):
    with open(filename, 'r') as file:
        return [s.strip() for s in file.readlines()]


digits = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def get_digit(s, reverse=False):
    rate = 1 if not reverse else -1
    return int(next(c for c in s[::rate] if c.isdigit()))


def get_digit_spelled(s, reverse=False):
    rate = 1 if not reverse else -1
    candidates = []
    for c in s[::rate]:
        if c.isdigit():
            return int(c)
        candidates = [
            (spelling, digit, idx+1) for spelling, digit, idx in candidates
            if spelling[idx+1] == c
        ]
        for spelling, digit, idx in candidates:
            if idx == len(spelling)-1:
                return digit
        candidates.extend(
            [spelling[::rate], digit, 0] for spelling, digit in digits.items()
            if c == spelling[::rate][0]
        )


class Solution(unittest.TestCase):

    def test_star_1(self):
        data = get_input('01-python/input.txt')
        print(sum(get_digit(s) * 10 + get_digit(s, True) for s in data))

    def test_star_2(self):
        data = get_input('01-python/input.txt')
        print(sum(get_digit_spelled(s) * 10 + get_digit_spelled(s, True)
              for s in data))


if __name__ == '__main__':
    unittest.main()
