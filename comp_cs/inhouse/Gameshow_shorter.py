MOD = 998244353

fact, invfact = [1 for _ in range(10**6 + 1)], [1 for _ in range(10**6 + 1)]

for i in range(2, len(fact)):
    fact[i] = fact[i - 1] * i % MOD

invfact[10**6] = pow(fact[10**6], MOD - 2, MOD)
for i in range(10**6 - 1, 1, -1):
    invfact[i] = invfact[i + 1] * (i + 1) % MOD

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(pow(b + 1, MOD - 2, MOD) * fact[b + c] * invfact[c - 1] % MOD)
