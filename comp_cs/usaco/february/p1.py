T, C = map(int, input().split())
for t in range(T):
    n = int(input())
    l, r = input(), input()
    if l.count("J") != r.count("J") or l.count("N") % 2:
        print("NO")
        continue
    cnt = {"JJ": 0, "NN": 0, "JN": 0, "NJ": 0}
    for i in range(n):
        cnt[l[i] + r[i]] += 1
    if cnt["JN"] == 0 and cnt["JJ"] != 0 and cnt["NN"] != 0:
        print("NO")
        continue

    print("YES")
    if C == 0:
        continue
    lst = {"JJ": [], "NN": [], "JN": [], "NJ": []}
    for i in range(n):
        lst[l[i] + r[i]].append(i + 1)

    if lst["NJ"]:
        ans = lst["JJ"] + [lst["JN"][0]] + lst["NN"] + [lst["NJ"][0]]
    else:
        ans = lst["JJ"] + lst["NN"]
    for i in range(1, len(lst["NJ"])):
        ans += [lst["JN"][i]]
        ans += [lst["NJ"][i]]
    s = "J" * len(lst["JJ"])
    if len(lst["JN"]) == 0:
        if not s:
            s = "NJ" * (len(lst["NN"]) // 2)
    else:
        cur = True
        for i in range(1 + len(lst["NN"])):
            s += "J" if cur else "N"
            cur = not cur
        s += "J" if cur else "N"
        for _ in range(1, len(lst["NJ"])):
            s += "J" if cur else "N"
            cur = not cur
            s += "J" if cur else "N"

    print(" ".join(str(v) for v in ans))
    print(s)

# zig zag pattern, down up down up
