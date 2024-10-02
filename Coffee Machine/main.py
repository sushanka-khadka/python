from menu import menu as menu
from menu import resources as resources  
import os
# import time

profit =0
def report(order):    
  print(f"\tWater: {resources['water']} ml")
  print(f"\tMilk: {resources['milk']}ml")
  print(f"\tCoffee: {resources['coffee']}g")
  print(f"\tFoam: {resources['foam']}ml")
  print(f"\tMoney: ${profit}")

def payment():  
  print('\nquarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01')
  print(f'Please pay ${drink["price"]} for your drink.')
  print('enter the unit:')   # no of coins
  quarter=int(input('Quarter: '))
  dimes=int(input('Dimes: '))
  nickels =int(input('Nickels: '))
  pennies =int(input('Pennies: '))
  coins = quarter*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01
  print('coins: $',round(coins,2))
  if coins>= drink['price'] :   # checks for sufficient money 
    print('Refunded Money: $',round(coins-drink['price'],2))
    print('Enjoy your drink')
    return True
  else:
    print('Not enough money! Money refunded.')    
    if input('do you want to cancel order (y/n): ') =='n':
      os.system('cls')
      payment()
    else:      
      return False

def check_resources(order):
  for item in menu[order]['ingredients']:
    if menu[order]['ingredients'][item] > resources[item]:
      print(f'Sorry there is not enough {item}')
      return False    
  return True
  

is_on =True
while is_on:
  os.system('cls')
  print('''Welcome to the coffee machine
     options:
      * products available:
        1. expresso
        2. americano
        3. latte
        4. cappuccino
      * off
      * report  
Enter product_name or 'off' to turn off the machine or 'report'
        ''')
  
  order = input ('what would you like to have ? ')
  order = order.lower()
  os.system('cls')
  drink =''
  if order == 'off':
    is_on =False
  elif order =='report':
    report(order)
  elif  order in menu:
    drink = menu[order]
    # print(drink)
    
    if check_resources(order):
      # print('enough resources')
      print('Your order has been placed.')    
      if payment():   # successful payment 
        for item in menu[order]['ingredients']:
          resources[item] -= menu[order]['ingredients'][item]
        profit += drink['price']
        # print('Enjoy your drink')        
      else:
        print('Order Cancelled.')  
    else:
      pass
  else:
    print('Not understandable')
  
  # print("Please wait for a while...")
  # time.sleep(2)
  input('press enter to continue...')

print('Revenue collected: ' ,profit)



# order ='latte'
# for item in menu[order]['ingredients'] :
#   print(f"{item.title()} : {menu[order]['ingredients'][item]}")
#   print(f"{menu[order]['ingredients']}")