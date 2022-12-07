import itertools
import functools
import re
import math
import sys

from collections import defaultdict
from copy import deepcopy

INPUT_FILE = 'input.txt'

def read_file(filename, func=None):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            result.append(func(line.strip()) if func else line.strip())
    return result

def compute(node):
    if isinstance(node, int):
        return node, 0
    answer = 0
    dir_size = 0
    for value in node.values():
        temp_d_size, temp_answer = compute(value)
        dir_size += temp_d_size
        answer += temp_answer
    if dir_size <= 100000:
        answer += dir_size
    return dir_size, answer

def build_filesystem():
    lines = read_file(INPUT_FILE)
    cwd = root = {}
    stack = []
    idx = 0
    while idx < len(lines):
        line = lines[idx]
        if line.startswith("$"):
            if line[2:4] == "cd":
                _dir = line[5:]
                if _dir == '/':
                    cwd = root
                    stack = []
                elif _dir == '..':
                    cwd = stack.pop()
                else:
                    if _dir not in cwd:
                        cwd[_dir] = {}
                    stack.append(cwd)
                    cwd = cwd[_dir]
        else:
            cmd, params = line.split()
            if cmd == 'dir':
                if cmd not in cwd:
                    cwd[params] = {}
            else:
                cwd[params] = int(cmd)
        idx += 1
    return root

def main1():
    cwd = build_filesystem()
    _, answer = compute(cwd)
    print(answer)

def get_size(node):
    if isinstance(node, int):
        return node
    return sum(map(get_size, node.values()))

def compute_v2(node, free_space):
    ans = sys.maxsize
    node_size = get_size(node)
    if node_size >= free_space:
        ans = node_size
    for value in node.values():
        if isinstance(value, dict):
            a = compute_v2(value, free_space)
            ans = min(a, ans)
    return ans
            

def main2():
    cwd = build_filesystem()
    size = get_size(cwd)
    free_space = size - (70_000_000 - 30_000_000)
    answer = compute_v2(cwd, free_space)
    print(answer)
    
if __name__ == "__main__":
    main1()
    main2()
