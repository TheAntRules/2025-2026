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
from bisect import bisect_left, bisect_right

for T in range(ii()):
    n, k = mi()
    x = sorted(lmi())
    res = [lmi() for _ in range(k)]
    dres = []
    for l, r, t in res:
        dres.append((l, 1))
        dres.append((r + 1, -1))
    dres.sort()
    print(x)
    print(dres)

    tcur = 0
    currentrestrictions = 0
    ans = 0

    thingies = []
    for location, dr in dres:
        while tcur < n and x[tcur] < location:
            thingies.append((x[tcur], currentrestrictions))
            tcur += 1

        currentrestrictions += dr
    print(thingies)
    thingiesind0 = [v[0] for v in thingies]
    for l, r, t in res:
        locl = bisect_left(thingiesind0, l)
        locr = bisect_right(thingiesind0, r)
        numtrees = locr - locl

    print()

# 2 3 3 3 4 5 6 6 7
# (l,r)=(3,6)
# 1,8

"""3
7 1
8 4 10 1 2 6 7
2 9 3
7 2
8 4 10 1 2 6 7
2 9 3
1 10 1
7 2
8 4 10 1 2 6 7
1 122 3
1 10 4

"""
