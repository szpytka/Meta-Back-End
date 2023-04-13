list1 = [0, 1, 2, 3, 4, 5]

print(list1[2])

list2 = ["A", "B", "C"]

list3 = ["Hello", 1, True, 40.22]

list4 = [1, [2, 3, 4], 5, 6]


print(*list1)
print(list1, sep=" ")
print(list1)

list1.insert(len(list1), 6)
print(list1)

list1.append(7)
print(list1)

list1.extend([8, 9, 10])
print(list1)

list1.pop(4)
print(list1)

del list1[2]
print(list1)

for x in list1:
    print(x)
