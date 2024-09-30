import random
import os

def guess(mode):
  os.system('cls')
  if mode == 'hard':
    attempt = 5
  else:
    attempt = 10
  print(f'you have {attempt} attempts left')
  random_numer = random.randint(1,100)

  print(f'''\n about number:
    is_even:{True if random_numer % 2 == 0 else False}
    is_divisible_by_5: {'yes' if random_numer % 5 == 0 else 'no'}
    ''')
  
  while attempt > 0:    
    x= int(input('make a guess: '))
    if x == random_numer:
      print(f'You got it! The answer was {x}')
      break
    if x < random_numer:
      print('too low')
    else:
      print('too high')
    attempt -= 1
    print(f'you have {attempt} attempts left\n')
    

'''
even:
higher / lower
divisible by 5
'''

while True:
  os.system('cls')
  print('*'*5 + 'Welcome to number guessing game'+ '*'*5)
  print('I am thinking of a number between 1 and 100')
  mode = input('choose difficulty: "easy" or "hard"\t')
  guess(mode)
  if input('\n type "e" to exit else continue : ') == 'e':
   break
    
