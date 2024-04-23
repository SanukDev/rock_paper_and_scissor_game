# This is a sample Python script to create a rock paper and scissors game .

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

#Write your code below this line 👇
print("Welcome to the Rock, Paper, Scissors Game!")

#Player's choice
player_choice = int(input(print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")))



#Computer's choice
import random

computer_choice = random.randint(0,2)

#Printing the choices
game_image = [rock, paper, scissors]
print("Your choice:")
print(game_image[player_choice])


print("Computers choice:")
print(game_image[computer_choice])

#Comparing the choices
if player_choice == computer_choice:
  print("It's a draw")
elif player_choice == 0 and computer_choice == 1:
  print("You lose")
elif player_choice == 0 and computer_choice == 2:
  print("You win")
elif player_choice == 1 and computer_choice == 0:
  print("You win")
elif player_choice == 1 and computer_choice == 2:
  print("You lose")
elif player_choice == 2 and computer_choice == 0:
  print("You lose")
elif player_choice == 2 and computer_choice == 1:
  print("You win")
else:
  print("Invalid choice")

