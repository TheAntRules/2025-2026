def binarytoint(n):
    n = str(n)
    nm = 0
    for i, c in enumerate(n):
        nm += int(c) * 2 ** (len(n) - i - 1)
    return nm


def inttobinary(n):
    return bin(int(n))[2:]


candidates = []

dk, s = input().split()
dk = int(dk)
bk = inttobinary(dk)


def recur(curr, remaining):
    global dk, bk
    if len(curr) > len(bk) - 1:
        return [curr]
    if len(curr) == len(bk) - 1:
        if remaining:
            return (
                [curr]
                + recur(curr + remaining[0], remaining[1:])
                + recur(curr, remaining[1:])
            )
        else:
            return [curr]
    if not remaining:
        return []
    return [] + recur(curr + remaining[0], remaining[1:]) + recur(curr, remaining[1:])


things = recur("", s)
fnal = []
for thing in things:
    if thing[0] != "0":
        fnal.append(thing)
fnal = set(fnal)
mx = 0
for item in fnal:
    if binarytoint(item) <= dk:
        mx = max(mx, binarytoint(item))
print(len(s) - len(inttobinary(mx)))
