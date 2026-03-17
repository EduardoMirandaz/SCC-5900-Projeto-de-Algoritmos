operations = int(input())

while operations > 0:
    choosed_courses_set = {}
    most_common = 0

    for i in range(operations):
        key = frozenset(input().split())
        choosed_courses_set[key] = choosed_courses_set.get(key, 0) + 1

        tmp = choosed_courses_set[key]
        if tmp > most_common:
            most_common = tmp
            # print(key)

    most_common = max(most_common, operations) if most_common == 1 else most_common

    print(most_common)

    operations = int(input())

