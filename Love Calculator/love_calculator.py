name_1 = input("Enter your name: ");
name_2 = input("Enter your partner's name: ");

# name_1= 'anil'
# name_2 = 'jack'

name = name_1 + name_2;
name = name.lower()

true = name.count('t') + name.count('r') + name.count('u') + name.count('e')
love = name.count('l') + name.count('o') + name.count('v') + name.count('e')

love_score = str(true) + str(love)

if int(love_score) < 10 or int(love_score) > 90:
  print(f'Your love score is  {love_score}%, you go together like coke and mentos')
elif int(love_score) >= 40 and int(love_score) <= 50:
  print(f'Your love score is  {love_score}%, you are alright together')
else:
  print(f'Your love score is  {love_score}%')

