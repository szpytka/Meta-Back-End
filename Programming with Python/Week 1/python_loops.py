favorites = ["Creme Brulee", "Apple Pie", "Churros", "Tiramisu", "Chocolate Cake"]

for i in range(10):
    print(f"Looping... {i}")

for idx, item in enumerate(favorites):
    print(f"I like this desert: {idx+1} {item}")

count = 0
while count < len(favorites):
    print(f"I like this desert {favorites[count]}")
    count += 1
