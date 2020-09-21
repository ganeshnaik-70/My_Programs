import random


def game():
    choices = ["Stone", "Paper", "Scissor"]
    run = True
    while run:
        print("1 : Stone\n"
              "2 : Paper\n"
              "3 : Scissor\n"
              "4 : Exit")
        user_choice = int(input("Enter Your Choice : "))
        if user_choice == 4:
            print("Exiting....")
            break
        if user_choice < 0 or user_choice > 4:
            print("Enter Proper choice")
            print("--"*30)
        else:
            print("You choice is", choices[user_choice - 1])
            com_choice = random.choice(choices)
            print("Computer choice is", com_choice)

            if user_choice == 1 and com_choice == choices[user_choice - 1]:
                print("Ohhh!! Its Draw")
                print("--" * 30)

            if user_choice == 2 and com_choice == choices[user_choice - 1]:
                print("Ohhh!! Its Draw")
                print("--" * 30)

            if user_choice == 3 and com_choice == choices[user_choice - 1]:
                print("Ohhh!! Its Draw")
                print("--" * 30)

            if user_choice == 1 and com_choice == choices[2]:
                print("WoW You Won!!!")
                print("--" * 30)

            if user_choice == 2 and com_choice == choices[0]:
                print("WoW You Won!!!")
                print("--" * 30)

            if user_choice == 3 and com_choice == choices[1]:
                print("WoW You Won!!!")
                print("--" * 30)

            if user_choice == 1 and com_choice == choices[1]:
                print("You Lost :/...")
                print("--" * 30)

            if user_choice == 2 and com_choice == choices[2]:
                print("You Lost :/...")
                print("--" * 30)

            if user_choice == 3 and com_choice == choices[0]:
                print("You Lost :/...")
                print("--" * 30)
    return


game()
