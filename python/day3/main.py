import itertools
import functools
import re
import math

from copy import deepcopy

INPUT_FILE = 'input.txt'

def read_file(filename, func=None):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            result.append(func(line.strip()) if func else line.strip())
    return result


def split_list(items):
    half = len(items)//2
    return items[:half], items[half:]

MAPPER = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main1():
    lines = read_file(INPUT_FILE)
    ans = 0
    for line in lines:
        bag_a, bag_b = split_list(line)
        common = set(bag_a) & (set(bag_b))
        ans += MAPPER.index(common.pop()) + 1
    print(ans)

def main2():
    lines = read_file(INPUT_FILE)
    
if __name__ == "__main__":
    main1()
    main2()
