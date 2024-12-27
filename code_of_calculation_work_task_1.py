def B(m, i):
    if m % 2 == 0 and m > 2:
        if i < m - 1:
            return i
        else:
            return m - 2
    else:
        return m - 1
    
def PERM(m):
    if m == 1:
        print(*P)
    else:
        for i in range (m):
            PERM(m - 1)
            if i < m:
                j = B(m, i)
                P[i], P[m - 1] = P[m - 1], P[i]
                
def generate_permutations(n):
    global P
    P = list(range(1, n + 1))
    PERM(n)
    
# if __name__ == "__main__":
#     n = int(input("Enter n: "))
generate_permutations(4)
