# ruff: noqa
from math import floor, ceil, gcd, lcm, comb

ii = lambda: int(input())
mi = lambda: map(int, input().split())
lmi, smi = lambda: list(mi()), lambda: set(mi())
llmi = lambda n: [lmi() for _ in range(n)]

yes = lambda: print("YES")
no = lambda: print("NO")
yn = lambda x: print("YES" if x else "NO")


inside = lambda i, j, a, b: 0 <= i < a and 0 <= j < b
prefix_sum = lambda a: [(s := a[0])] + [(s := s + v) for v in a[1:]]
suffix_sum = lambda a: prefix_sum(a[::-1])[::-1]
# ruff: enable
# -----------------------------------------------

MOD = 998244353

fact = [1]
for i in range(1, 10**6 + 1):
    fact.append(fact[-1] * i % MOD)

invfact = [pow(fact[10**6], MOD - 2, MOD)]
for i in range(10**6, 0, -1):
    invfact.append(invfact[-1] * i % MOD)

invfact = invfact[::-1]

for _ in range(ii()):
    a, b, c = lmi()
    print(pow(b + 1, MOD - 2, MOD) * fact[b + c] * invfact[c - 1] % MOD)
