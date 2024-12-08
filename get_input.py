import os


def read_input(filename: str = os.path.join(".", "input.txt")):
    with open(filename, "r") as fp:
        for l in fp.readlines():
            yield l
