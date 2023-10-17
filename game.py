#Libraries
import os

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
