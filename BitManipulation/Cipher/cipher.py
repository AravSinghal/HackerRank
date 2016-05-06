from redef_input import *

n, k = [int(x.strip()) for x in input().split(' ')] # type: int, int
s = ''.join(list(input().strip()))

b = [0] * n
i = 0

above = k - 1

for idx in range(len(s)):
    c = int(s[idx])
    r = 0
    for a in range(max(0, idx - above), min(idx, n - 1)):
        r ^= int(b[a])
    b[i] = c ^ r
    i += 1
    if i >= n:
        break

print(''.join([str(x) for x in b]))