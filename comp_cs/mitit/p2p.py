for T in range(int(input())):
    a, b = map(str, input().split())
    cnt = lambda s, c: sum(c == v for v in s)

    def cn(s):
        for i in range(len(s)):
            if s[-i - 1] == "P":
                return i
        return len(s)

    print(
        "YES"
        if a.count("P") == b.count("P") and a[::-1].find("P") == b[::-1].find("P")
        else "NO"
    )
