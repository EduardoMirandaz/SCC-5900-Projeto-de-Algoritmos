def gera_sub(index, array, subarray, total, best):
    if index == len(array):
        s = sum(subarray)
        diff = abs(total - 2 * s)
        return min(best, diff)

    # include current element
    subarray.append(array[index])
    best = gera_sub(index + 1, array, subarray, total, best)

    # exclude current element
    subarray.pop()
    best = gera_sub(index + 1, array, subarray, total, best)

    return best


n = int(input())
mangos_weight = [int(i) for i in input().split()]

total = sum(mangos_weight)

result = gera_sub(0, mangos_weight, [], total, float('inf'))
print(result)