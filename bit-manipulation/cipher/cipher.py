from redef_input import *
from typing import List


n, k = get_delimited_int_list()  # type: int, int
s = ''.join(list(input().strip()))


def decode(n: int, k: int, s: str) -> List[int]:
    b = [0] * n
    i = 0
    r = 0

    for idx in range(len(s)):
        c = int(s[idx])

        if i >= k:
            r ^= b[i - k]

        b[i] = c ^ r
        r ^= b[i]

        i += 1
        if i >= n:
            break

    return b


b = decode(n, k, s)

print(''.join([str(x) for x in b]))
