alphabets =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
size = len(alphabets)

import art


def caesar(text,shift):  
  caesar_text=''
  for letter in text:    
    if letter.lower() in alphabets:
      if letter.isupper():   
        # checks for uppercase if true converts to lower and then to original
        caesar_text += (alphabets[(alphabets.index(letter.lower()) +shift) % size]).upper()
      else:      
        caesar_text += alphabets[(alphabets.index(letter) + shift) % size] 
    else:
      caesar_text += letter
  if shift >=0:
    print(f'Encrypted text: {caesar_text}')
  else:
    print(f'Decrypted text: {caesar_text}')


play_continue =True
while play_continue:  
  plain_text = input('enter any text to encode or decode : ')
  shift = int(input('Enter the shift positon \n\t +ve for encryption \n\t -ve for decryption\n'))

  caesar(plain_text,shift)

  check =input('\ntype "yes" to continue:  ')

  if check == 'yes':
    print('\n')
    continue
  else:
    play_continue = False
  
