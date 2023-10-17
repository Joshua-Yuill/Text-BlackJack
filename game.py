#Libraries
import os
import time
import random as r

#Functions
def mainMenu():
    os.system('cls') #clear terminal
    print(" ____   _       ____    __  __  _   ____   ____    __  __  _  ")
    print("|    \ | |     /    |  /  ]|  |/ ] |    | /    |  /  ]|  |/ ] ")
    print("|  o  )| |    |  o  | /  / |  ' /  |__  ||  o  | /  / |  ' /  ")
    print("|     || |___ |     |/  /  |    \  __|  ||     |/  /  |    \  ")
    print("|  O  ||     ||  _  /   \_ |     \/  |  ||  _  /   \_ |     \ ")
    print("|     ||     ||  |  \     ||  .  |\  `  ||  |  \     ||  .  | ")
    print("|_____||_____||__|__|\____||__|\_| \____||__|__|\____||__|\_| ")
    print("                                                             ")
    print("1. Play")
    print("2. Rules")
    print("3. Quit")
    print("4. Credits")
    print(" ")
    selection = input("What would you like to do? [1-4]: ")

    if selection == "1":
        play()
         
    elif selection == "2":
        rules()

    elif selection == "3":
        exit(1)

    elif selection == "4":
        credits()

    else:
        print("That was and ivlaid input, please try again")
        time.sleep(15)
        mainMenu()


    return
def rules():
    print("Instructions: ")
    return

def credits():

    return

def play():
    os.system('cls') #clear terminal
    
    cards = ["Ah", "Ad", "Ac", "As",
    "2h", "2d", "2c", "2s",
    "3h", "3d", "3c", "3s",
    "4h", "4d", "4c", "4s",
    "5h", "5d", "5c", "5s",
    "6h", "6d", "6c", "6s",
    "7h", "7d", "7c", "7s",
    "8h", "8d", "8c", "8s",
    "9h", "9d", "9c", "9s",
    "10h", "10d", "10c", "10s",
    "Jh", "Jd", "Jc", "Js",
    "Qh", "Qd", "Qc", "Qs",
    "Kh", "Kd", "Kc", "Ks"]

    r.shuffle(cards)

    cards.insert((r.randint(0,51)), 'SHUFFLE')


    print(cards)




    return

play()