#!/usr/bin/env python3

import unittest

# given an positive integer n, return the smallest number k
# 1). larger than n
# 2). k in decimal has unique digits


def smallest_number_larger_than_n_with_unique_digits(n):
    n += 1

    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n // 10

    try:
        backtrack(digits, len(digits)-1, set())
        return int("1023456789"[:len(digits)+1])
    except Indicator:
        n = 0
        for i in reversed(digits):
            n = 10 * n + i
        return n


def backtrack(digits, p, used):
    if p < 0:
        raise Indicator()

    while digits[p] < 10:
        k = digits[p]
        if k in used:
            pass
        else:
            used.add(k)
            backtrack(digits, p-1, used)
            for i in range(p):
                digits[i] = 0
            used.remove(k)
        digits[p] = k+1


# to rewind stack rapidly
class Indicator(Exception):
    pass


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_smallest_number_larger_than_n_with_unique_digits(self):
        self.assertEqual(smallest_number_larger_than_n_with_unique_digits(1024), 1025)
        self.assertEqual(smallest_number_larger_than_n_with_unique_digits(98765), 102345)


if __name__ == '__main__':
    unittest.main()

