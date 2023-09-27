import string
import random


def generatePassword(length: int = 10):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password


password = generatePassword()
print(f"generate password: {password}")
