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
# ruff: enable
# -----------------------------------------------
for T in range(ii()):
    n = ii()
    a = lmi()
