# program to predict a euro cup winners with scorecard Spain vs England

import random
england_score= random.randint(0,1)
spain_score = random.randint(0,1)
england_pen=0
spain_pen=0
# print(f'England score is {england_score} and Spain score is {spain_score}')

# regular time
if (england_score != spain_score):
  if (england_score > spain_score):
    print(f'England Wins with score {england_score}-{spain_score}')
  else:
    print(f'Spains Wins with score {spain_score}-{england_score}')

else:  
  # extra time
  print('score_card:  eng-esp:',england_score,'-',spain_score)
  print('Game goes to extra time!')
  
  england_score += random.randint(0,2)
  spain_score += random.randint(0,2)
  if (england_score != spain_score):
    if (england_score > spain_score):
      print(f'England Wins on extra time with score {england_score}-{spain_score}')
    else:
      print(f'Spains Wins on extra time with score {spain_score}-{england_score}')
  else:
    #  penalty shootout
    print('score_card:  eng-esp:',england_score,'-',spain_score)
    print('Game goes to penalty shootout!')

    england_pen += random.randint(0,5)
    spain_pen += random.randint(0,5)
    if (england_score > spain_score):
      print(f'England Wins on penalty shootout with score {england_score}({england_pen})-{spain_score}({spain_pen})')
    else:
      print(f'Spains Wins on penalty shootout with score {spain_score}({spain_score})-{england_score}({england_pen})')

# print('score_card:  eng-esp:',england_score,'-',spain_score)

players_eng = ('saka','foden','bellingham','kane','rice','pickford','watkins','palmer')
players_esp= ('yamal','nico','olmo','morata','rodri','fabian','cucurella','simon')
players = players_eng + players_esp
players_motm = tuple([player.capitalize() for player in players])
motm = players_motm = random.choice(players_motm)
print('Man of the Match:',motm);

