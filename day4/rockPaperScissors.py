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

game_images = [rock, paper, scissors]

userInput = int(input('Choose 0 for rock 1 for paper and 2 for scissors \n'))
computer_choice = random.randint(0, 2)

if userInput >= 3 or userInput < 0:
  print('You typed an invalid number. you lose!')
else:
  print(game_images[userInput])
  print(f'computer chose:')
  print(game_images[computer_choice])

  if userInput == 0 and computer_choice == 2:
    print('user wins')
  elif (computer_choice > userInput):
    print('Computer Wins')
  elif (computer_choice == userInput):
    print('Draw')
  elif computer_choice == 0 and userInput == 2:
    print('You lose')
  elif userInput > computer_choice:
    print('You win!')


