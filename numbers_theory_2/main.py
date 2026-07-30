import sys

input = sys.stdin.readline

MOD = 10**9 + 7

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(pow(a, b, MOD))