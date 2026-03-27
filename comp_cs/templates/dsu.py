class DSU:
    def __init__(self, n):
        self.e = [-1] * n

    def get(self, x):
        if self.e[x] < 0:
            return x
        self.e[x] = self.get(self.e[x])
        return self.e[x]

    def same(self, a, b):
        return self.get(a) == self.get(b)

    def size(self, x):
        return -self.e[self.get(x)]

    def unite(self, x, y):
        x, y = self.get(x), self.get(y)
        if x == y:
            return False
        if self.e[x] > self.e[y]:
            x, y = y, x
        self.e[x], self.e[y] = self.e[x] + self.e[y], x
        return True


# ruff: enable
# -----------------------------------------------
