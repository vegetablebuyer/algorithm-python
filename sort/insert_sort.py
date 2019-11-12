#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random


def insert_sort(collect):
    """
    对列表进行插入排序
    :param collect: 待排序的列表
    :return: 排序后的列表
    基本思想：
        将第一个元素组成的子数组当成已排序的数组，
        从第二个元素开始，每个元素在前面的子数组中找到相应的位置插入
    时间复杂度：
        最优：O(n)
        最差：O(n^2)
    空间复杂度：O(1)
    """
    for index in range(1, len(collect)):
        # 默认第一个元素组成的数组为已排序的数组
        insert_index = index
        while insert_index > 0 and collect[insert_index] < collect[insert_index-1]:
            collect[insert_index], collect[insert_index-1] = collect[insert_index-1], collect[insert_index]
            insert_index -= 1

    return collect


if __name__ == "__main__":
    c_collect = [random.randint(10, 50) for _ in range(10)]
    print("before the insert sort: {0}".format(c_collect))
    c_collect = insert_sort(c_collect)
    print("after the insert sort: {0}".format(c_collect))
