import os
import time
import random

for i in range(1, 32):
    with open("testc.txt", "a") as file:
        randomNumber = random.randint(999, 9999)
        file.write(f"{randomNumber}")
        os.system("git add .")
        os.system(
            f'git commit -m "{randomNumber}" --date="2023-01-{i if i >= 10 else f"0{i}"}"'
        )
    time.sleep(1)
