f = None


def file_input():
    global f
    if f is None:
        f = open('input.txt')

    return f.readline()


input = raw_input = file_input
