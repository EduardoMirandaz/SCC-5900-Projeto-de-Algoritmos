from collections import deque
import sys

input = sys.stdin.readline

number_of_intersections, number_of_streets = map(int, input().split())

adjacency_list = [[] for _ in range(number_of_intersections + 1)]
residual_capacity = [[0] * (number_of_intersections + 1)
                     for _ in range(number_of_intersections + 1)]

original_streets = []

for _ in range(number_of_streets):
    intersection_a, intersection_b = map(int, input().split())

    # Keep the street exactly as it appears in the input
    original_streets.append((intersection_a, intersection_b))

    adjacency_list[intersection_a].append(intersection_b)
    adjacency_list[intersection_b].append(intersection_a)

    residual_capacity[intersection_a][intersection_b] += 1
    residual_capacity[intersection_b][intersection_a] += 1


def find_augmenting_path(source_intersection,
                         destination_intersection,
                         predecessor):
    predecessor[:] = [-1] * (number_of_intersections + 1)
    predecessor[source_intersection] = source_intersection

    bfs_queue = deque([source_intersection])

    while bfs_queue:
        current_intersection = bfs_queue.popleft()

        for neighbor_intersection in adjacency_list[current_intersection]:

            if (predecessor[neighbor_intersection] == -1 and
                    residual_capacity[current_intersection][neighbor_intersection] > 0):

                predecessor[neighbor_intersection] = current_intersection

                if neighbor_intersection == destination_intersection:
                    return True

                bfs_queue.append(neighbor_intersection)

    return False


source_intersection = 1
port_intersection = number_of_intersections

predecessor = [-1] * (number_of_intersections + 1)

# Edmonds-Karp max flow
while find_augmenting_path(source_intersection,
                           port_intersection,
                           predecessor):

    bottleneck_capacity = float("inf")

    current_intersection = port_intersection

    while current_intersection != source_intersection:
        previous_intersection = predecessor[current_intersection]

        bottleneck_capacity = min(
            bottleneck_capacity,
            residual_capacity[previous_intersection][current_intersection]
        )

        current_intersection = previous_intersection

    current_intersection = port_intersection

    while current_intersection != source_intersection:
        previous_intersection = predecessor[current_intersection]

        residual_capacity[previous_intersection][current_intersection] -= bottleneck_capacity
        residual_capacity[current_intersection][previous_intersection] += bottleneck_capacity

        current_intersection = previous_intersection


# Find vertices reachable from the vault in the residual graph
reachable_from_vault = [False] * (number_of_intersections + 1)

search_queue = deque([source_intersection])
reachable_from_vault[source_intersection] = True

while search_queue:
    current_intersection = search_queue.popleft()

    for neighbor_intersection in adjacency_list[current_intersection]:

        if (not reachable_from_vault[neighbor_intersection] and
                residual_capacity[current_intersection][neighbor_intersection] > 0):

            reachable_from_vault[neighbor_intersection] = True
            search_queue.append(neighbor_intersection)


streets_to_close = []

for intersection_a, intersection_b in original_streets:
    if reachable_from_vault[intersection_a] != reachable_from_vault[intersection_b]:
        streets_to_close.append((intersection_a, intersection_b))

# Sort by a, then b, exactly as required
streets_to_close.sort()

print(len(streets_to_close))

for intersection_a, intersection_b in streets_to_close:
    print(intersection_a, intersection_b)