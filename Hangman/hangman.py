import hangman_art
import random 
import hangman_words

print(hangman_art.icon)


words =[]
for word in hangman_words.words:
  words.append(word.lower())


chosen_word = random.choice(words)
len = len(chosen_word)
chosen_word = list(chosen_word)

# print(chosen_word)

# print(' '.join(chosen_word))

result = []
for i in range(len):
  result.append('_')

print(' '.join(result))
lives =0
print('Total lives: ',6-lives)
while lives<6:
  check = False
  guess = input('\nGuess a letter: ').lower()
  if guess in result:
    print('You have already guessed this letter')
  else:  
    for i in range(len):
      if guess == chosen_word[i]:
        result[i] = guess
        check = True
      else:
        pass
    if check == False:
      lives += 1
      print('lives left:',6-lives)
      print(hangman_art.stages[lives])
    print(' '.join(result))
    
    # if '_' not in result:
    if result == chosen_word:
      print('\n\nyou won'.upper())
      exit()
print('You lose')
print('Actual word is: ', ''.join(chosen_word))


# while len>0:
#   guess = input('\nGuess a letter: ').lower()
#   for letter in chosen_word:
#     if guess == letter:      
#       result[chosen_word.index(letter)] = guess    
#     else:
#       --len;
#   print(result)
