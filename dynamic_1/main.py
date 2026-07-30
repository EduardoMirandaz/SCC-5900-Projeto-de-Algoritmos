def min_climbing_cost(costs):
    n = len(costs)
    if n == 0:
        return 0
    if n == 1:
        return costs[0]

    # dp0 = min cost to reach step i-2
    # dp1 = min cost to reach step i-1
    dp0 = costs[0]
    dp1 = costs[1]

    for i in range(2, n):
        curr = costs[i] + min(dp0, dp1)
        dp0, dp1 = dp1, curr

    # top can be reached from last or second-last step
    return min(dp0, dp1)


n = int(input().strip())
costs = list(map(int, input().split()))

print(min_climbing_cost(costs))