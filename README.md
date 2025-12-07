# advent-of-code

## Usage

The `run_solution` script is the entry point to run any of the available completed days for the [Advent of Code](https://adventofcode.com) mini-projects. You can specify the `--year` and `--day` to specify a particular solver and then provide input to run against via pipe. Alternatively, you can specify a `--test-case` to use a pre-existing input/answer map. This looks in the respective `./_<year>/day_<day>/tests/case_<test-case>/` directory for an `input.txt` as well as any optionally provided answer keys for part `1.out` or part `2.out`.  
  
  If no year is given, the latest within the directory the script is ran will be used. If no day is given, the latest directory that matches the `/day_\d+/` pattern within the chosen `year` directory will be used.
  
### Examples

`./run_solution -y 2025 -d 1 -c 1` - Run the solution for Year 2025 Day 1 using `case_1` test case input / answer keys.  
  
`cat my_input.txt | ./run_solution` - Run the solution for the latest year and day using the contents of `my_input.txt` as the input. No answer key will be used.

## Adding New Days and Solvers

To add new days and solvers, simply create the `day_<day>` directory under the desired `_<year>` directory. Create a `solution.py` file and `__init__.py` file under this directory with the following contents:
```python
# ex. _2025/day_1/__init__.py
from .solution import *
```
Within the `solution.py` file, either or both function definitions must exist:  
```python
# ex. _2025/day_1/solution.py
def solve_1(solution_input: List[str]) -> Any:
    return answer
def solve_2(solution_input: List[str]) -> Any:
    return answer
```
these represent the answers to each part of the advent for that day's puzzle. If either solve function is missing, that part will simply be omitted from the answer and a warning will be output.

### Adding test cases

You can optionally add test cases to use the `--test-case / -c` flag by creating a directory `tests/` within the `_<year>/day_<day>/` _(as in `_2025/day_1/tests/`, for example)_ and then providing the cases as such `./tests/case_[0-9]`. Each test case expects the following files within its subdirectory:  
- `input.txt` - the input which will be passed to the solver functions
- `1.out` - the answer key for part 1 solution. (Optional)
- `2.out` - the answer key for part 2 solution. (Optional)

_Note: if no answer key is provided for either or both parts, no test validation will be done._