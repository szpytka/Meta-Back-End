my_d = {1: "Test", "Name": "Jakub"}

print(my_d)
print(type(my_d))

print(my_d[1])
print(my_d["Name"])
my_d[2] = "Test 2"
my_d[1] = "not a test"
print(my_d)

del my_d[1]
print(my_d)

print("---------------------")

for key, value in my_d.items():
    print(f"key: {key}, value: {value}")
