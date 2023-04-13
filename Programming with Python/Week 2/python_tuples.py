my_tuple = (1, "strings", 4.5, True)

print(my_tuple[2])
print(type(my_tuple))
print(my_tuple.count("strings"))
print(my_tuple.index(4.5))

for x in my_tuple:
    print(x)

# tuples are immutable and can not be changed (can not be assigned)
