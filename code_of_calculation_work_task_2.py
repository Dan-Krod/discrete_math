def print_partition(BLOCK, n):
  
    partition = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        partition[BLOCK[i]].append(i)
    partition = [tuple(part) for part in partition if part]
    print(partition)
          
def partition_algorithm(n):
  
    BLOCK = [0] * (n + 1)
    FORWARD = [True] * (n + 1)
    NEXT = [0] * (n + 1)
    PREV = [0] * (n + 1)

    for i in range(1, n + 1):
        BLOCK[i] = 1
        FORWARD[i] = True

    NEXT[1] = 0
    print_partition(BLOCK, n)

    j = n  

    while j > 1:
        k = BLOCK[j]
        if FORWARD[j]:  
            if NEXT[k] == 0:  
                NEXT[k] = j
                PREV[j] = k
                NEXT[j] = 0
            if NEXT[k] > j: 
                PREV[j] = k
                NEXT[j] = NEXT[k]
                PREV[NEXT[j]] = j
                NEXT[k] = j
            BLOCK[j] = NEXT[k]
        else:  
            BLOCK[j] = PREV[k]
            if k == j: 
                if NEXT[k] == 0:
                    NEXT[PREV[k]] = 0
                else:
                    NEXT[PREV[k]] = NEXT[k]
                    PREV[NEXT[k]] = PREV[k]

        print_partition(BLOCK, n)
        j = n
        while (j > 1) and ((FORWARD[j] and (BLOCK[j] == j)) or (not FORWARD[j] and (BLOCK[j] == 1))):
            FORWARD[j] = not FORWARD[j]
            j -= 1

if __name__ == "__main__":
    n = int(input("Enter n: "))
    partition_algorithm(n)
