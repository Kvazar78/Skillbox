password = ''

letters = 'abcdefgihjklmnopqrstuvwxyz'
upper_letters = 'ABCDEFGIHJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
symbols = '!@#$%^&*()_+-=\'\\"'

alphabet = letters + upper_letters + digits + symbols

import random

#print(random.choice(alphabet))

N = 10

for i in range(N):
    char = random.choice(alphabet)
    password += char

print(password)