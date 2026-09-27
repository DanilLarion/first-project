import random
import string


length = int(input("Welcome to the password generator!\nPlease specify the password length: "))
password = random.sample(string.ascii_letters + string.digits
                         + string.ascii_uppercase + string.punctuation, length)
print("Here your password:","".join(password))