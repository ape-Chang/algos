#!/usr/bin/env python3

import unittest


# 《算法新解》前言的第一个例子：输入n个非负整数的数组，返回最小的不在这个数组中的数

def min_free_id_v1(lst):
    slot_count = len(lst) + 1
    slot_occupied = [False] * slot_count
    for item in lst:
        if item < slot_count:
            slot_occupied[item] = True
    return slot_occupied.index(False)


class Test(unittest.TestCase):
    def test_min_free_id_v1(self):
        self.assertEqual(min_free_id_v1([18, 4, 8, 9, 16, 1, 14, 7, 19, 3, 0, 5, 2, 11, 6]), 10)


if __name__ == '__main__':
    unittest.main()
