# FIRST TASK
# Знаходження об'єднання двох множин
def find_union(set1, set2):
    unit_set = set()
    for elem in set1:
        unit_set.add(elem)
    for elem in set2:
        unit_set.add(elem)

    return unit_set

# SECOND TASK
# Знаходження декартового добутку двох множин
def find_cartesian_product(set1, set2):
    cartesian_product_set = set()
    for elem1 in set1:
        for elem2 in set2:
            cartesian_product_set.add((elem1, elem2))
            
    return cartesian_product_set


# Приклади
set1 = {1, 2, 3, 6, 7, 10}
set2 = {3, 4, 5, 6, 7, 8}

print(f"Об'єднання двох множин - {find_union(set1, set2)}")
print(f"Декартовоий добуток двох множин - {find_cartesian_product(set1, set2)}")
