import random

flag =True
while flag :
    num = input("type a number for an upper bound : ")

    if num.isdigit() :
        print("Let's play like that !.....")

        num = int(num)
        flag =False
    else :
        print("Invalid input ! Try again..")


secret = random.randint(1,num)
guess = None
count =1


while guess != secret :
    guess = input("please type a number between 1 and" + str(num) + ":")
    if guess.isdigit() :
        guess = int(guess)

    if guess == secret:
        print("you got it !")
    else :
        print("please try again..!")
        count +=1
print("It took you",count,"guesss....")