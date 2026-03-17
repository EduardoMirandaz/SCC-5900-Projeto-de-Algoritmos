n, s = [int(i) for i in input().split()]
v = list([int(i) for i in input().split()])


# We use this map to store the count of each value in the list, so we can easily 
# find the complement of each value and check how many of them are on the list
values_occurrencies_count = {}

pairs_found_count = 0

for value in v:
    # Here, we add to the pairs_found_count the amount of the complementary values found
    # For example, if s is 10 and value(vi) is 4, we add to "pairs_found_count" the amount of 6 (10-4) on the list. 
    pairs_found_count += values_occurrencies_count.get(s - value, 0)

    # Here we just keep tracking of how many of each value are on the list 
    values_occurrencies_count[value] = values_occurrencies_count.get(value, 0) + 1

print(pairs_found_count)

