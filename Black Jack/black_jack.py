#  Black jack
import random
import black_lib
import os

cards =[11,2,3,4,5,6,7,8,9,10,10,10,10]
computer_cards=[]
user_cards=[]

def get_card(): 
  """This function will return a random card from the cards list"""
  return random.choice(cards)
#  initially two cards for user and computer

def calculate_sum(drawn_cards):
  ans = sum(drawn_cards)
  if ans ==21 and len(cards):
    return 0  # black jack
  else:
    return ans

# user_score =0
# computer_score =0

def compare_score(user_score,computer_score):
  if user_score == computer_score:
    print('Draw 🤝')
  elif user_score ==0:
    print('You win! (black jack 😎)')
  elif computer_score ==0:
    print('you lose 🤡 \nopponent got black jack')  
  elif user_score >21:
    print('You lose(overflow) 😭')
  elif  computer_score > 21:
    print('You win(overflow) 😎')
  elif user_score > computer_score:
    print('You win 😎')
  else:
    print('You lose 😭')
  print(f'\ncomputer cards {computer_cards} and score {computer_score}')
  print(f'user cards {user_cards} and score {user_score}')

# game_over =False

def game_play():  
  os.system('cls')
  print(black_lib.icon)  
  for i in range(2):
    computer_cards.append(get_card())
    user_cards.append(get_card())
  user_score,computer_score = 0,0
  game_over =False
  while not game_over :
    user_score = calculate_sum(user_cards)
    computer_score = calculate_sum(computer_cards)
    print(f'Your cards: {user_cards}, current_score: {user_score}')
    print(f'Computer first card: {computer_cards[0]} ')
    
    if user_score > 21 and 11 in user_cards:
      user_cards.remove(11)
      user_cards.append(1)
      user_score = calculate_sum(user_cards)      
      print(f'Your cards: {user_cards}, current_score: {user_score}')
      print(f'Computer first card: {computer_cards[0]} ')
      
    if user_score ==0 or computer_score ==0 or user_score > 21:
      game_over =True
    else:
      add_card =input('\n Do you want to draw another card?\n\t type "y" or "n" ')
      if add_card == 'y':
        user_cards.append(get_card())
        user_score =calculate_sum(user_cards)
        # print(f'Your cards: {user_cards}, current_score: {user_score}')
        # print(f'Computer first card: {computer_cards[0]} ')
      else:
        game_over =True

  while computer_score !=0  and computer_score <17:
    computer_cards.append(get_card())
    computer_score = calculate_sum(computer_cards)
    # print(f'Your cards: {user_cards}, current_score: {user_score}')
    # print(f'Computer first card: {computer_cards[0]} ')
  
  compare_score(user_score,computer_score)
  
  if input('\ntype "y" to continue:  ') == 'y':
    computer_cards.clear()
    user_cards.clear()
    game_play()


game_play()