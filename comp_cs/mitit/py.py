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
prefix_sum = lambda a: [(s := a[0])] + [(s := s + v) for v in a[1:]] + [0]
# ruff: enable
# -----------------------------------------------

m = {}
m["MI"] = "IM"
m["IM"] = "IM"
m["TI"] = "IT"
m["IT"] = "IT"
m["MT"] = "MT"
m["TM"] = "MT"


for T in range(ii()):
    a, b, c = lmi()
    if a == b == c == 1:
        yes()
        print("TMI")
        continue
    if a == b == c:
        yes()
        print("MTITMI" * (a // 2) + "MTI" * (a % 2))
        continue

    l = [(a, "M"), (b, "I"), (c, "T")]
    q = sorted(l)[::-1]
    x, y, z = sorted([a, b, c])[::-1]
    if q[1][0] == q[2][0] == 0:
        if q[0][0] == 1:
            yes()
            print(q[0][1])
        else:
            no()
    elif q[2][0] == 0:
        if x <= y + 1:
            yes()
            s = f"{q[1][1] + q[0][1]}" * q[1][0]
            if q[0][0] - q[1][0] == 0:
                print(s)
            elif s[-1] == q[0][1]:
                print(q[0][1] + s)
            else:
                print(s + q[0][1])
        else:
            no()
    else:
        if q[2][0] + q[1][0] >= q[0][0]:
            yes()
            a, b, c = q[0][0], q[1][0], q[2][0]
            r1 = f"{q[0][1] + q[2][1]}"
            if r1[1] == "I":
                r1 = r1[::-1]
            s = r1 * (a - b)
            c -= a - b
            a -= a - b
            r2 = m[f"{q[0][1] + q[1][1]}"][::-1]
            if r2[0] == r1[1]:
                r2 = r2[::-1]
            s += r2 * (b - c)
            a -= b - c
            b -= b - c
            if c == 0:
                print(s)
                continue

            if s[-1] == "M":
                s += "IMT" + "MTITMI" * ((a - 1) // 2) + "MTI" * ((a + 1) % 2)
            elif s[-1] == "T":
                s += "MTITMI" * (a // 2) + "MTI" * (a % 2)
            else:
                if s[-2] == "T":
                    s += "TMIMTI" * (a // 2) + "TMI" * (a % 2)
                else:
                    s += "MTITMI" * (a // 2) + "MTI" * (a % 2)
            print(s)
            continue
        elif q[1][0] + q[2][0] + 1 == q[0][0]:
            if q[0][1] == "I":
                no()
                continue
            yes()
            a, b, c = q[0][0], q[1][0], q[2][0]
            r1 = f"{q[0][1] + q[2][1]}"
            s = r1 * (c)
            a -= c
            c = 0

            s += f"{q[0][1] + q[1][1]}" * q[1][0]
            if s[-1] == q[0][1]:
                print(q[0][1] + s)
            else:
                print(s + q[0][1])
        else:
            no()
