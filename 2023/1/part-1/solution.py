#!/usr/bin/env python3

from pathlib import Path
import os
import sys

inputfile = os.path.join(Path(sys.path[0]).parent.absolute(), "input.txt")

numbers = [str(i) for i in range(10)]

def main():
    with open(inputfile, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    summ = 0
    for line in lines:
        nums = [char for char in line if char in numbers]
        summ += int(nums[0] + nums[-1])

    print(summ)

if __name__ == "__main__":
    main()
