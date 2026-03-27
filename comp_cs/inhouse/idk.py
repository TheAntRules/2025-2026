# ruff: noqa
from math import floor, ceil, gcd

ii = lambda: int(input())
mi = lambda: map(int, input().split())
lmi, smi = lambda: list(mi()), lambda: set(mi())
llmi = lambda n: [lmi() for _ in range(n)]

yes = lambda: print("YES")
no = lambda: print("NO")
yn = lambda x: print("YES" if x else "NO")

MOD = 10**9 + 7

modular_inv = lambda n, mod: pow(n, mod - 2, mod)
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


def factorize(n):
    global ps
    n = int(n)
    facs = []
    for p in ps:
        if p * p > n:
            break
        if n % p == 0:
            cnt = 0
            while n % p == 0:
                n //= p
                cnt += 1
            facs.append([p, cnt])
    if n > 1:
        facs.append([n, 1])
    return facs


def divisors(n, facs=None):
    global ps
    if facs is None:
        facs = factorize(n)
    ds = [1]
    for p, e in facs:
        new = []
        for d in ds:
            for ex in range(e + 1):
                new.append(d * (p**ex))
        ds = new
    return ds


# -----------------------------------------------

sieve_primes(10**3)
sumnum = [i for i in range(5 * 10**5)]
for i in range(2, 4 * 10**5 + 2):
    f = factorize(i)
    for prime, exponent in f:
        sumnum[i] = sumnum[i] * (prime - 1) // prime
pfx = [0]
for val in sumnum[1:]:
    pfx.append(pfx[-1] + val)

q = ii()
for _ in range(q):
    l, r = mi()
    print(pfx[r] - pfx[l - 1])
