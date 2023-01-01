import random

name = input("Enter your name: ")
print("")
print("                           Welcome",name)
print(" ")
choice = 'yes'
while True:
    if choice == "no":
        break
    n_range = int((input("Enter your lower range no : ")))
    n_range1 = int((input("Enter your end range no : ")))

    print("")
    print("                           Okay be ready to guess one no between - ",n_range,'to',n_range1)
    score = 0
    b = 0
    while b<3:
        user_n1 = int(input("Guess the number! : "))
        real_no = random.randint(n_range,n_range1)
        if user_n1==real_no:
            score =  score + 1
            print("                   Congrats!!")
            print("")
        elif user_n1 > real_no:
            print("                   have one more try Your guess was too high! no. was---",real_no)
            print("")
        elif user_n1<real_no:
            print("                   have one more try Your guess was too small! no. was---",real_no)
            print("")
        else:
            print("                   better luck next time")
        b = b +1

    print("                                                               your score  ",score)
    if score == 0:
        print("Better Luck Next Time!")
    choice = input("Do you want to play again? yes-no: ")

