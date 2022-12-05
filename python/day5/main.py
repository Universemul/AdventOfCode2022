import itertools
import functools
import re
import math

from copy import deepcopy

INPUT_FILE = 'input.txt'

def create_stacks(lines):
    stacks = []
    cursor = 0
    while True:
        line = lines[cursor]
        if line == "\n":
            cursor += 1
            break
        stacks.append([line[k * 4 + 1] for k in range(len(line) // 4)])
        cursor += 1
    stacks.pop()

    stacks = [list("".join(c).strip()[::-1]) for c in zip(*stacks)]
    return stacks, cursor

def compute(lines, keep_order=False):
    stacks, cursor = create_stacks(lines)
    while cursor < len(lines):
        line = lines[cursor]
        n, from_, to_ = map(int, re.findall("\d+", line))
        stacks[to_ - 1].extend(stacks[from_ - 1][-n:] if keep_order else stacks[from_ - 1][-n:][::-1])
        stacks[from_ - 1] = stacks[from_ - 1][:-n]
        cursor += 1
    print("".join([s[-1] for s in stacks if s]))

def main1():
    lines = open(INPUT_FILE, "r").readlines()
    compute(lines)

def main2():
    lines = open(INPUT_FILE, "r").readlines()
    compute(lines, True)

if __name__ == "__main__":
    main1()
    main2()
