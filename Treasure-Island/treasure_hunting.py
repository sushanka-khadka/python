print('''

████████ ██████  ███████  █████  ███████ ██    ██ ██████  ███████ 
   ██    ██   ██ ██      ██   ██ ██      ██    ██ ██   ██ ██      
   ██    ██████  █████   ███████ ███████ ██    ██ ██████  █████   
   ██    ██   ██ ██      ██   ██      ██ ██    ██ ██   ██ ██      
   ██    ██   ██ ███████ ██   ██ ███████  ██████  ██   ██ ███████ 



''')


print("Welcome to Treasure Island.".upper())
print("your mission is to find the treasure.")

user = input('You\'re at a crossroad, where do you want to go? Type "left" or "right" \n')
user=user.lower()

if user == "left":
  user = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
  user=user.lower()  
  if user == 'wait':
    user=input(f'You arrive at the island unharmed. There is a house with 3 doors. One red,one yellow and one blue. Which colour do you choose?\n')
    user=user.lower()
    if user == 'red' :
      print('Game Over!!!\n Burned by fire!')
    elif user == 'blue':
      print('Game Over!!!\n Eaten by Beasts!')
    elif user == 'yellow':
        print('Congrats!!!\n You Win!!!')
    else:
      print('GAME OVER')
  else:  
    print('Game Over!!!\n Attacked by Crocodile!')  
else:
  print('Game Over!!!\n Fall into a hole')

