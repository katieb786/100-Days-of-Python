import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors \n"))
if choice > 2 or choice < 0:
    print("You entered an invalid number. You lose! :(")
else:
    computer = random.randint(0, 2)
    computer_choice = game[computer]
    player_choice = game[choice]

    print(player_choice)
    print("Computer chose:")
    print(computer_choice)

    if choice == computer:
        print("It's a draw! :/")
    elif choice == 0 and computer == 2:
        print("You win! :D")
    elif choice == 1 and computer == 0:
        print("You win! :D")
    elif choice == 2 and computer == 1:
        print("You win! :D")
    else:
        print("You lose! :(")

