import os
import time
import random

break_out = False

for i in range(1, 30):  # days
    for x in range(1, 5):  # months
        for j in range(1, random.randint(1, 4)):  # number of commits
            with open("testc.txt", "a") as file:
                randomHour = random.randint(1, 25)
                randomMinutes = random.randint(1, 61)
                randomSeconds = random.randint(1, 61)
                randomNumber = random.randint(999, 9999)
                file.write(f"{randomNumber}\n")
                os.system("git add .")
                os.system(
                    f'git commit -m "{randomNumber}" --date="2023-01-{i if i >= 10 else f"0{i}"} {randomHour}:{randomMinutes}:{randomSeconds}"'
                )
            if x == 4 and i > 10:
                break_out = True
                break
            time.sleep(1)
        if break_out:
            break
    if break_out:
        break
