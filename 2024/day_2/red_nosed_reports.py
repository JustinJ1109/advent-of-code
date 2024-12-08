import os
import sys
from get_input import read_input

# https://adventofcode.com/2024/day/2

"""
--- Day 2: Red-Nosed Reports ---
Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?

--- Part Two ---
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
"""
ASC = 1
DESC = -1


def is_valid(left: int, right: int, direction: int) -> bool:
    return not (
        (left < right and direction == DESC)
        or (left > right and direction == ASC)
        or (abs(left - right) < 1 or abs(left - right) > 3)
    )


def main():

    reports_safe_count = 0
    for i, line in enumerate(read_input(os.path.join(".", "test_input.txt"))):
        report = [int(x) for x in line.strip().split(" ")]
        direction = 0

        skipped_number = -1
        left_i, right_i = 0, 1
        reports_safe_count += 1
        while right_i < len(report):
            left_level = report[left_i]
            right_level = report[right_i]

            if left_i == 0:
                if left_level < right_level:
                    direction = ASC
                elif left_level > right_level:
                    direction = DESC
            elif not is_valid(left_level, right_level, direction):
                if skipped_number >= 0:
                    reports_safe_count -= 1
                    break
                skipped_number = left_i
                left_i -= 1
                continue
            right_i += 1
            left_i += 1
            if skipped_number >= 0 and left_i == skipped_number:
                left_i += 1

    print(f"Number of safe reports: {reports_safe_count}")


if __name__ == "__main__":
    main()
