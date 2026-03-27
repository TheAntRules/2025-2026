def make0(q, n):
    c0 = []
    if q[:3] == "100":
        c0.append((1, 2))
        c0.append((0, 2))
    elif q[:2] == "11":
        i = 0
        while i < n and q[i] == "1":
            i += 1
        c0.append((0, i - 1))

    for l, r in c0:
        q = (
            q[:l]
            + "".join(["0" if v == "1" else "1" for v in q[l : r + 1]])
            + q[r + 1 :]
        )

    ca = []
    if q[n - 3 : n] == "001":
        ca.append((n - 3, n - 2))
        ca.append((n - 3, n - 1))
    elif q[n - 2 : n] == "11":
        i = n - 1
        while i >= 0 and q[i] == "1":
            i -= 1
        ca.append((i + 1, n - 1))
    for l, r in ca:
        q = (
            q[:l]
            + "".join(["0" if v == "1" else "1" for v in q[l : r + 1]])
            + q[r + 1 :]
        )

    i = 0
    l = 0
    if q == "0" * n:
        return c0
    c1 = []
    while i < n - 1:
        if s[i] == s[i + 1] == "1":
            if not l:
                l = 2
            else:
                l += 1
        if l and s[i + 1] == "0":
            c1.append((i - l + 1, i))
            l = 0
        i += 1
    if l:
        c1.append((i - l + 1, n - 1))
    for l, r in c1:
        q = (
            q[:l]
            + "".join(["0" if v == "1" else "1" for v in q[l : r + 1]])
            + q[r + 1 :]
        )
    c2 = []
    for i in range(n - 2):
        if q[i : i + 3] == "101":
            l, r = i, i + 2
            c2.append((l, r))
            q = (
                q[:l]
                + "".join(["0" if v == "1" else "1" for v in q[l : r + 1]])
                + q[r + 1 :]
            )
    sm = sum(int(v) for v in q)
    c3 = []
    if sm > 1:
        i = 0
        while q[i] != "1":
            i += 1
        i += 1
        l = i
        while i < n:
            if q[i] == "1":
                r = i - 1
                c3.append((l, r))
                c3.append((l - 1, r + 1))
                l = i + 1
            i += 1
    if sm == 1:
        i = 0
        while q[i] != "1":
            i += 1
        if i == 1:
            l = i + 1
            r = n - 1
            c3.append((l, r))
            c3.append((l - 1, r))
        else:
            l = 0
            r = i - 1
            c3.append((l, r))
            c3.append((l, r + 1))

    for l, r in c3:
        q = (
            q[:l]
            + "".join(["0" if v == "1" else "1" for v in q[l : r + 1]])
            + q[r + 1 :]
        )
    return c0 + ca + c1 + c2 + c3


for T in range(int(input())):
    n, s, t = int(input()), input(), input()
    ans = make0(s, n) + make0(t, n)[::-1]
    print(len(ans))
    for l, r in ans:
        print(l + 1, r + 1)

"""

"""


""""""
