# rock scissors paper game
import os
import random
import time

def info():
    print('''
        Rock Paper Scissors game
        plese select one 
            1. Rock
            2. Paper
            3. Scissors
            4. Exit
        Rules:
            1. Paper beats rock
            2. scissors beats paper
            3. rock beats scissors
             Have fun!   
    
    ''')
    

while(True):
    info()
    user_1=int(input('Your choice:'))
    if(user_1==4):
        print('game over!!!')
        break
    elif(user_1>=5):
        print('choose between 1 to 4')
    else:
        #Game={'rock':1,'paper':2,'scissors':3}
        Game={1:'rock',2:'paper',3:'scissors'}
        ai_1=random.randint(1,3)
        ai=Game.get(ai_1)
        user=Game.get(user_1)
#         print(user,'\n',ai)
        print(f'user:{user} \nai={ai}\n')

        if(user=='rock' and ai=='paper'):            
            print('you choose Rock i choose paper. I won!!!')
            time.sleep(0.9)
        elif(user=='rock' and ai== 'scissors'):
            print('you choose Rock i choose Scissors. You won!!!')
            time.sleep(0.9)
        elif(user=='paper' and ai=='scissors'):
            print('you choose Paper i choose Scissors. I won!!!')
            time.sleep(0.9)
        elif(user=='paper' and ai=='rock'):
            print('you choose Paper i choose Rock. You won!!!')
            time.sleep(0.9)
        elif(user=='scissors' and ai=='rock'):
            print('you choose Scissors i choose Rock. I won!!!')
            time.sleep(0.9)
        elif(user=='scissors' and ai=='paper'):
            print('you choose Scissors i choose Paper. You won!!!')
            time.sleep(0.9)
        else:
            print('Draw. Please continue')
            time.sleep(0.9)
#        os.system('cls')
    input('press enter to continue...')
    os.system('cls')
    # os.system('clear')
        