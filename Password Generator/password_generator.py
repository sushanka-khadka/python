import random

print('password generator'.title())
pass_len = int(input ('how many characters do you want in your password? '))

numbers = ['0','1','2','3','4','5','6','7','8','9']
lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

symbols = [',','.','/','?','!','@','#','$','%','^','&','*','(',')','-','+','=','_','~','`','{','}','[',']','|',':',';','<','>','"','\'','\\','']

password = ""

for i in range(1,pass_len+1):
  password += random.choice(lower + upper + numbers + symbols)

print(f'your password is {password}')


# Another Method
'''
nr_symbols = int(input('how many symbols do you want: '))
nr_lower = int(input('how many lower case do you want: '))
nr_upper = int(input('how many upper case do you want: '))
nr_numbers = int(input('how many numbers do you want: '))

password = random.choices(upper, k=nr_upper)
password += random.choices(lower, k=nr_lower)
password += random.choices(numbers, k=nr_numbers)
password += random.choices(symbols, k=nr_symbols)

print(password)
random.shuffle(password)    # -- no need to shuffle

print(password)

new_pass =''
for char in password:
  new_pass += char

print(f'your password is {new_pass}')
'''