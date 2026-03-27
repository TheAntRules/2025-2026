# ruff: noqa
from math import floor, ceil, gcd
from bisect import bisect_right, bisect

ii = lambda: int(input())
mi = lambda: map(int, input().split())
lmi, smi = lambda: list(mi()), lambda: set(mi())
llmi = lambda n: [lmi() for _ in range(n)]

yes = lambda: print("YES")
no = lambda: print("NO")
yn = lambda x: print("YES" if x else "NO")

MOD = 10**9 + 7
# ruff: enable
# -----------------------------------------------


def sieve_primes(n):
    global ps
    n = int(n)
    isprime = bytearray(b"\x01") * (n + 1)
    isprime[0] = isprime[1] = 0
    for i in range(int(n**0.5) + 1):
        if isprime[i]:
            isprime[i * i : n + 1 : i] = [False] * ((n + 1 - (n % i) - i * i) // i + 1)
    ps = [i for i, v in enumerate(isprime) if v]


# -----------------------------------------------

sieve_primes(1e6)

for T in range(ii()):
    d = ii()
    p1 = ps[bisect_right(ps, d)]
    p2 = ps[bisect(ps, p1 + d - 1)]
    print(p1 * p2)
    # print(p1, p2, p1 * p2)
