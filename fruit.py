import random
class fruit_quiz:
    def __init__(self):
        self.fruits={'apple':'red', 'mango':'yellow', 'watermelon':'green','papaya':'orange'}
    def quiz(self):
        while(True):
            fruit,color= random.choice(self.fruits.items())
            print("What is the color of {}".format(fruit))
            ans= input()
            if ans.lower()==color:
                print("Correct answer")
            else:
                print("Incorret answer")
            option= int(input("Enter 0 to play again otherwise enter 1: "))
            if option:
                break
print("Welcom to fruit quiz")
fq= fruit_quiz()
fq.quiz()