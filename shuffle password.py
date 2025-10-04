import random
import string

length = int(input("Enter the length of the password: "))

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))
 
random.shuffle(list(password))
shuffled_password = ''.join(random.sample(password, len(password)))

print("Shuffled password:", shuffled_password)