import random

class FruitQuiz:
    def __init__(self):
       
        self.fruits ={'apple':'red', 'orange':'orange', 'banana':'yellow', 'watermelon':'green',}
    
    def quiz(self):
        while (True):
                
                fruit, color = random.choice(list(self.fruits.items()))

                print("What is the color of {}".format(fruit))
                user_answer = input()

                if user_answer.lower() == color:
                    print("Correct!")   
                else:
                    print("Incorrect!")
                
                option = int(input("enter 0 to exit or 1 to continue: "))
                if (option):
                    break

print("Thank you for playing the Fruit Color Quiz!")
fq = FruitQuiz()
fq.quiz()

        
        
