with open("newfile.txt", "a") as file:
    file.write("This is a new file created!\n")
    file.writelines(["New line\n", "This is another line to be added\n"])
