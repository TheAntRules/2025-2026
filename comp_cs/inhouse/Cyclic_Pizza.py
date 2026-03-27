for T in range(int(input())):
    n = int(input())
    a = [input() for _ in range(n)]

    dv = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            dv.append(i)
            dv.append(n // i)
    dv.sort()

    rshift = [[v == (v[d:] + v[:d]) for d in dv] for v in a]
    cnt1 = min(d for j, d in enumerate(dv) if all(rshift[i][j] for i in range(n)))

    a = [[a[j][i] for j in range(n)] for i in range(n)]

    rshift = [[v == (v[d:] + v[:d]) for d in dv] for v in a]
    cnt2 = min(d for j, d in enumerate(dv) if all(rshift[i][j] for i in range(n)))

    print(n // cnt1 * n // cnt2)
