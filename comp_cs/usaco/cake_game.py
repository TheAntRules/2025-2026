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

for T in range(ii()):
    n = ii()
    a = lmi()
    if n == 2:
        print(sum(a), 0)
        continue
    ne = (n - 1) // 2
    prefix = []
    sm = 0
    for v in a:
        sm += v
        prefix.append(sm)
    suffix = []
    for v in a:
        suffix.append(sm)
        sm -= v
    mx = max(suffix[n - ne], prefix[ne - 1])
    for i in range(ne - 1):
        mx = max(mx, prefix[i] + suffix[n - ne + i + 1])
    print(sum(a) - mx, mx)
