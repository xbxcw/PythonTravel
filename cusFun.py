import math
import os
import time


def bubble_sort(array):
    """
    冒泡排序
    :param array: list
    :return: array list
    """
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def find_specified_file(path, suffix=''):
    """
    查找指定文件
    :param path: 根目录
    :param suffix: 格式，默认是空
    :return: 文件地址列表
    """
    _file = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(suffix):
                _file.append(os.path.join(root, file))
    return _file


def change_time(allTime):
    day = 24 * 60 * 60
    hour = 60 * 60
    min = 60
    if allTime < 60:
        return "%d sec" % math.ceil(allTime)
    elif allTime > day:
        days = divmod(allTime, day)
        return "%d days, %s" % (int(days[0]), change_time(days[1]))
    elif allTime > hour:
        hours = divmod(allTime, hour)
        return '%d hours, %s' % (int(hours[0]), change_time(hours[1]))
    else:
        mins = divmod(allTime, min)
        return "%d mins, %d sec" % (int(mins[0]), math.ceil(mins[1]))


def customStrftime(t):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))


def create_directory(directory):
    """
    创建路径，如果文件夹不存在，就创建
    :param directory (str)
    :return: directory(str)
    """
    if not os.path.exists(directory):
        os.mkdir(directory)
    return directory
