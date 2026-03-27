# ruff: noqa
import math

ii = lambda: int(input())
mi = lambda: map(int, input().split())
lmi, smi = lambda: list(mi()), lambda: set(mi())
llmi = lambda n: [lmi() for _ in range(n)]

yes = lambda: print("YES")
no = lambda: print("NO")
yn = lambda x: print("YES" if x else "NO")

MOD = 10**9 + 7
# ruff: enable
# -----------------------------------------------

prefix = {"GHz": 9, "MHz": 6, "kHz": 3, "Hz": 0, "mHz": -3, "uHz": -6, "nHz": -9}
prefix_list = sorted(prefix.items(), key=lambda v: v[1])


def convert(n, unit):
    return n * 10 ** (prefix[unit] + 9)


for T in range(ii()):
    v1, operator, v2 = input().split(",")
    components = v1.split(" ")
    v1 = int(components[0])
    unit1 = components[1] if len(components) > 1 else ""

    components = v2.split(" ")
    v2 = int(components[0])
    unit2 = components[1] if len(components) > 1 else ""

    if operator in ["+", "-"] and (unit1 == "" or unit2 == ""):
        if unit1 == "" and unit2 == "":
            print(v1 + v2)
            continue
        print("INVALID")
        continue
    if unit1 == "" and unit2 == "":
        print(v1 * v2)
        continue

    preans = 0
    if operator == "*":
        if unit1 == "":
            v2_converted = convert(v2, unit2)
            preans = v1 * v2_converted
        if unit2 == "":
            v1_converted = convert(v1, unit1)
            preans = v1_converted * v2
    else:
        v1_converted = convert(v1, unit1)
        v2_converted = convert(v2, unit2)
        preans = v1_converted + v2_converted if operator == "+" else v1_converted - v2_converted
    preans = preans // 1
    if preans == 0:
        print("0 GHz")
        continue
    thingy = str(preans)[::-1]
    i = 0
    while i < len(thingy) and thingy[i] == "0":
        i += 1
    num_zeroes = i
    j = 0
    while num_zeroes >= 3 and j < len(prefix_list):
        j += 1
        num_zeroes -= 3
        preans /= 1000
    print(round(preans), prefix_list[j][0])


"""10
6 mHz,+,75 kHz
59 uHz,-,55 kHz
22 nHz,+,35
58 Hz,-,61 mHz
13 kHz,+,11 kHz
61 GHz,-,32 GHz
90 kHz,-,99 Hz
55 Hz,*,90
60 uHz,+,58 Hz
9,*,55 uHz
"""
