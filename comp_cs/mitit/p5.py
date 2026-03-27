# ruff: noqa
from math import floor, ceil, gcd, lcm, comb

ii = lambda: int(input())
mi = lambda: map(int, input().split())
lmi, smi = lambda: list(mi()), lambda: set(mi())
llmi = lambda n: [lmi() for _ in range(n)]

yes = lambda: print("YES")
no = lambda: print("NO")
yn = lambda x: print("YES" if x else "NO")

MOD = 10**9 + 7
add = lambda *a: sum(a) % MOD
mul = lambda a, b: (a * b) % MOD
power = lambda a, b: pow(a, b, MOD)

inside = lambda i, j, a, b: 0 <= i < a and 0 <= j < b
prefix_sum = lambda a: [(s := a[0])] + [(s := s + v) for v in a[1:]]
suffix_sum = lambda a: prefix_sum(a[::-1])[::-1]
from sys import stdout
# ruff: enable
# -----------------------------------------------


def query(i, j):
    print(f"? {i + 1} {j + 1}")
    stdout.flush()
    return ii()


for T in range(ii()):
    n = ii()
    q = []

    for i in range(0, n - 2, 3):
        a = query(i, i + 1)
        b = query(i + 1, i + 2)
        g = gcd(a, b)
        q.append(a // g)
        q.append(g)
        q.append(b // g)
    if n % 3 != 0:
        a = query(n - 1, n - 2)
        b = query(n - 2, n - 3)
        g = gcd(a, b)
        if n % 3 == 1:
            q.append(a // g)
        else:
            q.append(g)
            q.append(a // g)
    print("! " + " ".join(map(str, q)))


# 0 1, 1 2,
