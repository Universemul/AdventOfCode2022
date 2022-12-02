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

def main1():
    lines = read_file(INPUT_FILE)
    total = 0
    for l in lines:
        left, right = l.split()
        a = "ABC".index(left)
        b = "XYZ".index(right)
        total += b + 1
        if a == b:
            total += 3
        else:
            total += 6 if (b - a) % 3 == 1 else 0
    print(total)

def main2():
    lines = read_file(INPUT_FILE)
    total = 0
    for l in lines:
        left, right = l.split()
        a = "ABC".index(left)
        match right:
            case "X": # lose
                total += (a - 1) % 3 + 1 
            case "Y": # draw
                total += 3 + a + 1
            case "Z": # win
                total += 6 + (a + 1) % 3 + 1
    print(total)


if __name__ == "__main__":
    main1()
    main2()
