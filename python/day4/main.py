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

def include_range(_min, _max):
    return range(_min, _max + 1)

def get_range(item):
    return set(include_range(*map(int, item.split('-'))))

def main1():
    lines = read_file(INPUT_FILE)
    ans = 0
    for l in lines:
        left, right = (get_range(x) for x in l.split(','))
        ans += 1 if len(left - right) == 0 or len(right - left) == 0 else 0 
    print(ans)

def main2():
    lines = read_file(INPUT_FILE)
    ans = 0
    for l in lines:
        left, right = (get_range(x) for x in l.split(','))
        ans += 1 if (left & right) else 0
    print(ans)
    
if __name__ == "__main__":
    main1()
    main2()
