#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random


def bubble_sort(collect):
    """
    对列表进行冒泡排序
    :param collect: 待排序的列表
    :return: 排序后的列表
    基本思想：
        以从小到大排序为例，
        相邻的元素进行比较，
        将较大的元素交换到高位，
        每经过一趟排序就可以将最大的元素交换至最高位
    时间复杂度：
        最优：O(n)
        最差：O(n^2)
    空间复杂度：O(1)
    """
    length = len(collect)
    swapped = False
    for i in range(length - 1):
        for j in range(length - i - 1):
            if collect[j] > collect[j+1]:
                collect[j], collect[j+1] = collect[j+1], collect[j]
                swapped = True
        if not swapped:
            # swapped为False表示这一趟列表已经是有序的，不需要排序
            break
    return collect


if __name__ == "__main__":
    c_collect = [random.randint(10, 50) for _ in range(10)]
    print("before the bubble sort: {0}".format(c_collect))
    c_collect = bubble_sort(c_collect)
    print("after the bubble sort: {0}".format(c_collect))
