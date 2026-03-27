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

# ruff: enable
# -----------------------------------------------
for T in range(ii()):
    n, x, y = mi()
    s = input()
    p = lmi()
