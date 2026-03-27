def gcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, g = gcd(b, a % b)
        return y, x - (a // b) * y, g


# -----------------------------------------------
