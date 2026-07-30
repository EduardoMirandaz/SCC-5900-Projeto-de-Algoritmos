import sys

input = sys.stdin.readline

n = int(input())

nums = [int(input()) for _ in range(n)]

MAX = 10**6

# divisors[i] = number of divisors of i
divisors = [0] * (MAX + 1)

# Sieve-style preprocessing
for i in range(1, MAX + 1):
    for j in range(i, MAX + 1, i):
        divisors[j] += 1

# Answer queries
for x in nums:
    print(divisors[x])