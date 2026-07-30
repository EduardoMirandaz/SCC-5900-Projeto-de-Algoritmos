def max_robbery(values):
    n = len(values)
    if n == 0:
        return 0
    if n == 1:
        return values[0]

    prev2 = values[0]                  # dp[i-2]
    prev1 = max(values[0], values[1])  # dp[i-1]

    for i in range(2, n):
        curr = max(prev1, prev2 + values[i])
        prev2, prev1 = prev1, curr

    return prev1


n = int(input().strip())
values = list(map(int, input().split()))

print(max_robbery(values))