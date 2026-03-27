# ruff: noqa
ii = lambda: int(input())
mi = lambda: map(int, input().split())
lmi, smi = lambda: list(mi()), lambda: set(mi())
llmi = lambda n: [lmi() for _ in range(n)]

# ruff: enable
# -----------------------------------------------


n, m = mi()
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = mi()
    edges[a].append(b)
    edges[b].append(a)
visited = [False for _ in range(n + 1)]
cnt = 0
places = []
for i in range(1, n + 1):
    if visited[i]:
        continue
    places.append(i)
    visited[i] = True
    stack = edges[i]
    while stack:
        cur = stack.pop()
        if visited[cur]:
            continue
        visited[cur] = True
        stack += edges[cur]
    cnt += 1
if cnt == 1:
    print(0)
else:
    print(cnt - 1)
    for i in range(cnt - 1):
        print(places[i], places[i + 1])
