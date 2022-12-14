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
    cycle = 0
    marked_cycles = [20, 60, 100, 140, 180, 220]
    stack = []
    register = 1
    
    def add_cycle():
        nonlocal cycle
        nonlocal marked_cycles
        cycle += 1
        if cycle in marked_cycles:
            stack.append(cycle * register)
    
    for line in lines:
        if line.startswith("noop"):
            add_cycle()
        else:
            add_cycle()
            add_cycle()
            buffer = int(line.split()[1])
            register += buffer
    print(sum(stack))


def main2():
    lines = read_file(INPUT_FILE)
    cycle = 0
    register = 1
    crt = ["." for _ in range(240)]

    def add_pixel_to_crt():
        nonlocal cycle
        nonlocal crt
        pos_pixel = cycle % 40
        marker = "#" if abs(register - pos_pixel) <= 1 else "."
        crt[cycle % 240] = marker
        cycle += 1

    for line in lines:
        if line.startswith("noop"):
            add_pixel_to_crt()
        else:
            add_pixel_to_crt()
            add_pixel_to_crt()
            buffer = int(line.split()[1])
            register += buffer
    for idx in range(0, 240, 40):
        print("".join(crt[idx:idx+40]))
    
if __name__ == "__main__":
    main1()
    main2()
