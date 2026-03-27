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
