def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def div(a,b):
  if b==0:
    print('Math Error!!! \nDivision by zero')
    exit()
  else:
    return a/b
def mod(a,b):
  return a%b
def exp(a,b):
  return a**b

operations ={
  '+':add,
  '-':sub,
  '*':mul,
  '/':div,
  '%': mod,
  '^': exp
}

icon ='''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''