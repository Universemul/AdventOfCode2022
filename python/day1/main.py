import itertools
import functools
import re
import math

from copy import deepcopy
from collections import defaultdict

INPUT_FILE = 'input.txt'

def read_file(filename, func=None):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            result.append(func(line.strip()) if func else line.strip())
    return result

def get_elves():
    lines = read_file(INPUT_FILE)
    elves = []
    current = 0
    for l in lines:
        if not l:
            elves.append(current)
            current = 0
            continue
        current += int(l)
    return sorted(elves, reverse=True)

def main2():
    elves = get_elves()
    print(sum(elves[:3]))

def main1():
    elves = get_elves()
    print(elves[0])

def inline_solution():
    lines = open(INPUT_FILE, 'r').read().split('\n\n')
    elves = sorted([sum(map(int, elf.split())) for elf in lines], reverse=True)
    print(elves[0])
    print(sum(elves[:3]))

if __name__ == "__main__":
    main1()
    main2()
