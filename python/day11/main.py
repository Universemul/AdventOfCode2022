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

def get_starting_items(line):
    return [int(x.strip()) for x in line[15:].split(',')]

def get_operation(line):
    line = line[17:].strip()
    return line

def get_test(test, success, failure):
    return (int(test[19:].strip()), int(success[25:].strip()), int(failure[26:].strip()))

def compute(lines, rounds):
    monkeys = []
    _mod = 1
    
    for group in lines:
        infos = group.split('\n')
        _, idx = infos[0].split()
        idx = int(idx.strip().replace(':', ''))
        items = get_starting_items(infos[1].strip())
        operation = get_operation(infos[2].strip())
        divide_by, success, failure = get_test(infos[3].strip(), infos[4].strip(), infos[5].strip())
        _mod *= divide_by
        monkeys.append((idx, items, operation, divide_by, success, failure))

    counts = [0 for _ in monkeys]
    items = [x[1] for x in monkeys]
    for i in range(rounds):
        for i in range(len(monkeys)):
            monkey = monkeys[i]
            for item in items[i]:
                counts[i] += 1
                _level = eval(monkey[2].replace("old", str(item)))
                if rounds == 20: #part1
                    _level //= 3.0
                else: #part2
                    _level %= _mod
                if _level % monkey[3] == 0:
                    items[monkey[4]].append(_level)
                else:
                    items[monkey[5]].append(_level)
            items[i].clear()
    counts.sort()
    print(counts[-1] * counts[-2])

def main1():
    lines = open(INPUT_FILE, "r").read().split("\n\n")
    compute(lines, 20)

def main2():
    lines = open(INPUT_FILE, "r").read().split("\n\n")
    compute(lines, 10000)
    
if __name__ == "__main__":
    main1()
    main2()
