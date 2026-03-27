a = []
lists = []
pt = False
for t in range(30):
    a.append(t)
    p = t // 2
    a = a[1 : p + 1] + [a[0]] + a[p + 1 :]
    lists.append(a[::])
    print(*a)
    if pt:
        # print(t, "\t", a.index(3) if t > 3 else "", "\t", *a)
        # print(t, "\t", a.index(3) if t > 3 else "")
        pt = False
    # if t > 4 and a.index(3) == 0:
    #     pt = True


# for i in range(0, 50):
#     print(i, "\t", *lists[i])


def solve1(c, t):
    if t < 10:
        return lists[t].index(c)
    if c == t:
        return c
    if t < c * 3:
        return min(c, c * 3 - t - 1)
    ti = c * 3
    pos = ti // 2
    if c == 0:
        ti, pos = 4, 2
    elif c == 1:
        ti, pos = 5, 2
    store = []
    while t >= ti:
        store.append([pos, ti])
        ti += pos + 1
        pos = ti // 2
    return store[-1][1] - (t - store[-1][0])


def solve2(x, t):
    if t <= 5000:
        return lists[t][x]
    for i in range(t + 1):
        if solve1(i, t) == x:
            return i


for q in range(int(input())):
    tp, a, b = map(int, input().split())
    if tp == 1:
        c, t = a, b
        print(solve1(c, t))
    else:
        x, t = a, b
        print(solve2(x, t))


# for c in range(10):
#     for t in range(c, c + 100):
#         if solve1(c, t) != lists[t].index(c):
#             print(c, t, solve1(c, t), lists[t].index(c))
#
# 1 4 9
