"""
This module is for reading input from a file instead of stdin.
"""

f = None


def file_input() -> str:
    """
    Read a single line from input.txt in the working directory.
    :return: The next line from input.txt (with newline)
    """
    global f
    if f is None:
        try:
            f = open('input.txt')
        except FileNotFoundError:
            print('No input.txt found, creating and exiting.')
            open('input.txt', 'w').close()
            exit(-1)

    return f.readline()


input = raw_input = file_input
