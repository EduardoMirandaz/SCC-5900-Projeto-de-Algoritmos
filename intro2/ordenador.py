with open("ordenados.txt", "w") as file:
    while True:
        file.write(' '.join(sorted(list(input().split())))+'\n')