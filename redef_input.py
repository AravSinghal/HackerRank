"""
This module is for reading input from a file instead of stdin.
"""

f = None


def file_input() -> str:
    """
    Read a single line from test_input.txt in the working directory.
    :return: The next line from test_input.txt (with newline)
    """
    global f
    if f is None:
        try:
            f = open('test_input.txt')
        except FileNotFoundError:
            print('No test_input.txt found, creating and exiting.')
            open('test_input.txt', 'w').close()
            exit(-1)

    return f.readline()


def get_delimited_int_list():
    """
    Read a line from test_input.txt and return a delimited int list.
    :return: A list containing integers read from the file.
    """
    return [int(x.strip()) for x in input().split(' ')]


input = raw_input = file_input
