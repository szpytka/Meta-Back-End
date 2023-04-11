num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62, 78, 43, 88, 39, 53, 67, 89, 11]
counter = 0

for idx, item in enumerate(num_list):
    counter += 1
    if item == 36:
        print(f"Item found at position: {idx}")
        break
    if item > 45:
        print("Over 45")
    else:
        print("Under 45")

print(counter)
