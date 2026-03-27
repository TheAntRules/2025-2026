for T in range(int(input())):

    def solve():
        n, m = map(int, input().split())
        l = list(map(int, input().split()))
        r = list(map(int, input().split()))
        cns = [list(map(int, input().split())) for _ in range(m)]
        for i in range(m):
            cns[i][0] -= 1
            cns[i][1] -= 1
        a = [0.5 for _ in range(n)]
        known = set()
        cnsnew = []
        for x, y, z in cns:
            if x == y:
                if x in known and a[x] * 2 != z:
                    print(-1)
                    return
                if z % 2 == 1:
                    print(-1)
                    return
                a[x] = z // 2
                known.add(x)
            else:
                cnsnew.append([x, y, z])
        cns = cnsnew

        nbrs = [[] for _ in range(n)]
        for x, y, z in cns:
            nbrs[x].append((y, z))
            nbrs[y].append((x, z))

        stack = list(known)

        while stack:
            v = stack.pop()
            for nbr, z in nbrs[v]:
                if a[nbr] != 0.5:
                    if a[nbr] + a[v] != z:
                        print(-1)
                        return
                else:
                    a[nbr] = z - a[v]
                    known.add(nbr)
                    stack.append(nbr)

        # only completely unsolved a values remain
        nbrs = [[] for _ in range(n)]
        for x, y, z in cns:
            if a[x] in known or a[y] in known:
                continue
            nbrs[x].append((y, z))
            nbrs[y].append((x, z))
        visited = [False for _ in range(n)]
        stack = []
        components = []
        for i in range(n):
            if nbrs[i]:
                cs = []
                stack.append(i)
                while stack:
                    x = stack.pop()
                    if visited[x]:
                        continue
                    cs.append(x)
                    visited[x] = True
                    for y, z in nbrs[x]:
                        l[y] = max(l[y], z - r[x])
                        r[y] = min(r[y], z - l[x])
                        stack.append(y)
                components.append(cs)
        ans = 0
        for component in components:
            intervals = [(l[i], r[i]) for i in component]
            events = []
            for l, r in intervals:
                events.append((l, 1))
                events.append((r + 1, -1))
            events.sort()
            cur, best = 0, 0
            for loc, d in events:
                cur += d
                best = max(best, cur)
            ans += best
        for i, v in enumerate(a):
            if v != 0.5 and l[i] <= v <= r[i]:
                ans += 1
        print(ans)

    solve()
