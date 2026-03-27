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
# ruff: enable
# -----------------------------------------------
