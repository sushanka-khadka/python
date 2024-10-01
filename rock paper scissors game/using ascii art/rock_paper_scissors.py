print('1. rock \n2. paper \n3. scissors\n4. exit')

print('''
RULES:
1.rock beats scissors
2. scissors beats paper
3. paper beats rock
''')

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

import random
game_images =[rock,paper,scissors]

while True:
  user = int(input('\nEnter your choice: '))
  if user >4 and user <1:
    print('Invalid choice! You lose')
  elif user == 4:
    break
  else:
    print(f'You chose: {game_images[user-1]}')
    
    computer = random.randint(1,3)
    print(f'Computer choose: {game_images[computer-1]}')
    if user == 1 and computer == 3:
      print('You win')  
    elif user == 3 and computer == 1:
      print('You lose')  
    elif user > computer:
      print('You win')
    elif computer>user:
      print('You lose')
    elif user == computer:
      print('It\'s a draw')
    else:
      break