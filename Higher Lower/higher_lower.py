from game_data import accounts
from game_data import data
from game_data import icon
import random
import os
# print(data['account'].lower()=='ronaldo')


# print(accounts[rando,.random.choice(accounts)])

# print(accounts[random.choice(accounts)])

# print(accounts['leomessi'])

# print(random.choice(accounts))



# print(random.choice(data))
# print(random.choice(accounts))

def format_data (account):
  # print(f" {account['account']}, {account['description']}, {account['followers']}")
  return f"{account['account']}, {account['description']}"


  # print(f"({account['account']})")


# print(data[random.randint(0,30)])
# print(f'')
# data = list(data.values())

account_a = random.choice(data)
account_b = random.choice(data)
# print(f'Choice A: {format_data(account_a)}')        
# print(f'Choice B: {format_data(account_b)}')        
# ans = input('Who has got most followers: Type "a" or "b": ')

# if (account_a['followers'] >= account_b['followers'] and ans == 'a') or (account_b['followers'] > account_a['followers'] and ans == 'b') :
#     print('You are right')
# else:   
#     print('You are wrong')

score =0
right =True
while right:
  os.system('clear')
  print(icon)
  print(f'Your current score: {score}')
  print(f'Choice A: {format_data(account_a)}')        
  print(f'Choice B: {format_data(account_b)}')        
  ans = input('Who has got most followers: Type "a" or "b": ')

   # every time both the choice are altered
  # if (account_a['followers'] >= account_b['followers'] and ans == 'a') or (account_b['followers'] > account_a['followers'] and ans == 'b') :
  #   print('You are right')
  #   score += 1
  #   account_a = random.choice(data)
  # else:   
  #   print('You are wrong')
  #   right =False

  
  # to retreive the previous with most followers
  if (account_a['followers'] >= account_b['followers']) :
    if ans == 'a':
      print('You are right')
      score += 1
    else:
      print('You are wrong')
      right = False 
  else:
    if ans == 'b':
      print('You are right')
      account_a = account_b
      score += 1 
    else:   
      print('You are wrong') 
      right = False
      
  print('Your score: ',score)  
  account_b = random.choice(data)


# for rank in data:
#   print(rank,data[rank]['account'],data[rank]['followers'])

# print(data.values())

