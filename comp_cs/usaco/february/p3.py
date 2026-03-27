def hash(a, b):
    return str(a) + "|" + str(b)


n = int(input())
a = list(map(int, input().split()))
ranges = []
q = set()
for v in a:
    q.add(v)
numunique = len(q)
cnts = {k: 0 for k in q}
l = 0
r = 0
cnts[a[0]] += 1
numunique -= 1
while True:
    r += 1
    if cnts[a[r]] == 0:
        numunique -= 1
    cnts[a[r]] += 1
    if numunique == 0:
        break

while True:
    while l < n and cnts[a[l]] > 1:
        cnts[a[l]] -= 1
        l += 1
    if l == n:
        break
    ranges.append([l, r])
    cur = a[l]
    cnts[cur] -= 1
    l += 1
    while a[r % n] != cur:
        r += 1
        cnts[a[r % n]] += 1
# print(ranges)


answers = []
for i in range(n):
    ans = 67676767
    for l, r in ranges:
        if l <= i <= r:
            ans = min(ans, 2 * (i - l) + r - i)
            ans = min(ans, 2 * (r - i) + i - l)
        if l <= i + n <= r:
            ans = min(ans, 2 * (i + n - l) + r - i - n)
            ans = min(ans, 2 * (r - i - n) + i + n - l)
    s = set()
    for j in range(i + 1, i + n):
        s.add(a[j % n])
        if len(s) == len(q):
            ans = min(ans, j - i)
    s = set()
    for j in range(i - 1, i - n, -1):
        s.add(a[j % n])
        if len(s) == len(q):
            ans = min(ans, i - j)
    answers.append(str(ans))

print(" ".join(answers))
