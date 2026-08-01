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

rock_paper_scissors = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)

print(rock_paper_scissors[computer_choice] + "\nComputer chose:\n" + rock_paper_scissors[user_choice])

if user_choice == computer_choice:
    print("It's a Draw")
elif user_choice > computer_choice:
    print("You win")
elif computer_choice > user_choice:
    print("You win")
elif user_choice == 0 and computer_choice == 2:
    print("You lose")
elif computer_choice == 0 and user_choice == 2:
    print("You win")
elif user_choice >= 3 and user_choice < 0:
    print("You Typed an invalid number, you lose!")

