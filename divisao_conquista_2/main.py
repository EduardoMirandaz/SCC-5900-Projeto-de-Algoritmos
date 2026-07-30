def can_split(distances, max_km, max_days):
    days = 1
    current = 0

    for d in distances:
        if current + d <= max_km:
            current += d
        else:
            days += 1
            current = d

    return days <= max_days


t = int(input())

for _ in range(t):
    number_of_inns, sleep_nights = map(int, input().split())

    distances = [int(input()) for _ in range(number_of_inns + 1)]

    # number of days = nights + 1
    max_days = sleep_nights + 1

    left = max(distances)
    right = sum(distances)

    answer = right

    while left <= right:
        mid = (left + right) // 2

        if can_split(distances, mid, max_days):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)