MOD = 10**9 + 7

def fast_pow(base, exp):
    result = 1
    base %= MOD

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % MOD
        
        base = (base * base) % MOD
        exp //= 2

    return result


t = int(input())

for _ in range(t):
    car, c = map(int, input().split())
    print(fast_pow(car, c))

