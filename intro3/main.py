import heapq

num_of_queries = int(input())
queries = []

for _ in range(num_of_queries):
    _, id, T = input().split()
    id = int(id)
    T = int(T)

    # We store on the format (next_time, id, period)
    heapq.heappush(queries, (T, id, T))

num_of_executions = int(input())

while num_of_executions > 0:

    elapsed_time, id, tick = heapq.heappop(queries) 
    print(id)
    heapq.heappush(queries, (elapsed_time+tick, id, tick))
    num_of_executions -= 1
