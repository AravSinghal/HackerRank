f = None


def file_input() -> str:
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
