import os
import re

from get_input import read_input

"""
--- Day 7: Bridge Repair ---
The Historians take you to a familiar rope bridge over a river in the middle of a jungle. The Chief isn't on this side of the bridge, though; maybe he's on the other side?

When you go to cross the bridge, you notice a group of engineers trying to repair it. (Apparently, it breaks pretty frequently.) You won't be able to cross until it's fixed.

You ask how long it'll take; the engineers tell you that it only needs final calibrations, but some young elephants were playing nearby and stole all the operators from their calibration equations! They could finish the calibrations if only someone could determine which test values could possibly be produced by placing any combination of operators into their calibration equations (your puzzle input).

For example:

190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
Each line represents a single equation. The test value appears before the colon on each line; it is your job to determine whether the remaining numbers can be combined with operators to produce the test value.

Operators are always evaluated left-to-right, not according to precedence rules. Furthermore, numbers in the equations cannot be rearranged. Glancing into the jungle, you can see elephants holding two different types of operators: add (+) and multiply (*).

Only three of the above equations can be made true by inserting operators:

190: 10 19 has only one position that accepts an operator: between 10 and 19. Choosing + would give 29, but choosing * would give the test value (10 * 19 = 190).
3267: 81 40 27 has two positions for operators. Of the four possible configurations of the operators, two cause the right side to match the test value: 81 + 40 * 27 and 81 * 40 + 27 both equal 3267 (when evaluated left-to-right)!
292: 11 6 16 20 can be solved in exactly one way: 11 + 6 * 16 + 20.
The engineers just need the total calibration result, which is the sum of the test values from just the equations that could possibly be true. In the above example, the sum of the test values for the three equations listed above is 3749.

Determine which equations could possibly be true. What is their total calibration result?

--- Part Two ---
The engineers seem concerned; the total calibration result you gave them is nowhere close to being within safety tolerances. Just then, you spot your mistake: some well-hidden elephants are holding a third type of operator.

The concatenation operator (||) combines the digits from its left and right inputs into a single number. For example, 12 || 345 would become 12345. All operators are still evaluated left-to-right.

Now, apart from the three equations that could be made true using only addition and multiplication, the above example has three more equations that can be made true by inserting operators:

156: 15 6 can be made true through a single concatenation: 15 || 6 = 156.
7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
192: 17 8 14 can be made true using 17 || 8 + 14.
Adding up all six test values (the three that could be made before using only + and * plus the new three that can now be made by also using ||) produces the new total calibration result of 11387.

Using your new knowledge of elephant hiding spots, determine which equations could possibly be true. What is their total calibration result?
"""

DATA = list(read_input(os.path.join(".", "input.txt")))


memo = {}

# cache_stats = {"hits": [], "misses": []}


def memoize(func):
    def wrapped(*args, **kwargs):
        if memo.get((func.__name__, *args)):
            # cache_stats["hits"].append((func.__name__, *args))
            return memo[(func.__name__, *args)]

        # cache_stats["misses"].append((func.__name__, *args))
        res = func(*args, **kwargs)
        memo[(func.__name__, *args)] = res
        return res

    return wrapped


@memoize
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


@memoize
def add(x, y):
    return x + y


@memoize
def mult(x, y):
    return x * y


@memoize
def concat(x, y):
    return int(str(x) + str(y))


def main(operand_map: dict):
    total = 0
    for line in DATA:
        answer, *operands = [int(s) for s in re.findall(r"\d+", line)]

        # number of total different configurations the equation can be
        num_permutations = len(operand_map) ** (len(operands) - 1)

        # ex. i==1, i==2
        for i in range(num_permutations):
            # represent the current permutations as a base_n number (base2 for p.1, base3 for p.2) mask
            # to determine which operant should be placed between the current and next number
            op_mask = "".join(str(n) for n in numberToBase(i, len(operand_map))).rjust(
                len(operands) - 1, "0"
            )

            ans = operands[0]
            for right in range(1, len(operands)):
                if ans > answer:
                    break
                ans = operand_map[op_mask[right - 1]](ans, operands[right])
            if ans == answer:
                total += ans
                break

    print(f"Answer: {total}")
    return total


op_map_part_1 = {
    "0": mult,
    "1": add,
}

op_map_part_2 = {
    **{k: v for k, v in op_map_part_1.items()},
    "2": concat,
}
print("Part 1:")
res = main(op_map_part_1)
assert res == 20665830408335
print()
print("Part 2:")
main(op_map_part_2)
