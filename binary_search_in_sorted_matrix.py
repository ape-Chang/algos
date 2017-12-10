#!/usr/bin/env python3

import unittest

# determine if key occurs in a sorted matrix.
# the matrix if sorted ascending, for each row and column.


def binary_search_in_sorted_matrix(matrix, key):
    from_row = 0
    to_row = len(matrix) - 1
    from_column = 0
    to_column = len(matrix[0]) - 1

    if matrix[from_row][from_column] > key or matrix[to_row][to_column] < key:
        return False

    prev = matrix[from_row][to_column]
    while True:
        from_row = poi_of_column(matrix, to_column, from_row, to_row, key)
        to_column = poi_of_row(matrix, from_row, from_column, to_column, key)
        if matrix[from_row][to_column] == prev:
            break
        else:
            prev = matrix[from_row][to_column]

    return prev == key


def poi_of_column(matrix, column, low, high, key):
    while low < high:
        middle = (low + high) // 2
        if matrix[middle][column] == key:
            return middle

        if matrix[middle][column] > key:
            high = middle
        else:
            low = middle + 1
    return low


def poi_of_row(matrix, row, low, high, key):
    while low < high:
        middle = (low + high) // 2
        if matrix[row][middle] == key:
            return middle

        if matrix[row][middle] > key:
            high = middle
        else:
            low = middle + 1
    return low


# test case

class Test(unittest.TestCase):

    def setUp(self):
        self.param = [[1, 2, 3],
                      [4, 7, 8],
                      [7, 8, 9]]

    def test_binary_search_in_sorted_matrix(self):
        self.assertTrue(binary_search_in_sorted_matrix(self.param, 3))
        self.assertTrue(binary_search_in_sorted_matrix(self.param, 7))
        self.assertFalse(binary_search_in_sorted_matrix(self.param, 5))


if __name__ == '__main__':
    unittest.main()
