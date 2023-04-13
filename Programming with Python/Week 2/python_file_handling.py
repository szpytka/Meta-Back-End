file = open("test.txt", mode="r")

data = file.readline()

print(data)

file.close()


with open("test.txt", mode="r") as file:
    data = file.readline()
    print(data)
