import random

def good_password_generator(length=10):
    letters = 'abcdefgihjklmnopqrstuvwxyz'
    upper_letters = 'ABCDEFGIHJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    symbols = '!@#$%^&*()_+-=\'\\"'

    alphabet = letters + upper_letters + digits + symbols

    password = ''
    for i in range(length):
        char = random.choice(alphabet)
        password += char

    return password

popular_passwords = """password
123456
12345678
1234
qwerty
12345
dragon
pussy
baseball
football"""

popular_passwords = popular_passwords.split('\n')
counter = 0

def bad_password_generator():
    global counter
    password = popular_passwords[counter]

    counter += 1
    if counter >= len(popular_passwords):
        counter = 0

    return password
#
# print(good_password_generator())
# print(good_password_generator(0))
print(good_password_generator())
# print(good_password_generator(10))
for i in range (15):
    print(bad_password_generator())
# print(good_password_generator(100))
