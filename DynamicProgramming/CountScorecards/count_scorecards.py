from redef_input import *

# Starts here

mod = 10 ** 9 + 7

cache = {}


def save(s, n, m, d):
    global cache
    if n not in cache:
        cache[n] = {}
    if m not in cache[n]:
        cache[n][m] = {}
    cache[n][m][d] = s


def permutate(n, m, depth):
    global cache, mod, req_n
    if depth <= 1:
        #return 0 if n > m else 1
        return [] if n > m else [n]

    #s = 0
    s = []
    for i in range(min(m, n) + 1):
        new_max = m if i != m and i != req_n - 1 else m - 1
        new_n = n - i
        new_d = depth - 1
        exists = new_n in cache and new_max in cache[new_n] and new_d in cache[new_n][new_max]

        #sub_s = 0
        sub_s = [i]
        if exists:
            sub_s += cache[new_n][new_max][new_d]
        else:
            sub_s = permutate(new_n, new_max, new_d)
            save(sub_s, new_n, new_max, new_d)
            sub_s += [i]

        s = (s + sub_s if depth < req_n - 1 else [sub_s])# % mod
    return s


req_n = 0

t = int(input())
for it in range(t):
    n = int(input())
    total = (n * (n - 1)) / 2
    S = [int(i) for i in raw_input().strip().split(' ')]
    m = max(max(S), n - 1)
    for i in S:
        if i == -1:
            req_n += 1
            continue
        total -= i
        if i == m:
            m -= 1

    if total < 0:
        print(0)
        continue

    x = permutate(total, m, req_n)
    print(x)
    continue
