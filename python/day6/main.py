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

def compute(nbr_markers):
    lines = read_file(INPUT_FILE)
    line = lines[0]
    idx = 0
    while idx < len(line):
        subset = line[idx:idx + nbr_markers]
        if len(set(subset)) == nbr_markers:
            break
        idx += 1
    print(idx + nbr_markers)

def main1():
    compute(4)

def main2():
    compute(14)
    
if __name__ == "__main__":
    main1()
    main2()
