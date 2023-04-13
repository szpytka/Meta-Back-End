set_a = {1, 2, 3, 4, 5, 5, 5, 5, "1232321"}

set_a.add(6)

set_a.remove(2)

set_a.discard(3)

print(set_a)

set_b = {1, 2, 3, 4, 5, 6, 7, 8}
print(set_a.union(set_b))  # or print(set_a | set_b) -> works the same

print(
    set_a.intersection(set_b)
)  # matching elements, print(set_a & set_b) -> works the same

print(set_a.difference(set_b))  # differences print(set_a - set_b) works the same

print(
    set_a.symmetric_difference(set_b)
)  # all the elements exist here or here but not in both print(set_a ^ set_b) the

# set -> collection of nonduplicates
# cant access set index like set[1]
