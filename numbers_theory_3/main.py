import sys

input = sys.stdin.readline

MOD = 10**9 + 7

n = int(input())

for _ in range(n):
    a, b, c = map(int, input().split())

    # Compute b^c mod (MOD-1)
    exponent = pow(b, c, MOD - 1)

    # Compute a^(b^c) mod MOD
    answer = pow(a, exponent, MOD)

    print(answer)