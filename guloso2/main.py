executions_amount = int(input())

for _ in range(executions_amount):
    bridge_size, zombies_amount = [int(i) for i in input().split()]

    min_path, max_path = 0, 0
    
    zombies_positions = input().split()

    for i in zombies_positions:
        
        distance_to_end = abs(bridge_size-int(i))

        min_path = max(min_path, min(distance_to_end, int(i)))
        max_path = max(max_path, max(distance_to_end, int(i)))
        
    print(min_path, max_path)



