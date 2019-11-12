#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random


def select_sort(collect):
    """
    对数组进行选择排序
    :param collect: 待排序的数组
    :return: 已排序的数组
    基本思想：
        从头至尾扫描序列，找出最小的一个元素，和第一个元素交换
        接着从剩下的元素中继续这种选择和交换方式，最终得到一个有序序列
    时间复杂度：
        最优：O(n^2)
        最差：O(n^2)
    空间复杂厚：O(n)
    """
    for i in range(0, len(collect)-1):
        # 只要第1至第(n-1)个最小的元素找到了，最后一个最小元素也不需要找了
        least_index = i
        for j in range(i, len(collect)):
            if collect[j] < collect[least_index]:
                least_index = j
        if least_index != i:
            collect[i], collect[least_index] = collect[least_index], collect[i]
    return collect


if __name__ == "__main__":
    c_collect = [random.randint(10, 50) for _ in range(10)]
    print("before the select sort: {0}".format(c_collect))
    c_collect = select_sort(c_collect)
    print("after the select sort: {0}".format(c_collect))