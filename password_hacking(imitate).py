import random
import string
import time


password = input("Password:")

print("Hacking password...")
time.sleep(1)

chars = string.ascii_letters + string.digits + string.punctuation

for i in range(len(password)):
    while True:
        guess = "".join(
            random.choice(chars) for _ in range(i + 1)
        )

        print("\r" + guess, end="")
        time.sleep(0.05)

        if random.randint(1, 15) == 1:
            break

print("Password found:", password)