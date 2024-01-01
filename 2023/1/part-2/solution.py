#!/usr/bin/env python3

from pathlib import Path
import os
import sys

inputfile = os.path.join(Path(sys.path[0]).parent.absolute(), "input.txt")
# inputfile = "input.txt"

numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def main():
    with open(inputfile, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    summ = 0
    for line in lines:
        old_line = line
        word_num = ""
        pointer = 0
        while pointer < len(line):
            char = line[pointer]
            if char in numbers.values():
                word_num = ""
                pointer += 1
                continue

            word_num += char

            for word in numbers.keys():
                if word in word_num:
                    line = line.replace(word, numbers[word])
                    pointer = pointer - (len(word) - 1)
                    word_num = ""
                    break

            pointer += 1

        nums = [char for char in line if char in numbers.values()]
        summ += int(nums[0] + nums[-1])

        new_line = line
        width = 50
        # print(f"Old line: {old_line:{width}} New line: {new_line:{width}} First num: {nums[0]:{width}} Last num: {nums[-1]:{width}}")
        print(f"{old_line:{width}} {new_line:{width}} {nums[0]:{width}} {nums[-1]:{width}}")

    print(summ) # 53261:  That's not the right answer; your answer is too high.

if __name__ == "__main__":
    main()
