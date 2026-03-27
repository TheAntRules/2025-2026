for T in range(int(input())):
    n = int(input())
    x, y, s, r = [], [], [], []
    for _ in range(n):
        a, b, c, d = input().split()
        d = 1 if d == "awaken" else 0
        x.append(float(a))
        y.append(float(b))
        s.append(float(c))
        r.append(float(d))
    works = [[0 for _ in range(-50, 50)] for _ in range(-50, 50)]
    for a in range(-50, 50):
        for b in range(-50, 50):
            xe, ye = a + 0.5, b + 0.5
            semin, semax = 1.0, 10**6
            for i in range(n):
                val = s[i] * ((x[i] - xe) ** 2 + (y[i] - ye) ** 2)
                if r[i]:
                    semin = max(semin, val)
                else:
                    semax = min(semax, val)
                if semin > semax:
                    break
            works[a + 50][b + 50] = int(semin <= semax)
    minx, maxx, miny, maxy = 50, -50, 50, -50
    for i in range(-50, 50):
        for j in range(-50, 50):
            if works[i + 50][j + 50]:
                minx = min(minx, i)
                maxx = max(maxx, i)
                miny = min(miny, j)
                maxy = max(maxy, j)
    print(minx, miny, maxx + 1, maxy + 1)


"""1
21
33.6239 -31.4136 1089.34 awaken
-455271 -295916 5.59319e-06 slept_through
20.384 -16.3127 1259.84 slept_through
10.7386 -31.3388 6233.21 awaken
19.3955 -30.7652 71961.8 slept_through
16.1209 -44.3118 1828.68 slept_through
12.4368 -50.9239 718.874 awaken
-2.32518 -14.9587 465.911 slept_through
10.5647 -20.3886 1747.09 slept_through
11.8555 -30.9808 9017.88 awaken
28.3334 -15.8029 786.009 awaken
8.16466 -40.2186 1851.97 slept_through
37.1651 -36.0378 762.005 slept_through
8.4499 -42.2115 1488.97 awaken
12.8582 -29.2644 11449.2 slept_through
14.0778 -32.6948 22568.8 awaken
4.32715 -14.6896 663.094 slept_through
10.1237 -12.5952 693.265 awaken
25.436 -14.0386 847.733 slept_through
31.1306 -20.0385 900.013 awaken
27.9654 -33.0316 2611.11 awaken
"""
