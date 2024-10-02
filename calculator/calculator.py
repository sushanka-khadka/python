import calculator_lib as cal
import os

def calculate():
  print(cal.icon)
  do_calc = True
  a= float(input('enter first number: '))
  while do_calc:    
    b= float(input ('enter next number:')) 
    for symbol in cal.operations.keys():
      print(symbol,end='\t')
    symbol =input('\nenter operation: ')    

    if symbol not in cal.operations.keys():   
      print('invalid operation')
      symbol =input('\nenter operation listed above: ')
    else:
      pass
    
    calc_func = cal.operations[symbol]  
    ans = calc_func(a,b)
    print(f'\n {a} {symbol} {b} = {ans}')
  
    should_continue = input('press "y" to continue, "n" to start new calculation or "e" to exit:  ')
    if should_continue == 'y':
      a = ans
    elif should_continue == 'n':      
      os.system('cls')
      calculate()
    else:
      break

calculate()