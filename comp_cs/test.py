binary = lambda n: bin(n)[2:]
for n in range(16):
    print(binary(n), bin(-n), n & -n)
