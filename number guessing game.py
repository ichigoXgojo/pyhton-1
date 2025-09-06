import random
playing = True
number = str(random.randint(10,20 ))

print("i will genrate a number from 0 to 9 and you have to guess it")

while playing:

    guess = input("give me your best guess! \n")
    if guess == number:
        print("you guessed it right")
        print("the number was ", number)
        break
    else:
        print("wrong guess, try again")